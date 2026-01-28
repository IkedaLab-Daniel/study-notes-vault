# MongoDB DeleteOne & DeleteMany - Node.js Driver

## Overview

MongoDB provides two primary methods for deleting documents:
- **`deleteOne()`** - Deletes a single document (first match)
- **`deleteMany()`** - Deletes multiple documents (all matches)

**Additional Methods:**
- **`findOneAndDelete()`** - Atomic find and delete with return of deleted document
- **Soft Delete Pattern** - Mark as deleted instead of removing (covered in examples)

---

## deleteOne() Method

### Basic Syntax

```javascript
const result = await collection.deleteOne(filter, options);
```

### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `filter` | Object | Query criteria to match document(s) |
| `options` | Object | Optional settings (writeConcern, collation, hint) |

### Return Value

Returns a **`DeleteResult`** object:

```javascript
{
  acknowledged: true,      // Operation acknowledged by server
  deletedCount: 1         // Number of documents deleted (0 or 1)
}
```

### Basic Examples

```javascript
const { MongoClient, ObjectId } = require('mongodb');

const client = new MongoClient('mongodb://localhost:27017');
await client.connect();
const db = client.db('myDatabase');
const users = db.collection('users');

// Delete by _id
const result = await users.deleteOne({ 
  _id: new ObjectId('507f1f77bcf86cd799439011') 
});

console.log(result.acknowledged);  // true
console.log(result.deletedCount);  // 1 (if found) or 0 (if not found)

// Delete by field
const result = await users.deleteOne({ 
  email: 'user@example.com' 
});

// Delete with multiple conditions
const result = await users.deleteOne({
  email: 'user@example.com',
  isActive: false,
  deletedAt: { $exists: false }
});

// Delete first matching document
const result = await users.deleteOne({ 
  status: 'pending' 
});
// Deletes only the first pending user found
```

### Checking Deletion Success

```javascript
const result = await users.deleteOne({ 
  _id: new ObjectId('507f1f77bcf86cd799439011') 
});

if (result.deletedCount === 0) {
  console.log('No document found to delete');
  // or throw error
  throw new Error('User not found');
} else {
  console.log('Document deleted successfully');
}
```

---

## deleteMany() Method

### Basic Syntax

```javascript
const result = await collection.deleteMany(filter, options);
```

### Parameters

Same as deleteOne(), but affects **all matching documents**.

### Return Value

Returns a **`DeleteResult`** object:

```javascript
{
  acknowledged: true,      
  deletedCount: 25        // Number of documents deleted (0 to N)
}
```

### Basic Examples

```javascript
// Delete all matching documents
const result = await users.deleteMany({ 
  isActive: false 
});

console.log(result.deletedCount); // e.g., 25

// Delete with date range
const cutoffDate = new Date('2025-01-01');
const result = await users.deleteMany({
  lastLogin: { $lt: cutoffDate },
  status: 'inactive'
});

// Delete all documents (DANGEROUS!)
const result = await users.deleteMany({});
console.log(`Deleted ${result.deletedCount} documents`);

// Delete with complex filter
const result = await logs.deleteMany({
  level: 'debug',
  timestamp: { 
    $lt: new Date(Date.now() - 30 * 24 * 60 * 60 * 1000) // Older than 30 days
  }
});
```

---

## Options

### Common Options for Both Methods

```javascript
const options = {
  writeConcern: { w: 'majority', wtimeout: 5000 },
  collation: { locale: 'en', strength: 2 },
  hint: { email: 1 },  // Use specific index
  comment: 'Deleting inactive users'
};

await collection.deleteOne(filter, options);
await collection.deleteMany(filter, options);
```

| Option | Type | Description |
|--------|------|-------------|
| `writeConcern` | Object | Write concern settings |
| `collation` | Object | Collation rules for string comparison |
| `hint` | String/Object | Index to use for the delete operation |
| `comment` | String | Comment for operation tracking |

### Write Concern Example

