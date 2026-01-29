# MongoDB UpdateOne & UpdateMany - Node.js Driver

## Overview

MongoDB provides two primary methods for updating documents:
- **`updateOne()`** - Updates a single document (first match)
- **`updateMany()`** - Updates multiple documents (all matches)

**Additional Methods:**
- **`replaceOne()`** - Replaces entire document (covered separately)
- **`findOneAndUpdate()`** - Atomic find and update with return options

---

## updateOne() Method

### Basic Syntax

```javascript
const result = await collection.updateOne(filter, update, options);
```

### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `filter` | Object | Query criteria to match document(s) |
| `update` | Object | Update operations to apply |
| `options` | Object | Optional settings (upsert, arrayFilters, etc.) |

### Return Value

Returns an **`UpdateResult`** object:

```javascript
{
  acknowledged: true,        // Operation acknowledged by server
  matchedCount: 1,          // Number of documents matched
  modifiedCount: 1,         // Number of documents modified
  upsertedCount: 0,         // Number of documents upserted (if upsert: true)
  upsertedId: null          // _id of upserted document (if applicable)
}
```

### Basic Examples

```javascript
const { MongoClient, ObjectId } = require('mongodb');

const client = new MongoClient('mongodb://localhost:27017');
await client.connect();
const db = client.db('myDatabase');
const users = db.collection('users');

// Update single field
const result = await users.updateOne(
  { email: 'john@example.com' },      // Filter
  { $set: { isActive: true } }         // Update
);

console.log(result.matchedCount);    // 1
console.log(result.modifiedCount);   // 1

// Update by _id
await users.updateOne(
  { _id: new ObjectId('507f1f77bcf86cd799439011') },
  { $set: { lastLogin: new Date() } }
);

// Update multiple fields
await users.updateOne(
  { email: 'john@example.com' },
  { 
    $set: { 
      isActive: true,
      updatedAt: new Date(),
      'profile.verified': true
    } 
  }
);
```

---

## updateMany() Method

### Basic Syntax

```javascript
const result = await collection.updateMany(filter, update, options);
```

### Parameters

Same as updateOne(), but affects **all matching documents**.

### Return Value

Returns an **`UpdateResult`** object:

```javascript
{
  acknowledged: true,        
  matchedCount: 25,         // All documents that matched filter
  modifiedCount: 25,        // All documents that were actually changed
  upsertedCount: 0,         
  upsertedId: null          
}
```

### Basic Examples

```javascript
// Update all matching documents
const result = await users.updateMany(
  { isActive: false },               // Filter: all inactive users
  { $set: { status: 'dormant' } }    // Update
);

console.log(result.matchedCount);    // e.g., 25
console.log(result.modifiedCount);   // e.g., 25

// Update all documents in collection
await users.updateMany(
  {},                                 // Empty filter = all documents
  { $set: { updatedAt: new Date() } }
);

// Update with complex filter
await products.updateMany(
  { 
    category: 'Electronics',
    price: { $lt: 100 }
  },
  { 
    $set: { 
      onSale: true,
      discount: 0.15 
    } 
  }
);
```

---

## Update Operators

### $set - Set Field Value

```javascript
// Set single field
await users.updateOne(
  { _id: userId },
  { $set: { email: 'newemail@example.com' } }
);

// Set multiple fields
await users.updateOne(
  { _id: userId },
  { 
    $set: { 
      email: 'new@example.com',
      updatedAt: new Date(),
      isVerified: true
    } 
  }
);

// Set nested field (dot notation)
await users.updateOne(
  { _id: userId },
  { 
    $set: { 
      'profile.firstName': 'John',
      'profile.lastName': 'Doe',
      'address.city': 'New York'
    } 
  }
);

// Create field if doesn't exist
await users.updateOne(
  { _id: userId },
  { $set: { newField: 'value' } }  // Creates field
);
```

### $unset - Remove Field

