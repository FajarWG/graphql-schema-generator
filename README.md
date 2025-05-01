# GraphQL Schema Generator

A tool to generate GraphQL schemas from various data sources including JSON files, APIs, and MongoDB collections. The generated schemas can be output as both `.graphql` files and Python Graphene classes.

## Features

- Generate GraphQL schemas from:
  - JSON files
  - REST APIs
  - MongoDB collections
- Convert schemas to:
  - `.graphql` files
  - Python Graphene classes
- Support for:
  - Nested objects
  - Arrays
  - Custom types
  - Complex data structures

## Installation

1. Clone the repository

```bash
git clone https://github.com/FajarWG/graphql-schema-generator.git
```

2. Install dependencies

```bash
cd graphql-schema-generator
npm install
```

## Usage

### 1. JSON/API to GraphQL Schema

Edit the configRest.js file to customize which json or Rest API endpoint will be generated to the graphql schema.

```javascript
[
  {
    type: "file",
    path: path.join(__dirname, "/dumpJson/input.json"),
    typeName: "UserData",
  },
  {
    type: "api",
    url: "https://api.example.com/data",
    typeName: "ApiData",
  },
];
```

To generate, just do the command:

```bash
npm run generate
```

### 2. MongoDB to GraphQL Schema

Configure your MongoDB connection in `configDb.js`:

```javascript
module.exports = {
  mongodb: {
    uri: "mongodb://localhost:27017",
    dbName: "your_database",
    collections: ["collection1", "collection2"],
  },
};
```

Generate schema:

```bash
npm run generate:db
```

## Output Examples

### GraphQL Schema (.graphql)

```graphql
type UserData {
  id: ID!
  name: String!
  email: String!
  age: Int!
}

type NestedData {
  items: [ItemType!]!
  count: Int!
}

type ItemType {
  id: String!
  value: Float!
}
```

### Python Graphene Classes (.py)

```python
import graphene

class UserData(graphene.ObjectType):
    id = graphene.ID()
    name = graphene.String()
    email = graphene.String()
    age = graphene.Int()

class ItemType(graphene.ObjectType):
    id = graphene.String()
    value = graphene.Float()

class NestedData(graphene.ObjectType):
    items = graphene.List(ItemType)
    count = graphene.Int()
```

## Requirements

- Node.js >= 14

## Dependencies

- `mongodb`: MongoDB driver for Node.js

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## Authors

- [Github: @FajarWG](https://www.github.com/FajarWG)
- [LinkedIn: @fajarwg](https://www.linkedin.com/in/fajarwg)
- [Instagram: @fajarwgumelar](https://www.instagram.com/fajarwgumelar/)
