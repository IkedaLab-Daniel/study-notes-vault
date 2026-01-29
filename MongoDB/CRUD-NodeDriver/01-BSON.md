# MongoDB BSON & Node.js Driver Guide

## What is BSON?

**BSON** (Binary JSON) is a binary-encoded serialization format used by MongoDB to store documents and make remote procedure calls.

- **Created for:** MongoDB's internal data storage and network transfer
- **Key benefit:** Efficient storage, fast traversal, and additional data types beyond JSON

---

## BSON vs JSON Comparison

| Feature | JSON | BSON |
|---------|------|------|
| **Format** | Text-based | Binary-encoded |
| **Human-readable** | Yes | No (binary) |
| **Size** | Smaller (text) | Larger (includes type info + length prefixes) |
| **Parsing Speed** | Slower | Faster (optimized for traversal) |
| **Data Types** | Limited (string, number, boolean, null, object, array) | Extended (Date, ObjectId, Binary, Decimal128, etc.) |
| **Use Case** | Data interchange, APIs | MongoDB storage, internal operations |
| **Encoding/Decoding** | Native in JavaScript | Requires BSON library |

### Key Differences

```javascript
// JSON limitations
{
  "date": "2026-01-30T10:00:00Z",  // String, not a Date object
  "number": 123.45,                 // Only doubles, no Int32/Int64
  "id": "507f1f77bcf86cd799439011" // String, not ObjectId
}

// BSON advantages
{
  "date": ISODate("2026-01-30T10:00:00Z"), // Native Date type
  "count": NumberInt(42),                   // 32-bit integer
  "price": NumberDecimal("123.45"),         // Precise decimal
  "_id": ObjectId("507f1f77bcf86cd799439011") // MongoDB ObjectId
}
```

---

## BSON Data Types

### Core BSON Types in MongoDB

| Type | BSON Type Number | Description |
|------|------------------|-------------|
| **Double** | 1 | 64-bit floating point |
| **String** | 2 | UTF-8 string |
| **Object** | 3 | Embedded document |
| **Array** | 4 | Array of values |
| **Binary data** | 5 | Binary data/byte array |
| **ObjectId** | 7 | 12-byte unique identifier |
| **Boolean** | 8 | true/false |
| **Date** | 9 | UTC datetime (64-bit integer) |
| **Null** | 10 | Null value |
| **32-bit integer** | 16 | Int32 |
| **64-bit integer** | 18 | Int64/Long |
| **Decimal128** | 19 | 128-bit decimal floating point |

---

## Using BSON in Node.js Driver

### 1. Installation & Setup

```bash
npm install mongodb
```

```javascript
const { MongoClient, ObjectId, Binary, Long, Decimal128 } = require('mongodb');
// or ES6
import { MongoClient, ObjectId, Binary, Long, Decimal128 } from 'mongodb';
```

### 2. ObjectId - Most Common BSON Type

```javascript
const { ObjectId } = require('mongodb');

// Create new ObjectId
const id = new ObjectId();
console.log(id); // ObjectId('507f1f77bcf86cd799439011')

// Convert string to ObjectId
const idFromString = new ObjectId('507f1f77bcf86cd799439011');

// Get timestamp from ObjectId (first 4 bytes)
const timestamp = id.getTimestamp();
console.log(timestamp); // Date object

// Check if valid ObjectId string
ObjectId.isValid('507f1f77bcf86cd799439011'); // true
ObjectId.isValid('invalid'); // false

// Usage in queries
await collection.findOne({ _id: new ObjectId('507f1f77bcf86cd799439011') });

// Convert ObjectId to string
const idString = id.toString();
// or
const idString = id.toHexString();
```

### 3. Date Type

```javascript
// MongoDB stores dates as BSON Date (64-bit UTC milliseconds)

// Insert with JavaScript Date
await collection.insertOne({
  name: 'Event',
  createdAt: new Date(), // Automatically converted to BSON Date
  eventDate: new Date('2026-01-30T10:00:00Z')
});

// Query by date range
await collection.find({
  createdAt: {
    $gte: new Date('2026-01-01'),
    $lt: new Date('2026-12-31')
  }
}).toArray();

// Important: Always use Date objects, not strings
// ❌ Bad
await collection.insertOne({ date: '2026-01-30' }); // Stored as string!

// ✅ Good
await collection.insertOne({ date: new Date('2026-01-30') }); // Stored as BSON Date
```

### 4. Binary Data