```javascript
// Remove single field
await users.updateOne(
  { _id: userId },
  { $unset: { temporaryField: '' } }  // Value doesn't matter
);

// Remove multiple fields
await users.updateOne(
  { _id: userId },
  { 
    $unset: { 
      temporaryField: '',
      oldData: '',
      'profile.nickname': ''
    } 
  }
);

// Note: $unset removes the field entirely from document
```

### $inc - Increment/Decrement Number

```javascript
// Increment by positive number
await users.updateOne(
  { _id: userId },
  { $inc: { loginCount: 1 } }  // Adds 1
);

// Decrement by negative number
await products.updateOne(
  { _id: productId },
  { $inc: { stock: -5 } }  // Subtracts 5
);

// Multiple increments
await stats.updateOne(
  { _id: statId },
  { 
    $inc: { 
      views: 1,
      likes: 1,
      shares: 1
    } 
  }
);

// Increment with decimals
await users.updateOne(
  { _id: userId },
  { $inc: { balance: 50.75 } }
);

// Creates field with value if doesn't exist
await users.updateOne(
  { _id: userId },
  { $inc: { newCounter: 1 } }  // If newCounter doesn't exist, sets to 1
);
```

### $mul - Multiply Number

```javascript
// Multiply field value
await products.updateOne(
  { _id: productId },
  { $mul: { price: 1.1 } }  // Increase by 10%
);

// Apply discount
await products.updateOne(
  { _id: productId },
  { $mul: { price: 0.85 } }  // 15% discount
);

// Multiple multiplications
await stats.updateOne(
  { _id: statId },
  { 
    $mul: { 
      score: 2,
      weight: 0.5
    } 
  }
);
```

### $min - Update if New Value is Less

```javascript
// Only update if new value is smaller
await products.updateOne(
  { _id: productId },
  { $min: { lowestPrice: 99.99 } }
);
// Updates lowestPrice only if 99.99 < current lowestPrice

// Useful for tracking minimums
await stats.updateOne(
  { userId: userId },
  { $min: { minResponseTime: 150 } }
);
```

### $max - Update if New Value is Greater

```javascript
// Only update if new value is larger
await products.updateOne(
  { _id: productId },
  { $max: { highestPrice: 199.99 } }
);
// Updates highestPrice only if 199.99 > current highestPrice

// Useful for tracking maximums
await stats.updateOne(
  { userId: userId },
  { $max: { maxScore: 950 } }
);
```

### $currentDate - Set to Current Date

```javascript
// Set to current date/time
await users.updateOne(
  { _id: userId },
  { 
    $currentDate: { 
      lastModified: true,           // Sets to current Date
      lastLogin: { $type: 'date' }  // Explicit date type
    } 
  }
);

// Timestamp type (internal MongoDB timestamp)
await logs.updateOne(
  { _id: logId },
  { 
    $currentDate: { 
      timestamp: { $type: 'timestamp' } 
    } 
  }
);
```

### $rename - Rename Field

```javascript
// Rename single field
await users.updateOne(
  { _id: userId },
  { $rename: { 'name': 'fullName' } }
);

// Rename multiple fields
await users.updateOne(
  { _id: userId },
  { 
    $rename: { 
      'name': 'fullName',
      'age': 'years',
      'profile.phone': 'profile.phoneNumber'
    } 
  }
);
```

---

## Array Update Operators

### $push - Add Element to Array

```javascript
// Add single element
await users.updateOne(
  { _id: userId },
  { $push: { tags: 'premium' } }
);

// Add with $each (multiple elements)
await users.updateOne(
  { _id: userId },
  { 
    $push: { 
      tags: { 
        $each: ['verified', 'premium', 'active'] 
      } 
    } 
  }
);

// Add with $position (insert at specific index)
await users.updateOne(
  { _id: userId },
  { 
    $push: { 
      tags: { 
        $each: ['featured'],
        $position: 0  // Insert at beginning
      } 
    } 
  }
);

// Add with $slice (limit array size)
await users.updateOne(
  { _id: userId },
  { 
    $push: { 
      recentViews: { 
        $each: [newItem],
        $slice: -10  // Keep only last 10 items
      } 
    } 
  }
);

// Add with $sort (sort array after push)
await users.updateOne(
  { _id: userId },
  { 
    $push: { 
      scores: { 
        $each: [{ score: 85, date: new Date() }],
        $sort: { score: -1 },  // Sort by score descending
        $slice: 5              // Keep top 5
      } 
    } 
  }
);
```

