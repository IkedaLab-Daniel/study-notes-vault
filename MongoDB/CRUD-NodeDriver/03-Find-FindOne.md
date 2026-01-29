# MongoDB Find & FindOne - Node.js Driver

## Overview

MongoDB provides two primary methods for reading/querying documents:
- **`findOne()`** - Returns a single document (first match)
- **`find()`** - Returns a cursor to multiple documents

---

## findOne() Method

### Basic Syntax

```javascript
const document = await collection.findOne(filter, options);
```

### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `filter` | Object | Query criteria (empty {} finds any document) |
| `options` | Object | Optional settings (projection, sort, etc.) |

### Return Value

- Returns the **first matching document** or **`null`** if no match found
- Returns an **Object** (not a cursor)
- Immediately retrieves the document (no need for `.toArray()`)

### Basic Examples

```javascript
const { MongoClient, ObjectId } = require('mongodb');

const client = new MongoClient('mongodb://localhost:27017');
await client.connect();
const db = client.db('myDatabase');
const users = db.collection('users');

// Find any single document
const anyUser = await users.findOne();
console.log(anyUser); // First document in collection or null

// Find by _id
const user = await users.findOne({ 
  _id: new ObjectId('507f1f77bcf86cd799439011') 
});

// Find by field
const user = await users.findOne({ 
  email: 'john@example.com' 
});

// Find with multiple conditions (AND)
const user = await users.findOne({
  email: 'john@example.com',
  age: { $gte: 18 },
  isActive: true
});
```

### Handling Null Results

```javascript
const user = await users.findOne({ email: 'notfound@example.com' });

if (user) {
  console.log('User found:', user.name);
} else {
  console.log('No user found');
}

// Or use optional chaining
console.log(user?.name ?? 'Not found');
```

---

## find() Method

### Basic Syntax

```javascript
const cursor = collection.find(filter, options);
const documents = await cursor.toArray();
```

### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `filter` | Object | Query criteria (empty {} finds all documents) |
| `options` | Object | Optional settings (projection, sort, limit, skip, etc.) |

### Return Value

- Returns a **Cursor** object (not the actual documents)
- Must call cursor methods to retrieve documents:
  - `.toArray()` - Get all results as array
  - `.forEach()` - Iterate through results
  - `.next()` - Get next document
  - `.hasNext()` - Check if more documents available

### Basic Examples

```javascript
// Find all documents
const cursor = users.find();
const allUsers = await cursor.toArray();
console.log(allUsers); // Array of all user documents

// Find with filter
const activeUsers = await users.find({ 
  isActive: true 
}).toArray();

// Find with multiple conditions
const results = await users.find({
  age: { $gte: 18, $lte: 65 },
  country: 'USA',
  isActive: true
}).toArray();
```

### Cursor Methods

```javascript
// Method 1: toArray() - Get all at once
const users = await collection.find({ age: { $gte: 18 } }).toArray();

// Method 2: forEach() - Iterate one by one
await collection.find({ age: { $gte: 18 } }).forEach(user => {
  console.log(user.name);
});

// Method 3: for await...of - Async iteration
const cursor = collection.find({ age: { $gte: 18 } });
for await (const user of cursor) {
  console.log(user.name);
}

// Method 4: next() and hasNext() - Manual iteration
const cursor = collection.find({ age: { $gte: 18 } });
while (await cursor.hasNext()) {
  const user = await cursor.next();
  console.log(user.name);
}

// Method 5: Stream - For very large datasets
const cursor = collection.find({ age: { $gte: 18 } });
const stream = cursor.stream();
stream.on('data', user => console.log(user.name));
stream.on('end', () => console.log('Done'));
```

---

## Query Filters & Operators

### Comparison Operators

