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

## 📘 Relational Model & ER Model 

### ✅ Why the Relational Model?
- **Most widely used** data model
- Offers:
  - **Logical data independence**
  - **Physical data independence**
  - **Physical storage independence**
- Data is stored in **tables** (rows and columns)

---

### 🧩 Entity Relationship (ER) Model

- Alternative to the relational model
- Used as a **design tool** for relational databases
- Represents:
  - **Entities** (objects/nouns like books, authors)
  - **Attributes** (properties of entities)
  - **Relationships** (how entities interact)

#### 📐 ER Diagram Elements
| Component      | Representation  | Example                     |
|----------------|------------------|------------------------------|
| Entity         | Rectangle         | `Book`, `Author`, `Loan`     |
| Attribute      | Oval              | `Title`, `Edition`, `Year`   |
| Relationship   | Diamond (not shown here) | `Writes`, `Borrows`         |

---

### 🏗️ Mapping ER Model to Relational Model

- **Entity ➝ Table**
- **Attribute ➝ Column**
- **Instance ➝ Row**

#### 🧾 Example: Book Entity ➝ Book Table

| Column       | Data Type    | Description                           |
|--------------|--------------|---------------------------------------|
| Title        | `VARCHAR`    | Variable-length character string      |
| Edition      | `INTEGER`    | Numeric edition number                |
| Year         | `INTEGER`    | Year the book was written             |
| ISBN         | `CHAR`       | Contains dashes, fixed length         |

---

### 🔑 Keys in Relational Databases

#### Primary Key
- **Uniquely identifies** each row (tuple) in a table
- **Prevents duplication**
- **Used to create relationships**

#### Foreign Key
- A primary key from another table
- **Creates a link** between related tables

---

### 🧠 Key Concepts Recap

- **Relational model** offers flexibility and independence
- **Entities** = objects; **Attributes** = properties of entities
- Tables are mapped from entities; attributes become columns
- Common data types:
  - `CHAR`, `VARCHAR` – for text
  - `INTEGER`, `DECIMAL` – for numbers
  - `DATE`, `TIME`, `TIMESTAMP` – for date/time
- **Primary key** ensures uniqueness
- **Foreign key** maintains relationships

## 🐍 Django Web Framework Summary

### 🌟 What is Django?
- High-level, **accessible**, **open-source** Python web framework
- Follows **Model-View-Controller (MVC)** pattern
- Built for **rapid development** and **code reusability**
- Commonly described as **"batteries included"**

---

### 🛠️ Core Features

### ✅ Build Capabilities
- Supports a wide range of web apps:
  - CMS (Content Management System)
  - Social Media platforms
  - Business Applications
  - Blogs and E-commerce sites

### 📦 Out-of-the-Box Functionality
- **ORM (Object Relational Mapping)**:
  - Define data models using Python classes
  - Perform queries, inserts, updates, deletes
- **Template Engine**:
  - Separates business logic from presentation logic
- **Admin Interface**:
  - Auto-generated and customizable backend UI

### 🔒 Security
- Built-in protection against:
  - XSS (Cross-site scripting)
  - CSRF (Cross-site request forgery)
  - SQL Injection
- Password hashing and session management

### 👤 Authentication & Authorization
- User account management (registration, login, password)
- Fine-grained permissions and access control

---

### 🧱 Extensibility & Modularity

- Supports reusable **Django Apps (modules)**
- Popular integrations:
  - `gettext` for localization
  - `Django Simple Captcha` for bot protection
- Built-in **forms module** with validation logic

---

### 🌐 Architecture & Deployment

#### 🧩 Stateless Architecture
- Follows **"Share Nothing"** model
- Each server instance handles requests **independently**
- Easier to **scale** horizontally

#### 🧪 Testing Support
- Built-in support for:
  - Unit tests
  - Integration tests
  - Functional tests
- Includes:
  - Test runner
  - Assertions
  - Fixtures

#### ☁️ Platform Agnostic
- Runs on **any OS or cloud provider**
- Examples: Azure, AWS, GCP
- Python’s portability enables broad deployment options

---

### 🧑‍🤝‍🧑 Community & Ecosystem

- Large, global, and active developer community
- Regular updates with:
  - New features
  - Performance optimizations
  - Security patches
