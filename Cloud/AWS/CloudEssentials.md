# AWS Cloud Essentials Course:

> Module 1: Introduction to Cloud

## AWS Cloud Essentials – Lesson 1 Summary

* **Introductions**

  * *Morgan Willis*: Principal Cloud Technologist, AWS Training & Certification. Background in IT support and teaching; passionate about helping learners grow in cloud.
  * *Rudy Chetty*: Chief Techfluencer & Principal Solutions Architect, AWS Partners. 20+ years in tech, originally from South Africa; passionate about education.
  * *Alan Meridian*: Instructor, AWS Training & Certification. 8+ years at AWS, delivered hundreds of trainings, emphasizes simple explanations.

* **Course Goals**

  * Explain AWS Cloud fundamentals with analogies, examples, and demos.
  * Keep concepts simple and practical.
  * Show real-world AWS service use cases.

* **AWS Overview**

  * AWS is the world’s most comprehensive and widely adopted cloud platform.
  * Offers services in compute, databases, storage, AI, content delivery, and more.
  * Millions of customers use AWS for agility, cost savings, and faster innovation.

* **Client-Server Model (Coffee Shop Analogy)**

  * *Client*: Customer making a request (Alan).
  * *Server*: Barista fulfilling the request (Morgan).
  * Request → validation → response (e.g., order coffee = get coffee).
  * Represents how cloud servers handle requests and deliver results.

* **Complexity of Applications**

  * Real business solutions often involve multiple servers and components.
  * The course will build from basic to more complex cloud concepts.

* **AWS Key Concept: Pay Only for What You Use**

  * Compared to staffing a coffee shop: employees (resources) are only paid for hours worked.
  * On-premises data centers = over-provisioning, wasted costs.
  * AWS = provision resources on demand, scale up/down instantly.
  * Stop paying immediately once resources are deprovisioned.

* **Takeaway**

  * First AWS concept learned: **pay-as-you-go model**.
  * AWS enables flexible, cost-efficient, and scalable IT operations.
  * This foundation will support deeper exploration of cloud concepts throughout the course.

## AWS Cloud Essentials – History and Definition of Cloud Computing

* **Origins of AWS**

  * Early 2000s: Amazon.com needed more servers, storage, and compute to support ecommerce growth.
  * Amazon developed standardized tools for efficiency and scalability.
  * 2003: Idea emerged to share this model with other companies.
  * 2004: First service launched – **Amazon Simple Queue Service (SQS)**.
  * 2006: Added **Amazon Simple Storage Service (S3)** for storage and **Amazon Elastic Compute Cloud (EC2)** for compute.
  * Initially popular with startups and developers; soon attracted enterprises due to scalability and cost-effectiveness.
  * Expanded services rapidly into databases, networking, analytics, and more.
  * Today: AWS powers a large portion of the internet, serving startups, enterprises, and governments globally.

* **Definition of Cloud Computing**

  * *On-demand delivery of IT resources over the internet with pay-as-you-go pricing*.
  * **On-demand**: Use resources only when needed (e.g., store data in S3, delete when no longer required).
  * **Delivery over the internet**: Access resources remotely from anywhere with an internet connection.
  * **Pay-as-you-go pricing**: Stop paying immediately when resources are deprovisioned. No contracts or upfront costs.

* **Data Centers and AWS Advantage**

  * Data centers house servers with redundant power, cooling, and security for reliability.
  * Historically, businesses had to run their own data centers or co-locate with others.
  * AWS enabled businesses to run apps in AWS-managed data centers instead of owning infrastructure.
  * Freed teams from repetitive infrastructure tasks, allowing them to focus on innovation.

* **Key Takeaway**

  * Cloud computing simplifies IT by eliminating infrastructure management, providing flexibility, scalability, and cost savings.
  * AWS transformed from solving Amazon’s IT needs to becoming the global leader in cloud computing.

## Six Benefits of AWS Cloud

1. **Pay as you go** – Replace large upfront costs with variable expenses. You only pay for what you use, with built-in billing and budgeting tools to help save money.

2. **Economies of scale** – AWS buys hardware in massive quantities at lower prices and passes those savings to customers.

3. **Stop guessing capacity** – No need to over- or under-provision hardware. AWS lets you scale resources up or down in minutes to meet real demand.