### $pull - Remove Elements from Array

```javascript
// Remove all matching values
await users.updateOne(
  { _id: userId },
  { $pull: { tags: 'inactive' } }
);

// Remove with condition
await users.updateOne(
  { _id: userId },
  { 
    $pull: { 
      scores: { $lt: 50 }  // Remove all scores < 50
    } 
  }
);

// Remove documents from array of documents
await users.updateOne(
  { _id: userId },
  { 
    $pull: { 
      items: { status: 'deleted' }  // Remove items where status is 'deleted'
    } 
  }
);

// Remove multiple values with $in
await users.updateOne(
  { _id: userId },
  { 
    $pull: { 
      tags: { $in: ['old', 'deprecated', 'unused'] }
    } 
  }
);
```

### $pop - Remove First or Last Element

```javascript
// Remove last element
await users.updateOne(
  { _id: userId },
  { $pop: { tags: 1 } }  // 1 = last element
);

// Remove first element
await users.updateOne(
  { _id: userId },
  { $pop: { tags: -1 } }  // -1 = first element
);
```

### $addToSet - Add if Not Exists (No Duplicates)

```javascript
// Add only if not already present
await users.updateOne(
  { _id: userId },
  { $addToSet: { tags: 'premium' } }
);
// Won't add 'premium' if already in tags array

// Add multiple unique values
await users.updateOne(
  { _id: userId },
  { 
    $addToSet: { 
      tags: { 
        $each: ['premium', 'verified', 'active'] 
      } 
    } 
  }
);
// Only adds values that aren't already in array
```

### $pullAll - Remove Multiple Specific Values

```javascript
// Remove exact values from array
await users.updateOne(
  { _id: userId },
  { 
    $pullAll: { 
      tags: ['old', 'deprecated', 'temp'] 
    } 
  }
);
```

### $ (Positional Operator) - Update First Match in Array

```javascript
// Update first matching array element
await users.updateOne(
  { 
    _id: userId,
    'items.id': 123  // Find document where items array has element with id=123
  },
  { 
    $set: { 
      'items.$.quantity': 5  // Update that specific element
    } 
  }
);

// Update nested field in matched array element
await users.updateOne(
  { 
    _id: userId,
    'orders.orderId': 'ORD-123'
  },
  { 
    $set: { 
      'orders.$.status': 'shipped',
      'orders.$.shippedAt': new Date()
    } 
  }
);
```

### $[] (All Positional Operator) - Update All Array Elements

```javascript
// Update all elements in array
await users.updateOne(
  { _id: userId },
  { 
    $set: { 
      'items.$[].inStock': true  // Update all items
    } 
  }
);

// Increment all scores
await users.updateOne(
  { _id: userId },
  { 
    $inc: { 
      'scores.$[]': 10  // Add 10 to all scores
    } 
  }
);
```

### $[identifier] (Filtered Positional) - Update Matching Array Elements

```javascript
// Update only array elements matching condition
await users.updateOne(
  { _id: userId },
  { 
    $set: { 
      'items.$[elem].discount': 0.2  // Update matching items
    } 
  },
  { 
    arrayFilters: [{ 'elem.price': { $gte: 100 } }]  // Only items with price >= 100
  }
);

// Multiple conditions
await users.updateOne(
  { _id: userId },
  { 
    $set: { 
      'orders.$[order].status': 'cancelled'
    } 
  },
  { 
    arrayFilters: [
      { 
        'order.status': 'pending',
        'order.createdAt': { $lt: new Date('2026-01-01') }
      }
    ]
  }
);
```

