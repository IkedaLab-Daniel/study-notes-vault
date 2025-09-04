# Google Cloud Computing Foundations Certificate

>> Course 1: Google Cloud Computing Foundations: Cloud Computing Fundamentals

## Google Cloud Computing Foundations Course

### Course Overview

* Designed for beginners with little to no background in cloud computing.
* Covers **cloud computing, big data, and machine learning** concepts.
* Explains how Google Cloud fits into these areas.
* Consists of **10 modules**, **25 hands-on labs**, and **4 final challenge labs** (about 24 hours of experiential learning).
* Opportunity to earn **4 Google Cloud skill badges**.

### Course Modules

1. **So, what's the cloud anyway?** – Introduction to cloud concepts and business impact.
2. **Start with a solid platform** – Different ways to interact with Google Cloud.
3. **Use Google Cloud to Build your Apps** – Building apps with Google Cloud resources and serverless services.
4. **Where do I store this stuff?** – Structured and unstructured storage models.
5. **There's an API for that!** – Application-managed service options in the cloud.
6. **You can't secure the cloud, right?** – Security in Google Cloud.
7. **It helps to network** – Building secure networks in the cloud.
8. **Keeping an eye on things** – Tools for cloud automation and management.
9. **You have the data, but what are you doing with it?** – Managed big data services in the cloud.
10. **Let machines do the work** – Introduction to machine learning.

### Hands-On Labs

* Hosted on **Google Cloud Skills Boost** (real environments, not simulations).
* Accessible through a standard web browser with temporary credentials provided.
* Includes instructions, live scenarios, and free credits for lab use.
* Labs must be **started and ended properly** (using Start Lab and End Lab buttons).

### Skill Badges Earned

By completing labs and challenge labs, learners can earn the following badges:

* **Implement Load Balancing on Compute Engine**
* **Set Up an App Dev Environment on Google Cloud**
* **Build a Secure Google Cloud Network**
* **Prepare Data for ML APIs on Google Cloud**

Each badge involves hands-on labs leading to a **final Challenge Lab** as a capstone.

## Module 1: So, What's the Cloud Anyway?

### Learning Objectives

By the end of this module, you will be able to:

* Identify what cloud computing is and its impact on technology and business.
* Explore the concept of **cloud computing**.
* Compare and contrast **physical, virtual, and cloud architectures**.
* Differentiate between **IaaS, PaaS, and SaaS**.
* Get introduced to **Google Cloud compute, storage, big data, and ML services**.
* Examine the **Google network** and how it powers cloud computing.

### Module Flow

1. Definition of **cloud computing**.
2. Comparison of **cloud vs. traditional architecture**.
3. Exploration of **IaaS, PaaS, and SaaS** models.
4. Overview of **Google Cloud architecture**.
5. **Quiz and recap** of the topics covered.

## Introduction to Cloud Computing

### Definition

Cloud computing, as defined by the **US National Institute of Standards and Technology (NIST)**, is a model of using IT resources that has **five key traits**:

1. **On-demand and self-service** – Users can provision computing resources (processing, storage, network) through a web interface without human intervention.
2. **Accessible over the internet** – Resources can be accessed from anywhere with a connection.
3. **Resource pooling** – Providers maintain a large pool of resources, allocate them to users as needed, and achieve cost efficiency through bulk purchasing.
4. **Elasticity** – Resources can scale up or down quickly depending on demand.
5. **Pay-as-you-go** – Customers only pay for what they use or reserve; charges stop when usage stops.

### Infrastructure Analogy

* **Infrastructure** = underlying framework of facilities and systems.
* Example: A **city's infrastructure** includes transportation, power, water, and communication.
* In IT, infrastructure includes the services and systems that support applications and users.

### Google Cloud Focus

* The course will cover **Google Cloud infrastructure services**.
* Learners will gain familiarity with what these services do and how to begin using them.

## Cloud Architecture and Evolution

### From Traditional to Cloud

* **First Wave: Colocation**

  * Users rented **physical space** in data centers instead of owning infrastructure.
  * Provided financial efficiency but still relied on physical servers.