```javascript
// Wait for majority of replica set members
await users.deleteOne(
  { _id: userId },
  { 
    writeConcern: { 
      w: 'majority',      // Wait for majority
      wtimeout: 5000      // Timeout after 5 seconds
    } 
  }
);

// Fastest (don't wait for acknowledgment) - RISKY
await logs.deleteMany(
  { level: 'debug' },
  { 
    writeConcern: { w: 0 }  // Fire and forget
  }
);
```

### Hint Example (Force Index Usage)

```javascript
// Create index first
await users.createIndex({ email: 1 });

// Force deletion to use email index
await users.deleteOne(
  { email: 'user@example.com' },
  { hint: { email: 1 } }
);

// Or use index name
await users.deleteOne(
  { email: 'user@example.com' },
  { hint: 'email_1' }
);
```

---

## findOneAndDelete() Method

### Atomic Find and Delete

Returns the **deleted document** instead of just count.

```javascript
const deletedDoc = await collection.findOneAndDelete(filter, options);
```

### Return Value

Returns the **deleted document** or **null** if not found.

```javascript
const deletedUser = await users.findOneAndDelete({ 
  email: 'user@example.com' 
});

if (deletedUser) {
  console.log('Deleted user:', deletedUser);
  // Can access deletedUser.name, deletedUser._id, etc.
} else {
  console.log('No user found to delete');
}
```

### Options

```javascript
const options = {
  projection: { name: 1, email: 1 },     // Fields to return
  sort: { createdAt: -1 },               // Sort before deleting
  maxTimeMS: 5000,                       // Timeout
  collation: { locale: 'en' }
};

const deletedDoc = await collection.findOneAndDelete(filter, options);
```

### Use Cases

```javascript
// Delete and get deleted document for logging
const deletedUser = await users.findOneAndDelete({ _id: userId });
if (deletedUser) {
  await auditLog.insertOne({
    action: 'user_deleted',
    userId: deletedUser._id,
    userEmail: deletedUser.email,
    deletedBy: currentUserId,
    deletedAt: new Date()
  });
}

// Delete oldest job from queue
const job = await jobQueue.findOneAndDelete(
  { status: 'pending' },
  { sort: { createdAt: 1 } }  // Oldest first
);

if (job) {
  await processJob(job);
}

// Delete and return specific fields only
const deletedUser = await users.findOneAndDelete(
  { email: 'user@example.com' },
  { projection: { _id: 1, email: 1 } }
);
```

---

## deleteOne vs deleteMany vs findOneAndDelete

| Feature | deleteOne | deleteMany | findOneAndDelete |
|---------|-----------|------------|------------------|
| **Documents Deleted** | First match only | All matches | First match only |
| **Return Value** | DeleteResult (count) | DeleteResult (count) | Deleted document or null |
| **Performance** | Fastest | Slower (scans all) | Moderate |
| **Atomicity** | Atomic | Each delete atomic, not overall | Atomic |
| **Use Case** | Delete specific document | Bulk deletions | Need deleted document data |

### When to Use deleteOne

```javascript
// ✅ Delete specific document by _id
await users.deleteOne({ _id: userId });

// ✅ Delete by unique field
await users.deleteOne({ email: userEmail });

// ✅ Delete first matching (queue pattern)
await tasks.deleteOne({ status: 'completed' });

// ✅ When you don't need deleted document
await sessions.deleteOne({ token: sessionToken });
```

### When to Use deleteMany

```javascript
// ✅ Bulk cleanup
await users.deleteMany({ 
  lastLogin: { $lt: new Date('2024-01-01') } 
});

// ✅ Delete all matching criteria
await logs.deleteMany({ 
  level: 'debug',
  timestamp: { $lt: cutoffDate }
});

// ✅ Clear collection (CAREFUL!)
await tempData.deleteMany({});

// ✅ Delete related documents
await orders.deleteMany({ userId: deletedUserId });
```

### When to Use findOneAndDelete

