# Cloud Concepts

## 1.1 Explain cloud advantages to stakeholders

- Describe cloud infrastructure
- Distinguish between cloud service models, such as IaaS, PaaS, and SaaS
- Explain how cloud facilitates building applications faster and more cost-effectively than traditional models

**Key Points:**
- **Cloud Infrastructure**: Distributed computing resources (servers, storage, networking) accessed over the internet, managed by cloud providers in data centers
- **Service Models**:
  - **IaaS (Infrastructure as a Service)**: Virtual machines, storage, networks (e.g., EC2, Azure VMs)
  - **PaaS (Platform as a Service)**: Development platforms without managing infrastructure (e.g., App Service, Elastic Beanstalk)
  - **SaaS (Software as a Service)**: Ready-to-use applications (e.g., Office 365, Salesforce)
- **Advantages**: No upfront hardware costs, pay-as-you-go, global reach, automatic updates, faster time-to-market

## 1.2 Explain cost to stakeholders

- Identify the use case (new development or transition of existing product or service)
- Identify the resources that will be required to construct the service or product using cloud-hosted components (including compute, data, and network costs)
- Describe support plan that will be required to meet performance, availability, scalability, and reliability (PASR) criteria
- Consider factors that determine return on investment

**Key Points:**
- **Cost Components**: Compute (VM hours), storage (GB/month), data transfer (egress charges), support plans
- **Pricing Models**: Pay-as-you-go, reserved instances (discounts for commitments), spot/preemptible instances
- **PASR Considerations**: Higher availability/performance tiers cost more; balance business needs with budget
- **ROI Factors**: Reduced capital expenses, lower maintenance costs, faster deployment, elasticity reduces waste

## 1.3 Explain performance to stakeholders

- Identify performance criteria
- Consider which solutions meet the performance criteria
- Assess cost and availability of technical expertise
- Explain the performance benefits of edge computing

**Key Points:**
- **Performance Metrics**: Response time, throughput, latency, CPU/memory utilization
- **Solutions**: Choose appropriate VM sizes, use caching (CDN), optimize database queries, load balancing
- **Edge Computing**: Processing data closer to users/devices reduces latency, improves response time
- **Trade-offs**: Higher performance often requires more expensive resources or specialized expertise

## 1.4 Explain reliability to stakeholders

- Identify reliability criteria, including network speeds
- Consider which solutions meet the criteria
- Understand service-level agreement (SLA) of the cloud provider
- Consider disaster-recovery and backup plans (including backup redundancy or replication factor)

**Key Points:**
- **Reliability**: System's ability to function correctly and consistently over time
- **SLA**: Provider's commitment to uptime (e.g., 99.9% = ~8.76 hours downtime/year)
- **Network Considerations**: Bandwidth requirements, latency tolerance, redundant connections
- **DR/Backup**: Regular backups, replication across regions, automated failover, recovery time objectives (RTO/RPO)

## 1.5 Explain availability to stakeholders

- Identify the use case (new development or transition of existing product or service)
- Identify any upstream or downstream SLAs that will govern availability requirements
- Establish availability metrics
- Assess the SLA offered by the cloud-hosted solution

**Key Points:**
- **Availability**: Percentage of time a system is operational and accessible
- **High Availability**: Multi-zone deployments, load balancers, health checks, auto-recovery
- **Availability Zones**: Isolated data centers within a region for fault tolerance
- **Dependencies**: Your availability limited by weakest link in dependency chain

## 1.6 Explain scalability to stakeholders

- Identify the use case (new development or transition of existing product or service)
- Understand that rules can be set to adjust resources based on need

**Key Points:**
- **Vertical Scaling (Scale Up)**: Increase VM size (more CPU/RAM) - has limits, requires downtime
- **Horizontal Scaling (Scale Out)**: Add more instances - preferred for cloud, supports auto-scaling
- **Auto-scaling**: Automatically adjust resources based on metrics (CPU, traffic) - saves costs during low demand
- **Elasticity**: Ability to quickly scale up or down as demand changes