- Contributions are open-source and community-driven

---

### 🌍 Notable Apps Built with Django

| App              | Use Case                              |
|------------------|----------------------------------------|
| Instagram        | Photo & video sharing social media     |
| Spotify          | Music streaming infrastructure         |
| YouTube (partial)| Video-sharing platform                 |
| Washington Post  | Content Management System (CMS)        |

---

### 📌 Key Takeaways
- Django supports rapid and secure web development.
- Offers a full-stack solution with built-in tools and features.
- Easily extendable and scalable.
- Ideal for developers looking to deploy robust web applications efficiently.

## 🧠 Object-Oriented Analysis and Design (OOAD)

### 🎯 What is OOAD?
- OOAD stands for **Object-Oriented Analysis and Design**
- A methodology for **analyzing** and **designing** software systems
- Used when development will be done using **object-oriented programming (OOP)** languages (e.g., Java, C++, Python)

---

### 🧱 Core Concepts of OOP

#### 🔹 Objects
- Represent real-world entities
- Contain:
  - **Data (attributes/properties)**
  - **Behavior (methods/actions)**

#### 🔹 Classes
- **Blueprints/templates** for objects
- Define:
  - Attributes (e.g., `LastName`)
  - Methods (e.g., `cancelAppointment()`)
- Example:
  - Class: `Patient`
  - Object: `Nia Patel` (instance of `Patient`)

#### 🔹 Instantiation
- Creating an actual object from a class
- Attributes are assigned specific values
- Methods become usable to perform actions

---

### 🔄 Purpose of OOAD

- Break down a system into **interacting objects**
- Enables **modular design** and **parallel development**
- Promotes **code reuse**, **flexibility**, and **scalability**

---

### 📊 UML Diagrams in OOAD

#### 🔹 Class Diagram (Structural UML Diagram)
- Represents the **structure** of a system
- Shows:
  - **Classes**
  - **Attributes** (data)
  - **Methods** (behavior)
  - **Relationships** (e.g., inheritance, association)

#### 🔹 Inheritance
- Subclass inherits properties and methods from the **parent class**
- May also define **additional attributes/methods**

#### 🧬 Example:
```

MedicalPersonnel
├── Nurse
├── Doctor
│   └── Specialist
└── Technician

```
- `Doctor` inherits from `MedicalPersonnel`
- `Specialist` inherits from `Doctor`

---

### 🧾 Summary
- OOAD involves planning a system based on **interacting objects**
- **Objects = Data + Behavior**
- **Classes** serve as blueprints for objects
- **Class diagrams** show object relationships, inheritance, and structure

## 🧠 Integrating SQL with Object-Oriented Programming (OOP) and ORM

### 🗃️ The Role of Databases in Applications

* Software developers often use **databases** as the main data store.
* To access and manipulate data, they must integrate **SQL statements** into their **application code** using **database APIs**.
* Data retrieved from the database is returned as a **Cursor**, a structure used to **iterate over result rows**.

---

### 🔄 Many-to-Many Relationships

* **Entities**: `Course` and `Learner`
* A **Course** can have many Learners, and a **Learner** can enroll in many Courses.
* This **Many-to-Many relationship** is stored using an **associative table**.

---

### 🐍 Example: Executing SQL in Python

1. **Connect** to SQLite:

   ```python
   import sqlite3
   conn = sqlite3.connect('courses.db')
   cursor = conn.cursor()
   ```
2. **Insert** a learner:

   ```python
   cursor.execute("INSERT INTO learner (first_name, last_name) VALUES (?, ?)", ("John", "Doe"))
   ```
3. **Query** the learner:

   ```python
   cursor.execute("SELECT * FROM learner")
   print(cursor.fetchone())
   ```

---

### 🧱 OOP vs SQL: Data Modeling

| Aspect                | OOP                            | SQL                            |
| --------------------- | ------------------------------ | ------------------------------ |
| Entity Representation | Classes & Objects              | Tables, Rows & Columns         |
| Data Manipulation     | Methods                        | SQL DML (INSERT, UPDATE, etc.) |
| Relationships         | Inheritance, Association, etc. | JOIN, FOREIGN KEY              |

