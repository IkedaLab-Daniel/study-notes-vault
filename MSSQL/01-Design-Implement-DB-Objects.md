# Design and develop database solutions

## Database Object Design Fundamentals

Unlike application code, database object design decisions across SQL Server, Azure SQL Database, Azure SQL Managed Instance, and Microsoft Fabric are highly permanent. Foundational choices—such as storage formats, tracking mechanisms, or identity generation—are difficult to change later and can cause disruptive migrations if chosen incorrectly. Designing objects properly upfront enables systems to scale, evolve, and support advanced capabilities without painful rewrites.

### Key Learning Objectives

* **Table Design:** Structure tables with appropriate data types and choose between rowstore and columnstore indexes based on transactional or analytical workloads.
* **Specialized Tables:** Deploy specialized types for specific architectural needs:
* *In-memory* for high throughput
* *Temporal* for audit trails
* *External* for lakehouse integration
* *Ledger* for compliance and verification
* *Graph* for complex relationships


* **Constraints & Validation:** Enforce data integrity using primary/foreign keys, unique/CHECK constraints, and DEFAULT values.
* **Advanced Features:** Utilize JSON columns for flexible schemas, optimize platform-specific indexes, and implement SEQUENCE objects for distributed ID generation.
* **Partitioning Strategies:** Design table and index partitioning to handle massive datasets, essential for Hyperscale, multi-TB, and time-series databases.

### Why It Matters

Effective database object design directly drives system success across several pillars:

* **Performance:** Reduces query execution times through optimized structures.
* **Data Integrity:** Ensures data accuracy and consistency at the engine level.
* **Maintenance:** Simplifies ongoing database administration and organization.
* **AI Capabilities:** Provides the proper data foundation required for AI integration.
* **Scalability:** Manages expanding datasets efficiently via advanced partitioning.

## Microsoft SQL Platforms Overview

Choosing the right Microsoft SQL platform requires understanding the trade-offs between Infrastructure-as-a-Service (IaaS) and Platform-as-a-Service (PaaS). PaaS offloads underlying infrastructure management (servers, networking, OS) to Azure, allowing developers to focus entirely on database design, data, and application logic.

### Platform Comparisons

* **Azure SQL Database (PaaS):** A fully managed database offering enterprise-grade performance without the infrastructure overhead.
* **Hyperscale Tier:** Eliminates traditional cloud database limits, offering flexible, auto-expanding storage and rapid read scale-out.
* **Serverless Tier:** Automatically scales compute based on workload and pauses during idle times to save costs (requires connection retry logic in the app).
* **Smart Features:** Includes intelligent query processing, automatic tuning, and built-in high availability (99.99% SLA).


* **Azure SQL Managed Instance (PaaS):** Designed for near 100% compatibility with SQL Server Enterprise Edition while providing PaaS benefits like automated patching and backups.
* **Capabilities:** Supports instance-level features like SQL Server Agent, Service Broker, and cross-database queries.
* **Hybrid & Performance:** Uses the Managed Instance link for near real-time synchronization and offers In-Memory OLTP for high-throughput workloads.


* **SQL Server on Azure Virtual Machines (IaaS):** Provides full control over the operating system, SQL Server instance, and engine configuration.
* **Use Case:** Best for applications requiring specific SQL versions, OS-level access, or granular control over high-availability architectures (like Always On availability groups).
* **Management:** Enhanced by the SQL IaaS Agent extension for automated backups, patching, and performance analysis.


* **SQL Database in Microsoft Fabric:** A developer-friendly database that seamlessly merges transactional operations with built-in analytics.
* **Zero-ETL Analytics:** Automatically mirrors operational data into OneLake as Delta Parquet files, allowing analytical queries without impacting transactional performance.
* **Modern Features:** Includes automatic indexing, AI integration (semantic search, RAG), git integration, and GraphQL APIs.

## Table Design Fundamentals

Effective table design is the bedrock of database efficiency. In relational databases, tables organize transactional data and enforce relationships, while in multidimensional analytics, they serve as fact and dimension tables. Design decisions—like data types, column sizing, constraints, and index strategies—directly dictate storage efficiency, query performance, and data integrity.

### Data Type Selection

Choosing the correct data type is critical. Changing types in production often requires disruptive table rebuilds. Incorrect types can cause wasted storage, sluggish performance, or critical data errors (e.g., using `FLOAT` instead of `DECIMAL` for financial data can introduce irreversible rounding errors).

**Common Data Types:**

* **Numeric:** `INT` (4 bytes), `BIGINT` (8 bytes), `DECIMAL` (varies), `FLOAT`. Use based on required range and precision.
* **String:** `VARCHAR` (1 byte/char, variable), `CHAR` (fixed), `NVARCHAR` (2 bytes/char, Unicode). Use `VARCHAR` for ASCII-only to save space; `NVARCHAR` for international data.
* **Date/Time:** `DATE` (3 bytes), `DATETIME2` (6-8 bytes), `DATETIMEOFFSET` (10 bytes). `DATETIME2` is preferred over legacy `DATETIME` for better precision.
* **Binary:** `VARBINARY`, `IMAGE`. Used for files, photos, or documents.
* **Special:** `UNIQUEIDENTIFIER` (16 bytes, GUIDs), `XML`, `JSON` (native binary in SQL 2025+). Avoid GUIDs as primary keys if `INT` suffices, as they inflate index size and slow joins.

### Table Size Estimation

Estimating table size is vital for capacity planning, backup/restore durations, and cloud cost calculations. A poorly designed table with an unnecessary 50 bytes per row can waste terabytes of storage annually at scale.

**Estimation Example:**

* `INT`: 4 bytes
* `NVARCHAR(50)`: ~40 bytes (average)
* `DATE`: 3 bytes
* `DECIMAL(10,2)`: 5 bytes
* *Row Overhead:* ~7 bytes
* *Total:* Sum these to find average row size, then multiply by expected row count.

### Design Best Practices

To ensure long-term performance and maintainability, follow these principles:

* **Right-Size Data Types:** Always use the smallest data type that safely holds your data.
* **Implement Constraints:** Use `NOT NULL`, `DEFAULT`, `CHECK`, and primary/foreign keys to enforce data quality at the database level.
* **Efficient Primary Keys:** Use `IDENTITY(1,1)` with `INT` or `BIGINT` for sequential, cluster-efficient surrogate keys.
* **Index Strategically:** Index columns frequently used in `WHERE`, `JOIN`, and `ORDER BY` clauses.
* **Workload-Specific Structures:** Use Columnstore indexes for analytical workloads and Rowstore for transactional workloads.
* **Plan for Growth & Compression:** Estimate future volumes early and consider row/page compression for large tables.
* **Normalize Logically:** Strike a balance between strict normalization and the practical performance needs of your queries.