4. **Increase speed and agility** – Quickly create test environments, experiment, and innovate without long setup times or wasted costs.

5. **Eliminate data center maintenance** – AWS manages the servers and infrastructure, letting you focus on customers instead of upkeep.

6. **Go global in minutes** – Easily expand to new regions worldwide by deploying to AWS-managed data centers, reducing setup from months/years to minutes.

## AWS Global Infrastructure and High Availability

* **High availability** ensures applications remain accessible with minimal downtime. If one component fails, another takes over.
* **Fault tolerance** goes further by allowing systems to keep running even if multiple components fail.

### AWS Setup

* **Regions**: Geographically separated areas (e.g., Paris, Tokyo, São Paulo, Dublin, Ohio) designed to be close to customers.
* **Availability Zones (AZs)**: Each Region contains 3+ AZs for redundancy. AZs are located apart from each other to avoid single points of failure (e.g., natural disasters).
* **Data centers in AZs**: Each has redundant power, networking, and connectivity for resilience.

### Why It Matters

* Running in one giant data center is risky—if it fails, everything goes down.
* By spreading infrastructure across multiple AZs and Regions, AWS provides high availability and fault tolerance.
* Businesses often use multiple Regions to ensure disaster recovery and uninterrupted operations.

## AWS Shared Responsibility Model

* **Both AWS and the customer share responsibility for security.**

* **AWS** is responsible for **security of the cloud**:

  * Physical infrastructure (data centers, hardware, access controls).
  * Network layer security.
  * Hypervisor/virtualization layer.

* **Customer** is responsible for **security in the cloud**:

  * Operating system (patching, user accounts, access).
  * Applications (configuration, updates, vulnerabilities).
  * Data (access controls, encryption, visibility settings).

### Key Idea

* AWS provides the foundation and tools (like secure locks).
* Customers must properly configure and use them (like locking the door).
* Responsibilities may shift depending on the AWS service used, but the principle remains:

  * **AWS secures the infrastructure.**
  * **Customers secure what they build and run on it.**

## Scenario: E-commerce company expanding globally with AWS

**1. AWS Global Infrastructure Benefits**

* **Latency reduction:** Hosting applications closer to customers (e.g., Ireland Region for Europe, Singapore Region for Asia).
* **Global reach without upfront cost:** Startups and small businesses can scale globally without building physical data centers.
* **High availability & fault tolerance:** By deploying across multiple Availability Zones (AZs), if one AZ fails, workloads failover to another.

**2. Shared Responsibility Model in Action**

* **AWS responsibility (security *of* the cloud):** Securing the data centers, networking, and underlying infrastructure.
* **Customer responsibility (security *in* the cloud):** Configuring applications securely, protecting sensitive data like credit card info, managing access, and ensuring compliance.

**3. Key Takeaway**

* AWS provides the **building blocks** (Regions, AZs, services, infrastructure).
* Businesses—whether startups or enterprises—can **combine those blocks** while staying accountable for their own security and compliance.
* Together, **Global Infrastructure + Shared Responsibility Model** enable businesses to scale quickly, stay resilient, and operate securely worldwide.

## Amazon EC2 Overview

* **Amazon EC2 (Elastic Compute Cloud):** Provides raw compute capacity in the cloud to host applications.
* **Client/Server model:** Just like the coffee shop analogy, EC2 servers process client requests and return responses.

**Key Features:**

* **Virtual Machines (VMs):** EC2 instances are VMs running on shared physical hosts (multi-tenancy).
* **Hypervisor:** Manages resource sharing and isolation between instances; AWS handles this layer.
* **On-demand & scalable:** Launch thousands of instances within minutes, stop/terminate when not needed, and pay only for running instances.
* **Flexible OS & software:** Choose Linux or Windows, and install any apps—web apps, databases, internal tools, or enterprise software.
* **Vertical scaling:** Resize instances by increasing CPU/memory as demand grows.
* **Networking control:** Configure access to servers, deciding whether instances are public or private.

**Main Benefit:**
VMs aren’t new, but AWS makes acquiring, managing, and scaling compute power **faster, easier, and more cost-effective** than running your own data center.

## EC2 Instance Types

