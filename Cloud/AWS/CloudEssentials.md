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