```javascript
// ✅ Need deleted document for audit trail
const deletedUser = await users.findOneAndDelete({ _id: userId });
await auditLog.insertOne({ deleted: deletedUser });

// ✅ Return deleted data to client
const deleted = await items.findOneAndDelete({ _id: itemId });
res.json({ success: true, deleted });

// ✅ Process deleted document
const job = await queue.findOneAndDelete({ status: 'pending' });
if (job) await processJob(job);

// ✅ Atomic claim-and-delete pattern
const task = await tasks.findOneAndDelete(
  { status: 'ready', assignedTo: null },
  { sort: { priority: -1 } }
);
```

---

## Soft Delete Pattern

### Instead of Deleting, Mark as Deleted

Many applications use "soft delete" - marking documents as deleted instead of removing them.

```javascript
// Instead of deleteOne
await users.deleteOne({ _id: userId });

// Use soft delete (updateOne)
await users.updateOne(
  { _id: userId },
  { 
    $set: { 
      isDeleted: true,
      deletedAt: new Date(),
      deletedBy: currentUserId
    } 
  }
);

// Query excludes deleted documents
const activeUsers = await users.find({ 
  isDeleted: { $ne: true }  // or { $exists: false }
}).toArray();
```

### Soft Delete Helper Functions

```javascript
// Soft delete function
async function softDelete(collection, filter, deletedBy) {
  return await collection.updateOne(
    filter,
    {
      $set: {
        isDeleted: true,
        deletedAt: new Date(),
        deletedBy: deletedBy
      }
    }
  );
}

// Restore deleted document
async function restore(collection, filter) {
  return await collection.updateOne(
    filter,
    {
      $unset: {
        isDeleted: '',
        deletedAt: '',
        deletedBy: ''
      }
    }
  );
}

// Hard delete (permanent)
async function hardDelete(collection, filter) {
  return await collection.deleteOne(filter);
}

// Usage
await softDelete(users, { _id: userId }, currentUserId);
await restore(users, { _id: userId });
await hardDelete(users, { _id: userId, isDeleted: true });
```

### Advantages of Soft Delete

- **Recoverable**: Can restore deleted data
- **Audit trail**: Know when and who deleted
- **Data integrity**: Keeps foreign key references intact
- **Legal compliance**: Some regulations require data retention

### Disadvantages of Soft Delete

- **Query complexity**: Must always filter out deleted docs
- **Index bloat**: Deleted docs still in indexes
- **Storage cost**: Deleted data still uses space
- **Unique constraints**: Deleted docs still count for uniqueness

---

## Complete Working Examples

### Example 1: Delete User with Cascade

```javascript
async function deleteUserWithRelatedData(userId) {
  const { MongoClient, ObjectId } = require('mongodb');
  
  const client = new MongoClient('mongodb://localhost:27017');
  
  try {
    await client.connect();
    const db = client.db('myApp');
    
    // Start session for transaction
    const session = client.startSession();
    
    try {
      await session.withTransaction(async () => {
        // Delete user's orders
        const ordersResult = await db.collection('orders').deleteMany(
          { userId: new ObjectId(userId) },
          { session }
        );
        
        // Delete user's sessions
        await db.collection('sessions').deleteMany(
          { userId: new ObjectId(userId) },
          { session }
        );
        
        // Delete user's notifications
        await db.collection('notifications').deleteMany(
          { userId: new ObjectId(userId) },
          { session }
        );
        
        // Finally delete user
        const userResult = await db.collection('users').deleteOne(
          { _id: new ObjectId(userId) },
          { session }
        );
        
        if (userResult.deletedCount === 0) {
          throw new Error('User not found');
        }
        
        console.log(`Deleted user and ${ordersResult.deletedCount} orders`);
      });
      
    } finally {
      await session.endSession();
    }
    
  } finally {
    await client.close();
  }
}
```

### Example 2: Cleanup Old Records