* **Analogy:** Like different coffee machines for customer preferences, EC2 offers instance types for different workloads.
* **Instance families:** Grouped by CPU, memory, storage, and networking capacity.

**Main Families:**

* **General Purpose:** Balanced compute, memory, and networking. Good for diverse workloads (e.g., web apps, code repositories).
* **Compute Optimized:** High-performance compute tasks (gaming servers, HPC, ML, scientific modeling).
* **Memory Optimized:** Best for processing large datasets in memory.
* **Accelerated Computing:** Uses hardware accelerators (GPUs, FPGAs) for graphics, ML, or heavy math calculations.
* **Storage Optimized:** High-performance local storage for data-heavy workloads.

**Instance Sizes:**

* Each family has multiple sizes (small → large).
* Bigger instances = more power, but higher cost.
* Choose based on workload needs and budget.

**Flexibility:**

* Instance type/size isn’t permanent—easily switch as workload demands change.
* Cloud advantage: adjust quickly without long-term commitment.

## Interacting with AWS Services through APIs

* **Everything in AWS is an API call.**
  APIs (Application Programming Interfaces) define how you interact with AWS services to provision, configure, and manage resources.

* **Three main ways to call AWS APIs:**

  1. **AWS Management Console** – a browser-based interface for visual management.

     * Ideal for beginners and test environments.
     * Useful for viewing bills, monitoring, and non-technical management tasks.
     * However, manual provisioning can lead to errors and is inefficient for production.
  2. **AWS Command Line Interface (CLI)** – enables text-based interaction via commands.

     * Supports automation and scripting.
     * Example commands:

       * `aws ec2 run-instances` → creates an EC2 instance
       * `aws ec2 describe-availability-zones` → lists availability zones
     * Can be used through **AWS CloudShell**, a managed cloud-based terminal with CLI preinstalled.
  3. **AWS Software Development Kit (SDK)** – allows programmatic interaction through code.

     * Supports multiple languages (e.g., Python, JavaScript, Java).
     * Example: a Python script using the SDK (Boto3) to list EC2 instances in a region.

* **Key Insight:**
  Whether you use the **Console**, **CLI**, or **SDK**, all interactions with AWS are API calls happening behind the scenes.

* **Automation Benefit:**
  Using CLI or SDK enables automation, consistency, and reduces human error—critical for scalable and predictable cloud deployments.

## Launching an EC2 Instance Using the AWS Management Console

* **Access the EC2 Console:**
  Navigate to the EC2 service in the AWS Management Console and select **“Launch instance.”**

* **1. Name the Instance:**
  Assign a name to identify your instance later.

* **2. Choose an Amazon Machine Image (AMI):**

  * AMI = a template that includes the OS and preinstalled software.
  * Select **Amazon Linux AMI** for a general-purpose web server.

* **3. Select an Instance Type:**

  * Defines CPU and memory resources.
  * Choose **t2.micro** (1 vCPU, 1 GB RAM) — eligible for the Free Tier.

* **4. Configure the Key Pair:**

  * Used for secure SSH login.
  * The **public key** is injected into the instance; you keep the **private key.**

* **5. Set Network Settings:**

  * Allow **HTTP traffic from the internet** to make it accessible as a web server.

* **6. Configure Storage:**

  * Allocate **8 GB** of storage using **gp3 EBS volume** (Elastic Block Store).

* **7. Add User Data (Optional Startup Script):**

  * Under **Advanced Details → User Data**, paste a script that installs and activates **Nginx**, turning the instance into a functioning web server.

* **8. Launch the Instance:**

  * Click **Launch instance** to start it.
  * Once running, view its details and copy the **public IP address**.

* **9. Verify the Web Server:**

  * Paste the public IP into a browser — you’ll see your **Nginx welcome page**, confirming the server is live.

* **Result:**
  You’ve successfully deployed an **EC2 instance running a basic web server**, ready for future configuration and scaling.

## Amazon EC2 Pricing Options

* **1. On-Demand Instances:**

  * Pay only for the time your instance runs (per second or per hour).
  * No upfront payment or long-term commitment.
  * Ideal for new users, testing, and unpredictable workloads.