Example:

* `Course` class: has `name`, `description`, and a list of learners
* `Learner` class: has `first_name`, `last_name`, `dob`, `occupation`, and a `print_profile()` method

---

### 🧩 Bridging the Gap: ORM (Object-Relational Mapping)

* ORM allows developers to use **OOP to interact with databases**.
* Maps class **objects** to database **rows** and vice versa.

Example:

```python
course = Course.objects.get(name="Introduction to Python")
learners = course.learners.all()
```

No need to write JOIN queries manually.

---

### 🛠️ Popular ORM Libraries

| Language   | ORM Libraries          |
| ---------- | ---------------------- |
| Python     | Django ORM, SQLAlchemy |
| Java       | Hibernate, OpenJPA     |
| JavaScript | Sequelize, TypeORM     |

---

### ✅ Pros of ORM

* Define databases with **class designs**
* **No SQL required** for CRUD
* **Multi-database support** through a unified interface
* **Faster** development & deployment

---

### ❌ Cons of ORM

* Imperfect mapping between **OOP & SQL models**
* **Tight coupling** of data access and business logic
* **Harder to debug** due to abstraction
* **Potential performance issues** due to inefficient SQL generation

---

### 🧾 Summary

* **SQL and OOP model data differently**
* **ORM bridges** the two paradigms
* ORM enables developers to work with databases **without writing SQL**
* **Advantages**: ease, speed, consistency across databases
* **Drawbacks**: mapping issues, debugging difficulty, performance limitations

---

> In this course, you’ll focus on **Django ORM**, a powerful and widely-used Python ORM tool.

## 🧰 Django ORM: Simplifying Database Operations in Python

### 🔄 What Is Django ORM?

* Django ORM (Object-Relational Mapping) is a component of the **Django Web Framework**.
* It **abstracts database interactions** by allowing developers to work with **Python classes and objects** instead of writing raw SQL queries.
* Each **Django model** maps to a **database table**.
* Each **object (instance of the model)** maps to a **row** in that table.
* Each **field** in the model maps to a **column** in the table.

---

### 🧱 Mapping Models to Tables

```python
from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
```

* Django automatically creates a `User` table with columns `first_name` (VARCHAR) and `date_of_birth` (DATE).
* Fields include optional **parameters** like:

  * `null=True`
  * `blank=True`
  * `default=value`
  * `primary_key=True`

---

### 🔗 Modeling Relationships

#### 1. **One-to-One Relationship**

**ER Example**: A `User` can have one `Instructor` profile.

```python
class Instructor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_full_time = models.BooleanField()
    total_learners = models.IntegerField()
```

> Django adds a foreign key in `Instructor` pointing to `User`.

---

#### 2. **Many-to-One Relationship**

**ER Example**: A `Course` can have many `Projects`.

```python
class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class Project(models.Model):
    name = models.CharField(max_length=100)
    grade = models.IntegerField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
```

> A `ForeignKey` creates a many-to-one relationship. Multiple `Project`s can link to a single `Course`.

---

#### 3. **Many-to-Many Relationship**

**ER Example**: `Course` and `Learner` have a many-to-many relationship.

```python
class Learner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    occupation = models.CharField(max_length=100)

class Course(models.Model):
    name = models.CharField(max_length=100)
    learners = models.ManyToManyField(Learner, through='Enrollment')
```

**Intermediate Model (with extra data):**

```python
class Enrollment(models.Model):
    learner = models.ForeignKey(Learner, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_enrolled = models.DateField()
```

> Use `through='Enrollment'` to customize and track details of the many-to-many link.

---

### 🧬 Inheritance in Django Models

#### 1. **Multi-Table Inheritance**

* Each class gets its own database table.

```python
class User(models.Model):
    name = models.CharField(max_length=50)

class Instructor(User):
    is_full_time = models.BooleanField()
```

> Django automatically creates a **one-to-one** link between `Instructor` and `User`.

#### 2. **Abstract Base Classes**

```python
class Person(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        abstract = True

class Learner(Person):
    occupation = models.CharField(max_length=100)
```

> `Person` does **not** create a database table. Only `Learner` does.

#### 3. **Proxy Models**