* **Second Wave: Virtualization**

  * Data centers used **virtual devices** (servers, CPUs, disks, load balancers, etc.).
  * Allowed flexibility but enterprises still had to **maintain and configure infrastructure**.

* **Third Wave: Container-Based Cloud (Google’s Model)**

  * Fully **automated, elastic cloud** architecture.
  * Infrastructure provisioning and configuration handled automatically.
  * Enables scalable data and services for faster application deployment.
  * Currently available to Google Cloud customers.

### Google’s Vision

* Future businesses will differentiate through **technology and software**.
* **High-quality data** is central to great software.
* Every company is becoming a **data company**.

### Energy and Sustainability

* Data centers use about **2% of the world’s electricity**.
* Google focuses on **efficiency and sustainability**:

  * First data centers to achieve **ISO 14001 certification** (resource efficiency, waste reduction).
  * Example: **Hamina, Finland Data Center**

    * Uses seawater cooling from the Bay of Finland.
    * First system of its kind globally, reducing energy use.
* Google’s sustainability milestones:

  * **Carbon neutral** in its first decade.
  * **100% renewable energy** in its second decade.
  * Goal: **Carbon-free operations by 2030**.

## IaaS, PaaS, SaaS, and Serverless

### Infrastructure as a Service (IaaS)

* Provides **raw compute, storage, and networking** resources.
* Organized virtually, similar to a physical data center.
* **Customers pay** for resources they **allocate ahead of time**.

### Platform as a Service (PaaS)

* Provides **libraries and infrastructure bindings** for applications.
* Developers focus more on **application logic** instead of infrastructure.
* **Customers pay** only for the **resources actually used**.

### Shift Toward Managed Services

* Cloud computing has moved toward **managed infrastructure and services**.
* Benefits:

  * Less time and money spent on infrastructure maintenance.
  * Faster and more reliable delivery of products and services.

### Serverless Computing

* Removes need for server configuration and infrastructure management.
* Developers focus **only on code**.
* Google’s serverless technologies:

  * **Cloud Run** – Deploys containerized microservices in a fully managed environment.
  * **Cloud Functions** – Manages event-driven code with **pay-as-you-go** pricing.

### Software as a Service (SaaS)

* Applications run in the **cloud**, not installed locally.
* Consumed directly over the internet by end users.
* Examples: **Gmail, Google Docs, Google Drive** (Google Workspace).

## Google Cloud Offerings and Infrastructure

### Three Layers of Google Cloud

1. **Networking and Security** – Foundation for all Google infrastructure and applications.
2. **Compute and Storage** – Decoupled so they can **scale independently**.
3. **Big Data and Machine Learning** – Tools for ingesting, storing, processing, and delivering insights and ML models without managing infrastructure.

### Compute Services

* **Compute Engine** – Virtual machines.
* **Google Kubernetes Engine (GKE)** – Managed Kubernetes.
* **App Engine** – Fully managed application hosting.
* **Cloud Run** – Serverless container deployment.
* **Cloud Functions** – Event-driven, serverless code execution.

### Storage Services

* **Cloud Storage** – Object storage.
* **Cloud SQL** – Managed relational database.
* **Spanner** – Global relational database with strong consistency.
* **Bigtable** – NoSQL database for large-scale workloads.
* **Firestore** – NoSQL document database.

### Big Data & Machine Learning Products

* **Cloud Storage, Dataproc, Bigtable, BigQuery, Dataflow, Firestore, Pub/Sub, Looker, Spanner**
* **AutoML** – Custom ML model training.
* **Vertex AI** – Unified ML platform for building and deploying models.

### Google’s Global Network

* **Largest of its kind**, with **billions invested**.
* Over **100 content caching nodes worldwide** for low latency and high throughput.
* Data centers in **North America, South America, Europe, Asia, and Australia**.

### Regions and Zones

* **Regions** = independent geographic areas (e.g., *europe-west2* = London).
* **Zones** = areas within regions where resources run.

  * Example: A Compute Engine VM runs in a specified zone.