```javascript
// Equal
await users.find({ age: 30 }).toArray();

// $eq (explicit equal)
await users.find({ age: { $eq: 30 } }).toArray();

// $ne (not equal)
await users.find({ age: { $ne: 30 } }).toArray();

// $gt (greater than)
await users.find({ age: { $gt: 18 } }).toArray();

// $gte (greater than or equal)
await users.find({ age: { $gte: 18 } }).toArray();

// $lt (less than)
await users.find({ age: { $lt: 65 } }).toArray();

// $lte (less than or equal)
await users.find({ age: { $lte: 65 } }).toArray();

// Range query
await users.find({ 
  age: { $gte: 18, $lte: 65 } 
}).toArray();

// $in (matches any value in array)
await users.find({ 
  status: { $in: ['active', 'pending'] } 
}).toArray();

// $nin (not in array)
await users.find({ 
  status: { $nin: ['banned', 'deleted'] } 
}).toArray();
```

### Logical Operators

```javascript
// $and (implicit when multiple fields)
await users.find({
  age: { $gte: 18 },
  isActive: true
}).toArray();

// $and (explicit - for same field)
await users.find({
  $and: [
    { age: { $gte: 18 } },
    { age: { $lte: 65 } }
  ]
}).toArray();

// $or
await users.find({
  $or: [
    { email: 'john@example.com' },
    { username: 'john_doe' }
  ]
}).toArray();

// $nor (not any of the conditions)
await users.find({
  $nor: [
    { status: 'banned' },
    { isDeleted: true }
  ]
}).toArray();

// $not
await users.find({
  age: { $not: { $gte: 18 } }
}).toArray();

// Complex combinations
await users.find({
  $and: [
    { age: { $gte: 18 } },
    {
      $or: [
        { country: 'USA' },
        { country: 'Canada' }
      ]
    }
  ]
}).toArray();
```

### Element Operators

```javascript
// $exists (field exists)
await users.find({ 
  middleName: { $exists: true } 
}).toArray();

// $exists (field doesn't exist)
await users.find({ 
  deletedAt: { $exists: false } 
}).toArray();

// $type (check BSON type)
await users.find({ 
  age: { $type: 'number' } 
}).toArray();

// $type with multiple types
await users.find({ 
  age: { $type: ['int', 'long', 'double'] } 
}).toArray();
```

### Array Operators

```javascript
// $all (array contains all elements)
await users.find({ 
  tags: { $all: ['premium', 'verified'] } 
}).toArray();

// $elemMatch (array element matches conditions)
await users.find({
  scores: { 
    $elemMatch: { $gte: 80, $lte: 100 } 
  }
}).toArray();

// $size (array has specific length)
await users.find({ 
  tags: { $size: 3 } 
}).toArray();

// Array contains value (simple)
await users.find({ 
  tags: 'premium' 
}).toArray();

// Array contains any value in list
await users.find({ 
  tags: { $in: ['premium', 'verified'] } 
}).toArray();
```

### String Operators (Regex)

```javascript
// $regex - Pattern matching
await users.find({ 
  name: { $regex: /^John/i } 
}).toArray();

// $regex with options
await users.find({ 
  email: { 
    $regex: '.*@gmail\\.com$',
    $options: 'i' // case insensitive
  } 
}).toArray();

// Contains substring (case insensitive)
await users.find({ 
  name: { $regex: 'john', $options: 'i' } 
}).toArray();

// Starts with
await users.find({ 
  name: { $regex: '^John' } 
}).toArray();

// Ends with
await users.find({ 
  email: { $regex: '@gmail\\.com$' } 
}).toArray();
```

### Nested Document Queries

```javascript
// Exact match (entire nested document)
await users.find({
  address: {
    street: '123 Main St',
    city: 'New York',
    zip: '10001'
  }
}).toArray();

// Dot notation (specific field in nested document)
await users.find({ 
  'address.city': 'New York' 
}).toArray();

await users.find({ 
  'profile.age': { $gte: 18 },
  'profile.country': 'USA'
}).toArray();

// Nested array elements
await users.find({ 
  'orders.0.status': 'shipped' // First order status
}).toArray();
```

