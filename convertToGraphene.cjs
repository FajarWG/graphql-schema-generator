const fs = require("fs");
const path = require("path");

function convertTypeToGraphene(type) {
  // Handle list types
  if (type.startsWith("[") && type.endsWith("]")) {
    const innerType = type.slice(1, -1);
    return `graphene.List(${convertTypeToGraphene(innerType)})`;
  }

  // Map GraphQL types to Graphene types
  const typeMap = {
    String: "graphene.String()",
    Int: "graphene.Int()",
    Float: "graphene.Float()",
    Boolean: "graphene.Boolean()",
    ID: "graphene.ID()",
  };

  return typeMap[type] || `graphene.Field('${type}')`;
}

function convertGraphQLToGraphene(schemaPath) {
  // Read the GraphQL schema
  const schema = fs.readFileSync(schemaPath, "utf-8");

  // Split into individual type definitions
  const typeBlocks = schema.split("\n\n");

  // Start building Python code
  let pythonCode = "import graphene\n\n";

  for (const block of typeBlocks) {
    if (!block.trim()) continue;

    // Extract type name and fields
    const typeMatch = block.match(/type\s+(\w+)\s*{([\s\S]*?)}/);
    if (!typeMatch) continue;

    const [_, typeName, fieldsStr] = typeMatch;

    // Start class definition
    pythonCode += `class ${typeName}(graphene.ObjectType):\n`;

    // Process fields
    const fields = fieldsStr.trim().split("\n");
    for (const field of fields) {
      const [name, type] = field
        .trim()
        .split(":")
        .map((s) => s.trim());
      if (!name || !type) continue;

      // Remove the ! for non-null fields
      const baseType = type.replace("!", "");
      const grapheneType = convertTypeToGraphene(baseType);

      // Add field definition
      pythonCode += `    ${name} = ${grapheneType}\n`;
    }

    pythonCode += "\n";
  }

  return pythonCode;
}

function main() {
  const inputPath = path.join(__dirname, "schema.graphql");
  const outputPath = path.join(__dirname, "schema.py");

  try {
    const pythonCode = convertGraphQLToGraphene(inputPath);
    fs.writeFileSync(outputPath, pythonCode);
    console.log(
      `Successfully converted GraphQL schema to Graphene Python code`
    );
    console.log(`Output saved to: ${outputPath}`);
  } catch (error) {
    console.error("Error converting schema:", error);
  }
}

// Run if called directly
if (require.main === module) {
  main();
}

module.exports = {
  convertGraphQLToGraphene,
  convertTypeToGraphene,
};
