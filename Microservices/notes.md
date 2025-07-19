# IBM: Application Development using Microservices and Serverless

## 🧱 Twelve-Factor App Methodology

### 🎯 Objectives
- Describe characteristics of **modern software development**
- Understand the **goal of twelve-factor apps**
- Identify and map the **12 factors** to phases of the **software delivery lifecycle** (code, deploy, operate)

---

## 🌐 Modern Software Delivery
- **Software-as-a-Service (SaaS)**: Centrally hosted, accessed via internet
- **Web apps**: Common daily tools (e.g., booking, tax filing)
- **Microservices**: Often used, but **not required**

---

## 🧑‍💻 Code Phase

### 1. **Codebase**
- One codebase tracked in **version control** (e.g., Git)
- One-to-many mapping: **one codebase, multiple deploys**
- Consistent code, varying versions (dev, test, prod)

### 2. **Dependencies**
- Explicitly declare **all dependencies**
- Prevent reliance on system-level packages or tools

### 5. **Build, Release, Run**
- **Build**: Compile code, collect dependencies, generate artifact
- **Release**: Combine build with environment-specific config
- **Run**: Launch application
- **Separation enforced**: No code change at runtime

### 10. **Dev/Prod Parity**
- **Minimize differences** between dev and prod
- Match backend services across environments
- Enables **continuous delivery** and **early bug detection**

---

## 🚀 Deploy Phase

### 3. **Config**
- Store **env-specific config** in **environment variables**
- Avoid hardcoding credentials or URLs

### 4. **Backing Services**
- Treat all services (local or third-party) the same
- Access via URL and credentials; **swap without code changes**

### 6. **Processes**
- Execute app as **stateless, share-nothing processes**
- Use backend services (e.g., DBs) for persistence

### 7. **Port Binding**
- Export services via **port binding**
- App runs own web server, listens on a declared port
- Enables discoverability and reusability

---

## ⚙️ Operate Phase

### 8. **Concurrency**
- Scale via **concurrent stateless processes**
- Add more processes to handle increasing load horizontally

### 9. **Disposability**
- Fast startup and graceful shutdown
- Enables **rapid deployments**, **robust scaling**

### 11. **Logs**
- Treat logs as **event streams**
- Write to **stdout**; environment handles log routing

### 12. **Admin Processes**
- One-off tasks (e.g., DB migrations)
- Run using **same codebase/config** as the app

---

## 🧠 Key Takeaways

- Modern development = **web-based SaaS**
- Twelve-factor apps support **efficiency, scalability, and maintainability**
- Factors mapped to:
  - **Code**: Codebase, Dependencies, Build/Release/Run, Dev/Prod Parity
  - **Deploy**: Config, Backing Services, Processes, Port Binding
  - **Operate**: Concurrency, Disposability, Logs, Admin Processes

## Microservices Architecture

Microservices architecture is a design approach in which a single application is built as a collection of **loosely coupled**, **independently deployable** services. Each service:

* Is **segregated by business functionality**, often referred to as a **bounded context**.
* Can have its **own technology stack**, including its own database and programming language.
* Communicates with others via **REST APIs**, **event streaming**, or **message brokers**.

### Key Characteristics

* **Independence**: Each microservice operates independently. This allows:

  * Easier updates and feature additions.
  * Faster development and deployment cycles.
* **Scalability**: Services can be **horizontally scaled** (i.e., “scaling out”) by adding more instances **only to components that need it**, reducing waste and infrastructure cost.
* **Fault Isolation**: A failure in one service typically **does not affect** the others.
* **Autonomous Teams**: Teams can work independently using the tools and languages best suited for their service.

### Communication Methods

* **API Calls**: Good for initial state setup.
* **Event Streaming / Message Brokers**: Better for **staying updated** and broadcasting **state changes**, which aids in efficient scaling and coordination.

### Summary from Video (2:31):

* Microservices break applications into independently deployable components.
* Each service communicates via **APIs**.
* Microservices allow different **technology stacks**.
* Components **scale individually** as needed.
* They **reduce risk** during updates or changes.
* **Failures are isolated** to the affected service, not the entire application.

## Monolithic vs SOA vs Microservices Architecture

### Monolithic Architecture

* **Definition**: All or most functionality exists within a single process and codebase.
* **Structure**: Managed in internal layers (UI, security, data access, etc.) that are tightly coupled.
* **Advantages**:

  * Simplicity
  * Easier to develop and deploy initially
* **Disadvantages**:

  * Becomes complex as scope increases
  * Difficult to modify or adopt new technology
* **Example**: Windows Forms Application with UI, business logic, and data access all in one.

### Service-Oriented Architecture (SOA)

* **Definition**: Built around service provider/consumer model with reusable, loosely coupled services.
* **Components**:

  * **Interface**: Executes requests
  * **Contract**: Defines interaction rules
  * **Implementation**: Service logic
* **Advantages**:

  * Supports parallel development
  * Enables reusability and reliability
* **Disadvantages**:

  * Complex to implement
  * Costly, requiring significant resources and expertise
* **Scope**: Enterprise-wide
* **Example**: Banking system exposing business functions over service interfaces.

### Microservices Architecture

* **Definition**: Application is broken into small, independent services with specialized responsibilities.
* **Characteristics**:

  * Each service is independently deployable and scalable
  * Services do not share data
  * Freedom to choose different tech stacks per service
* **Advantages**:

  * Flexibility to scale and innovate
  * Better modularity and targeted upgrades