---

## Projection (Field Selection)

### Basic Projection

```javascript
// Include specific fields (1 = include, _id included by default)
const users = await collection.find(
  { age: { $gte: 18 } },
  { projection: { name: 1, email: 1 } }
).toArray();
// Result: [{ _id: ..., name: '...', email: '...' }]

// Exclude _id
const users = await collection.find(
  { age: { $gte: 18 } },
  { projection: { name: 1, email: 1, _id: 0 } }
).toArray();
// Result: [{ name: '...', email: '...' }]

// Exclude specific fields (0 = exclude)
const users = await collection.find(
  { age: { $gte: 18 } },
  { projection: { password: 0, ssn: 0 } }
).toArray();
// Result: All fields except password and ssn
```

### Projection Rules

```javascript
// ✅ VALID: Include fields
{ projection: { name: 1, email: 1 } }

// ✅ VALID: Exclude fields
{ projection: { password: 0, secret: 0 } }

// ✅ VALID: Include fields + exclude _id
{ projection: { name: 1, email: 1, _id: 0 } }

// ❌ INVALID: Cannot mix include and exclude (except _id)
{ projection: { name: 1, password: 0 } } // Error!
```

### Nested Field Projection

```javascript
// Include nested fields
const users = await collection.find(
  {},
  { projection: { 
    'profile.firstName': 1, 
    'profile.lastName': 1,
    'address.city': 1 
  }}
).toArray();

// Exclude nested fields
const users = await collection.find(
  {},
  { projection: { 
    'profile.ssn': 0,
    'payment.cardNumber': 0 
  }}
).toArray();
```

### Array Projection Operators

```javascript
// $slice - Limit array elements
const users = await collection.find(
  {},
  { projection: { 
    name: 1,
    tags: { $slice: 5 } // First 5 elements
  }}
).toArray();

// $slice with skip
{ projection: { tags: { $slice: [10, 5] } }} // Skip 10, return 5

// $elemMatch - First matching array element
const users = await collection.find(
  {},
  { projection: { 
    name: 1,
    scores: { $elemMatch: { $gte: 80 } }
  }}
).toArray();
```

---

## Sort, Limit, Skip

### Sort

```javascript
// Ascending (1)
const users = await collection.find()
  .sort({ age: 1 })
  .toArray();

// Descending (-1)
const users = await collection.find()
  .sort({ createdAt: -1 })
  .toArray();

// Multiple fields
const users = await collection.find()
  .sort({ age: -1, name: 1 })
  .toArray();

// Using options parameter
const users = await collection.find(
  { isActive: true },
  { sort: { age: -1 } }
).toArray();
```

### Limit

```javascript
// Get first 10 documents
const users = await collection.find()
  .limit(10)
  .toArray();

// Combined with filter
const topUsers = await collection.find({ isActive: true })
  .sort({ score: -1 })
  .limit(10)
  .toArray();

// Using options parameter
const users = await collection.find(
  { isActive: true },
  { limit: 10 }
).toArray();
```

### Skip

```javascript
// Skip first 20 documents
const users = await collection.find()
  .skip(20)
  .toArray();

// Pagination pattern
const page = 2;
const pageSize = 10;
const users = await collection.find()
  .skip((page - 1) * pageSize)
  .limit(pageSize)
  .toArray();

// Using options parameter
const users = await collection.find(
  { isActive: true },
  { skip: 20, limit: 10 }
).toArray();
```

### Combining Sort, Limit, Skip

```javascript
// Order matters: sort -> skip -> limit
const users = await collection.find({ isActive: true })
  .sort({ createdAt: -1 })
  .skip(20)
  .limit(10)
  .toArray();

// All in options
const users = await collection.find(
  { isActive: true },
  {
    sort: { createdAt: -1 },
    skip: 20,
    limit: 10,
    projection: { name: 1, email: 1 }
  }
).toArray();
```