* **2. Savings Plans:**

  * Commit to consistent usage (in $/hour) for **1 or 3 years**.
  * Save up to **72%** on costs.
  * Applies across **instance families, sizes, OS, Regions**, and even to **AWS Fargate** and **Lambda**.

* **3. Reserved Instances (RIs):**

  * Best for **steady or predictable workloads**.
  * Up to **75% discount** compared to On-Demand.
  * Commit for **1 or 3 years** with payment options:

    * **All Upfront** – full payment at commitment
    * **Partial Upfront** – pay part now, rest over time
    * **No Upfront** – pay as you go

* **4. Spot Instances:**

  * Use **spare EC2 capacity** for up to **90% off** On-Demand price.
  * Can be **terminated anytime** by AWS (with a 2-minute warning).
  * Great for **flexible or fault-tolerant** workloads.

* **5. Dedicated Hosts:**

  * Reserve **entire physical servers** for exclusive use.
  * Provides full control over placement and resources.
  * Ideal for **compliance**, **security**, or **license-restricted** workloads (e.g., Windows, SQL Server).

**Summary:**
EC2 offers flexible pricing models to suit different needs — from temporary testing to long-term, high-security operations — helping balance **cost, flexibility, and workload requirements**.

## Scalability and Elasticity in AWS

* **AWS EC2 instances** can handle various workloads, such as hosting web apps, processing data, or serving customer requests.
* **Scalability and elasticity** allow systems to automatically grow or shrink capacity based on demand.
* Businesses often face **cyclical or unpredictable traffic**, making it costly to always plan for peak usage.
* With AWS, you can **provision resources dynamically** to meet real-time demand—keeping customers satisfied and costs efficient.
* **High availability** is achieved by creating redundant EC2 instances across **multiple Availability Zones (AZs)** to eliminate single points of failure.
* When demand increases, **additional instances** can be automatically launched to handle the load; when demand decreases, unnecessary instances are terminated.

This approach ensures **continuous service**, **cost efficiency**, and **automatic scaling** aligned with business needs.

## Scaling in AWS: Scale Out vs Scale Up

* **Scaling out (horizontal scaling):** Adds more instances to handle more tasks in parallel.
* **Scaling up (vertical scaling):** Upgrades existing instances with more CPU, RAM, or power.

In the **coffee shop analogy**, scaling out means adding more workers to serve customers faster, while scaling up means giving one worker more power—but it doesn’t always help.

* Different parts of the system can be scaled **independently** based on workload (e.g., more order-takers vs. drink-makers).
* When demand decreases, **idle instances are terminated** to save costs.

This is managed by **Amazon EC2 Auto Scaling**, which automatically adds or removes instances based on demand and performance metrics.

* **Amazon CloudWatch** collects these metrics (like CPU usage or latency).
* Scaling decisions happen **automatically and in real time**, ensuring optimal performance and cost efficiency.

## Elastic Load Balancing (ELB) in AWS

* **Problem:** Uneven traffic distribution across EC2 instances can cause overload on some while others stay idle.
* **Solution:** Use a **load balancer** to evenly route incoming requests among available instances.

**Elastic Load Balancing (ELB)** automatically distributes network traffic across multiple EC2 instances to improve **scalability, availability, and performance**.

* AWS manages patching, failover, and maintenance.
* ELB automatically **scales up or down** with demand at no extra hourly cost.
* It can handle both **internal and external** traffic.

**Example (Coffee Shop Analogy):**

* The **host** directs customers to the shortest cashier line—just like ELB directs traffic to the least busy instance.
* In a multi-tier web app, ELB provides a **single endpoint** for front-end instances to reach back-end instances.
* When new back-end instances launch, they register with the ELB and immediately start receiving requests—no need for manual configuration.

This setup **decouples tiers** and allows each layer to scale independently and efficiently.

## Messaging and Queuing with Amazon SQS and SNS

* In a tightly coupled system, components depend on each other—if one fails, the other is affected.
* Introducing a **buffer (queue)** between components creates a **loosely coupled architecture**, improving reliability and scalability.

**Amazon Simple Queue Service (SQS):**

* Provides reliable message queuing between software components.
* Messages (payloads) are stored in a queue until the receiver is ready to process them.
* Ensures no data loss even if one component is temporarily unavailable.
* Scales automatically and is easy to configure.
* Analogy: The *coffee order board* where cashiers post orders for baristas to pick up later.

