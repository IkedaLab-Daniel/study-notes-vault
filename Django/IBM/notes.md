# IBM: Developing Application with SQL Databases and Django

## 📊 Introduction to Data and Databases

### 🧠 What is Data?
- Data is a **collection of facts** in the form of:
  - Words
  - Numbers
  - Pictures
- Used everywhere: banks, credit card companies, PayPal, etc.
- Data is **critical**, so it must be:
  - **Secure**
  - **Easily stored**
  - **Quickly accessible**

---

### 🗃️ What is a Database?
- A **database** is a collection of organized data used for:
  - Input
  - Storage
  - Search & Retrieval
  - Modification

---

### 🛠️ What is a DBMS?
- **DBMS** (Database Management System) is a set of programs that:
  - Creates and maintains databases
  - Allows **querying** to store, extract, and modify data

#### 🧪 Example Use of Querying:
> Find all customers inactive for 6+ months using a query → DBMS fetches and returns the matching records.

- Though **Database** and **DBMS** are technically different, they are often used interchangeably.

---

### 🧩 Types of Databases

| Type              | Description |
|-------------------|-------------|
| **Relational (RDBMS)** | Tabular data (rows & columns), follows strict schema |
| **Non-Relational (NoSQL)** | Schema-less, flexible, handles large and diverse datasets |

---

### 🧮 Relational Databases (RDBMS)

- Based on **flat files**, but more powerful
- Organize data in **tables**
- Follow a **defined schema**
- Optimized for **large datasets** and **multi-table operations**
- Use **SQL (Structured Query Language)** for querying

---

### ☁️ Non-Relational Databases (NoSQL)

- Also called **"Not Only SQL"**
- Designed for:
  - **Volume** of big data
  - **Diversity** of data types
  - **Speed** and **scalability**
- Ideal for:
  - Cloud computing
  - IoT (Internet of Things)
  - Social media platforms
- Store data in a **schema-less** format
- Known for **high flexibility and performance**

---

### ✅ Summary

- **Data** is a valuable digital asset used by businesses everywhere.
- A **database** organizes and stores this data for fast access and updates.
- A **DBMS** is a software system that manages databases using **queries**.
- Two main types of databases:
  - **Relational (SQL)**: Structured, tabular data
  - **Non-relational (NoSQL)**: Flexible, big data-ready

## 🗄️ Relational Databases (RDBMS)

### 📘 What is a Relational Database?
- A **relational database** organizes data into **tables**.
- Tables consist of:
  - **Rows** → individual records
  - **Columns** → attributes of the data
- Tables can be **linked** by a common field (e.g., `CustomerID`).

---

### 🔗 Example: Linked Tables

#### Customer Table
| CustomerID | Name       | Address     | Phone        |
|------------|------------|-------------|--------------|
| 1          | Alice Smith| NY, USA     | 123-456-7890 |

#### Transaction Table
| TransactionDate | CustomerID | Amount | PaymentMethod |
|------------------|------------|--------|----------------|
| 2024-01-01       | 1          | $100   | Credit Card    |

- **Relation**: Linked by `CustomerID`
- **Querying** across tables helps generate reports (e.g., customer statements)

---

### 🔍 RDBMS vs Spreadsheets

| Feature                    | RDBMS                          | Spreadsheet           |
|----------------------------|--------------------------------|------------------------|
| Structure                  | Tabular, schema-based          | Tabular               |
| Data Volume                | Optimized for large volumes    | Limited rows/columns  |
| Relationships              | Can define relationships       | No formal relationships |
| Redundancy                 | Reduced via foreign keys       | High chance of duplication |
| Data Types & Constraints   | Enforced                       | Limited validation     |
| Query Language             | SQL                            | Manual operations      |
| Security & Access Control | Advanced role-based controls   | Basic or none          |

---

### ⚙️ SQL – Structured Query Language

- Standard language used to:
  - **Insert**, **Update**, **Delete**, and **Query** data
  - Perform **joins** to combine related tables
- Enables querying **millions of records** in seconds

---

### 🔐 Advantages of Relational Databases

- **Powerful querying** with SQL
- **Data integrity** via ACID compliance:
  - **A**tomicity
  - **C**onsistency
  - **I**solation
  - **D**urability
- **Flexibility**: Add tables/columns during runtime
- **Reduced redundancy** through relationships
- **Backups & Recovery**: Easy export/import, cloud mirroring
- **Scalability**: From desktop to cloud-based systems
- **Security**: Access control and data governance