---

## findOne vs find Comparison

| Feature | findOne | find |
|---------|---------|------|
| **Return Type** | Object or null | Cursor |
| **Results** | Single document (first match) | Multiple documents |
| **Needs toArray()** | No | Yes (for array of results) |
| **Performance** | Stops after first match | Retrieves all matches |
| **Null Handling** | Returns null if no match | Returns empty cursor |
| **Use Case** | Get one specific document | Get multiple documents |

### When to Use findOne

```javascript
// ✅ Get by unique identifier
const user = await users.findOne({ 
  _id: new ObjectId('...') 
});

// ✅ Check if exists
const existingUser = await users.findOne({ 
  email: userEmail 
});
if (existingUser) {
  throw new Error('Email already exists');
}

// ✅ Get most recent
const latestOrder = await orders.findOne(
  { userId: currentUserId },
  { sort: { createdAt: -1 } }
);

// ✅ Get any example document
const sampleProduct = await products.findOne();
```

### When to Use find

```javascript
// ✅ Get all matching documents
const activeUsers = await users.find({ 
  isActive: true 
}).toArray();

// ✅ Pagination
const page1 = await users.find()
  .skip(0)
  .limit(10)
  .toArray();

// ✅ Large result sets with cursor
const cursor = users.find({ country: 'USA' });
for await (const user of cursor) {
  await processUser(user);
}

// ✅ Count matches
const count = await users.find({ isActive: true }).count();
```

---

## Additional Cursor Methods

### count() and countDocuments()

```javascript
// count() - Deprecated, use countDocuments()
const count = await collection.find({ age: { $gte: 18 } }).count();

// countDocuments() - Recommended
const count = await collection.countDocuments({ age: { $gte: 18 } });

// estimatedDocumentCount() - Fast, no filter, approximate
const total = await collection.estimatedDocumentCount();
```

### explain()

```javascript
// Get query execution plan
const explanation = await collection.find({ age: { $gte: 18 } })
  .explain();

console.log(explanation.executionStats);
// Shows if index was used, documents scanned, etc.
```

### limit() Special Cases

```javascript
// Get first document (alternative to findOne)
const firstUser = await users.find()
  .limit(1)
  .toArray()
  .then(arr => arr[0]);

// But findOne is clearer
const firstUser = await users.findOne();
```

---

## Complete Working Examples

### Example 1: User Lookup and Authentication

```javascript
async function authenticateUser(email, password) {
  const { MongoClient } = require('mongodb');
  const bcrypt = require('bcrypt');
  
  const client = new MongoClient('mongodb://localhost:27017');
  
  try {
    await client.connect();
    const db = client.db('myApp');
    const users = db.collection('users');
    
    // Find user by email
    const user = await users.findOne(
      { email: email },
      { projection: { 
        password: 1, 
        isActive: 1, 
        role: 1,
        name: 1 
      }}
    );
    
    if (!user) {
      throw new Error('User not found');
    }
    
    if (!user.isActive) {
      throw new Error('Account is disabled');
    }
    
    // Verify password
    const isValid = await bcrypt.compare(password, user.password);
    
    if (!isValid) {
      throw new Error('Invalid password');
    }
    
    // Return user without password
    delete user.password;
    return user;
    
  } finally {
    await client.close();
  }
}
```

### Example 2: Pagination with Total Count