```javascript
const { Binary } = require('mongodb');

// Store binary data
const binaryData = new Binary(Buffer.from('Hello World'));

await collection.insertOne({
  filename: 'document.pdf',
  data: binaryData,
  subtype: Binary.SUBTYPE_DEFAULT // 0
});

// Binary subtypes
// SUBTYPE_DEFAULT (0) - Generic binary data
// SUBTYPE_FUNCTION (1) - Function
// SUBTYPE_BYTE_ARRAY (2) - Binary (Old)
// SUBTYPE_UUID (3) - UUID (Old)
// SUBTYPE_UUID_NEW (4) - UUID
// SUBTYPE_MD5 (5) - MD5
// SUBTYPE_ENCRYPTED (6) - Encrypted data
// SUBTYPE_USER_DEFINED (128) - User-defined

// Store UUID
const uuid = new Binary(Buffer.from('550e8400-e29b-41d4-a716-446655440000'.replace(/-/g, ''), 'hex'), Binary.SUBTYPE_UUID);
```

### 5. Long (64-bit Integer)

```javascript
const { Long } = require('mongodb');

// For large integers beyond JavaScript's safe integer range
// JavaScript safe range: -(2^53 - 1) to (2^53 - 1)

const bigNumber = Long.fromNumber(9007199254740992); // Beyond safe range
// or
const bigNumber = Long.fromString('9007199254740992');

await collection.insertOne({
  userId: 123,
  viewCount: bigNumber
});

// Retrieve and work with Long
const doc = await collection.findOne({ userId: 123 });
const count = doc.viewCount.toNumber(); // Convert back to JS number (if in safe range)
```

### 6. Decimal128 (Precise Decimal)

```javascript
const { Decimal128 } = require('mongodb');

// For financial calculations requiring precision
// JavaScript numbers are floating point (imprecise for decimals)

const price = Decimal128.fromString('99.99');
const tax = Decimal128.fromString('8.50');

await collection.insertOne({
  product: 'Widget',
  price: price,
  tax: tax
});

// Retrieve Decimal128
const product = await collection.findOne({ product: 'Widget' });
const priceValue = product.price.toString(); // '99.99'

// Important for financial data
// ❌ Bad: 0.1 + 0.2 = 0.30000000000000004
// ✅ Good: Decimal128 maintains precision
```

---

## Common Node.js Driver Patterns

### 1. Insert Documents with BSON Types

```javascript
await collection.insertOne({
  _id: new ObjectId(), // Usually auto-generated, but can specify
  username: 'john_doe',
  email: 'john@example.com',
  age: 30,
  balance: Decimal128.fromString('1500.50'),
  createdAt: new Date(),
  lastLogin: new Date(),
  profilePicture: new Binary(Buffer.from(imageData)),
  isActive: true,
  tags: ['premium', 'verified'],
  metadata: {
    loginCount: Long.fromNumber(150),
    preferences: { theme: 'dark' }
  }
});
```

### 2. Query with BSON Types

```javascript
// Find by ObjectId
const user = await collection.findOne({ 
  _id: new ObjectId('507f1f77bcf86cd799439011') 
});

// Date range query
const recentUsers = await collection.find({
  createdAt: { 
    $gte: new Date('2026-01-01'),
    $lt: new Date('2026-02-01')
  }
}).toArray();

// Decimal comparison
const expensiveProducts = await collection.find({
  price: { $gt: Decimal128.fromString('100.00') }
}).toArray();
```

### 3. Update with BSON Types

```javascript
await collection.updateOne(
  { _id: new ObjectId('507f1f77bcf86cd799439011') },
  {
    $set: { 
      lastModified: new Date(),
      balance: Decimal128.fromString('2000.00')
    },
    $inc: { 
      loginCount: Long.fromNumber(1) 
    }
  }
);
```

### 4. Aggregation with BSON Types

```javascript
const result = await collection.aggregate([
  {
    $match: {
      createdAt: { $gte: new Date('2026-01-01') }
    }
  },
  {
    $group: {
      _id: null,
      totalBalance: { $sum: '$balance' }, // Works with Decimal128
      count: { $sum: 1 }
    }
  }
]).toArray();
```

---

## Type Conversion & Handling

### JavaScript to BSON (Automatic)

```javascript
// These conversions happen automatically in Node.js driver
{
  string: "text",        // → BSON String
  number: 42,            // → BSON Double (default)
  number: 42.5,          // → BSON Double
  boolean: true,         // → BSON Boolean
  date: new Date(),      // → BSON Date
  null: null,            // → BSON Null
  array: [1, 2, 3],      // → BSON Array
  object: { a: 1 }       // → BSON Object/Document
}
```

