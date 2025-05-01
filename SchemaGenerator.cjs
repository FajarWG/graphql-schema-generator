const fs = require("fs");
const path = require("path");
const https = require("https");

async function fetchJsonFromApi(url) {
  return new Promise((resolve, reject) => {
    https
      .get(url, (res) => {
        let data = "";
        res.on("data", (chunk) => {
          data += chunk;
        });
        res.on("end", () => {
          try {
            resolve(JSON.parse(data));
          } catch (error) {
            reject(error);
          }
        });
      })
      .on("error", (error) => {
        reject(error);
      });
  });
}

function readJsonFromFile(filePath) {
  try {
    return JSON.parse(fs.readFileSync(filePath, "utf-8"));
  } catch (error) {
    console.error(`Error reading file ${filePath}:`, error);
    return null;
  }
}

async function processJsonSources(sources) {
  const results = {};

  for (const source of sources) {
    try {
      let jsonData;
      if (source.type === "file") {
        jsonData = readJsonFromFile(source.path);
      } else if (source.type === "api") {
        jsonData = await fetchJsonFromApi(source.url);
      }

      if (jsonData) {
        const types = generateGraphQLTypes(jsonData, source.typeName);
        Object.assign(results, types);
      }
    } catch (error) {
      console.error(`Error processing source ${source.typeName}:`, error);
    }
  }

  return results;
}

function inferGraphQLType(value) {
  if (typeof value === "string") return "String";
  if (typeof value === "number")
    return Number.isInteger(value) ? "Int" : "Float";
  if (typeof value === "boolean") return "Boolean";
  if (Array.isArray(value)) {
    if (value.length === 0) return "[String]";
    return `[${inferGraphQLType(value[0])}]`;
  }
  if (typeof value === "object" && value !== null) return "Object";
  return "String";
}

function generateGraphQLTypes(obj, typeName = "Root", types = {}) {
  const fields = {};
  for (const [key, value] of Object.entries(obj)) {
    const gqlType = inferGraphQLType(value);
    if (gqlType === "Object") {
      const nestedTypeName = `${typeName}_${key}`;
      fields[key] = nestedTypeName;
      generateGraphQLTypes(value, nestedTypeName, types);
    } else if (gqlType.startsWith("[")) {
      const innerType = inferGraphQLType(value[0]);
      if (innerType === "Object") {
        const nestedTypeName = `${typeName}_${key}`;
        fields[key] = `[${nestedTypeName}]`;
        generateGraphQLTypes(value[0], nestedTypeName, types);
      } else {
        fields[key] = gqlType;
      }
    } else {
      fields[key] = gqlType;
    }
  }

  types[typeName] = fields;
  return types;
}

function toGraphQLSchema(types) {
  return Object.entries(types)
    .map(([typeName, fields]) => {
      const fieldStrings = Object.entries(fields)
        .map(([key, type]) => `  ${key}: ${type}!`)
        .join("\n");
      return `type ${typeName} {\n${fieldStrings}\n}`;
    })
    .join("\n\n");
}

async function main() {
  const config = require("./configRest.js");

  try {
    const combinedTypes = await processJsonSources(config);
    const schema = toGraphQLSchema(combinedTypes);
    console.log(schema);

    fs.writeFileSync(path.join("./results", "schema.graphql"), schema, "utf-8");

    const { convertGraphQLToGraphene } = require("./convertToGraphene.cjs");
    const pythonCode = convertGraphQLToGraphene(
      path.join("./results", "schema.graphql")
    );
    fs.writeFileSync(path.join("./results", "schema.py"), pythonCode, "utf-8");
  } catch (error) {
    console.error("Error generating schema:", error);
  }
}

main();