---

## Options

### Common Options

```javascript
const options = {
  upsert: false,              // Insert if not found
  arrayFilters: [],           // Filters for array updates
  writeConcern: {},           // Write concern settings
  collation: {},              // Collation settings
  hint: {},                   // Index hint
  bypassDocumentValidation: false
};

await collection.updateOne(filter, update, options);
await collection.updateMany(filter, update, options);
```

### upsert Option

```javascript
// upsert: true - Insert if document doesn't exist
const result = await users.updateOne(
  { email: 'new@example.com' },
  { 
    $set: { 
      email: 'new@example.com',
      name: 'New User',
      createdAt: new Date()
    } 
  },
  { upsert: true }
);

// If document exists: updates it
// If document doesn't exist: creates it

console.log(result.matchedCount);   // 0 if inserted
console.log(result.modifiedCount);  // 0 if inserted
console.log(result.upsertedCount);  // 1 if inserted
console.log(result.upsertedId);     // ObjectId of new document if inserted
```

### $setOnInsert - Set Only on Insert (with upsert)

```javascript
// Set these fields only if document is inserted (not on update)
await users.updateOne(
  { email: 'user@example.com' },
  { 
    $set: { 
      lastLogin: new Date()  // Always set (update or insert)
    },
    $setOnInsert: {
      createdAt: new Date(), // Only set on insert
      role: 'user',          // Only set on insert
      isActive: true         // Only set on insert
    }
  },
  { upsert: true }
);
```

### arrayFilters Option

```javascript
// Update specific array elements matching filter
await students.updateOne(
  { _id: studentId },
  { 
    $set: { 
      'grades.$[grade].passed': true 
    } 
  },
  { 
    arrayFilters: [{ 'grade.score': { $gte: 60 } }]
  }
);

// Multiple array filters
await collection.updateOne(
  { _id: docId },
  { 
    $set: { 
      'items.$[item].discounted': true,
      'items.$[item].discount': 0.15
    } 
  },
  { 
    arrayFilters: [
      { 
        'item.category': 'Electronics',
        'item.price': { $gt: 100 }
      }
    ]
  }
);
```

---

## Combining Multiple Update Operators

```javascript
// Multiple operators in single update
await users.updateOne(
  { _id: userId },
  {
    $set: { 
      lastLogin: new Date(),
      'profile.verified': true
    },
    $inc: { 
      loginCount: 1,
      points: 10
    },
    $push: { 
      loginHistory: { 
        timestamp: new Date(),
        ip: '192.168.1.1'
      }
    },
    $unset: { 
      temporaryToken: ''
    }
  }
);

// Complex update with array operations
await products.updateOne(
  { _id: productId },
  {
    $set: { 
      updatedAt: new Date(),
      onSale: true
    },
    $inc: { 
      viewCount: 1
    },
    $mul: { 
      price: 0.9  // 10% discount
    },
    $addToSet: { 
      tags: 'featured'
    },
    $pull: { 
      tags: 'old-collection'
    }
  }
);
```

---

## updateOne vs updateMany Comparison

| Feature | updateOne | updateMany |
|---------|-----------|------------|
| **Documents Updated** | First match only | All matches |
| **Performance** | Faster (stops after first) | Slower (scans all) |
| **Use Case** | Update specific document | Bulk updates |
| **matchedCount** | 0 or 1 | 0 to N |
| **modifiedCount** | 0 or 1 | 0 to N |

### When to Use updateOne

```javascript
// ✅ Update specific user
await users.updateOne(
  { _id: userId },
  { $set: { lastLogin: new Date() } }
);

// ✅ Update by unique field
await users.updateOne(
  { email: userEmail },
  { $inc: { loginCount: 1 } }
);

// ✅ Increment counter for specific document
await posts.updateOne(
  { _id: postId },
  { $inc: { views: 1 } }
);

// ✅ Update first occurrence
await queue.updateOne(
  { status: 'pending' },
  { $set: { status: 'processing', startedAt: new Date() } }
);
```