```javascript
async function getUsersPaginated(page = 1, pageSize = 10, filters = {}) {
  const { MongoClient } = require('mongodb');
  
  const client = new MongoClient('mongodb://localhost:27017');
  
  try {
    await client.connect();
    const db = client.db('myApp');
    const users = db.collection('users');
    
    // Get total count
    const totalCount = await users.countDocuments(filters);
    
    // Get paginated results
    const results = await users.find(filters)
      .sort({ createdAt: -1 })
      .skip((page - 1) * pageSize)
      .limit(pageSize)
      .project({ password: 0 }) // Exclude password
      .toArray();
    
    return {
      data: results,
      pagination: {
        page,
        pageSize,
        totalCount,
        totalPages: Math.ceil(totalCount / pageSize),
        hasNextPage: page * pageSize < totalCount,
        hasPrevPage: page > 1
      }
    };
    
  } finally {
    await client.close();
  }
}

// Usage
const result = await getUsersPaginated(2, 20, { isActive: true });
console.log(result.data); // Array of 20 users
console.log(result.pagination); // Pagination metadata
```

### Example 3: Search with Multiple Criteria

```javascript
async function searchProducts(searchParams) {
  const { MongoClient } = require('mongodb');
  
  const client = new MongoClient('mongodb://localhost:27017');
  
  try {
    await client.connect();
    const db = client.db('ecommerce');
    const products = db.collection('products');
    
    // Build dynamic query
    const query = {};
    
    if (searchParams.keyword) {
      query.$or = [
        { name: { $regex: searchParams.keyword, $options: 'i' } },
        { description: { $regex: searchParams.keyword, $options: 'i' } },
        { tags: { $regex: searchParams.keyword, $options: 'i' } }
      ];
    }
    
    if (searchParams.category) {
      query.category = searchParams.category;
    }
    
    if (searchParams.minPrice || searchParams.maxPrice) {
      query.price = {};
      if (searchParams.minPrice) query.price.$gte = searchParams.minPrice;
      if (searchParams.maxPrice) query.price.$lte = searchParams.maxPrice;
    }
    
    if (searchParams.inStock) {
      query.stock = { $gt: 0 };
    }
    
    // Execute search
    const products = await collection.find(query)
      .sort({ [searchParams.sortBy || 'createdAt']: -1 })
      .limit(searchParams.limit || 50)
      .toArray();
    
    return products;
    
  } finally {
    await client.close();
  }
}

// Usage
const results = await searchProducts({
  keyword: 'laptop',
  category: 'Electronics',
  minPrice: 500,
  maxPrice: 2000,
  inStock: true,
  sortBy: 'price',
  limit: 20
});
```

### Example 4: Processing Large Dataset with Cursor

```javascript
async function processAllActiveUsers() {
  const { MongoClient } = require('mongodb');
  
  const client = new MongoClient('mongodb://localhost:27017');
  
  try {
    await client.connect();
    const db = client.db('myApp');
    const users = db.collection('users');
    
    const cursor = users.find({ isActive: true });
    
    let processedCount = 0;
    let errorCount = 0;
    
    // Process one by one to avoid loading all into memory
    for await (const user of cursor) {
      try {
        await sendEmailNotification(user.email);
        processedCount++;
        
        if (processedCount % 100 === 0) {
          console.log(`Processed ${processedCount} users...`);
        }
      } catch (error) {
        console.error(`Error processing user ${user._id}:`, error);
        errorCount++;
      }
    }
    
    console.log(`Complete: ${processedCount} processed, ${errorCount} errors`);
    
  } finally {
    await client.close();
  }
}
```

---

## Performance Best Practices

### 1. Use Projection to Limit Data Transfer

```javascript
// ❌ Bad - Retrieves all fields
const users = await collection.find({ age: { $gte: 18 } }).toArray();

// ✅ Good - Only get needed fields
const users = await collection.find(
  { age: { $gte: 18 } },
  { projection: { name: 1, email: 1, _id: 0 } }
).toArray();
```

### 2. Use Indexes for Common Queries

```javascript
// Create index on frequently queried field
await collection.createIndex({ email: 1 });
await collection.createIndex({ age: 1 });

// Compound index for multi-field queries
await collection.createIndex({ country: 1, age: -1 });

// Now queries are fast
const users = await collection.find({ email: 'john@example.com' }).toArray();
```

### 3. Limit Results