```javascript
async function cleanupOldRecords() {
  const { MongoClient } = require('mongodb');
  
  const client = new MongoClient('mongodb://localhost:27017');
  
  try {
    await client.connect();
    const db = client.db('myApp');
    
    // Delete logs older than 30 days
    const thirtyDaysAgo = new Date(Date.now() - 30 * 24 * 60 * 60 * 1000);
    
    const logsResult = await db.collection('logs').deleteMany({
      level: { $in: ['debug', 'info'] },
      timestamp: { $lt: thirtyDaysAgo }
    });
    
    // Delete expired sessions
    const sessionsResult = await db.collection('sessions').deleteMany({
      expiresAt: { $lt: new Date() }
    });
    
    // Delete unverified accounts older than 7 days
    const sevenDaysAgo = new Date(Date.now() - 7 * 24 * 60 * 60 * 1000);
    
    const usersResult = await db.collection('users').deleteMany({
      isVerified: false,
      createdAt: { $lt: sevenDaysAgo }
    });
    
    console.log('Cleanup complete:');
    console.log(`- Deleted ${logsResult.deletedCount} old logs`);
    console.log(`- Deleted ${sessionsResult.deletedCount} expired sessions`);
    console.log(`- Deleted ${usersResult.deletedCount} unverified accounts`);
    
    return {
      logs: logsResult.deletedCount,
      sessions: sessionsResult.deletedCount,
      users: usersResult.deletedCount
    };
    
  } finally {
    await client.close();
  }
}
```

### Example 3: Soft Delete with Audit Trail

```javascript
async function deleteUserWithAudit(userId, deletedBy) {
  const { MongoClient, ObjectId } = require('mongodb');
  
  const client = new MongoClient('mongodb://localhost:27017');
  
  try {
    await client.connect();
    const db = client.db('myApp');
    const users = db.collection('users');
    const auditLog = db.collection('auditLog');
    
    // Get user before deletion
    const user = await users.findOne({ _id: new ObjectId(userId) });
    
    if (!user) {
      throw new Error('User not found');
    }
    
    // Soft delete
    const result = await users.updateOne(
      { _id: new ObjectId(userId) },
      {
        $set: {
          isDeleted: true,
          deletedAt: new Date(),
          deletedBy: new ObjectId(deletedBy)
        }
      }
    );
    
    // Create audit log
    await auditLog.insertOne({
      action: 'user_deleted',
      targetUserId: new ObjectId(userId),
      targetUserEmail: user.email,
      performedBy: new ObjectId(deletedBy),
      timestamp: new Date(),
      details: {
        userName: user.name,
        userRole: user.role
      }
    });
    
    return { success: true, deletedUser: user.email };
    
  } finally {
    await client.close();
  }
}
```

### Example 4: Batch Delete with Limit

```javascript
async function batchDeleteOldData(batchSize = 1000) {
  const { MongoClient } = require('mongodb');
  
  const client = new MongoClient('mongodb://localhost:27017');
  
  try {
    await client.connect();
    const db = client.db('myApp');
    const logs = db.collection('logs');
    
    const cutoffDate = new Date(Date.now() - 90 * 24 * 60 * 60 * 1000);
    let totalDeleted = 0;
    
    while (true) {
      // Find batch of IDs to delete
      const docsToDelete = await logs.find({
        timestamp: { $lt: cutoffDate }
      })
      .limit(batchSize)
      .project({ _id: 1 })
      .toArray();
      
      if (docsToDelete.length === 0) {
        break; // No more documents to delete
      }
      
      // Extract IDs
      const ids = docsToDelete.map(doc => doc._id);
      
      // Delete batch
      const result = await logs.deleteMany({
        _id: { $in: ids }
      });
      
      totalDeleted += result.deletedCount;
      console.log(`Deleted batch: ${result.deletedCount} (Total: ${totalDeleted})`);
      
      // Optional: pause between batches to reduce load
      await new Promise(resolve => setTimeout(resolve, 100));
    }
    
    console.log(`Batch delete complete: ${totalDeleted} documents deleted`);
    return totalDeleted;
    
  } finally {
    await client.close();
  }
}
```