* **Zonal resources** – Operate in a single zone (downtime if zone unavailable).
* **Regional/multi-regional resources** – Increase redundancy and availability.

  * Example: **Spanner multi-region** replicates across multiple regions for low-latency global access.

### Scale and Availability

* Currently: **121 zones in 40 regions** (expanding).
* Latest information: [cloud.google.com/about/locations](https://cloud.google.com/about/locations).

## Module 2: Start with a Solid Platform

### Learning Objectives

By the end of this module, you will be able to:

* Explore the **Google Cloud Console**.
* Understand how **projects** are the basis for enabling and using services.
* Identify how **billing** works in Google Cloud.
* Install and configure the **Google Cloud SDK**.
* Recognize use cases for **Cloud Shell** and the **Cloud Shell code editor**.
* Explore how **APIs** work in Google Cloud.
* Manage Google Cloud services using the **Cloud Mobile App**.

### Module Flow

1. Introduction to the **Google Cloud Console**.
2. Understanding **projects**.
3. Overview of **billing options**.
4. Installing and configuring the **Cloud SDK**.
5. Using **Cloud Shell** and the **Cloud Shell code editor**.
6. Completing **two hands-on labs**.
7. Exploring **Google Cloud APIs**.
8. Managing services with the **Cloud Mobile App**.
9. **Quiz and summary** of the topics covered.

### Four Ways to Access Google Cloud

1. **Google Cloud Console (GUI)** – Web-based interface to manage and monitor resources.
2. **Google Cloud SDK & Cloud Shell** – Command-line tools for managing resources.
3. **Google Cloud APIs** – Programmatic access for developers.
4. **Google Cloud Mobile App** – Manage resources on the go.

---

### Google Cloud Console (focus)

* It’s the **Graphical User Interface (GUI)** for Google Cloud.
* Lets you **deploy, scale, and troubleshoot** production workloads.
* Provides features like:

  * Resource search & health checks.
  * Full management control over resources.
  * Budget setup & spend control.
  * **In-browser SSH** access to instances.

👉 To access: go to **[console.cloud.google.com](https://console.cloud.google.com/)**

## Google Cloud Resource Hierarchy

### Levels of the Hierarchy

1. **Resources**

   * Examples: Virtual Machines, Cloud Storage buckets, BigQuery tables, etc.
   * Represent the fundamental components in Google Cloud.

2. **Projects**

   * Basis for enabling and using Google Cloud services.
   * Used for managing APIs, billing, collaborators, and other services.
   * Each resource belongs to exactly one project.
   * Projects are billed and managed separately.

   **Project Identifiers**

   * **Project ID**: Globally unique, assigned by Google, immutable.
   * **Project Name**: User-created, not unique, changeable.
   * **Project Number**: Unique numeric ID, assigned by Google, used internally.

   **Project Management**

   * Managed with the **Resource Manager API**.
   * Functions include listing, creating, updating, deleting, and recovering projects.
   * Accessible through RPC and REST APIs.

3. **Folders**

   * Used to group projects under an organization.
   * Enable grouping by departments or teams.
   * Allow delegation of administrative rights for independent team management.
   * Require an organization node.

4. **Organization Node**

   * Top-level of the hierarchy.
   * Encompasses all folders, projects, and resources within the organization.

## Google Cloud Billing

### Project-Level Billing

* Billing is established at the **project level**.
* Each project is linked to a **billing account** where payment options and billing information are configured.
* Projects without a billing account can only access **free services**.
* Billing accounts are charged automatically and invoiced monthly or at threshold limits.
* **Sub accounts** can separate billing by project, often used by resellers for their clients.

### Cost Management Tools

1. **Budgets**

   * Defined at billing account or project level.
   * Can be a fixed limit or tied to metrics (e.g., % of previous month’s spend).

2. **Alerts**

   * Notify users when expenses approach budget limits.
   * Common thresholds: **50%, 90%, 100%** (customizable).
   * Example: \$20,000 budget with a 90% alert → notification at \$18,000.

3. **Reports**

   * Visual tool in the console.
   * Monitors expenditure by project or service.

4. **Quotas**

   * Prevent over-consumption due to errors or malicious attacks.
   * Applied at the project level.
   * **Types of Quotas**:

     * **Rate Quotas**: Reset after a specific time (e.g., GKE → 1,000 API calls every 100 seconds).
     * **Allocation Quotas**: Limit on number of resources (e.g., 5 VPC networks per project by default).
   * Some quotas can be increased via Google Cloud Support.

### Cost Estimation

* Use the **Google Cloud Pricing Calculator**: [cloud.google.com/products/calculator](https://cloud.google.com/products/calculator).

### 🌩️ What is Google Cloud SDK?

* A **set of command-line tools** for managing resources and applications on Google Cloud, directly from your desktop.
* Useful for developers and admins who want to interact with Google Cloud without always using the web console.

---

### 📦 Main Tools Included:

1. **`gcloud` CLI**

   * The primary tool for most Google Cloud products and services.
   * Example: deploying apps, managing Compute Engine instances, configuring APIs.

2. **`gcloud storage`**

   * Lets you interact with **Cloud Storage** (upload, download, list, manage buckets).

3. **`bq` (BigQuery CLI)**

   * Used to run queries, manage datasets, and interact with **BigQuery** from the command line.

---

### 📂 Installation

1. Go to [cloud.google.com/sdk](https://cloud.google.com/sdk).
2. Select your **operating system** (Windows, macOS, Linux).
3. Download and install following the OS-specific instructions.
4. All tools get installed inside the **`bin` directory**.

---

### ⚙️ Initial Configuration

* After installing, run:

  ```bash
  gcloud init
  ```
* You’ll be prompted to:

  * **Login** with your Google Cloud credentials.
  * Set your **default project**.
  * Choose a **default region and zone** for resources.

---

👉 Once configured, you can immediately start using commands like:

```bash
gcloud compute instances list
gcloud storage buckets list
bq query "SELECT name FROM dataset.table LIMIT 10"
```

## Cloud Shell

* **Definition**: Cloud Shell provides command-line access to Google Cloud resources directly from a browser.
* **Environment**:

  * Debian-based virtual machine.
  * Comes with a **persistent 5 GB home directory**.
  * Preinstalled with **Google Cloud SDK (`gcloud`)** and other utilities.
  * Always **up to date** and **fully authenticated**.

### Accessing Cloud Shell

* Go to **[console.cloud.google.com](https://console.cloud.google.com)**.
* Click the **Activate Cloud Shell** icon in the toolbar.
* A terminal window opens at the bottom of the console.

### Cloud Shell Code Editor

* Can be launched from the terminal window.
* Opens in a **new browser page**.
* Allows real-time file editing inside the Cloud Shell environment.
* Useful for **code-first applications** and **container-based workloads**.
* Supports both the built-in code editor and traditional text editors from the command prompt.

## Application Programming Interfaces (APIs)

* **Definition**: APIs provide a clean, well-defined interface that abstracts away implementation details, making software easier to develop and maintain.
* **Purpose**:

  * Allows developers to interact with services without needing to know their internal workings.
  * Underlying implementations can change as long as the API remains consistent.

### APIs in Google Cloud

* All Google Cloud services expose APIs for programmatic control.
* The **Google APIs Explorer** (in the console) lists available APIs and their versions.

### Developer Support

* Developers don’t need to code from scratch when using Google Cloud APIs.
* Google provides **Cloud Client Libraries** and **Google API Client Libraries** to simplify API usage.
* Supported programming languages:

  * **Java**
  * **Python**
  * **PHP**
  * **C#**
  * **Go**
  * **Node.js**
  * **Ruby**
  * **C++**

## Cloud Mobile App

* **Definition**: A mobile application to manage Google Cloud services directly from a mobile device, provided at no extra cost.

### Capabilities

* **Compute Engine**:

  * Start and stop instances.
  * Connect via **SSH**.
  * View logs.

* **Cloud SQL**:

  * Start and stop instances.

* **App Engine**:

  * View errors.
  * Roll back deployments.
  * Change traffic splitting.

* **Billing**:

  * View up-to-date billing information.
  * Receive billing alerts for projects exceeding budget.

* **Monitoring & Alerts**:

  * Customizable graphs (CPU usage, network usage, requests per second, server errors).
  * Alerts and incident management.

### Access

* Download at: **[cloud.google.com/console-app](https://cloud.google.com/console-app)**

## Module 2 Recap: Start with a Solid Platform

* **Google Cloud Console**: Explored the web-based GUI for managing resources.
* **Projects**: Learned how projects form the foundation for enabling and using Google Cloud services.
* **Billing**: Reviewed billing options, budgets, alerts, and quotas.
* **Google Cloud SDK**: Learned how to install, configure, and use command-line tools.
* **Cloud Shell & Code Editor**: Explored browser-based access and real-time code editing.
* **APIs**: Understood how APIs and client libraries enable interaction with Google Cloud services.
* **Cloud Mobile App**: Learned how to manage services, billing, and monitoring from a mobile device.

> Module 3

## Module 3: Use Google Cloud to Build Your Apps

* **Compute Options**: Explore the role of compute in the cloud.
* **Virtual Machines**: Learn how to build and manage VMs.
* **Elastic Applications**: Examine autoscaling for flexible resource usage.
* **PaaS with App Engine**: Leverage App Engine for platform-based development.
* **Event-Driven Services**: Build with Cloud Run functions.
* **Containers & Orchestration**: Identify how to containerize and orchestrate apps using Google Kubernetes Engine (GKE).
* **Cloud Run**: Develop and deploy scalable containerized applications.

**Extras**: Includes five hands-on labs, followed by a quiz and a summary.

## Compute Options in the Cloud

* **Compute Engine**: Best for general workloads needing dedicated resources.
* **App Engine**: Platform as a Service (PaaS) option for building applications.
* **Cloud Run Functions**: Serverless option for event-driven code execution.
* **Google Kubernetes Engine (GKE)**: Managed Kubernetes platform for running containers.
* **Cloud Run**: Fully managed serverless platform for developing and deploying scalable containerized applications.

Each of these compute services will be explored in this module.

## Compute Engine: Building and Deploying Applications

* **Overview**:

  * Create and run VMs in Google’s data centers and on its global fiber network.
  * No upfront investment; scalable to thousands of virtual CPUs.
  * Offers consistent, fast performance.

* **Virtual Machine Capabilities**:

  * Full operating system functionality.
  * Configure CPU, memory, storage, and OS (Linux, Windows Server, or custom images).
  * Supports web hosting, app hosting, and application backends.
  * Manage instances via Google Cloud Console or gcloud CLI.

* **Pricing and Discounts**:

  * **Per-second billing** with one-minute minimum.
  * **Sustained-use discounts** apply automatically for VMs running over 25% of a month.
  * **Committed-use discounts**: up to 57% savings for 1- or 3-year commitments.
  * **Preemptible VMs**: Up to 90% savings for interruptible workloads (e.g., batch jobs).

* **Tools**:

  * Google Cloud Pricing Calculator for estimates and discount projections.


## **Elastic Applications with Autoscaling**

1. **Choosing Machine Properties**

   * Compute Engine lets you choose:

     * Number of **vCPUs**
     * Amount of **memory**
   * Options include:

     * **Predefined machine types** (ready-made configs)
     * **Custom machine types** (your own CPU/RAM combo)

2. **Autoscaling**

   * Automatically **adds or removes VM instances** depending on load metrics (like CPU utilization or traffic).
   * Helps optimize costs while ensuring performance.

3. **Load Balancing**

   * Distributes incoming traffic across VMs to keep workloads balanced.
   * Google Cloud’s **VPC** provides different load balancing options (to be covered later).

4. **Scaling Options**

   * **Scale up** → Use bigger VMs (useful for memory-heavy databases or CPU-intensive analytics).
   * **Scale out** → Use more smaller VMs (most customers start here because it’s flexible and cost-efficient).

5. **Constraints**

   * Maximum CPUs per VM depend on:

     * The **machine family**
     * The **quota** assigned to your project (which is zone-dependent).

6. **More Info**

   * Specs for available VM machine types: [Google Cloud Machine Types Docs](https://cloud.google.com/compute/docs/machine-types)