### When to Use updateMany

```javascript
// ✅ Bulk status update
await users.updateMany(
  { lastLogin: { $lt: new Date('2025-01-01') } },
  { $set: { status: 'inactive' } }
);

// ✅ Apply discount to category
await products.updateMany(
  { category: 'Electronics' },
  { $mul: { price: 0.85 } }
);

// ✅ Update all documents
await collection.updateMany(
  {},
  { $set: { version: 2, updatedAt: new Date() } }
);

// ✅ Clean up old data
await logs.updateMany(
  { level: 'debug' },
  { $unset: { details: '' } }
);
```

---

## Complete Working Examples

### Example 1: User Profile Update

```javascript
async function updateUserProfile(userId, updates) {
  const { MongoClient, ObjectId } = require('mongodb');
  
  const client = new MongoClient('mongodb://localhost:27017');
  
  try {
    await client.connect();
    const db = client.db('myApp');
    const users = db.collection('users');
    
    // Build update document
    const updateDoc = {
      $set: {
        updatedAt: new Date()
      }
    };
    
    // Add profile updates
    if (updates.firstName) {
      updateDoc.$set['profile.firstName'] = updates.firstName;
    }
    if (updates.lastName) {
      updateDoc.$set['profile.lastName'] = updates.lastName;
    }
    if (updates.phone) {
      updateDoc.$set['profile.phone'] = updates.phone;
    }
    
    // Perform update
    const result = await users.updateOne(
      { _id: new ObjectId(userId) },
      updateDoc
    );
    
    if (result.matchedCount === 0) {
      throw new Error('User not found');
    }
    
    return {
      success: true,
      modified: result.modifiedCount > 0
    };
    
  } finally {
    await client.close();
  }
}
```

### Example 2: Inventory Management

```javascript
async function updateInventory(productId, quantityChange) {
  const { MongoClient, ObjectId } = require('mongodb');
  
  const client = new MongoClient('mongodb://localhost:27017');
  
  try {
    await client.connect();
    const db = client.db('ecommerce');
    const products = db.collection('products');
    
    const result = await products.updateOne(
      { 
        _id: new ObjectId(productId),
        stock: { $gte: Math.abs(quantityChange) }  // Ensure enough stock
      },
      {
        $inc: { stock: quantityChange },
        $set: { updatedAt: new Date() },
        $push: {
          stockHistory: {
            $each: [{
              change: quantityChange,
              timestamp: new Date(),
              type: quantityChange > 0 ? 'restock' : 'sale'
            }],
            $slice: -50  // Keep last 50 history items
          }
        }
      }
    );
    
    if (result.matchedCount === 0) {
      throw new Error('Product not found or insufficient stock');
    }
    
    return result;
    
  } finally {
    await client.close();
  }
}
```

### Example 3: Bulk Price Update with Discount

```javascript
async function applyDiscount(category, discountPercent) {
  const { MongoClient } = require('mongodb');
  
  const client = new MongoClient('mongodb://localhost:27017');
  
  try {
    await client.connect();
    const db = client.db('ecommerce');
    const products = db.collection('products');
    
    const multiplier = 1 - (discountPercent / 100);
    
    const result = await products.updateMany(
      { 
        category: category,
        isActive: true,
        price: { $gt: 0 }
      },
      {
        $mul: { price: multiplier },
        $set: { 
          onSale: true,
          salePercent: discountPercent,
          saleStartDate: new Date()
        },
        $addToSet: { tags: 'on-sale' }
      }
    );
    
    console.log(`Updated ${result.modifiedCount} products`);
    return result;
    
  } finally {
    await client.close();
  }
}

// Usage: Apply 20% discount to all Electronics
await applyDiscount('Electronics', 20);
```