### Example 5: Delete with Validation

```javascript
async function deleteWithValidation(collection, userId, currentUserId) {
  const { MongoClient, ObjectId } = require('mongodb');
  
  const client = new MongoClient('mongodb://localhost:27017');
  
  try {
    await client.connect();
    const db = client.db('myApp');
    const users = db.collection('users');
    
    // Check if user exists
    const user = await users.findOne({ _id: new ObjectId(userId) });
    
    if (!user) {
      throw new Error('User not found');
    }
    
    // Check permissions (can't delete admin, can't delete yourself, etc.)
    if (user.role === 'admin') {
      throw new Error('Cannot delete admin users');
    }
    
    if (userId === currentUserId) {
      throw new Error('Cannot delete your own account');
    }
    
    // Check if user has active orders
    const activeOrders = await db.collection('orders').countDocuments({
      userId: new ObjectId(userId),
      status: { $in: ['pending', 'processing'] }
    });
    
    if (activeOrders > 0) {
      throw new Error(`Cannot delete user with ${activeOrders} active orders`);
    }
    
    // All validations passed, proceed with deletion
    const result = await users.deleteOne({ _id: new ObjectId(userId) });
    
    if (result.deletedCount === 0) {
      throw new Error('Failed to delete user');
    }
    
    return { success: true, deletedUser: user.email };
    
  } finally {
    await client.close();
  }
}
```

---

## Performance Best Practices

### 1. Use Specific Filters

```javascript
// ❌ Bad - Deletes all documents
await collection.deleteMany({});

// ✅ Good - Specific filter
await collection.deleteMany({ 
  status: 'expired',
  expiresAt: { $lt: new Date() }
});
```

### 2. Delete in Batches for Large Datasets

```javascript
// ❌ Bad - Might timeout or lock collection
await logs.deleteMany({ 
  timestamp: { $lt: veryOldDate } 
}); // Could be millions of documents

// ✅ Good - Delete in batches
const BATCH_SIZE = 1000;
let deleted = 0;

while (true) {
  const ids = await logs.find({ timestamp: { $lt: veryOldDate } })
    .limit(BATCH_SIZE)
    .project({ _id: 1 })
    .toArray();
  
  if (ids.length === 0) break;
  
  const result = await logs.deleteMany({ 
    _id: { $in: ids.map(d => d._id) } 
  });
  
  deleted += result.deletedCount;
  console.log(`Deleted ${deleted} documents...`);
}
```

### 3. Use Indexes on Filter Fields

```javascript
// Create index on frequently deleted fields
await logs.createIndex({ timestamp: 1 });
await sessions.createIndex({ expiresAt: 1 });

// Now deletions are fast
await logs.deleteMany({ 
  timestamp: { $lt: cutoffDate } 
});
```

### 4. Consider Soft Delete for Recovery

```javascript
// Instead of permanent deletion
await users.deleteOne({ _id: userId });

// Use soft delete for recovery option
await users.updateOne(
  { _id: userId },
  { $set: { isDeleted: true, deletedAt: new Date() } }
);
```

### 5. Use Transactions for Related Deletions

```javascript
// ❌ Bad - Not atomic, partial deletion possible
await users.deleteOne({ _id: userId });
await orders.deleteMany({ userId: userId });
await sessions.deleteMany({ userId: userId });

// ✅ Good - All or nothing
const session = client.startSession();
await session.withTransaction(async () => {
  await users.deleteOne({ _id: userId }, { session });
  await orders.deleteMany({ userId: userId }, { session });
  await sessions.deleteMany({ userId: userId }, { session });
});
await session.endSession();
```

### 6. Check deletedCount

```javascript
const result = await users.deleteOne({ _id: userId });

if (result.deletedCount === 0) {
  // Handle not found case
  throw new Error('User not found');
}

// Proceed knowing deletion was successful
```