```javascript
// ❌ Bad - Could return millions of documents
const users = await collection.find({ isActive: true }).toArray();

// ✅ Good - Limit results
const users = await collection.find({ isActive: true })
  .limit(100)
  .toArray();
```

### 4. Use Cursor for Large Datasets

```javascript
// ❌ Bad - Loads all into memory at once
const allUsers = await collection.find().toArray();
for (const user of allUsers) {
  await processUser(user);
}

// ✅ Good - Process one at a time
const cursor = collection.find();
for await (const user of cursor) {
  await processUser(user);
}
```

### 5. findOne for Single Document

```javascript
// ❌ Bad - Returns cursor, needs toArray(), gets all matches
const users = await collection.find({ _id: userId }).toArray();
const user = users[0];

// ✅ Good - Returns document directly, stops after first match
const user = await collection.findOne({ _id: userId });
```

---

## Common Certification Pitfalls

### 1. Forgetting toArray() with find()

```javascript
// ❌ Wrong - cursor is not an array
const users = collection.find({ age: { $gte: 18 } });
console.log(users.length); // undefined! users is a Cursor

// ✅ Correct
const users = await collection.find({ age: { $gte: 18 } }).toArray();
console.log(users.length); // Works!
```

### 2. Not Checking for Null with findOne()

```javascript
// ❌ Wrong - will crash if user not found
const user = await collection.findOne({ email: 'unknown@example.com' });
console.log(user.name); // Error: Cannot read property 'name' of null

// ✅ Correct
const user = await collection.findOne({ email: 'unknown@example.com' });
if (user) {
  console.log(user.name);
} else {
  console.log('User not found');
}

// Or use optional chaining
console.log(user?.name ?? 'Not found');
```

### 3. Incorrect ObjectId String Comparison

```javascript
// ❌ Wrong - comparing ObjectId to string always fails
const user = await collection.findOne({ _id: '507f1f77bcf86cd799439011' });
// Returns null even if document exists!

// ✅ Correct - convert string to ObjectId
const user = await collection.findOne({ 
  _id: new ObjectId('507f1f77bcf86cd799439011') 
});
```

### 4. Mixing Projection Include/Exclude

```javascript
// ❌ Wrong - cannot mix 1 and 0 (except _id)
const users = await collection.find(
  {},
  { projection: { name: 1, password: 0 } }
).toArray(); // Error!

// ✅ Correct - include only
{ projection: { name: 1, email: 1 } }

// ✅ Correct - exclude only
{ projection: { password: 0, ssn: 0 } }

// ✅ Correct - include + exclude _id
{ projection: { name: 1, email: 1, _id: 0 } }
```

### 5. Inefficient Pagination with Skip

```javascript
// ❌ Bad - very slow for high page numbers
const page = 1000;
const users = await collection.find()
  .skip(page * 100) // Skips 100,000 documents!
  .limit(100)
  .toArray();

// ✅ Better - use range queries with indexed field
const lastSeenId = lastDocumentId;
const users = await collection.find({ 
  _id: { $gt: lastSeenId } 
})
  .limit(100)
  .toArray();
```

### 6. Not Using Await

```javascript
// ❌ Wrong - returns Promise, not document
const user = collection.findOne({ email: 'john@example.com' });
console.log(user.name); // Error: cannot read property of Promise

// ✅ Correct
const user = await collection.findOne({ email: 'john@example.com' });
console.log(user?.name);
```

### 7. Case-Sensitive String Matching

```javascript
// ❌ Wrong - case sensitive, might not match
const user = await collection.findOne({ email: 'John@Example.com' });
// Won't find 'john@example.com'

// ✅ Correct - case insensitive regex
const user = await collection.findOne({ 
  email: { $regex: '^john@example\\.com$', $options: 'i' } 
});

// ✅ Better - normalize email before storing and querying
const user = await collection.findOne({ 
  email: email.toLowerCase() 
});
```

---

## Quick Reference Card