### Example 4: Upsert Pattern (Find or Create)

```javascript
async function recordPageView(userId, pageUrl) {
  const { MongoClient, ObjectId } = require('mongodb');
  
  const client = new MongoClient('mongodb://localhost:27017');
  
  try {
    await client.connect();
    const db = client.db('analytics');
    const pageViews = db.collection('pageViews');
    
    const result = await pageViews.updateOne(
      { 
        userId: new ObjectId(userId),
        pageUrl: pageUrl,
        date: {
          $gte: new Date(new Date().setHours(0, 0, 0, 0)),
          $lt: new Date(new Date().setHours(23, 59, 59, 999))
        }
      },
      {
        $inc: { views: 1 },
        $set: { lastViewedAt: new Date() },
        $setOnInsert: {
          userId: new ObjectId(userId),
          pageUrl: pageUrl,
          date: new Date(),
          firstViewedAt: new Date()
        }
      },
      { upsert: true }
    );
    
    if (result.upsertedCount > 0) {
      console.log('New page view record created');
    } else {
      console.log('Page view count incremented');
    }
    
    return result;
    
  } finally {
    await client.close();
  }
}
```

### Example 5: Array Updates with Filters

```javascript
async function updateOrderItemStatus(orderId, itemId, newStatus) {
  const { MongoClient, ObjectId } = require('mongodb');
  
  const client = new MongoClient('mongodb://localhost:27017');
  
  try {
    await client.connect();
    const db = client.db('ecommerce');
    const orders = db.collection('orders');
    
    // Update specific item in items array
    const result = await orders.updateOne(
      { 
        _id: new ObjectId(orderId),
        'items.itemId': itemId
      },
      {
        $set: {
          'items.$.status': newStatus,
          'items.$.statusUpdatedAt': new Date()
        }
      }
    );
    
    if (result.matchedCount === 0) {
      throw new Error('Order or item not found');
    }
    
    // If all items are shipped, update order status
    const order = await orders.findOne({ _id: new ObjectId(orderId) });
    const allShipped = order.items.every(item => item.status === 'shipped');
    
    if (allShipped) {
      await orders.updateOne(
        { _id: new ObjectId(orderId) },
        { 
          $set: { 
            orderStatus: 'shipped',
            shippedAt: new Date()
          } 
        }
      );
    }
    
    return result;
    
  } finally {
    await client.close();
  }
}
```

---

## Performance Best Practices

### 1. Use Specific Filters

```javascript
// ❌ Bad - Updates all documents
await collection.updateMany(
  {},
  { $set: { field: 'value' } }
);

// ✅ Good - Updates only needed documents
await collection.updateMany(
  { status: 'pending', createdAt: { $lt: cutoffDate } },
  { $set: { status: 'expired' } }
);
```

### 2. Use updateOne for Single Documents

```javascript
// ❌ Bad - Scans all documents even after finding match
await collection.updateMany(
  { _id: userId },  // Only one document can match _id
  { $set: { lastLogin: new Date() } }
);

// ✅ Good - Stops after first match
await collection.updateOne(
  { _id: userId },
  { $set: { lastLogin: new Date() } }
);
```

### 3. Use Indexes on Filter Fields

```javascript
// Create index on frequently updated fields
await collection.createIndex({ email: 1 });
await collection.createIndex({ status: 1 });

// Now these updates are fast
await collection.updateOne(
  { email: 'user@example.com' },
  { $set: { lastLogin: new Date() } }
);
```

### 4. Batch Similar Updates

```javascript
// ❌ Bad - Multiple separate updates
for (const userId of userIds) {
  await users.updateOne(
    { _id: userId },
    { $set: { status: 'active' } }
  );
}

// ✅ Good - Single bulk update
await users.updateMany(
  { _id: { $in: userIds } },
  { $set: { status: 'active' } }
);
```

### 5. Check matchedCount vs modifiedCount