* **Disadvantages**:

  * Complex security management (e.g., TLS for each service)
  * Debugging becomes harder due to distributed nature
* **Scope**: Application-level
* **Example**: E-commerce app with separate services for orders, security, and analytics.

### Summary

* **Monolithic**: Interconnected and interdependent
* **SOA**: Reusable and enterprise-integrated services
* **Microservices**: Scalable, flexible, and independently deployable components

## Microservices Patterns

### Single-Page Application (SPA) Pattern

* **Purpose**: Enhances front-end user experience through dynamic content updates without full page reloads.
* **Architecture**:

  * Built with HTML, CSS, JavaScript
  * Interacts with backend REST APIs
* **Pros**:

  * Seamless user experience
  * Faster client-side interactions
* **Cons**:

  * Shifts complexity to backend
  * Not optimized for multi-channel (mobile + web) experiences

### Backend for Frontend (BFF) Pattern

* **Purpose**: Tailors backends to specific frontend channels (e.g., mobile vs. desktop).
* **How It Works**:

  * Each user interface (mobile, desktop) has its own backend microservice
  * These BFF services call other backend services as needed
* **Benefits**:

  * Optimized user experience per platform
  * Separation of concerns improves maintainability

### Strangler Pattern

* **Purpose**: Gradually migrate monolithic applications to microservices.
* **Steps**:

  1. **Transform**: Create a parallel microservice version.
  2. **Coexist**: Run both monolith and microservices side-by-side.
  3. **Eliminate**: Fully replace monolith functionality with microservices.
* **Analogy**: Like a vine slowly replacing a tree.

### Service Discovery Pattern

* **Purpose**: Enables services to dynamically find and communicate with each other.
* **Why It's Needed**:

  * Microservices scale dynamically
  * IPs and instances change due to failures or updates
* **Use Cases**:

  * Load balancing
  * Health checks
  * Auto-scaling coordination

### Additional Patterns

* **Entity and Aggregate Pattern**:

  * Used to group related entities (e.g., an order with multiple products)
  * Helps manage complex domain relationships

* **Adapter Pattern**:

  * Translates between incompatible interfaces (e.g., legacy systems or third-party APIs)
  * Acts like a plug adapter converting between formats or protocols

### Summary

* **SPA** improves user experience via dynamic updates.
* **BFF** supports customized frontend logic per platform.
* **Strangler** enables staged migration from monoliths.
* **Service Discovery** handles dynamic microservice communication.
* **Entity/Aggregate and Adapter** address domain modeling and integration.

## Microservices Anti-Patterns

### Don’t Build Microservices

* Avoid starting with microservices from the beginning.
* Only consider microservices when your monolithic application becomes too complex to update and maintain.
* Refactor into services *only* after experiencing real pain points in scalability or manageability.

### Not Taking Automation Seriously

* Microservices introduce multiple codebases, test pipelines, and deployments.
* Without proper **automation** (CI/CD, monitoring, testing) or **cloud services**, managing microservices becomes chaotic.
* Embrace **DevOps** practices or use **managed cloud solutions** early.

### Don’t Build Nanoservices

* Over-splitting leads to *nanoservices*—so small they increase complexity more than they add value.
* Prefer larger services until:

  * Deployment becomes hard
  * Data models grow too complex
  * Scaling requirements diverge

### Don’t Turn Into SOA

* Avoid confusing microservices with SOA.
* Microservices must be **fine-grained** and maintain **independent data storage** per service.
* Avoid falling into traditional, heavyweight SOA patterns—this compromises microservice agility.

### Don’t Build a Gateway for Each Service

* Don’t embed orchestration, authentication, routing, etc., into each service.
* Use a **central API Gateway** to handle:

  * Authentication
  * Throttling
  * Routing
  * Analytics
  * Transformation
* Promotes consistency and reduces duplication.

### Conclusion

Microservices aim to:

* Improve customer experience
* Adapt to new requirements
* Cut costs with granular business functions

But failing to avoid these **anti-patterns** can make microservices more of a burden than a benefit.

## What is REST?

REST (Representational State Transfer) is an architectural style for designing networked applications, particularly APIs, that provides a flexible and lightweight method of communication.

### Key Characteristics of RESTful APIs

* **HTTP-based**: All requests are made using standard HTTP methods.
* **Stateless**: Each request from client to server must contain all the information needed to understand and process it. No session state is stored on the server.
* **Client-server architecture**: Separation between the client and server, enabling independent development.
* **Uniform interface**: Standardized way of interacting with resources via URIs.

### HTTP Methods Used in REST

* **POST**: Create a new resource.
* **GET**: Retrieve a resource.
* **PUT**: Update a resource.
* **DELETE**: Delete a resource.

### Benefits of REST APIs

* **Scalability**: Stateless nature supports scaling across servers.
* **Simplicity**: Uses HTTP and JSON, making it easy to implement and consume.
* **Consistency**: Uniform interface ensures consistent access to resources.
* **Language-agnostic**: Can be used across various programming environments.

### Real-world Example: CEX.IO API

CEX.IO, a cryptocurrency exchange, uses a REST API to expose market data. Developers can retrieve data like the last price of a currency pair using standard HTTP requests. Their documentation includes request/response formats and code samples in multiple programming languages.

### Summary

* REST APIs offer scalable, stateless, and consistent interfaces.
* They operate over HTTP using POST, GET, PUT, and DELETE.
* REST defines a standard method for network communication.
* Used widely in microservices and modern web architectures.
