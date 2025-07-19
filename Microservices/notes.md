# IBM: Application Development using Microservices and Serverless

> Module 1

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

> Module 3

## Introduction to Serverless Computing

### What is Serverless Computing?

Serverless computing is a cloud-native development model where developers build and run applications without managing servers. The cloud provider handles infrastructure tasks like provisioning, scaling, patching, and managing servers.

> Defined by CNCF:
> “The concept of building and running applications that do not require server management. It describes a finer-grained deployment model where applications, bundled as one or more functions, are uploaded to a platform and then executed, scaled, and billed in response to the exact demand needed at the moment.”

---

### Core Components

* **Function-as-a-Service (FaaS):** Run application logic in the form of functions triggered by events.
* **Backend-as-a-Service (BaaS):** Utilize backend services like databases, queues, and storage without managing infrastructure.

---

### Evolution of Computing Models

| Model            | Deployment Time | Lifespan   | Description                                                |
| ---------------- | --------------- | ---------- | ---------------------------------------------------------- |
| Traditional      | Weeks/Months    | Years      | Physical machines with high upfront cost.                  |
| Virtual Machines | Minutes         | Days/Weeks | Virtualized infrastructure with better provisioning.       |
| Containers       | Seconds         | Hours      | OS-level virtualization with rapid scaling.                |
| **Serverless**   | Milliseconds    | Seconds    | Event-driven, fine-grained, infrastructure-free functions. |

---

### Key Characteristics

* **Hostless**: No server management required.
* **Elastic**: Instant auto-scaling based on demand.
* **Automated Load Balancing**: Distributes traffic across systems.
* **Stateless**: Each function call is isolated, improving scalability and performance.
* **Event-Driven**: Functions run only in response to specific triggers.
* **High Availability**: Built-in, with no extra effort needed.
* **Usage-Based Billing**: Pay only for compute time, not idle time.

---

### Serverless Function Lifecycle

1. Developer writes function code (e.g., Python, Node.js, Java).
2. Uploads function to cloud provider.
3. Defines events/triggers (e.g., HTTP request, file upload).
4. Trigger invokes function.
5. Cloud executes and manages runtime environment.

---

### Developer Benefits

* Focus on core logic, not infrastructure.
* Build with any major programming language.
* Easier testing and optimization.
* Extend apps by chaining simple, single-responsibility functions.
* Improve overall user experience and deployment speed.

---

### Comparison: Cloud Service Models

| Responsibility | Traditional | IaaS   | PaaS   | **Serverless** | SaaS   |
| -------------- | ----------- | ------ | ------ | -------------- | ------ |
| Applications   | You         | You    | You    | **You**        | Vendor |
| Data           | You         | You    | You    | **You**        | Vendor |
| Runtime        | You         | You    | Vendor | Vendor         | Vendor |
| Middleware     | You         | You    | Vendor | Vendor         | Vendor |
| OS             | You         | Vendor | Vendor | Vendor         | Vendor |
| Virtualization | You         | Vendor | Vendor | Vendor         | Vendor |
| Servers        | You         | Vendor | Vendor | Vendor         | Vendor |
| Storage        | You         | Vendor | Vendor | Vendor         | Vendor |
| Networking     | You         | Vendor | Vendor | Vendor         | Vendor |

---

### Summary

* Serverless allows code execution without server management.
* It includes FaaS for running code and BaaS for using cloud-based services.
* It improves scalability, flexibility, and developer productivity.
* Cloud providers manage the entire stack except the application logic.
* You only pay for what you use, making it cost-efficient.

## Serverless Pros and Cons

### Benefits of Serverless Computing

* **No Infrastructure Management**: Cloud providers handle provisioning, maintenance, patching, and scaling.
* **Cost-Effective**: Pay only per request; no charges for idle compute.
* **High Availability & Fault Tolerance**: Built-in by the cloud provider.
* **Faster Time to Market**: Functions deploy in milliseconds; teams focus solely on code.
* **Optimized Resource Usage**: Functions run only when triggered.
* **Built-in IDEs**: Accelerate development and deployment.
* **Supports Multiple Languages**: Use any popular programming language (as supported by provider).
* **Strong Third-Party Integration**: For auth, databases, messaging, and more.
* **Greener Computing**: Reduced compute waste due to idle-free architecture.
* **Encourages Innovation**: Low-cost experimentation is viable.

---

### Constraints of Serverless Computing

* **Not Ideal for Long-Running Workloads**: Pay-per-use model becomes costly.
* **Vendor Lock-In**: Deep dependency on specific cloud platforms and tools.
* **Cold Starts**: Latency introduced when functions are idle for long periods.
* **High Latency**: Not suited for real-time or time-critical applications (e.g. banking, healthcare).
* **Security Challenges**: Broader attack surface; relies on provider’s security.
* **Difficult Monitoring & Debugging**: Hard to simulate and trace distributed serverless environments.
* **Limited Language Support**: Tied to what cloud providers offer.
* **No Server Optimization**: Cannot tune performance or utilization.
* **No State Persistence**: Each invocation is stateless; use external caches like Redis/Memcached.

---

### Serverless vs Containers

#### Serverless – Pros (vs Containers)

* Lower operational cost (pay-per-use)
* Zero infrastructure management
* Instant auto-scaling
* Millisecond-level deployment
* Accelerated development cycle

#### Containers – Pros (vs Serverless)