```javascript
const result = await collection.updateOne(
  { _id: userId },
  { $set: { name: 'John' } }
);

// matchedCount = 0: Document doesn't exist
if (result.matchedCount === 0) {
  throw new Error('Document not found');
}

// matchedCount > 0 but modifiedCount = 0: No actual change
if (result.modifiedCount === 0) {
  console.log('Document found but no changes needed');
}
```

---

## Common Certification Pitfalls

### 1. Forgetting Update Operators

```javascript
// ❌ Wrong - This will replace entire document!
await collection.updateOne(
  { _id: userId },
  { name: 'John' }  // Missing $set!
);
// Result: Document now only has { _id: ..., name: 'John' }

// ✅ Correct - Use $set or other operators
await collection.updateOne(
  { _id: userId },
  { $set: { name: 'John' } }
);
```

### 2. Not Checking matchedCount

```javascript
// ❌ Wrong - Doesn't check if document exists
await collection.updateOne(
  { _id: userId },
  { $set: { name: 'John' } }
);
// Silent failure if userId doesn't exist

// ✅ Correct - Check result
const result = await collection.updateOne(
  { _id: userId },
  { $set: { name: 'John' } }
);

if (result.matchedCount === 0) {
  throw new Error('User not found');
}
```

### 3. Misunderstanding modifiedCount

```javascript
const result = await collection.updateOne(
  { _id: userId },
  { $set: { name: 'John' } }
);

// modifiedCount can be 0 even if matchedCount is 1
// This happens when the value is already 'John'
console.log(result.matchedCount);   // 1 (document found)
console.log(result.modifiedCount);  // 0 (no change needed)
```

### 4. Incorrect Array Update Syntax

```javascript
// ❌ Wrong - Replaces entire array
await collection.updateOne(
  { _id: userId },
  { $set: { tags: ['new'] } }
);
// Old tags are lost!

// ✅ Correct - Add to array
await collection.updateOne(
  { _id: userId },
  { $push: { tags: 'new' } }
);

// ✅ Or use $addToSet to avoid duplicates
await collection.updateOne(
  { _id: userId },
  { $addToSet: { tags: 'new' } }
);
```

### 5. Upsert with $inc Creating Incorrect Initial Value

```javascript
// ❌ Wrong - Creates { count: 1 } instead of { count: 0 }
await collection.updateOne(
  { _id: docId },
  { $inc: { count: 1 } },
  { upsert: true }
);
// If document doesn't exist, count starts at 1

// ✅ Correct - Use $setOnInsert for initial value
await collection.updateOne(
  { _id: docId },
  { 
    $inc: { count: 1 },
    $setOnInsert: { createdAt: new Date() }
  },
  { upsert: true }
);
```

### 6. Using updateMany Without Proper Filter

```javascript
// ❌ Dangerous - Updates ALL documents
await collection.updateMany(
  {},  // Empty filter!
  { $set: { deleted: true } }
);

// ✅ Always use specific filter with updateMany
await collection.updateMany(
  { status: 'inactive', lastLogin: { $lt: cutoffDate } },
  { $set: { deleted: true } }
);
```

### 7. Combining Incompatible Operators

```javascript
// ❌ Wrong - Can't $set and $unset same field
await collection.updateOne(
  { _id: userId },
  { 
    $set: { name: 'John' },
    $unset: { name: '' }  // Conflict!
  }
);

// ❌ Wrong - Can't $inc and $set same field
await collection.updateOne(
  { _id: userId },
  { 
    $inc: { count: 1 },
    $set: { count: 10 }  // Conflict!
  }
);
```

### 8. Positional Operator Without Array Match in Filter

```javascript
// ❌ Wrong - $ requires array field in filter
await collection.updateOne(
  { _id: userId },  // No array field specified!
  { $set: { 'items.$.quantity': 5 } }
);

// ✅ Correct - Include array element match in filter
await collection.updateOne(
  { _id: userId, 'items.id': 123 },  // Array match in filter
  { $set: { 'items.$.quantity': 5 } }
);
```

