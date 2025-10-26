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