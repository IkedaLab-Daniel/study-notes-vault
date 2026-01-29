# MongoDB InsertOne & InsertMany - Node.js Driver

## Overview

MongoDB provides two primary methods for inserting documents:
- **`insertOne()`** - Insert a single document
- **`insertMany()`** - Insert multiple documents in one operation

---

## insertOne() Method

### Basic Syntax

```javascript
const result = await collection.insertOne(document, options);
```

### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `document` | Object | The document to insert |
| `options` | Object | Optional settings (see options section) |

### Return Value

Returns a **`InsertOneResult`** object:

```javascript
{
  acknowledged: true,      // Operation acknowledged by server
  insertedId: ObjectId    // The _id of inserted document
}
```

### Basic Example

```javascript
const { MongoClient, ObjectId } = require('mongodb');

const client = new MongoClient('mongodb://localhost:27017');
await client.connect();
const db = client.db('myDatabase');
const collection = db.collection('users');

// Insert single document
const result = await collection.insertOne({
  name: 'John Doe',
  email: 'john@example.com',
  age: 30,
  createdAt: new Date()
});

console.log(result.acknowledged); // true
console.log(result.insertedId);   // ObjectId('...')
```

### With Explicit _id

```javascript
// MongoDB auto-generates _id if not provided
// But you can specify your own

const customId = new ObjectId();

const result = await collection.insertOne({
  _id: customId,  // Custom _id
  name: 'Jane Doe',
  email: 'jane@example.com'
});

console.log(result.insertedId.equals(customId)); // true
```

### Using Returned _id

```javascript
const result = await collection.insertOne({
  name: 'Alice',
  email: 'alice@example.com'
});

// Use the returned _id immediately
const userId = result.insertedId;

// Create related document
await ordersCollection.insertOne({
  userId: userId,  // Reference the user
  product: 'Laptop',
  price: 1200
});
```

---

## insertMany() Method

### Basic Syntax

```javascript
const result = await collection.insertMany(documents, options);
```

### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `documents` | Array | Array of documents to insert |
| `options` | Object | Optional settings (see options section) |

### Return Value

Returns a **`InsertManyResult`** object:

```javascript
{
  acknowledged: true,           // Operation acknowledged by server
  insertedCount: 3,             // Number of documents inserted
  insertedIds: {                // Map of inserted document _ids
    0: ObjectId('...'),         // Index 0 document _id
    1: ObjectId('...'),         // Index 1 document _id
    2: ObjectId('...')          // Index 2 document _id
  }
}
```

### Basic Example

```javascript
const result = await collection.insertMany([
  { name: 'John', email: 'john@example.com', age: 30 },
  { name: 'Jane', email: 'jane@example.com', age: 25 },
  { name: 'Bob', email: 'bob@example.com', age: 35 }
]);

console.log(result.acknowledged);    // true
console.log(result.insertedCount);   // 3
console.log(result.insertedIds);     
// { 0: ObjectId('...'), 1: ObjectId('...'), 2: ObjectId('...') }

// Access specific inserted IDs
console.log(result.insertedIds[0]);  // First document's _id
console.log(result.insertedIds[1]);  // Second document's _id
```

### Accessing Inserted IDs

```javascript
const users = [
  { name: 'Alice', role: 'admin' },
  { name: 'Bob', role: 'user' },
  { name: 'Charlie', role: 'user' }
];

const result = await collection.insertMany(users);

// Convert insertedIds object to array
const idArray = Object.values(result.insertedIds);
console.log(idArray); // [ObjectId('...'), ObjectId('...'), ObjectId('...')]

// Iterate through inserted IDs
for (const [index, id] of Object.entries(result.insertedIds)) {
  console.log(`Document ${index}: ${id}`);
}
```

---

## Options

### Common Options for Both Methods

```javascript
const options = {
  writeConcern: { w: 'majority', wtimeout: 5000 },
  bypassDocumentValidation: false,
  comment: 'Inserting new users'
};

await collection.insertOne(document, options);
await collection.insertMany(documents, options);
```

| Option | Type | Description |
|--------|------|-------------|
| `writeConcern` | Object | Write concern settings |
| `bypassDocumentValidation` | Boolean | Bypass document validation (default: false) |
| `comment` | String | Arbitrary comment for operation tracking |

### insertMany() Specific Option: ordered

```javascript
// Ordered insert (default: true)
await collection.insertMany(documents, { ordered: true });

// Unordered insert
await collection.insertMany(documents, { ordered: false });
```

**`ordered: true` (default)**
- Documents inserted in array order
- Stops on first error
- Documents before error are inserted
- Documents after error are NOT inserted

**`ordered: false`**
- Documents may be inserted in any order
- Continues after errors
- Attempts to insert ALL documents
- Returns bulk write error with details

