# MongoDB Basics For Students (Notes/Summaries)

---

# 📘 Database Fundamentals

## 💡 What is a Database?

A **database** is an organized collection of structured or unstructured information stored on a machine or in the cloud. It serves as the **back-end** of an application, supporting the **front-end** (buttons, search bars, etc.) by storing and retrieving data.

### 🔧 Database Management System (DBMS)

A **DBMS** is software that interacts with users, applications, and the database to manage data through **CRUD operations**:

* **Create**
* **Retrieve**
* **Update**
* **Delete**

It also handles:

* User permissions and security
* Data integrity
* Backup and recovery processes

---

## 🗂️ Types of Databases

Databases are commonly divided into two main categories:

### 1. **SQL Databases**

* Based on **Structured Query Language (SQL)**.
* Use **tables** with **rows (records)** and **columns (fields)** — similar to spreadsheets.
* Focus on relationships between data (relational databases).

### 2. **NoSQL Databases**

* Means “**Not Only SQL**” or **non-relational**.
* Use alternative data structures instead of tables.
* Designed for flexibility, scalability, and handling unstructured data.

---

## 🔍 Types of NoSQL Databases

### 🗝️ Key-Value Databases

* Store data as **key-value pairs**.
* Keys uniquely identify data values.
* Excellent for **large datasets** and **simple lookups**.
* Not ideal for **complex relationships**.

---

### 🕸️ Graph Databases

* Store data as **nodes** (entities) and **edges** (relationships).
* Great for understanding **connections** between data (e.g., **social networks**).
* Faster querying for relationship-heavy data.
* Often used **alongside** traditional databases.

---

### 📊 Column Databases

* Store data **by columns** instead of rows.
* Columns contain the same data type, allowing **better compression** and **faster reads**.
* Ideal for **analytical applications** that query specific columns.

---

### 📄 Document Databases

* Store data in **documents** (similar to JSON or XML).
* Documents are stored in **collections**.
* Flexible for **inconsistent or polymorphic data**.
* Closely aligned with **object-oriented programming**, reducing data translation.

---

**In summary:**
A **database** is a structured system for storing and managing data, powered by a **DBMS**.
The main distinction lies between **SQL (relational)** and **NoSQL (non-relational)** systems, each offering unique advantages depending on the data and application type.

---

# 🧩 Schemas and Data Modeling

## 🏗️ Schema

A **schema** is a set of **rules** that define how data is **stored, organized, and validated** in a database.

* In **SQL databases**, schemas strictly define table fields, data types, and constraints.

  * Example: The “quantity” field must be numeric, and “description” can have limited characters.
* In **NoSQL databases**, schemas are **flexible**, allowing easy changes to data structure.

---

## 🗺️ Data Modeling

**Data modeling** is the **organization and relationship** of data within a database — like a **blueprint** for how data connects.

* A **schema** enforces the rules of data storage.
* A **data model** shows **how data relates** across entities (often visualized in diagrams).

### 🔄 SQL vs NoSQL

| Feature       | SQL Databases                                 | NoSQL Databases                       |
| ------------- | --------------------------------------------- | ------------------------------------- |
| Structure     | Fixed (tables, rows, columns)                 | Flexible (documents, key-value, etc.) |
| Schema Update | Difficult and time-consuming                  | Easy and dynamic                      |
| Example       | Adding a new field requires updating all rows | Add field only where needed           |

NoSQL databases can enforce schemas if desired — from **minimal** (for prototypes) to **strict** (for scalable governance).

---

# 🧠 Structured, Semi-Structured, and Unstructured Data

### 📊 Structured Data

* **Highly organized and predictable** (e.g., tables).
* Easy for computers to process and query.
* Example: SQL database records.

---

### 🧾 Semi-Structured Data

* **Partially organized** but not in a strict format.
* Has a recognizable pattern but flexible structure.
* Examples: **JSON**, **XML** files.

---

### 🎥 Unstructured Data

* **No predefined structure or organization.**
* Includes **videos, images, audio, text documents**, etc.
* Makes up the **majority of real-world data**.
* Commonly used for **AI training and contextual data**.

---

**Summary:**

* **Schema** = Rules of data structure.
* **Data Model** = Conceptual organization and relationships.
* **NoSQL** provides **flexibility** for evolving data.
* Data can be **structured**, **semi-structured**, or **unstructured**, depending on how predictable and formatted it is.

# 📄 The Document Model

## ⚙️ Storage vs Compute

* **Traditional SQL Databases (1970s):**

  * Focused on **saving storage space**, which was expensive.
  * Used **normalization** — splitting data into multiple tables and linking with **keys**.
  * Required **joins** to combine data during queries → **computationally expensive**.

* **Modern NoSQL Databases:**

  * **Storage is cheap**, but **compute power is limited**.
  * Prioritize **reducing joins** and **increasing processing speed**.
  * Allow **flexible schemas**, enabling faster handling of large and varied datasets.
  * Willingly store **duplicate data** to improve performance.

---

## 🧬 Polymorphic Data