```python
class CustomUser(User):
    class Meta:
        proxy = True

    def custom_behavior(self):
        return "Hello!"
```

> Use proxy models to change behavior without modifying fields.

---

### 📊 Final Data Model Summary

| Model        | Relationship                                             |
| ------------ | -------------------------------------------------------- |
| `User`       | Base table with shared fields                            |
| `Learner`    | Inherits from `User`, M2M with `Course` via `Enrollment` |
| `Instructor` | Inherits from `User`, M2M with `Course`                  |
| `Course`     | M2M with `Learner` and `Instructor`                      |
| `Project`    | M2O with `Course`                                        |
| `Enrollment` | Join table for `Course` ↔ `Learner`                      |

---

### ✅ Summary

* Each **Django model** maps to a **table**.
* Each **field** maps to a **column** (with type and constraints).
* Django supports:

  * **One-to-One**
  * **Many-to-One**
  * **Many-to-Many** (with or without custom join models)
* **Model inheritance** allows sharing common fields or behavior.
* Django automatically generates the SQL schema based on your model classes.

With Django ORM, **you manage data like Python objects**, letting Django handle the SQL under the hood.

## 🔗 Django Model Relationships

### 📌 Key Relationships in Our Models

* `User` → `Instructor` and `Learner`: **One-to-One**
* `Course` → `Instructor` and `Learner`: **Many-to-Many**
* `Project` → `Course`: **Many-to-One**

---

### ➡️ Forward vs. ⬅️ Backward Relationships

#### ✅ **Forward (Explicit) Access**

You define this manually in your model using `ForeignKey`, `OneToOneField`, or `ManyToManyField`.

```python
class Learner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
```

Access user from learner:

```python
learner.user
```

#### 🔁 **Backward (Implicit) Access**

Django **automatically adds** reverse accessors for relationships.

From `User` to `Learner`:

```python
user.learner
```

> Django names the reverse access using the lowercase model name, unless specified otherwise via `related_name`.

---

### 🧬 Inheritance as One-to-One

When a model **inherits** another model, Django implicitly creates a one-to-one link.

```python
class Learner(User):
    ...
```

* Forward access:

  ```python
  learner.user_ptr
  ```

* Backward access (from `User`):

  ```python
  user.learner
  ```

---

### 🔄 Many-to-One Example: Project → Course

```python
class Project(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
```

* **Forward access** (explicit):

  ```python
  project.course
  ```

* **Backward access** (implicit):

  ```python
  course.project_set.all()
  ```

> `_set` is the default suffix unless overridden.

---

### 🔗 Many-to-Many Example: Course ↔ Instructor

```python
class Course(models.Model):
    instructors = models.ManyToManyField(Instructor)
```

* Forward:

  ```python
  course.instructors.all()
  ```

* Backward:

  ```python
  instructor.course_set.all()
  ```

---

## 🗑️ `on_delete` Options for ForeignKey

When the **related object is deleted**, these behaviors apply:

| Option        | Behavior Description                                                        |
| ------------- | --------------------------------------------------------------------------- |
| `CASCADE`     | Delete related objects too (default).                                       |
| `PROTECT`     | Prevent deletion if related objects exist.                                  |
| `SET_NULL`    | Set ForeignKey to `NULL` (only if `null=True`).                             |
| `SET_DEFAULT` | Set to default value.                                                       |
| `SET(...)`    | Set to a given value or callable.                                           |
| `DO_NOTHING`  | Does nothing – may cause **referential integrity errors**. Not recommended. |

---

## 🛠️ Managing Related Objects (Reverse Relations)

Assume:

```python
course = Course.objects.get(id=1)
learner = Learner.objects.get(id=2)
```

| Action      | Code Example                                |
| ----------- | ------------------------------------------- |
| Add         | `course.learners.add(learner)`              |
| Create      | `course.learners.create(user=some_user)`    |
| Remove      | `course.learners.remove(learner)`           |
| Clear All   | `course.learners.clear()`                   |
| Replace All | `course.learners.set([learner1, learner2])` |

---

### ✅ Summary

* **Only define relationships on one side (forward)**.
* **Django auto-generates reverse access** (backward relationships).
* **On deletion**, you can **control how related objects behave** via `on_delete`.
* You can **manage related objects dynamically** using `add()`, `create()`, `remove()`, `clear()`, and `set()` methods.