---

## Quick Reference Card

```javascript
// UPDATE ONE
const result = await collection.updateOne(filter, update, options);
// Returns: { acknowledged, matchedCount, modifiedCount, upsertedId }

// UPDATE MANY
const result = await collection.updateMany(filter, update, options);
// Returns: { acknowledged, matchedCount, modifiedCount, upsertedCount }

// FIELD OPERATORS
{ $set: { field: value } }              // Set field value
{ $unset: { field: '' } }               // Remove field
{ $inc: { number: 5 } }                 // Increment by 5
{ $mul: { number: 2 } }                 // Multiply by 2
{ $min: { field: 100 } }                // Update if new < current
{ $max: { field: 200 } }                // Update if new > current
{ $rename: { old: 'new' } }             // Rename field
{ $currentDate: { field: true } }       // Set to current date

// ARRAY OPERATORS
{ $push: { array: value } }                     // Add to array
{ $push: { array: { $each: [1,2,3] } } }       // Add multiple
{ $addToSet: { array: value } }                // Add if not exists
{ $pull: { array: value } }                    // Remove matching
{ $pullAll: { array: [1,2,3] } }              // Remove specific values
{ $pop: { array: 1 } }                         // Remove last (-1 = first)

// POSITIONAL OPERATORS
{ $set: { 'array.$.field': value } }           // Update first match
{ $set: { 'array.$[].field': value } }         // Update all
{ $set: { 'array.$[elem].field': value } }     // Update filtered
// With arrayFilters option: [{ 'elem.price': { $gt: 100 } }]

// OPTIONS
{ 
  upsert: true,                    // Insert if not found
  arrayFilters: [...],             // Filters for positional updates
  writeConcern: { w: 'majority' }
}

// UPSERT WITH $setOnInsert
{ 
  $set: { updated: new Date() },           // Always set
  $setOnInsert: { created: new Date() }    // Only on insert
}

// COMBINE OPERATORS
{
  $set: { field1: 'value' },
  $inc: { count: 1 },
  $push: { array: 'item' },
  $unset: { oldField: '' }
}
```

---

## Key Exam Points

### Remember for Certification:

1. **Always use update operators** ($set, $inc, etc.) - without them you replace entire document
2. **updateOne updates first match** only, **updateMany updates all matches**
3. **Check matchedCount** to verify document exists
4. **modifiedCount can be 0** even if matchedCount > 0 (no actual change)
5. **upsert: true** inserts document if not found
6. **$setOnInsert** only sets fields on insert, not update
7. **Positional operator $** requires array match in filter
8. **arrayFilters** required for $[identifier] syntax
9. **$push** adds to array, **$addToSet** adds only if unique
10. **Cannot combine conflicting operators** on same field

### Common Update Operators:

**Field Operators:**
- $set, $unset, $inc, $mul, $min, $max, $rename, $currentDate

**Array Operators:**
- $push, $pull, $pop, $addToSet, $pullAll

**Positional:**
- $ (first match), $[] (all), $[identifier] (filtered)

### Performance Tips:

- **Use updateOne** for single document updates (faster)
- **Index filter fields** for fast updates
- **Batch updates** with updateMany instead of loops
- **Use upsert** for find-or-create patterns
- **Limit array size** with $slice when using $push
- **Check matchedCount** before assuming success

---

## Summary

| Method | Updates | Use Case | Stops After First Match |
|--------|---------|----------|-------------------------|
| `updateOne()` | First match | Update specific document | Yes |
| `updateMany()` | All matches | Bulk updates | No |

**Critical Rules:**
- Must use update operators ($set, $inc, etc.) or entire document is replaced
- matchedCount tells if document was found
- modifiedCount tells if document was actually changed
- upsert creates document if not found
- Positional operators require specific syntax and filters
- Cannot mix conflicting operators on same field