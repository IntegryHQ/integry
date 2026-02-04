---
hidden: true
---

# Object Schema

Integry uses [JSON Schema](https://json-schema.org/specification) to define the structure of objects. JSON Schema is a declarative language that allows you to validate, annotate, and describe the structure of JSON data.

## Basic Types

JSON Schema supports the following primitive types:

| Type | Description | Example |
|------|-------------|---------|
| `string` | Text values | `"Hello World"` |
| `number` | Any numeric value | `3.14` |
| `integer` | Whole numbers only | `42` |
| `boolean` | True or false | `true` |
| `array` | Ordered list of values | `[1, 2, 3]` |
| `object` | Key-value pairs | `{"key": "value"}` |
| `null` | Null value | `null` |

## Defining a Simple Object

Here's a basic example of an object schema:

```json
{
  "type": "object",
  "properties": {
    "name": {
      "type": "string",
      "description": "The contact's full name"
    },
    "email": {
      "type": "string",
      "format": "email",
      "description": "The contact's email address"
    },
    "age": {
      "type": "integer",
      "minimum": 0
    }
  },
  "required": ["name", "email"]
}
```

This schema defines an object with three properties where `name` and `email` are required.

## Examples

### Contact Object

```json
{
  "type": "object",
  "properties": {
    "first_name": {
      "type": "string",
      "minLength": 1,
      "maxLength": 100
    },
    "last_name": {
      "type": "string",
      "minLength": 1,
      "maxLength": 100
    },
    "email": {
      "type": "string",
      "format": "email"
    },
    "phone": {
      "type": "string",
      "pattern": "^\\+?[0-9\\s\\-()]+$"
    },
    "tags": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "uniqueItems": true
    }
  },
  "required": ["first_name", "email"]
}
```

### Using Enums

```json
{
  "type": "object",
  "properties": {
    "status": {
      "type": "string",
      "enum": ["active", "inactive", "pending"],
      "description": "The current status of the record"
    },
    "priority": {
      "type": "integer",
      "enum": [1, 2, 3, 4, 5],
      "description": "Priority level from 1 (lowest) to 5 (highest)"
    }
  }
}
```

### Nested Objects

```json
{
  "type": "object",
  "properties": {
    "name": {
      "type": "string"
    },
    "address": {
      "type": "object",
      "properties": {
        "street": { "type": "string" },
        "city": { "type": "string" },
        "country": { "type": "string" },
        "postal_code": { "type": "string" }
      },
      "required": ["city", "country"]
    }
  }
}
```

### Array of Objects

```json
{
  "type": "object",
  "properties": {
    "order_id": {
      "type": "string"
    },
    "line_items": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "product_id": { "type": "string" },
          "quantity": { "type": "integer", "minimum": 1 },
          "price": { "type": "number", "minimum": 0 }
        },
        "required": ["product_id", "quantity"]
      },
      "minItems": 1
    }
  }
}
```

## Annotations

Following keys can be included to provide additional context about the schema:

| Keyword | Description |
|---------|-------------|
| `title` | A short title for the schema |
| `description` | A detailed description |
| `default` | Default value if none is provided |
| `examples` | Example values |

```json
{
  "type": "string",
  "title": "Email Address",
  "description": "The primary email address for the contact",
  "format": "email",
  "examples": ["user@example.com"],
  "default": ""
}
```

## Further Reading

For complete JSON Schema specifications and advanced features like conditional schemas, schema composition (`allOf`, `anyOf`, `oneOf`), and references (`$ref`), see the official documentation:

- [JSON Schema Specification](https://json-schema.org/specification)
- [Understanding JSON Schema](https://json-schema.org/understanding-json-schema)