---

## Common Certification Pitfalls

### 1. Not Checking deletedCount

```javascript
// ❌ Wrong - Assumes deletion succeeded
await users.deleteOne({ _id: userId });
console.log('User deleted'); // Might not have deleted anything!

// ✅ Correct - Check result
const result = await users.deleteOne({ _id: userId });

if (result.deletedCount === 0) {
  throw new Error('User not found');
} else {
  console.log('User deleted successfully');
}
```

### 2. Using deleteMany Without Filter

```javascript
// ❌ DANGEROUS - Deletes ALL documents
await collection.deleteMany({});

// ✅ Always use specific filter
await collection.deleteMany({ 
  status: 'inactive',
  lastLogin: { $lt: cutoffDate }
});
```

### 3. Deleting Without Cascade Consideration

```javascript
// ❌ Wrong - Orphans related documents
await users.deleteOne({ _id: userId });
// Orders, sessions, etc. still reference deleted user

// ✅ Correct - Delete related data or use soft delete
const session = client.startSession();
await session.withTransaction(async () => {
  await orders.deleteMany({ userId: userId }, { session });
  await sessions.deleteMany({ userId: userId }, { session });
  await users.deleteOne({ _id: userId }, { session });
});
await session.endSession();
```

### 4. Not Using await

```javascript
// ❌ Wrong - Returns Promise, doesn't wait
const result = collection.deleteOne({ _id: userId });
console.log(result.deletedCount); // undefined! result is a Promise

// ✅ Correct
const result = await collection.deleteOne({ _id: userId });
console.log(result.deletedCount); // Works!
```

### 5. Confusion Between deleteOne and findOneAndDelete

```javascript
// deleteOne returns count
const result = await users.deleteOne({ _id: userId });
console.log(result.deletedCount); // 1
console.log(result._id); // undefined - no document returned

// findOneAndDelete returns document
const deletedUser = await users.findOneAndDelete({ _id: userId });
console.log(deletedUser._id); // ObjectId(...)
console.log(deletedUser.email); // user@example.com
```

### 6. Trying to Delete by String _id

```javascript
// ❌ Wrong - _id is ObjectId, not string
await users.deleteOne({ _id: '507f1f77bcf86cd799439011' });
// deletedCount will be 0

// ✅ Correct - Convert to ObjectId
await users.deleteOne({ 
  _id: new ObjectId('507f1f77bcf86cd799439011') 
});
```

### 7. Not Handling Bulk Delete Errors

```javascript
// ❌ Wrong - No error handling
await logs.deleteMany({ timestamp: { $lt: cutoffDate } });

// ✅ Correct - Handle errors
try {
  const result = await logs.deleteMany({ 
    timestamp: { $lt: cutoffDate } 
  });
  console.log(`Deleted ${result.deletedCount} logs`);
} catch (error) {
  console.error('Delete failed:', error);
  // Handle error appropriately
}
```

### 8. Forgetting Soft Delete Filter in Queries

```javascript
// Using soft delete pattern
await users.updateOne(
  { _id: userId },
  { $set: { isDeleted: true } }
);

// ❌ Wrong - Still finds deleted users
const user = await users.findOne({ email: userEmail });

// ✅ Correct - Exclude deleted
const user = await users.findOne({ 
  email: userEmail,
  isDeleted: { $ne: true }
});

// Better - create a helper
async function findActiveUser(filter) {
  return await users.findOne({
    ...filter,
    isDeleted: { $ne: true }
  });
}
```

---

## Quick Reference Card