---

## Error Handling

### insertOne() Error Handling

```javascript
try {
  const result = await collection.insertOne({
    _id: new ObjectId('507f1f77bcf86cd799439011'),
    name: 'John'
  });
  
  console.log('Inserted:', result.insertedId);
  
} catch (error) {
  if (error.code === 11000) {
    console.error('Duplicate key error - document with this _id already exists');
  } else {
    console.error('Insert failed:', error.message);
  }
}
```

### Common Error Codes

| Code | Error Type | Description |
|------|-----------|-------------|
| `11000` | Duplicate Key | Document with same unique field already exists |
| `121` | Document Validation Failed | Schema validation failed |
| `2` | Bad Value | Invalid field value or type |

### insertMany() Error Handling - Ordered

```javascript
try {
  const result = await collection.insertMany([
    { _id: 1, name: 'Alice' },
    { _id: 2, name: 'Bob' },
    { _id: 1, name: 'Charlie' },  // Duplicate _id! Will cause error
    { _id: 3, name: 'David' }     // Won't be inserted (ordered mode)
  ], { ordered: true });
  
} catch (error) {
  console.error('Error code:', error.code); // 11000
  console.error('Documents inserted:', error.result.insertedCount); // 2
  console.error('Inserted IDs:', error.result.insertedIds); 
  // { 0: 1, 1: 2 } - Only first two documents
}
```

### insertMany() Error Handling - Unordered

```javascript
try {
  const result = await collection.insertMany([
    { _id: 1, name: 'Alice' },
    { _id: 2, name: 'Bob' },
    { _id: 1, name: 'Charlie' },  // Duplicate! Will fail
    { _id: 3, name: 'David' }     // WILL be inserted (unordered mode)
  ], { ordered: false });
  
} catch (error) {
  console.error('Some inserts failed');
  console.error('Documents inserted:', error.result.insertedCount); // 3
  console.error('Inserted IDs:', error.result.insertedIds);
  // { 0: 1, 1: 2, 3: 3 } - All except duplicate
  
  // Access individual errors
  console.error('Write errors:', error.writeErrors);
  // Array of errors for failed documents
}
```

---

## insertOne vs insertMany Comparison

| Feature | insertOne | insertMany |
|---------|-----------|------------|
| **Documents** | Single document | Multiple documents (array) |
| **Return** | Single insertedId | insertedIds object + count |
| **Performance** | One network round trip per call | Single round trip for all documents |
| **Atomicity** | Single document is atomic | Each document atomic, but operation is NOT atomic |
| **Error Handling** | Stops on error | Ordered: stops; Unordered: continues |
| **Use Case** | One-off inserts | Bulk data loading |

### When to Use insertOne

```javascript
// ✅ User registration (one user at a time)
await users.insertOne({
  username: req.body.username,
  email: req.body.email,
  password: hashedPassword,
  createdAt: new Date()
});

// ✅ Creating single related document
const orderId = await orders.insertOne({
  userId: currentUserId,
  items: cart.items,
  total: cart.total
});
```

### When to Use insertMany

```javascript
// ✅ Seeding database with initial data
await collection.insertMany([
  { category: 'Electronics', name: 'Laptop' },
  { category: 'Electronics', name: 'Phone' },
  { category: 'Books', name: 'MongoDB Guide' },
  { category: 'Books', name: 'Node.js Manual' }
]);

// ✅ Importing data from CSV/JSON file
const csvData = await parseCsvFile('users.csv');
await collection.insertMany(csvData);

// ✅ Batch processing
const batch = [];
for (const item of dataStream) {
  batch.push(processItem(item));
  
  if (batch.length >= 1000) {
    await collection.insertMany(batch);
    batch.length = 0; // Clear batch
  }
}
// Insert remaining
if (batch.length > 0) {
  await collection.insertMany(batch);
}
```

---

## Performance Best Practices

### 1. Batch Size for insertMany

```javascript
// ❌ Avoid: Very large single batch (memory issues)
const allDocs = []; // 1 million documents
await collection.insertMany(allDocs); // May fail or be slow

// ✅ Better: Process in chunks
const BATCH_SIZE = 1000;

for (let i = 0; i < allDocs.length; i += BATCH_SIZE) {
  const batch = allDocs.slice(i, i + BATCH_SIZE);
  await collection.insertMany(batch);
  console.log(`Inserted ${i + batch.length} / ${allDocs.length}`);
}
```

### 2. Unordered Inserts for Speed

```javascript
// If you don't care about order and want maximum speed
await collection.insertMany(documents, { 
  ordered: false  // Faster, continues on errors
});
```

### 3. Write Concern Trade-offs