**Amazon Simple Notification Service (SNS):**

* Used for **real-time, push-based messaging**.
* Sends messages instantly to subscribers (services or end users).
* Supports multiple delivery methods like **SMS, email, and mobile push notifications**.
* Analogy: The *barista calling out* an order when it’s ready.

Together, **SQS** and **SNS** enable **loose coupling, scalability, and fault tolerance** in AWS architectures.

## Managed vs Unmanaged Services and the Shift to Serverless

* **Amazon EC2** provides virtual machines for diverse workloads, offering high control but requiring management tasks like patching, scaling, and OS maintenance.
* EC2 is an **unmanaged service**, meaning AWS manages the infrastructure, but you manage what runs on it — aligning with the **Shared Responsibility Model**.

**Unmanaged vs Managed Services:**

* **Unmanaged services:** Full control and customization (like a manual espresso machine). Great flexibility, but more work for setup and maintenance.
* **Managed services:** AWS handles most operations (like a coffee pod machine). You configure it once, and AWS ensures reliability and scaling. Examples include **Elastic Load Balancing (ELB)**, **Simple Notification Service (SNS)**, and **Simple Queue Service (SQS)**.

**Serverless Computing:**

* You don’t manage or even see the underlying infrastructure.
* AWS automatically handles provisioning, scaling, high availability, and maintenance.
* You focus purely on application logic and functionality.

**Key takeaway:**
AWS offers a **spectrum of compute services**—from fully managed to fully customizable. The goal is to choose the balance of control and convenience that best fits your application needs. Sometimes you’ll want to craft everything by hand (like a barista), and other times you’ll prefer quick, effortless automation (like using a pod machine).

## AWS Lambda – Serverless Compute Service

* **AWS Lambda** is a **serverless compute service** (Function as a Service) that runs your code without provisioning or managing servers.
* You create a **Lambda function**, add your code, set up a **trigger**, and AWS runs your function automatically when triggered.
* **Triggers** can include events such as file uploads, data streams, or image processing.
* AWS handles **scaling, availability, patching, and security**, allowing you to focus solely on your code.
* Lambda functions can run for a **maximum of 15 minutes** per invocation.
* Ideal for **event-driven, short-duration tasks** like website requests, data processing, or report generation.
* Supports multiple programming languages including **Java, Python, and Node.js**, with the option to build **custom runtimes**.
* Integrates seamlessly with other **AWS services**, enabling complex applications without managing infrastructure.

## SQS and Lambda Integration

* **Architecture:** An **SQS queue** triggers a **Lambda function** automatically whenever a new message is added.
* **Permissions:** The Lambda function needs proper **IAM permissions** to access and read messages from the SQS queue.
* **Setup Process:**

  * Create an **SQS queue** and add messages.
  * In the **Lambda console**, use an **SQS blueprint** to create a function.
  * Choose a **runtime** (e.g., Node.js, Java, Python, or a custom runtime).
  * Create an **execution role** (e.g., `Demo_Lambert_Role`) using the **Amazon SQS poller policy** to allow Lambda to poll messages.
  * Configure an **SQS trigger** linked to the queue.
* **Execution:** Lambda retrieves, logs, and processes messages automatically from SQS.
* **Monitoring:** Use **Amazon CloudWatch Logs** to view function metrics and logs, confirming successful message processing.
* **Result:** Messages disappear from the SQS queue immediately after being processed by the Lambda function.

## AWS Containers Overview

* **Problem:** Applications often fail outside the developer’s machine due to inconsistent environments.
* **Solution:** **Containers** package code, runtime, dependencies, and configuration into one portable unit, ensuring consistency, isolation, faster startup, and efficient resource use.
* **Challenge:** Managing containers manually is complex—requiring monitoring, scaling, updates, and networking.
* **Fix:** **Container orchestration services** automate lifecycle management, scaling, recovery, and updates.

### AWS Container Services

* **Amazon ECS (Elastic Container Service):**

  * AWS-managed container orchestration.
  * Simplified, tightly integrated with AWS.
  * Manages infrastructure and scaling based on your parameters.