## 1.7 Recommend off-the-shelf (OTS) or custom solutions as needed

- Identify the use case (new development or transition of existing product or service)
- Evaluate if an existing OTS offering meets performance, availability, scalability, and reliability needs
- Evaluate the technical effort needed for a custom solution
- Evaluate whether a custom solution can exceed OTS solution on PASR criteria
- Off-the-shelf include Microsoft Office 365, Adobe Express
- Cloud providers for custom solutions: Microsoft Azure, AWS, Google Cloud, and IBM Cloud

**Key Points:**
- **OTS Solutions**: Pre-built SaaS applications, faster deployment, lower initial cost, less customization
- **Custom Solutions**: Built on IaaS/PaaS, full control, tailored to specific needs, requires development resources
- **Decision Factors**: Time-to-market, budget, unique requirements, existing expertise, integration needs
- **Hybrid Approach**: Use OTS for common functions, custom for competitive differentiators

# Developing Cloud Architecture

## 2.1 Choose between public, private, and hybrid cloud implementations

- Identify the security and privacy requirements for the solution (focusing on networking options that each provides)
- Consider limits imposed by tenancy in various cloud implementations

**Key Points:**
- **Public Cloud**: Shared infrastructure, cost-effective, highly scalable, less control over security
- **Private Cloud**: Dedicated infrastructure, greater control, higher costs, meets strict compliance needs
- **Hybrid Cloud**: Combination of both, sensitive data on-premise/private, other workloads in public cloud
- **Multi-tenancy**: Resources shared among customers (public), isolated resources (private/single-tenant)

## 2.2 Draw an architectural diagram (show data flows)

- Break down the proposed solution into compute, data, and networking components
- Produce logical groupings for the components
- Mark data flows between components (including the protocol)
- Identify system and component boundaries (including responsibility model)

**Key Points:**
- **Components**: VMs/containers (compute), databases/storage (data), VPCs/subnets/load balancers (network)
- **Logical Grouping**: Frontend tier, backend/API tier, database tier, external services
- **Data Flows**: Show direction, protocols (HTTPS, TCP, etc.), indicate synchronous vs asynchronous
- **Responsibility Model**: Shared responsibility - provider manages infrastructure, customer manages data/access

## 2.3 Define requirements

- Decide whether to virtualize server, network, storage, and desktop
- Explain the benefits of using serverless architecture
- Consider networking infrastructure, storage devices, memory, and end-user devices required

**Key Points:**
- **Virtualization Benefits**: Better resource utilization, isolation, easier management, faster provisioning
- **Serverless**: No server management, pay per execution, auto-scales, ideal for event-driven workloads (e.g., Lambda, Azure Functions)
- **Requirements Gathering**: CPU/RAM needs, storage capacity/type, bandwidth, latency requirements, client device support
- **Trade-offs**: Serverless has cold starts and execution time limits; VMs offer more control

## 2.4 Identify how services communicate through application programming interfaces (APIs)

- Identifying services with which the application needs to integrate
- Interact with a service using an API

**Key Points:**
- **APIs**: Interfaces for services to communicate (REST, GraphQL, gRPC)
- **REST APIs**: HTTP-based, use JSON/XML, standard methods (GET, POST, PUT, DELETE)
- **Authentication**: API keys, OAuth tokens, service accounts for secure access
- **Integration**: Cloud services expose APIs for storage, databases, AI services, monitoring, etc.

## 2.5 Create virtual machines

- Determine the operating system for the virtual machines
- Choose the appropriate size for the virtual machines
- Decide on geographic setting for the virtual machines (latency, legal requirements)
- Configure options (e.g., time limitations, scaling, backups) for the virtual machines

**Key Points:**
- **OS Selection**: Linux (cost-effective, open-source) vs Windows (compatibility, licensing costs)
- **VM Sizing**: Balance CPU, RAM, storage based on workload; start small and scale up
- **Region/Zone**: Choose closer to users for lower latency; consider data residency laws
- **Configuration**: Set auto-shutdown schedules, enable backups/snapshots, configure monitoring and alerts