```javascript
// Faster (less safe) - doesn't wait for replication
await collection.insertOne(doc, {
  writeConcern: { w: 1 }  // Primary only
});

// Safer (slower) - waits for majority replication
await collection.insertOne(doc, {
  writeConcern: { w: 'majority', wtimeout: 5000 }
});
```

---

## Complete Working Examples

### Example 1: User Registration with insertOne

```javascript
async function registerUser(userData) {
  const { MongoClient } = require('mongodb');
  
  const client = new MongoClient('mongodb://localhost:27017');
  
  try {
    await client.connect();
    const db = client.db('myApp');
    const users = db.collection('users');
    
    // Check if user exists
    const existingUser = await users.findOne({ 
      email: userData.email 
    });
    
    if (existingUser) {
      throw new Error('User already exists');
    }
    
    // Insert new user
    const result = await users.insertOne({
      username: userData.username,
      email: userData.email,
      password: userData.hashedPassword, // Already hashed
      role: 'user',
      isActive: true,
      createdAt: new Date(),
      updatedAt: new Date(),
      profile: {
        firstName: userData.firstName,
        lastName: userData.lastName
      }
    });
    
    console.log('User registered:', result.insertedId);
    return result.insertedId;
    
  } catch (error) {
    console.error('Registration failed:', error);
    throw error;
  } finally {
    await client.close();
  }
}
```

### Example 2: Bulk Import with insertMany

```javascript
async function importProducts(productsArray) {
  const { MongoClient } = require('mongodb');
  
  const client = new MongoClient('mongodb://localhost:27017');
  
  try {
    await client.connect();
    const db = client.db('ecommerce');
    const products = db.collection('products');
    
    const BATCH_SIZE = 500;
    let totalInserted = 0;
    let totalFailed = 0;
    
    for (let i = 0; i < productsArray.length; i += BATCH_SIZE) {
      const batch = productsArray.slice(i, i + BATCH_SIZE);
      
      // Add timestamps to each document
      const documentsWithTimestamps = batch.map(product => ({
        ...product,
        createdAt: new Date(),
        updatedAt: new Date()
      }));
      
      try {
        const result = await products.insertMany(
          documentsWithTimestamps,
          { ordered: false } // Continue on errors
        );
        
        totalInserted += result.insertedCount;
        console.log(`Batch ${Math.floor(i / BATCH_SIZE) + 1}: ${result.insertedCount} inserted`);
        
      } catch (error) {
        if (error.code === 11000) {
          // Bulk write error with some duplicates
          totalInserted += error.result.insertedCount;
          totalFailed += error.writeErrors.length;
          console.log(`Batch had ${error.writeErrors.length} duplicates`);
        } else {
          throw error;
        }
      }
    }
    
    console.log(`Import complete: ${totalInserted} inserted, ${totalFailed} failed`);
    return { inserted: totalInserted, failed: totalFailed };
    
  } finally {
    await client.close();
  }
}
```

### Example 3: Transaction with Inserts

```javascript
async function createOrderWithItems(orderData, items) {
  const { MongoClient } = require('mongodb');
  
  const client = new MongoClient('mongodb://localhost:27017');
  
  try {
    await client.connect();
    const db = client.db('store');
    
    // Start session for transaction
    const session = client.startSession();
    
    try {
      await session.withTransaction(async () => {
        const orders = db.collection('orders');
        const orderItems = db.collection('orderItems');
        
        // Insert order
        const orderResult = await orders.insertOne({
          userId: orderData.userId,
          total: orderData.total,
          status: 'pending',
          createdAt: new Date()
        }, { session }); // Pass session for transaction
        
        const orderId = orderResult.insertedId;
        
        // Insert order items with order reference
        const itemsWithOrderId = items.map(item => ({
          ...item,
          orderId: orderId
        }));
        
        await orderItems.insertMany(itemsWithOrderId, { session });
        
        console.log('Order created with items');
        return orderId;
      });
      
    } finally {
      await session.endSession();
    }
    
  } finally {
    await client.close();
  }
}
```

---

## Common Certification Pitfalls

### 1. Forgetting await

```javascript
// ❌ Wrong - returns Promise, not result
const result = collection.insertOne({ name: 'John' });
console.log(result.insertedId); // undefined! Result is a Promise

// ✅ Correct
const result = await collection.insertOne({ name: 'John' });
console.log(result.insertedId); // ObjectId('...')
```

### 2. Not Handling Errors

```javascript
// ❌ Wrong - unhandled duplicate key error will crash app
await collection.insertOne({ _id: 1, name: 'John' });
await collection.insertOne({ _id: 1, name: 'Jane' }); // Crashes!

// ✅ Correct
try {
  await collection.insertOne({ _id: 1, name: 'Jane' });
} catch (error) {
  if (error.code === 11000) {
    console.log('Duplicate key error');
  }
}
```