---

### ☁️ Popular RDBMS and Cloud Databases

| Type              | Examples                                      |
|-------------------|-----------------------------------------------|
| On-Premise        | IBM DB2, MySQL, PostgreSQL, Oracle, SQL Server |
| Cloud-Based (DBaaS)| Amazon RDS, Google Cloud SQL, Azure SQL DB   |

---

### 📈 Use Cases for RDBMS

1. **OLTP (Online Transaction Processing)**  
   - Handles high-volume transactions and user queries
   - Ideal for applications like banking, shopping carts

2. **OLAP (Online Analytical Processing)**  
   - Used in data warehouses for **business intelligence**

3. **IoT (Internet of Things)**  
   - Suitable for fast, lightweight data processing from devices

---

### ⚠️ Limitations of RDBMS

- Not suited for **semi-structured or unstructured data**
- **Schema migration** between different RDBMS can be complex
- **Field length limits** restrict data volume per column
- Less flexible for **big data**, **social media**, and **cloud-native** needs

---

### ✅ Summary

- RDBMS is ideal for **structured data**, offering **powerful querying**, **integrity**, and **flexibility**.
- Tables relate through **common keys**, minimizing redundancy.
- Despite the rise of NoSQL, **relational databases remain dominant** in many industries.

## 🗃️ NoSQL Databases

### 📌 What is NoSQL?
- **NoSQL** = "Not Only SQL" (not "No SQL")
- A **non-relational** database design offering:
  - **Flexible schemas**
  - **High performance**
  - **Easy scalability**
- Stores **structured**, **semi-structured**, and **unstructured** data
- Does **not require fixed tables or schemas**
- Some support SQL-like queries, but not mandatory

---

### 🧩 Types of NoSQL Databases

#### 1. 🗝️ Key-Value Store
- **Data Structure**: `{ "key": "value" }`
- **Use Cases**:
  - Session management
  - Caching
  - Real-time recommendations
- **Examples**: Redis, Memcached, DynamoDB
- **Limitation**: Poor for complex querying or relationships

#### 2. 📄 Document-Based
- **Data Structure**: JSON-like documents
- **Use Cases**:
  - E-commerce platforms
  - Medical records
  - CRMs & analytics
- **Examples**: MongoDB, CouchDB, Cloudant
- **Limitation**: Limited support for multi-operation transactions

#### 3. 📊 Column-Based
- **Data Structure**: Column families (not rows)
- **Use Cases**:
  - Time-series data
  - IoT and sensor data
  - High write throughput apps
- **Examples**: Cassandra, HBase
- **Limitation**: Less flexible for changing query patterns

#### 4. 🌐 Graph-Based
- **Data Structure**: Nodes (data) + Edges (relationships)
- **Use Cases**:
  - Social networks
  - Fraud detection
  - Access control
- **Examples**: Neo4j, CosmosDB
- **Limitation**: Not ideal for high-volume analytics

---

### 🚀 Advantages of NoSQL

- **Scalability**: Easily scales across data centers and cloud
- **Flexible schemas**: Supports dynamic and schema-less data
- **High performance** for big data and real-time apps
- **Low-cost** architecture: Uses commodity hardware
- **Agility**: Easy to iterate and develop modern applications

---

### 🆚 NoSQL vs RDBMS

| Feature                        | RDBMS                            | NoSQL                                 |
|-------------------------------|----------------------------------|----------------------------------------|
| Schema                        | Fixed, rigid schema              | Flexible or schema-less                |
| Query Language                | SQL                              | Varies (no standard)                   |
| Data Types                    | Structured                       | Structured, semi-, and unstructured    |
| Scalability                   | Vertical                         | Horizontal (scale-out)                 |
| Cost                          | High (commercial systems)        | Low (commodity hardware)               |
| ACID Compliance               | Yes                              | Rarely (eventual consistency common)   |
| Maturity                      | Very mature and stable           | Newer, evolving rapidly                |
| Use Cases                     | OLTP, OLAP, BI                   | Big data, real-time web/mobile apps    |

---

### 🔚 Conclusion

- NoSQL databases are ideal for **modern, cloud-native** applications.
- Offer **performance, scalability, and flexibility** beyond traditional RDBMS.
- Increasingly adopted for **mission-critical** use cases alongside traditional databases.