```javascript
// FIND ONE DOCUMENT
const user = await collection.findOne({ email: 'john@example.com' });
// Returns: document or null

// FIND MULTIPLE DOCUMENTS
const users = await collection.find({ age: { $gte: 18 } }).toArray();
// Returns: array of documents

// WITH PROJECTION
const users = await collection.find(
  { age: { $gte: 18 } },
  { projection: { name: 1, email: 1, _id: 0 } }
).toArray();

// WITH SORT, LIMIT, SKIP
const users = await collection.find({ isActive: true })
  .sort({ createdAt: -1 })
  .skip(20)
  .limit(10)
  .toArray();

// COMMON OPERATORS
{ age: { $eq: 30 } }              // Equal
{ age: { $ne: 30 } }              // Not equal
{ age: { $gt: 18 } }              // Greater than
{ age: { $gte: 18 } }             // Greater than or equal
{ age: { $lt: 65 } }              // Less than
{ age: { $lte: 65 } }             // Less than or equal
{ age: { $in: [20, 25, 30] } }    // In array
{ age: { $nin: [20, 25, 30] } }   // Not in array

// LOGICAL OPERATORS
{ $and: [{ age: { $gte: 18 } }, { age: { $lte: 65 } }] }
{ $or: [{ email: '...' }, { username: '...' }] }
{ $nor: [{ banned: true }, { deleted: true }] }
{ age: { $not: { $gte: 18 } } }

// REGEX
{ name: { $regex: /^John/i } }
{ email: { $regex: '@gmail\\.com$' } }

// NESTED DOCUMENTS
{ 'address.city': 'New York' }
{ 'profile.age': { $gte: 18 } }

// ARRAYS
{ tags: 'premium' }                    // Contains value
{ tags: { $all: ['a', 'b'] } }        // Contains all
{ tags: { $in: ['a', 'b'] } }         // Contains any
{ tags: { $size: 3 } }                // Array length

// CURSOR ITERATION
for await (const doc of cursor) {
  console.log(doc);
}

// COUNT
const count = await collection.countDocuments({ age: { $gte: 18 } });
```

---

## Key Exam Points

### Remember for Certification:

1. **findOne returns** document or null, **find returns** cursor
2. **Must use toArray()** to get array from find() cursor
3. **Always check for null** after findOne()
4. **Projection**: Cannot mix include (1) and exclude (0), except _id
5. **Order**: filter → sort → skip → limit
6. **Case sensitive** by default, use $regex with options: 'i' for case-insensitive
7. **Dot notation** for nested documents: 'address.city'
8. **ObjectId strings** must be converted: new ObjectId(stringId)
9. **Cursor methods**: toArray(), forEach(), hasNext(), next(), stream()
10. **Performance**: Use indexes, projection, limit for large datasets

### Common Query Operators:

- **Comparison**: $eq, $ne, $gt, $gte, $lt, $lte, $in, $nin
- **Logical**: $and, $or, $nor, $not
- **Element**: $exists, $type
- **Array**: $all, $elemMatch, $size
- **String**: $regex

### Performance Tips:

- **Use findOne** instead of find().limit(1) for single documents
- **Create indexes** on frequently queried fields
- **Use projection** to limit returned fields
- **Use limit()** to prevent huge result sets
- **Use cursors** (not toArray) for very large datasets
- **Avoid skip** for large offsets, use range queries instead

---

## Summary

| Method | Return Type | Use Case | Null Check Needed |
|--------|-------------|----------|-------------------|
| `findOne()` | Document or null | Get single specific document | Yes |
| `find()` | Cursor | Get multiple documents | No (empty cursor) |

**Key Differences:**
- findOne stops after first match (more efficient for single document)
- find retrieves all matches (returns cursor, needs toArray())
- findOne returns null if no match, find returns empty cursor
- Both support same filters, operators, and options
- Projection cannot mix include and exclude (except _id)
- Always use indexes on queried fields for performance