This model API makes it easy to manipulate related data while keeping your code clean and avoiding direct SQL.

## 🧩 Online Course App Models

Entities used in the app:
- **Content Models**: `Course`, `Lesson`, `Question`, `Choice`
- **User Models**: `User`, `Instructor`, `Learner`
- **Action Models**: `CourseEnrollment`, `Submission`

---

## 🛠️ Django Admin Site for Content Management

### 🎯 Purpose
- Separates **content publishers (admin)** from **users (learners)**
- Instructors and site managers use the admin site to manage:
  - Courses
  - Lessons
  - Questions
  - Choices

---

## 👤 Create Superuser for Admin Site

```bash
python manage.py createsuperuser
```

> Prompts for username and password.
> Once created, start server and log in via `/admin`.

---

## 📝 Register Models in Admin

In `onlinecourse/admin.py`:

```python
from django.contrib import admin
from .models import Course, Instructor

admin.site.register(Course)
admin.site.register(Instructor)
```

Refresh the admin page to see **Course** and **Instructor** under *Onlinecourse* section.

---

## 🧮 Model Field Widgets in Admin

* Boolean: checkbox (`is_full_time`)
* Integer: number input (`total_learners`)
* Related model (`User`) is editable through the linked Instructor model
* Some fields like `total_learners` are better calculated automatically, not managed manually

---

## 🧩 Customize Admin Form Fields

To control **which fields are shown** and their order:

```python
class CourseAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'name', 'description']

admin.site.register(Course, CourseAdmin)
```

Only `pub_date`, `name`, and `description` fields are now shown when adding/editing courses.

---

## 📚 Inline Models (Nested Forms)

To edit related models (like `Lesson`) inside the parent model (`Course`) form:

```python
class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5  # max additional lesson forms

class CourseAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'name', 'description']
    inlines = [LessonInline]
```

Now, adding a Course also allows adding **up to 5 Lessons inline**.

---

## 📋 Display Fields in List View

To control which fields show in the table view of a model:

```python
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'pub_date']
```

Now only `name` and `pub_date` appear in the course list.

---

## 🔍 Search & Filter in Admin List View

To enable search and filters:

```python
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'pub_date']
    search_fields = ['name']
    list_filter = ['pub_date']
```

* Adds a **search box** to find courses by name
* Adds a **filter sidebar** for pub\_date

---

## ✅ Summary

* Django admin is a powerful, customizable tool for managing models.
* You can:

  * Control displayed fields with `fields` and `list_display`
  * Add related models inline using `Inline` classes
  * Add search and filter capabilities
* Helps non-technical users manage content easily without extra code
Í
## Django Function-Based Views Summary

- A **Django view** is a Python function that takes an **HTTP request** and returns an **HTTP response**.
- The **request object** includes read-only metadata:
  - `method` (e.g. GET, POST)
  - headers
  - parameters
  - payload

### Example View Logic:
- Query the first course from the database.
- Pass the course name into an HTML template.
- Return an `HttpResponse` object with HTML content.

### HttpResponse Constructor Can Accept:
- A string
- An HTML page
- A byte string

### Mapping URL to View:
- Done in the app’s `urls.py` file (URLConf).
- Use the `path()` function:
  - **First argument**: `route` (URL pattern)
  - **Second argument**: view function
  - **Third (optional)**: `name` (reference for reverse URL lookup)

### Namespacing with app_name:
- Use `app_name = "onlinecourse"` to namespace views.
- Reference views using `onlinecourse:course`.

### HTTP Status Codes:
- `200 OK`: Request processed successfully.
- `404 Not Found`: Course not found or error occurred.
- Use `HttpResponse(content, status=404)` to return custom error messages or pages.

### Recap:
- Django views handle requests and return responses.
- You map views to URL patterns.
- Status codes help indicate success or failure.

# Django Templates Summary

## What is a Django Template?
A **Django template** is an HTML file embedded with Django **template tags** and **variables**. It's used to present data dynamically to the user, rendered by the Django template engine.

---

## Template Folder Structure
To add a template to the `onlinecourse` app:

```

onlinecourse/
├── templates/
│   └── onlinecourse/
│       └── course\_list.html

```

- The **first `onlinecourse`** is the app folder.
- The **second `onlinecourse`** inside `templates` is for **namespace** to avoid name clashes with templates from other apps.

---

## Rendering a Template

- Templates are rendered **with a context**—a dictionary-like object containing variables.
- Django replaces variables with their values and executes tags like `{% if %}`, `{% for %}`, etc.
- Example:
  ```django
  {% if course_list %}
    {% for course in course_list %}
      <h1>{{ course.name }}</h1>
      <p>{{ course.description }}</p>
    {% endfor %}
  {% else %}
    <p>No courses available.</p>
  {% endif %}
```

---

## Views and Context

* Views gather data and **pass it to templates** using the `render()` method:

  ```python
  def index(request):
      courses = Course.objects.all()
      context = {'course_list': courses}
      return render(request, 'onlinecourse/course_list.html', context)
  ```

* Parameters to `render()`:

  1. `request`
  2. Template path (relative to `templates/`)
  3. `context` dictionary

---

## Output

* The `course_list.html` template receives course data from the view and displays it dynamically.
* Example output includes headers and paragraphs for:

  * Introduction to Python
  * Django Course

---

## Adding Static Files (CSS)

* Use `{% load static %}` at the top of the HTML.

* Reference static files using `{% static 'css/style.css' %}`.

* Example:

  ```html
  <link rel="stylesheet" href="{% static 'css/style.css' %}">
  ```

* Add CSS classes to HTML elements to style:

  ```html
  <body class="main-body">
    <p class="course-desc">{{ course.description }}</p>
    <hr class="divider">
  </body>
  ```

---

## Result

* CSS styles are applied:

  * Light gray background
  * Green course descriptions
  * Horizontal line separators

---

## Key Takeaways

* Django templates separate presentation from logic.
* Views provide data using context dictionaries.
* Static files like CSS enhance template design.

## Django Views: Function-Based vs Class-Based

### Function-Based Views (FBVs)

- Simple Python functions that handle requests and return responses.
- Example:
```python
  def course_view(request):
      course = Course.objects.first()
      return HttpResponse(f"Course: {course.name}")
```

#### ✅ Pros:

* Easy to read and understand.
* Explicit control over logic.

#### ❌ Cons:

* Not easily reusable or extendable.
* Requires manual method checks (`if request.method == 'POST'`).

---

### Class-Based Views (CBVs)

* Views written as Python classes, subclassing `django.views.View`.
* Organize code by HTTP method (`get()`, `post()`, etc.).
* Example:

  ```python
  from django.views import View

  class CourseView(View):
      def get(self, request):
          course = Course.objects.first()
          return HttpResponse(f"Course: {course.name}")
  ```

  URL configuration:

  ```python
  path('course/', CourseView.as_view(), name='course')
  ```

#### How It Works:

1. `.as_view()` returns a callable view.
2. The `dispatch()` method routes to the correct handler (`get`, `post`, etc.).

#### ✅ Pros:

* Better structure for handling different methods.
* Supports mixins and inheritance.

#### ❌ Cons:

* More abstract and complex.
* Can be harder to trace and debug.

---

### Generic Class-Based Views (GCBVs)

* Built-in CBVs for common patterns like displaying a list, handling forms, etc.
* Example:

  ```python
  from django.views.generic.detail import DetailView

  class CourseDetailView(DetailView):
      model = Course
      template_name = "onlinecourse/course_detail.html"
  ```

#### ✅ Pros:

* Less code for common tasks.
* Easy to build CRUD views.

#### ❌ Cons:

* Less flexible if customization is needed.
* More layers of abstraction.

---

### Summary Table

| Type                | Pros                  | Cons                           | Best For                                   |
| ------------------- | --------------------- | ------------------------------ | ------------------------------------------ |
| Function-Based      | Clear, explicit       | Repetitive, not reusable       | Simple, custom views                       |
| Class-Based         | Organized, reusable   | More complex, less transparent | Moderate to complex logic                  |
| Generic Class-Based | Very concise for CRUD | Harder to customize deeply     | Standard CRUD operations and form handling |