```javascript
// DELETE ONE
const result = await collection.deleteOne(filter);
// Returns: { acknowledged: true, deletedCount: 0 or 1 }

// DELETE MANY
const result = await collection.deleteMany(filter);
// Returns: { acknowledged: true, deletedCount: N }

// FIND ONE AND DELETE
const deletedDoc = await collection.findOneAndDelete(filter, options);
// Returns: deleted document or null

// CHECK DELETION
const result = await collection.deleteOne({ _id: userId });
if (result.deletedCount === 0) {
  throw new Error('Not found');
}

// DELETE WITH OPTIONS
await collection.deleteOne(filter, {
  writeConcern: { w: 'majority' },
  hint: { email: 1 },
  comment: 'Deleting user'
});

// SOFT DELETE (preferred for recovery)
await collection.updateOne(
  { _id: userId },
  { 
    $set: { 
      isDeleted: true,
      deletedAt: new Date()
    } 
  }
);

// CASCADE DELETE (with transaction)
const session = client.startSession();
await session.withTransaction(async () => {
  await orders.deleteMany({ userId }, { session });
  await users.deleteOne({ _id: userId }, { session });
});
await session.endSession();

// BATCH DELETE
const ids = await collection.find(filter)
  .limit(1000)
  .project({ _id: 1 })
  .toArray();

await collection.deleteMany({ 
  _id: { $in: ids.map(d => d._id) } 
});

// CLEANUP OLD RECORDS
await logs.deleteMany({
  timestamp: { $lt: new Date(Date.now() - 30 * 24 * 60 * 60 * 1000) }
});
```

---

## Key Exam Points

### Remember for Certification:

1. **deleteOne deletes first match** only, **deleteMany deletes all matches**
2. **Always check deletedCount** - 0 means nothing was deleted
3. **findOneAndDelete returns** the deleted document (or null)
4. **No undo** - deletions are permanent (unless using soft delete)
5. **Empty filter {} with deleteMany** deletes ALL documents
6. **Transactions** recommended for cascade deletes
7. **Soft delete** uses updateOne with isDeleted flag
8. **Batch large deletes** to avoid timeouts and locks
9. **Use indexes** on filter fields for performance
10. **ObjectId strings** must be converted: new ObjectId(stringId)

### Method Comparison:

| Method | Returns | Count | Document |
|--------|---------|-------|----------|
| `deleteOne()` | DeleteResult | 0 or 1 | No |
| `deleteMany()` | DeleteResult | 0 to N | No |
| `findOneAndDelete()` | Document/null | N/A | Yes |

### Common Patterns:

**Hard Delete:**
- Permanent removal from database
- Cannot be recovered
- Faster queries (no deleted docs)
- Simpler implementation

**Soft Delete:**
- Mark as deleted, don't remove
- Can be recovered/restored
- Maintains data integrity
- Requires filtering deleted docs in queries

### Performance Tips:

- **Use deleteOne** for single documents (faster)
- **Index filter fields** for fast deletions
- **Batch large deletions** (1000 docs at a time)
- **Use transactions** for related deletions
- **Consider TTL indexes** for automatic cleanup
- **Monitor deletedCount** to verify success

### Error Handling:

```javascript
try {
  const result = await collection.deleteOne({ _id: userId });
  
  if (result.deletedCount === 0) {
    throw new Error('Document not found');
  }
  
  console.log('Deleted successfully');
  
} catch (error) {
  console.error('Delete failed:', error);
  // Handle error
}
```

---

## Summary

| Method | Deletes | Returns | Use Case |
|--------|---------|---------|----------|
| `deleteOne()` | First match | DeleteResult (count) | Delete specific document |
| `deleteMany()` | All matches | DeleteResult (count) | Bulk deletions, cleanup |
| `findOneAndDelete()` | First match | Deleted document | Need deleted data |

**Critical Rules:**
- deletedCount = 0 means no documents were deleted
- Always use specific filters with deleteMany to avoid accidents
- Permanent deletion cannot be undone (use soft delete for recovery)
- Use transactions when deleting related documents across collections
- Check deletedCount to verify deletion success
- Convert string _id to ObjectId before deleting

**Best Practices:**
- Consider soft delete for user-facing deletions
- Use hard delete for logs and temporary data
- Always validate before deletion
- Create audit trail for important deletions
- Batch large deletion operations
- Use indexes on filter fields