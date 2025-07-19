# IBM: Application Development using Microservices and Serverless

```md
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
```
