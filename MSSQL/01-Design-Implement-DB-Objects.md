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