* Easier local and cloud testing
* Highly portable (OS, language, and provider agnostic)
* Minimal latency, suitable for real-time workloads
* Ideal for long-running processes and batch jobs
* Full control over configuration and resources
* Support for any programming language

> **Hybrid Use**: Serverless and containers can be combined.
> *Industry guidance: “Build serverless first, then use containers if needed.”*

---

### Serverless vs Traditional Computing

#### Serverless – Pros (vs Traditional)

* No need to set up or maintain infrastructure
* Cost-efficient: pay only for usage
* Automatic scalability
* Access to built-in integrations and libraries

#### Traditional – Pros (vs Serverless)

* Full control of data and infrastructure
* Use of standard networking (IP-based access)
* Security contained within organizational boundaries
* Minimal vendor lock-in

---

### Summary

* Serverless simplifies development and enhances scalability and cost-efficiency.
* It is best suited for event-driven, short-lived, and unpredictable workloads.
* Limitations include latency, lack of control, and difficulty in debugging.
* Serverless, containers, and traditional computing each have their place—often used together for optimal solutions.

## Introduction to the FaaS Model

### What is FaaS?

* **Function-as-a-Service (FaaS)** is a cloud computing service enabling you to run code in response to events, without managing infrastructure.
* It is a **subset of serverless computing**.
* Applications are composed of **small, independent functions**, each performing a single task.
* Functions are written in any supported programming language.
* FaaS functions are **stateless**, but state can be preserved using external services like caches.
* Functions execute in **milliseconds**, handle requests in **parallel**, and scale **automatically**.
* Billing is based on **execution time**, not server size or idle time.
* FaaS can be deployed in **hybrid or on-prem environments**.

---

### Benefits of FaaS

* **No infrastructure management**: Focus entirely on application logic.
* **Cost-efficient**: Pay only when code is executed—no costs for idle time.
* **Automatic scalability**: Functions scale up or down independently based on demand.
* **High availability**: Functions are deployed across regions/availability zones without extra cost.
* **Faster time-to-market**: Quick deployment cycles accelerate product delivery.
* **Efficient resource use**: Functions are lightweight and event-driven.

---

### Serverless Stack Components

1. **FaaS** – Executes application logic/functions.
2. **BaaS** – Provides backend services like databases, storage, messaging, etc.
3. **API Gateway** – Routes external requests to appropriate functions.

#### Workflow Example:

* Events (HTTP, webhooks, scheduled jobs) reach the **API Gateway**.
* The gateway invokes relevant **FaaS functions**.
* Functions process the events, potentially interacting with **BaaS services**.
* Responses return through the API Gateway to the client.

---

### Real-World Example: Image Upload

* A user uploads a profile image to object storage.
* This event triggers a cloud function (e.g., IBM Cloud Function).
* The function creates a thumbnail image.
* The thumbnail is stored for use on the website.

---

### FaaS Best Practices

* Functions should perform **a single task** (micro-function).
* Keep functions **lightweight, efficient, and fast-loading**.
* Avoid excessive use of third-party libraries (slows initialization).
* Don’t over-divide logic—**too many functions** increase cost and complexity.
* Leverage **external storage/cache** for persistence (e.g., Redis, Memcached).

---

### Managed FaaS Providers

* **AWS Lambda**
* **Google Cloud Functions**
* **Azure Functions**
* **IBM Cloud Functions**
* **OpenShift Cloud Functions**
* Others: Netlify, Oracle, Twilio

### Self-Managed FaaS Platforms

* **Fission** – Kubernetes-native serverless functions
* **Fn Project** – Container-native platform
* **Knative** – Kubernetes-based FaaS framework
* **OpenFaaS** – Turns Linux/Windows processes into functions

---

### Summary

* FaaS enables execution of code in response to events without infrastructure overhead.
* It's cost-effective, scalable, and ideal for microservice-style architectures.
* A serverless stack includes FaaS, BaaS, and an API Gateway.
* Multiple managed and self-managed FaaS options are available depending on needs.

## The Serverless Framework

### What is the Serverless Framework?
- Free, open-source web framework written in **Node.js**
- Originally built for **AWS Lambda**, but supports:
  - **Microsoft Azure**
  - **Google Cloud Platform**
  - **Apache OpenWhisk**
- Provides a **CLI** for:
  - Structure
  - Automation
  - Best practices
- Enables building **event-driven** serverless architectures

---

### Core Concepts

#### Function
- Independent unit of execution (like a microservice)
- Performs a **single task**
- Triggered by **events**

#### Event
- Source that triggers a function
- Examples:
  - HTTP request (API Gateway)
  - File uploaded to an S3 bucket

#### Resource
- Infrastructure components used by functions
- Examples:
  - **Databases**
  - **S3 buckets**

#### Service
- Organizational unit in Serverless Framework
- Defined using `serverless.yml`
- Includes definitions for:
  - **Functions**
  - **Events**
  - **Resources**
- Entire service is deployed using CLI in one go

---

### Hello World Demo (AWS + Python)

1. **Install CLI**  
   `npm install -g serverless`

2. **Create a service**  
   Run `serverless` command to go through setup wizard

3. **Deploy**  
   - CLI outputs a **URL**
   - Access the URL to see result

4. **Modify Function Code**  
   - Change return value to `"Hello World"`
   - **Redeploy** and test again

---

### Key Takeaways
- Serverless Framework helps you define and deploy functions, events, and resources via `serverless.yml`
- Functions are small units of code triggered by events
- Each service is self-contained and managed via the CLI