* **MongoDB** can handle **unstructured and semi-structured** data easily.
* You can **combine different data types** in a single database.
* Adding **new fields or features** doesn’t require modifying existing tables or schemas.

---

## 🏗️ MongoDB’s Hierarchy

**Hierarchy:**
`Documents → Collections → Database → Node → Cluster`

### 🔑 Golden Rule

> “Data that is accessed together should be stored together.”

This reduces the need for joins and improves performance.

**Metaphor:**

* SQL: Disassemble a car and store each part separately (normalized, space-saving).
* MongoDB: Store the car as a whole — easier to access and extend.

---

## 🧾 Document Model Syntax (MongoDB Example)

```json
{
  "_id": ObjectId("5f4f7fef2d4b45b7f11b6d7a"),
  "user_id": "Sean",
  "age": 29,
  "Status": "A"
}
```

### 📘 Notes

* Each **document** uses **JSON-like syntax** (key-value pairs inside `{}` braces).
* **_id** field = unique identifier (primary key).

  * Must be **unique**, **immutable**, and **non-array type**.
  * Can be **auto-generated** or **manually assigned**.
* A **collection** is a group of related documents.

  * Common fields are typical but not mandatory (unless schema validation is enforced).

---

## ⚡ Misconception Clarified

> “Non-relational” ≠ “No relationships.”

* MongoDB can still represent **relationships** between data, just not through traditional SQL joins.

---

## 🧠 Key Points to Remember

* **Flexibility:** Works well with **unstructured** and **semi-structured** data.
* **Hierarchy:** `Documents → Collections → Database → Node → Cluster`
* **Golden Rule:** Store **related data together**.
* **Syntax Familiarity:** JSON-like format with key-value pairs.

MongoDB’s document model emphasizes **speed, scalability, and flexibility** for modern data workloads.

# 🌐 Distributed Database Architecture

## 🧠 Overview

Modern databases must handle **massive global workloads** with **high availability** and **no data loss**. MongoDB achieves this through a **distributed architecture**, ensuring performance, scalability, and reliability.

---

## 📈 Scaling

### ⚙️ Definition

**Scaling** means adjusting hardware resources to match user or operational demand.

* **Scale Up (Vertical Scaling):** Add more power (CPU, RAM, storage) to a single machine.
* **Scale Down:** Reduce hardware when demand is lower.

Proper scaling prevents underperformance or overspending.

### 🏗️ Vertical Scaling

* Adds **more resources** to a single machine (e.g., faster CPU, larger disk).
* **Pros:** Simple setup, improved performance.
* **Cons:**

  * Expensive upfront.
  * Limited scalability (hardware caps).
  * Inefficient for fluctuating workloads.

📘 *Example:* Buying powerful servers to handle peak loads (10,000 users), even when average traffic is 5,000 → leads to wasted resources during off-peak times.

---

### 🌍 Horizontal Scaling (Sharding)

* Spreads data across **multiple machines**.
* Each machine handles a **portion of the data**.
* **Benefits:**

  * Use cheaper, smaller servers.
  * Efficient scaling for high-demand workloads.
* **Tradeoff:** More complexity in management.

💡 Works best in the **cloud**, where capacity can be dynamically adjusted.

---

## ☁️ Where’s the Hardware?

* **Cloud Provisioning:** Virtually reserving CPU, memory, storage, and network resources.
* Enables **easy vertical or horizontal scaling** without physical upgrades.
* Reduces **upfront cost** and provides **on-demand scalability**.

---

## 🧬 Replication

### 🔁 Definition

**Replication** stores **multiple synchronized copies** of data across nodes for redundancy and high availability.

### 🧩 MongoDB Replica Set

* A **replica set** = group of nodes with identical data.
* Recommended: **Odd number of nodes (minimum 3)**.

  * **Primary Node:** Handles write operations.
  * **Secondary Nodes:** Hold copies for redundancy.

If one node fails, others continue operations seamlessly.

---

## ⚖️ Consistency & Performance

### 🧩 Read and Write Concerns

MongoDB uses **Read** and **Write Concerns** to manage how strictly data is synchronized across nodes.

* Controls **how** and **when** operations are confirmed.
* Balances between **speed**, **consistency**, and **availability**.

---

## 📚 The CAP Theorem

> **C**onsistency, **A**vailability, **P**artition Tolerance — you can only fully optimize **two** at a time.

* **Consistency:** All nodes show the same data at the same time.
* **Availability:** Database remains operational even during failures.
* **Partition Tolerance:** System continues despite network partitions.

MongoDB lets administrators **configure tradeoffs** based on workload and application importance.

---

## 🧠 Key Points to Remember

* **Scaling:**

  * *Vertical* → add power to one machine.
  * *Horizontal* → add more machines (sharding).
* **Replication:**

  * Creates redundant nodes for reliability and data protection.
* **CAP Theorem:**

  * Tradeoff between **Consistency**, **Availability**, and **Partition Tolerance**.
* **MongoDB’s Distributed Design:**

  * Ensures high performance, flexibility, and fault tolerance for modern applications.