### 3. Misunderstanding insertMany Atomicity

```javascript
// ❌ Wrong assumption: insertMany is NOT atomic as a whole
// If operation fails midway, some documents are already inserted

// ✅ Correct: Use transactions for atomic multi-document operations
const session = client.startSession();
await session.withTransaction(async () => {
  await collection.insertMany(docs, { session });
});
await session.endSession();
```

### 4. Incorrect insertedIds Access

```javascript
const result = await collection.insertMany([
  { name: 'Alice' },
  { name: 'Bob' }
]);

// ❌ Wrong - insertedIds is an object, not array
console.log(result.insertedIds[0]); // Works, but confusing

// ✅ Correct - understand it's an object with numeric keys
console.log(result.insertedIds[0]); // First document
console.log(result.insertedIds[1]); // Second document

// Convert to array if needed
const idsArray = Object.values(result.insertedIds);
```

### 5. Ordered vs Unordered Confusion

```javascript
// ordered: true (default) - stops on first error
try {
  await collection.insertMany([
    { _id: 1 },
    { _id: 2 },
    { _id: 1 }, // Duplicate! Error here
    { _id: 3 }  // NOT inserted
  ], { ordered: true });
} catch (e) {
  console.log(e.result.insertedCount); // 2
}

// ordered: false - continues after errors
try {
  await collection.insertMany([
    { _id: 1 },
    { _id: 2 },
    { _id: 1 }, // Duplicate! Error here
    { _id: 3 }  // IS inserted
  ], { ordered: false });
} catch (e) {
  console.log(e.result.insertedCount); // 3
}
```

---

## Quick Reference Card

```javascript
// IMPORT
const { MongoClient, ObjectId } = require('mongodb');

// INSERT ONE
const result = await collection.insertOne({
  name: 'John',
  email: 'john@example.com',
  createdAt: new Date()
});
// Returns: { acknowledged: true, insertedId: ObjectId('...') }

// INSERT MANY
const result = await collection.insertMany([
  { name: 'Alice' },
  { name: 'Bob' },
  { name: 'Charlie' }
]);
// Returns: { 
//   acknowledged: true, 
//   insertedCount: 3,
//   insertedIds: { 0: ObjectId('...'), 1: ObjectId('...'), 2: ObjectId('...') }
// }

// WITH OPTIONS
await collection.insertOne(doc, {
  writeConcern: { w: 'majority' },
  bypassDocumentValidation: false
});

await collection.insertMany(docs, {
  ordered: false,  // Continue on errors (default: true)
  writeConcern: { w: 'majority' }
});

// ERROR HANDLING
try {
  await collection.insertOne(doc);
} catch (error) {
  if (error.code === 11000) {
    console.log('Duplicate key');
  }
}

// BATCH PROCESSING
const BATCH_SIZE = 1000;
for (let i = 0; i < allDocs.length; i += BATCH_SIZE) {
  const batch = allDocs.slice(i, i + BATCH_SIZE);
  await collection.insertMany(batch);
}
```

---

## Key Exam Points

### Remember for Certification:

1. **insertOne returns `insertedId`** (singular ObjectId)
2. **insertMany returns `insertedIds`** (object with numeric keys) and `insertedCount`
3. **Default behavior**: ordered inserts (stops on first error)
4. **ordered: false** continues inserting after errors
5. **Each document insert is atomic**, but insertMany as a whole is NOT atomic
6. **Error code 11000** = duplicate key error
7. **_id auto-generated** if not provided
8. **Must use await** - all insert methods return Promises
9. **Write concern** affects durability and performance
10. **Batch processing** recommended for large datasets (500-1000 docs per batch)

### Performance Tips:

- **insertMany** is faster than multiple insertOne calls (single network round trip)
- **Unordered inserts** (`ordered: false`) are faster
- **Lower write concerns** are faster but less safe
- **Batch large imports** into chunks to avoid memory issues
- **Use transactions** when you need multi-document atomicity

---

## Summary

| Method | Purpose | Return Value | Best For |
|--------|---------|--------------|----------|
| `insertOne()` | Insert 1 document | `{ acknowledged, insertedId }` | Single document operations, user actions |
| `insertMany()` | Insert multiple documents | `{ acknowledged, insertedCount, insertedIds }` | Bulk imports, seeding, batch processing |

**Key Differences:**
- insertMany is more efficient for multiple documents (single round trip)
- insertMany has `ordered` option to control error handling behavior
- insertMany is NOT atomic across all documents (use transactions for that)
- Both auto-generate _id if not provided
- Both support write concerns and validation bypass options