### Explicit Type Specification

```javascript
// When you need specific BSON types (not automatic)
const { Int32, Long, Decimal128 } = require('mongodb');

{
  count: new Int32(42),              // 32-bit integer
  bigNumber: Long.fromNumber(1000),  // 64-bit integer
  price: Decimal128.fromString('99.99'), // Precise decimal
  _id: new ObjectId(),               // ObjectId
  data: new Binary(buffer)           // Binary data
}
```

---

## Best Practices for Certification

### 1. Always Use Proper Types

```javascript
// ❌ Avoid storing dates as strings
{ createdAt: "2026-01-30" }

// ✅ Use Date objects
{ createdAt: new Date("2026-01-30") }

// ❌ Don't use strings for ObjectIds in queries
collection.findOne({ _id: "507f1f77bcf86cd799439011" })

// ✅ Convert to ObjectId
collection.findOne({ _id: new ObjectId("507f1f77bcf86cd799439011") })
```

### 2. Financial Data Precision

```javascript
// ❌ JavaScript numbers lose precision
{ price: 99.99 } // May become 99.98999999999999

// ✅ Use Decimal128
{ price: Decimal128.fromString("99.99") }
```

### 3. Large Numbers

```javascript
// ❌ Numbers beyond safe integer range
{ views: 9007199254740993 } // Loses precision!

// ✅ Use Long
{ views: Long.fromString("9007199254740993") }
```

### 4. ObjectId Validation

```javascript
// Always validate ObjectId strings before conversion
if (ObjectId.isValid(idString)) {
  const user = await collection.findOne({ _id: new ObjectId(idString) });
} else {
  throw new Error('Invalid ObjectId format');
}
```

---

## Common Exam Topics

### Know These BSON Concepts:

1. **BSON is binary, not human-readable** (unlike JSON)
2. **BSON includes type information** (JSON doesn't)
3. **BSON supports more data types** than JSON (Date, ObjectId, Binary, etc.)
4. **ObjectId is 12 bytes**: 4-byte timestamp + 5-byte random + 3-byte counter
5. **Dates are stored as UTC milliseconds** (64-bit integer)
6. **Decimal128 for financial precision** (not JavaScript numbers)
7. **Long for 64-bit integers** beyond JavaScript safe range
8. **BSON is optimized for traversal**, not size

### Common Pitfalls:

```javascript
// ❌ PITFALL: Comparing ObjectId with string
if (doc._id === '507f1f77bcf86cd799439011') // Always false!

// ✅ CORRECT: Convert to string first
if (doc._id.toString() === '507f1f77bcf86cd799439011')

// ❌ PITFALL: Decimal arithmetic with JavaScript
const total = 0.1 + 0.2; // 0.30000000000000004

// ✅ CORRECT: Use Decimal128 or calculate in aggregation
const total = Decimal128.fromString('0.1') // Store as BSON, calculate in DB

// ❌ PITFALL: Date string comparisons
{ createdAt: { $gte: "2026-01-01" } } // String comparison!

// ✅ CORRECT: Use Date objects
{ createdAt: { $gte: new Date("2026-01-01") } }
```

---

## Quick Reference Card

```javascript
const { 
  MongoClient, 
  ObjectId,    // _id fields
  Binary,      // Binary data, files, UUIDs
  Long,        // Large integers > 2^53
  Decimal128,  // Precise decimals (money)
  Int32,       // 32-bit integers
  Double,      // 64-bit floating point (default for numbers)
  Timestamp    // Internal MongoDB timestamp (not for user data)
} = require('mongodb');

// Most used in certification:
const doc = {
  _id: new ObjectId(),                    // Auto-generated if omitted
  createdAt: new Date(),                  // Always use Date objects
  price: Decimal128.fromString("99.99"),  // Financial data
  count: Long.fromNumber(1000000),        // Large integers
  active: true,                           // Boolean
  tags: ["a", "b"],                       // Array
  meta: { key: "value" }                  // Nested document
};
```

---

## Summary

- **BSON = Binary JSON**: Optimized for MongoDB storage and traversal
- **More types than JSON**: ObjectId, Date, Binary, Decimal128, Long
- **Node.js Driver**: Automatically handles most conversions
- **Key types to master**: ObjectId, Date, Decimal128, Long
- **For certification**: Know when to use explicit BSON types vs. automatic conversion
- **Common mistakes**: String dates, string ObjectIds, floating-point precision issues