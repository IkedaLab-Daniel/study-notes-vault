# MongoDB CRUD Operations: Replace, Update, and Delete

## Replace Operations

### replaceOne()
Replaces a single document that matches the filter criteria with a new document.

**Syntax:**
```javascript
db.collection.replaceOne(
   <filter>,
   <replacement>,
   {
      upsert: <boolean>,
      writeConcern: <document>,
      collation: <document>
   }
)
```

**Example:**
```javascript
db.users.replaceOne(
   { name: "John Doe" },
   { name: "John Doe", age: 30, city: "New York", status: "active" }
)
```

**Key Points:**
- Replaces the entire document (except `_id`)
- Only replaces the first matching document
- Returns a document with `matchedCount`, `modifiedCount`, and `upsertedId`
- Cannot use update operators like `$set` in replacement document

---

## Update Operations

### updateOne() with $set
Updates specific field values in a single document without replacing the entire document.

**Syntax:**
```javascript
db.collection.updateOne(
   <filter>,
   { $set: { <field1>: <value1>, <field2>: <value2>, ... } },
   <options>
)
```

**Example:**
```javascript
db.products.updateOne(
   { _id: 100 },
   { $set: { price: 29.99, inStock: true } }
)
```

**Key Points:**
- Only modifies specified fields
- Creates the field if it doesn't exist
- Preserves other fields in the document
- Updates only the first matching document

---

### updateOne() with $push
Adds a value to an array field. If the array doesn't exist, it creates it.

**Syntax:**
```javascript
db.collection.updateOne(
   <filter>,
   { $push: { <arrayField>: <value> } },
   <options>
)
```

**Example:**
```javascript
db.users.updateOne(
   { name: "Alice" },
   { $push: { hobbies: "photography" } }
)
```

**Advanced Example with Modifiers:**
```javascript
db.students.updateOne(
   { name: "Bob" },
   { 
      $push: { 
         scores: { 
            $each: [85, 90, 78],
            $sort: -1,
            $slice: 5
         } 
      } 
   }
)
```

**Key Points:**
- Appends value to end of array
- Creates array if field doesn't exist
- Can use `$each` to push multiple values
- Can use `$sort`, `$slice`, and `$position` modifiers

---

### updateOne() with upsert Option
Updates a document if it exists, or inserts a new document if no match is found.

**Syntax:**
```javascript
db.collection.updateOne(
   <filter>,
   <update>,
   { upsert: true }
)
```

**Example:**
```javascript
db.inventory.updateOne(
   { item: "canvas" },
   { 
      $set: { 
         item: "canvas",
         qty: 100,
         size: { h: 28, w: 35.5, uom: "cm" }
      }
   },
   { upsert: true }
)
```

**Key Points:**
- `upsert: true` means "update or insert"
- If no match found, inserts new document
- Return value includes `upsertedId` if document was inserted
- Useful for ensuring a document exists

---

### findAndModify()
Finds a single document and modifies it, returning either the original or modified document.

**Syntax:**
```javascript
db.collection.findAndModify({
   query: <document>,
   sort: <document>,
   remove: <boolean>,
   update: <document>,
   new: <boolean>,
   fields: <document>,
   upsert: <boolean>
})
```

**Example:**
```javascript
db.orders.findAndModify({
   query: { status: "pending" },
   sort: { priority: -1 },
   update: { $set: { status: "processing" } },
   new: true
})
```

**Key Points:**
- Returns the document (before or after modification)
- `new: true` returns modified document, `new: false` returns original
- Atomic operation - useful for queues and transactions
- Can be used with `remove: true` to find and delete
- More flexible than `updateOne()` when you need the document value

---

### updateMany()
Updates all documents that match the filter criteria.

**Syntax:**
```javascript
db.collection.updateMany(
   <filter>,
   <update>,
   <options>
)
```

**Example:**
```javascript
db.products.updateMany(
   { category: "electronics" },
   { 
      $set: { onSale: true },
      $inc: { discountPercent: 10 }
   }
)
```

**Example - Update all documents:**
```javascript
db.users.updateMany(
   {},  // Empty filter matches all documents
   { $set: { verified: false } }
)
```

**Key Points:**
- Updates ALL matching documents
- Returns `matchedCount` and `modifiedCount`
- Use empty filter `{}` to update all documents
- Be careful - can affect many documents at once

---

## Delete Operations

### deleteOne()
Deletes a single document that matches the filter criteria.

**Syntax:**
```javascript
db.collection.deleteOne(
   <filter>,
   {
      writeConcern: <document>,
      collation: <document>
   }
)
```

**Example:**
```javascript
db.users.deleteOne({ email: "test@example.com" })
```

**Example with multiple matches:**
```javascript
// Only deletes the first match
db.products.deleteOne({ status: "discontinued" })
```

**Key Points:**
- Deletes only the first matching document
- Returns `deletedCount` (0 or 1)
- If multiple documents match, only first one (in natural order) is deleted
- Use with specific `_id` for precise deletion

---

### deleteMany()
Deletes all documents that match the filter criteria.

**Syntax:**
```javascript
db.collection.deleteMany(
   <filter>,
   {
      writeConcern: <document>,
      collation: <document>
   }
)
```

**Example:**
```javascript
db.logs.deleteMany({ 
   createdAt: { $lt: new Date("2025-01-01") } 
})
```

**Example - Delete all documents:**
```javascript
db.tempCollection.deleteMany({})  // Deletes ALL documents
```

**Key Points:**
- Deletes ALL matching documents
- Returns `deletedCount` with number of deleted documents
- Empty filter `{}` deletes all documents in collection
- More efficient than multiple `deleteOne()` calls
- Cannot be undone - use with caution

---

## Common Update Operators

### Field Update Operators
- `$set` - Sets the value of a field
- `$unset` - Removes a field from document
- `$inc` - Increments field value by specified amount
- `$mul` - Multiplies field value by specified amount
- `$rename` - Renames a field
- `$min` - Updates field if specified value is less than current
- `$max` - Updates field if specified value is greater than current
- `$currentDate` - Sets field to current date

### Array Update Operators
- `$push` - Adds element to array
- `$pop` - Removes first or last element
- `$pull` - Removes all matching elements
- `$pullAll` - Removes all specified values
- `$addToSet` - Adds element only if not already present
- `$` - Acts as placeholder for first matching element

---

## Best Practices

1. **Always use specific filters** - Avoid accidental updates/deletes
2. **Test with findOne() first** - Verify your filter matches correctly
3. **Use appropriate method** - Choose based on your needs:
   - Single vs multiple documents
   - Replace vs update specific fields
4. **Consider upsert** - When you want to ensure a document exists
5. **Check return values** - Verify operations succeeded
6. **Use transactions** - For related operations that must succeed together
7. **Be cautious with deleteMany()** - Can't be undone

---

## Return Value Examples

**updateOne/updateMany:**
```javascript
{
   "acknowledged": true,
   "matchedCount": 1,
   "modifiedCount": 1,
   "upsertedId": null
}
```

**deleteOne/deleteMany:**
```javascript
{
   "acknowledged": true,
   "deletedCount": 3
}
```
