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
