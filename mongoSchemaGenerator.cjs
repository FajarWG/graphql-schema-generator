const { MongoClient } = require("mongodb");
const fs = require("fs");
const path = require("path");

async function inferTypeFromValue(value) {
  if (Array.isArray(value)) {
    if (value.length === 0) return "String";
    return inferTypeFromValue(value[0]);
  }

  switch (typeof value) {
    case "string":
      return isNaN(Date.parse(value)) ? "String" : "DateTime";
    case "number":
      return Number.isInteger(value) ? "Int" : "Float";
    case "boolean":
      return "Boolean";
    case "object":
      if (value === null) return "String";
      if (value instanceof Date) return "DateTime";
      if (value._bsontype === "ObjectId") return "ID";
      return "Object";
    default:
      return "String";
  }
}

async function analyzeDocument(doc, fields, prefix = "", nestedTypes = {}) {
  for (const [key, value] of Object.entries(doc)) {
    const fieldName = prefix ? `${prefix}_${key}` : key;

    if (!fields.has(fieldName)) {
      fields.set(fieldName, new Set());
    }

    const type = await inferTypeFromValue(value);
    fields.get(fieldName).add(type);

    if (type === "Object") {
      // Create nested type name
      const nestedTypeName = prefix ? `${prefix}_${key}` : `${key}Type`;

      // Store nested fields
      if (!nestedTypes[nestedTypeName]) {
        nestedTypes[nestedTypeName] = new Map();
        await analyzeDocument(
          value,
          nestedTypes[nestedTypeName],
          nestedTypeName,
          nestedTypes
        );
      }

      // Update field type to reference nested type
      fields.get(fieldName).delete("Object");
      fields.get(fieldName).add(nestedTypeName);
    } else if (
      Array.isArray(value) &&
      value.length > 0 &&
      typeof value[0] === "object"
    ) {
      // Handle arrays of objects
      const nestedTypeName = prefix ? `${prefix}_${key}Item` : `${key}Item`;

      if (!nestedTypes[nestedTypeName]) {
        nestedTypes[nestedTypeName] = new Map();
        await analyzeDocument(
          value[0],
          nestedTypes[nestedTypeName],
          nestedTypeName,
          nestedTypes
        );
      }

      fields.get(fieldName).delete("Object");
      fields.get(fieldName).add(`[${nestedTypeName}]`);
    }
  }
  return nestedTypes;
}

async function analyzeCollection(collection, sampleSize = 100) {
  const fields = new Map();
  const nestedTypes = {};

  const samples = await collection
    .aggregate([{ $sample: { size: sampleSize } }])
    .toArray();

  for (const doc of samples) {
    await analyzeDocument(doc, fields, "", nestedTypes);
  }

  return { fields, nestedTypes };
}

async function generateGraphQLSchema(uri, dbName, collections) {
  const client = new MongoClient(uri);
  let schema = "";

  try {
    await client.connect();
    console.log("Connected to MongoDB");

    const db = client.db(dbName);

    for (const collectionName of collections) {
      const collection = db.collection(collectionName);
      const { fields, nestedTypes } = await analyzeCollection(collection);

      // Generate nested type definitions first
      for (const [typeName, typeFields] of Object.entries(nestedTypes)) {
        schema += `type ${typeName} {\n`;
        for (const [fieldName, types] of typeFields.entries()) {
          const typeArray = Array.from(types);
          const fieldType = typeArray[0];
          schema += `  ${fieldName}: ${fieldType}!\n`;
        }
        schema += "}\n\n";
      }

      // Generate main type
      schema += `type ${collectionName} {\n`;
      for (const [fieldName, types] of fields.entries()) {
        const typeArray = Array.from(types);
        const fieldType = typeArray[0];

        if (fieldName === "_id") {
          schema += `  id: ID!\n`;
        } else {
          schema += `  ${fieldName}: ${fieldType}!\n`;
        }
      }
      schema += "}\n\n";
    }
  } finally {
    await client.close();
  }

  return schema;
}

async function main() {
  const config = require("./configDb.js");

  try {
    const mongoSchema = await generateGraphQLSchema(
      config.mongodb.uri,
      config.mongodb.dbName,
      config.mongodb.collections
    );

    fs.writeFileSync(
      path.join("./results", "mongodb-schema.graphql"),
      mongoSchema,
      "utf-8"
    );

    const { convertGraphQLToGraphene } = require("./convertToGraphene.cjs");
    const pythonCode = convertGraphQLToGraphene(
      path.join("./results", "mongodb-schema.graphql")
    );
    fs.writeFileSync(
      path.join("./results", "mongodb-schema.py"),
      pythonCode,
      "utf-8"
    );

    console.log(
      "Generated both GraphQL schema and Python Graphene code from MongoDB"
    );
  } catch (error) {
    console.error("Error generating schema:", error);
  }
}

if (require.main === module) {
  main().catch(console.error);
}

module.exports = {
  generateGraphQLSchema,
  analyzeCollection,
  inferTypeFromValue,
};