* **Amazon EKS (Elastic Kubernetes Service):**

  * Runs **Kubernetes** clusters on AWS.
  * Offers flexibility and control for large-scale or hybrid setups.

### Supporting Service

* **Amazon ECR (Elastic Container Registry):**

  * Secure, managed registry to store and retrieve container images.

### Compute Options for Containers

* **Amazon EC2:** You manage the underlying virtual machines—offers full control.
* **AWS Fargate:** Serverless option where AWS manages the servers—offers convenience and no infrastructure management.

### Example Workflow

1. Upload container images to **ECR**.
2. Choose orchestration service: **ECS** or **EKS**.
3. Choose compute option: **EC2** (managed) or **Fargate** (serverless).

**Result:** AWS provides a convenient, scalable, and efficient container environment—so you can focus on building and improving your application.

## AWS Purpose-Built Compute Services

* **AWS Elastic Beanstalk:**

  * Simplifies deployment and management of applications on EC2.
  * Automatically provisions and configures infrastructure (network, instances, load balancers, scaling).
  * Allows saving and redeploying environment configurations.
  * You retain visibility and control over the underlying resources.

* **AWS Batch:**

  * Ideal for compute-intensive workloads like data processing, simulations, and large-scale calculations.
  * Automatically manages and scales infrastructure across EC2 instances.
  * Lets you focus on development and analysis instead of server management.

* **Amazon Lightsail:**

  * Simplified and cost-effective hosting for web apps and websites.
  * Handles much of the complexity of traditional hosting.
  * Great for users who want a quick, easy-to-manage solution.

* **AWS Outposts:**

  * Provides a **hybrid cloud** solution by extending AWS infrastructure to on-premises environments.
  * Offers a consistent AWS experience both locally and in the cloud.
  * Ideal for use cases requiring low latency, data residency, or hybrid integration.

**Summary:**
AWS provides purpose-built compute services for different needs—from simple app hosting and batch processing to hybrid deployments—helping you focus on your goals while AWS manages the heavy lifting.

☕ **AWS Global Infrastructure — The Coffee Shop Goes International**

Your thriving coffee shop is expanding worldwide — and that’s the perfect analogy for understanding how **AWS Global Infrastructure** works.

---

### 🌍 **1. Choosing Locations = Choosing AWS Regions**

When expanding globally, you must decide **where** to open new shops.
You consider:

* **Customer demand**
* **Local regulations**
* **Operational costs**

Similarly, when deploying applications on AWS, you choose **AWS Regions** based on:

* **Proximity to your users** (to reduce latency)
* **Compliance and data residency laws**
* **Service availability and pricing**

Each AWS Region is a **separate geographical area** with **multiple Availability Zones**, giving you high availability and fault tolerance.

---

### 🧃 **2. Coffee Carts = Edge Locations**

Your smaller coffee carts at airports and markets serve your most popular drinks quickly.
They’re compact, fast, and efficient.

That’s exactly what **AWS Edge Locations** do:

* They **cache frequently accessed content** like images and videos.
* They deliver data to users **faster**, reducing load times.
* They are part of **Amazon CloudFront (AWS’s CDN)** — ensuring users get content from the **nearest location**.

Think of it as your favorite latte being brewed right next door instead of across town.

---

### ⚙️ **3. Consistency Across All Shops = Infrastructure as Code (IaC)**

You want every cappuccino — whether made in **Stockholm** or **Seattle** — to taste the same.
You achieve that through:

* **Standardized recipes**
* **Automated, programmable coffee machines**

AWS achieves this through **Infrastructure as Code (IaC)** — specifically using **AWS CloudFormation**:

* You **define your infrastructure (servers, databases, networking)** as code.
* You can **replicate, deploy, and manage** identical environments anywhere in the world.
* Ensures **consistency, automation, and scalability** across all deployments.

---

### ☁️ **Summary**

| Coffee Shop Analogy               | AWS Equivalent               | Purpose                                 |
| --------------------------------- | ---------------------------- | --------------------------------------- |
| Choosing new shop locations       | **AWS Regions**              | Choose where your workloads run         |
| Coffee carts for popular drinks   | **Edge Locations**           | Deliver content closer to users         |
| Standardized recipes and machines | **AWS CloudFormation (IaC)** | Automate and standardize infrastructure |