## 2.6 Identify data storage requirements

- Distinguish between structured and unstructured data
- Determine amount of storage needed
- Consider location of storage
- Consider storage security

**Key Points:**
- **Structured Data**: Tables with schema (SQL databases like RDS, Azure SQL) - transactions, relationships
- **Unstructured Data**: Files, images, videos (object storage like S3, Blob Storage) - scalable, cheaper
- **Storage Types**: Block (VM disks), file (shared file systems), object (web/mobile apps), database
- **Security**: Encryption at rest and in transit, access controls, private endpoints, regular backups

# Implementing the Cloud Development Life Cycle

## 3.1 Create content in virtual environments

- Understand that a source-code management system needs to be set up
- Install and configure the prerequisite packages in the virtual environment
- Save changes and keep track of the codes in a source code management system (such as Github)

**Key Points:**
- **Source Control**: Git-based systems (GitHub, GitLab, Azure Repos) - track changes, collaboration, versioning
- **Virtual Environments**: Isolated development spaces, install dependencies without conflicts
- **Best Practices**: Commit frequently with descriptive messages, use branches for features, code reviews via pull requests
- **Configuration**: Use requirements.txt (Python), package.json (Node.js) to document dependencies

## 3.2 Perform testing

- Provide different test cases, test scenarios, and test scripts
- Run the tests and report the bugs iteratively

**Key Points:**
- **Test Types**: Unit (individual functions), integration (component interaction), end-to-end (user workflows)
- **Test Automation**: Scripts run automatically in CI/CD pipeline, faster feedback
- **Test Environments**: Separate dev, test, staging environments that mirror production
- **Bug Tracking**: Document issues, prioritize, assign, verify fixes - use tools like Jira, Azure Boards

## 3.3 Structure the overall cloud-based solution

- Integrate systems and applications within the selected environment
- Integrate systems and applications with legacy systems
- Integrate systems and applications with third-party applications
- Distinguish between containers and virtual machines
- Know when to choose containers (Docker) instead of virtual machines (Hyper-V)
- Choose when to use microservices

**Key Points:**
- **Containers vs VMs**: Containers share OS kernel (lighter, faster startup), VMs have full OS (more isolation)
- **When to Use Containers**: Microservices, portable apps, consistent environments, rapid scaling
- **When to Use VMs**: Different OS requirements, legacy apps, stronger isolation needed
- **Microservices**: Break app into small, independent services - easier to scale, deploy, and maintain
- **Integration**: APIs, message queues, ETL tools to connect systems; consider data consistency

## 3.4 Deploy application

- Decide on the strategy to deploy a new application, replacing a previous one
- Understand version control
- Identify cloud-hosted solutions to create code and data pipelines (e.g., cloud-native CI/CD offerings and workflow automation like GitHub Actions)
- Identify existing CI/CD practices

**Key Points:**
- **Deployment Strategies**: Blue-green (two environments, switch traffic), canary (gradual rollout), rolling updates
- **Version Control**: Tag releases, semantic versioning (major.minor.patch), rollback capability
- **CI/CD Tools**: GitHub Actions, Azure DevOps, AWS CodePipeline, Jenkins - automate build, test, deploy
- **Pipeline Stages**: Source → Build → Test → Deploy; automated triggers on code commits

# Deploy the Application

## 4.1 Manage operational costs

- Understand usage-based pricing
- Scale up and scale down to meet demand cost-effectively

**Key Points:**
- **Usage-Based Pricing**: Pay only for what you use (compute hours, storage GB, API calls)
- **Cost Optimization**: Right-size resources, use auto-scaling, delete unused resources, reserved instances for predictable workloads
- **Monitoring Costs**: Use cost management tools, set budgets and alerts, track spending by resource/team
- **Elasticity**: Scale down during off-peak hours to reduce costs while maintaining performance during peak times

## 4.2 Develop business continuity and disaster recovery policy

- Identify potential risks and disaster scenarios
- Establish on-premise vs offsite backup strategy

