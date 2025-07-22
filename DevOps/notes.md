# Cloud Native, DevOps, Agile, and NoSQL

## Get Started with Cloud Native, DevOps, Agile, and NoSQL

### Course Overview
This course is designed to provide you with the foundational knowledge and practical skills to build, deploy, and manage cloud-native applications using modern development practices and tools.

---

### Learning Objectives
By the end of this course, you will be able to:
- Acquire comprehensive knowledge of **cloud-native concepts** and development skills.
- Utilize **DevOps** and **CI/CD methodologies** to enhance development efficiency.
- Implement **Agile practices** for adaptive, fast-paced software delivery.
- Understand the role of **NoSQL databases** in handling big data and building resilient applications.

---

### Course Modules

#### Module 1: Cloud Concepts
- Learn about **cloud deployment models** (Public, Private, Hybrid, Multicloud).
- Explore **cloud service models** (IaaS, PaaS, SaaS).
- Review the **CNCF Trail Map** to understand cloud-native technology paths.

#### Module 2: DevOps and CI/CD Tools
- Tools introduced:
  - **GitHub** for version control and collaboration
  - **Tekton** and **Jenkins** for CI/CD automation
- Focus: Automate and streamline development pipelines for faster delivery.

#### Module 3: Agile Project Management
- Tool introduced:
  - **ZenHub**, a project management tool that integrates with GitHub
- Focus: Enhancing team collaboration and visibility in Agile workflows.

#### Module 4: NoSQL Databases
- Databases covered:
  - **MongoDB**
  - **IBM Cloudant**
- Learn about their:
  - Document-oriented data models
  - Architecture and advantages
  - Use cases in cloud-native apps

#### Final Module: Capstone Project
- Apply tools and concepts from previous modules
- Develop and present a complete cloud-native application project

---

### Course Features
- **Intermediate-level** curriculum with guided instructional videos
- **Interactive activities** to reinforce learning
- **Hands-on labs** to practice real-world skills
- **Community forums** for collaboration and support
- **Practice and graded assessments** for knowledge validation
- **Shareable badge and certificate** upon successful completion

---

### Prerequisites
You should already be familiar with:
- Basic computer and programming terminology
- Version control, debugging, and software testing
- Integrated Development Environments (IDEs)

---

> Module 1

## Cloud Computing Overview

### Learning Objectives
After completing this module, you will be able to:
- Define **Cloud Computing**
- Explain the **5 Essential Characteristics** of Cloud Computing
- Describe the **4 Cloud Deployment Models**
- Describe the **3 Cloud Service Models**

---

### What is Cloud Computing?
Cloud computing is the **on-demand delivery** of computing resources—such as servers, storage, databases, networking, software—**over the internet** with **pay-per-use pricing**.

#### NIST Definition:
> "Cloud computing is a model for enabling convenient, on-demand network access to a shared pool of configurable computing resources... that can be rapidly provisioned and released with minimal management effort or service provider interaction."

---

### Five Essential Characteristics of Cloud Computing
1. **On-Demand Self-Service**  
   Users can provision computing resources automatically without human interaction with the provider.

2. **Broad Network Access**  
   Services are available over the network and accessed through standard platforms (mobile, tablets, laptops, etc.).

3. **Resource Pooling**  
   Resources are pooled to serve multiple customers using a **multi-tenant model**. Physical resources are dynamically assigned and reassigned.

4. **Rapid Elasticity**  
   Capabilities can be elastically scaled up or down according to demand. To the user, resources may appear unlimited.

5. **Measured Service**  
   Usage is automatically monitored, controlled, and reported, providing transparency for both provider and consumer.

---

### Four Deployment Models
| Model         | Description                                                                 |
|---------------|-----------------------------------------------------------------------------|
| **Public**    | Resources are available over the internet and shared across organizations. |
| **Private**   | Resources are used exclusively by one organization, either on-premises or hosted. |
| **Hybrid**    | Combines public and private clouds, allowing data and applications to be shared. |
| **Community** | Shared by several organizations with common concerns (e.g., compliance, mission). |

---

### Three Service Models
| Model         | Description                                                                 |
|---------------|-----------------------------------------------------------------------------|
| **IaaS**      | *Infrastructure as a Service* - Provides basic computing infrastructure like servers, storage, and networks. Example: AWS EC2 |
| **PaaS**      | *Platform as a Service* - Offers platforms for developers to build and deploy apps. Example: Google App Engine |
| **SaaS**      | *Software as a Service* - Delivers software applications over the internet on a subscription basis. Example: Microsoft 365 |

---

### Summary
- Cloud computing enables flexible, cost-efficient access to computing resources.
- It is defined by five essential characteristics: **self-service, broad access, resource pooling, elasticity,** and **measured usage**.
- It can be deployed through **public, private, hybrid,** or **community** models.
- Services are delivered through **IaaS, PaaS,** and **SaaS** models, catering to different layers of the technology stack.

## Cloud Native Applications

### Learning Objectives
After completing this module, you will be able to:
- Describe the **difference between monolithic and cloud native applications**
- List the **layers of the cloud native solution stack**
- Discuss the **benefits of cloud native applications**

---

### Monolithic vs. Cloud Native Applications

#### Monolithic Applications:
- Built as a **single, tightly-coupled unit** combining UI, business logic, and data layers
- Typically **stateful** and rely on **load balancing**
- **Difficult to scale** and **prone to outages** causing poor user experience
- Example: A legacy enterprise app deployed on a few centralized servers

#### Cloud Native Applications:
- Composed of **independent microservices** working together
- Microservices are often packaged in **containers**
- **Stateless**, scalable, and resilient to failure
- Support **continuous delivery** and **agile development**
- Designed for **public, private, hybrid, or multi-cloud environments**

---

### Software as a Service (SaaS) & The Twelve-Factor App Methodology
- SaaS: Software centrally hosted and accessed via the internet
- Examples: Online reservation systems, tax-filing platforms, email clients
- **Twelve-Factor App Methodology** provides best practices for building scalable and maintainable cloud apps
- Microservices and twelve-factor methodology are often used together (but not required)

---

### Layers of the Cloud Native Solution Stack

| Layer                          | Description |
|-------------------------------|-------------|
| **Cloud Infrastructure**      | Environment setup for public, private, hybrid, or multi-cloud |
| **Scheduling & Orchestration**| Tools like **Kubernetes**, **Istio**, and **Knative** that manage deployments |
| **Application & Data Services**| Backing services (databases, APIs, message queues) integrated into your app |
| **Application Runtimes**      | Middleware for running cloud apps |
| **Application Code**          | The actual microservices and app logic |

---

### Standardization in Cloud Native Apps
To support scalability and maintainability:
- Use **standardized logging**
- Emit **standardized events**
- Provide a **standard service catalog** used across microservices
- Implement **standardized tracing** for monitoring

This **commoditization** means development teams can focus on building features instead of reinventing infrastructure components.

---

### Benefits of Cloud Native Applications
- **Scalability**: Microservices can scale independently
- **Resilience**: Faults in one service don't crash the entire app
- **Agility**: Faster development and deployment cycles
- **Innovation**: Focus on application logic instead of support systems
- **Cost-efficiency**: Take advantage of the commoditized solution stack

---

### Summary
- Monolithic apps are hard to scale and recover from outages
- Cloud native apps use microservices and containers to improve scalability and resilience
- The **cloud native stack** defines the architecture and roles of components
- **Standardization and commoditization** empower innovation and agility in modern cloud app development