**Key Points:**
- **Disaster Scenarios**: Data center outage, data corruption, cyberattack, natural disasters
- **RTO/RPO**: Recovery Time Objective (max downtime), Recovery Point Objective (max data loss)
- **Backup Strategy**: Automated regular backups, store in different region, test restore procedures
- **DR Approaches**: Backup/restore (cheapest), pilot light (minimal running), warm standby, hot site (most expensive)

## 4.3 Provide support to users

- Identify protection and security policies for external and internal users
- Provide application and hardware support for internal users
- Provide training tools for internal and external users

**Key Points:**
- **Support Tiers**: Self-service (documentation, FAQs), help desk, escalation to technical teams
- **Security Policies**: Strong passwords, MFA, acceptable use policies, incident reporting procedures
- **Training**: Onboarding materials, user guides, video tutorials, sandbox environments for practice
- **Feedback Loop**: Collect user feedback, track support tickets, identify common issues for improvement

## 4.4 Monitor cloud systems

- Log events
- Monitor hardware and software (e.g., interpret graphs and dashboards)
- Understand notifications or alerts for provisioning backup

**Key Points:**
- **Logging**: Capture system events, errors, access logs - use centralized logging (CloudWatch, Azure Monitor)
- **Metrics**: CPU, memory, disk, network utilization, application response times, error rates
- **Dashboards**: Visual representations of key metrics, real-time monitoring, historical trends
- **Alerts**: Set thresholds, notify teams via email/SMS/Slack when issues detected, automated responses

# Understanding Cloud Governance

## 5.1 Comply with privacy and regulatory requirements

- Identify relevant privacy requirements based on geographical and domain constraints (e.g. BIPA, HIPAA, PDP, FERPA, COPPA, GDPR, CCPA, etc.) as well as organization-specific policies
- Identify cloud-provider compliance for these privacy regulations
- Assess types of data managed within the environment
- Assess location and storage of data
- Be aware of NIST and ISO frameworks and standards

**Key Points:**
- **Key Regulations**: GDPR (EU data protection), HIPAA (US healthcare), CCPA (California privacy), FERPA (education records)
- **Data Classification**: Public, internal, confidential, restricted - different protection levels
- **Data Residency**: Some regulations require data stored in specific countries/regions
- **Compliance Certifications**: Verify cloud provider has relevant certifications (SOC 2, ISO 27001, HIPAA compliance)
- **Frameworks**: NIST Cybersecurity Framework, ISO standards provide best practice guidelines

## 5.2 Comply with ethical guidelines

- Consider the impact of bias, lack of transparency, and lack of accountability
- Explain potential bias and transparency challenges with prebuilt services

**Key Points:**
- **Bias in AI/ML**: Training data may contain historical biases affecting decisions (hiring, lending, etc.)
- **Transparency**: Users should understand how automated decisions are made, "black box" problem
- **Accountability**: Clear ownership when systems make errors or cause harm
- **Prebuilt Services**: Facial recognition, sentiment analysis may have biases; test with diverse data sets
- **Ethical Principles**: Fairness, privacy, safety, inclusivity should guide development

## 5.3 Managing cloud security

- Understand options and concepts for identity verification and authentication, including digital identity and multifactor authentication
- Understand access policies and authorizations (e.g., options for access; vendor-provided roles vs. custom roles and permissions; and access hygiene, including least privilege access, removal of access when not needed and disabling accounts)
- Understand the importance of data security and encryption
- Understand options to protect against unauthorized access in cloud environments (including intrusion detection and prevention, firewalls)

**Key Points:**
- **Authentication**: MFA (something you know + have + are), SSO (single sign-on), federated identity
- **Authorization**: Role-Based Access Control (RBAC), least privilege principle - give minimum required permissions
- **Encryption**: At rest (stored data) and in transit (data moving over network), use TLS/SSL, manage encryption keys
- **Network Security**: Firewalls, security groups, private subnets, VPNs for secure connections
- **Monitoring**: Intrusion detection/prevention systems (IDS/IPS), log analysis, security audits
- **Access Hygiene**: Regular access reviews, disable inactive accounts, rotate credentials, remove departing employees