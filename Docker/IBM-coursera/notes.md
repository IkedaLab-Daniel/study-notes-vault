# Containers with Docker, Kurnetes, and Openshift

## Introduction to Cloud-Native Development and Containers

* **Cloud-native** is a modern approach to developing scalable, dynamic applications that are hybrid cloud–friendly.
* **Containers** play a central role in this approach, offering a standardized method to package and run applications.

### Analogy: Containers and Shipping

* Like standardized **shipping containers**, software containers encapsulate all needed components (code, libraries, settings) so they can run consistently across environments.
* Containers allow seamless movement between environments (dev, test, prod, physical, virtual, or cloud) without compatibility issues.

### Key Features of Containers

* **Lightweight** – Small size (often MBs), quick to launch.
* **Platform-independent** – Run on cloud, on-prem, desktop, etc.
* **OS-independent** – Work across Windows, Linux, macOS.
* **Language/IDE-independent** – Support Python, Java, Node.js, etc.
* **Fast & isolated** – Improve deployment and runtime performance.
* **Secure & portable** – Self-contained and transferable.

### Traditional Environment Challenges

* No app isolation or dedicated resources.
* Poor server utilization (under/overuse).
* Expensive provisioning and maintenance.
* Limited scalability and performance during peak loads.
* Manual, error-prone deployments.
* Complex hardware-based resiliency.
* Limited automation and portability.

### Container Advantages

* Solve the challenges of traditional environments:

  * **Quick deployment**
  * **Improved CPU/memory use**
  * **Lower costs**
  * **Cross-environment portability**
  * **Support for microservices**
  * **Automated app creation and updates**

### Common Challenges with Containers

* **Security risks** if the host OS is compromised.
* **Management complexity** with large numbers of containers.
* **Legacy migration** can be difficult.
* **Right-sizing** containers for performance vs. resource use.

### Popular Container Technologies

* **Docker** – Most widely used container platform.
* **Podman** – Daemon-less, more secure alternative to Docker.
* **LXC** – Ideal for data-intensive workloads.
* **Vagrant** – Offers strong isolation; more like a VM manager.

### Summary

* Containers are a key tool in modern, cloud-native development.
* They reduce deployment time and costs, increase efficiency, and support cutting-edge architectures like microservices.
* Adoption brings major benefits but also requires overcoming security, management, and migration challenges.

## Docker Overview

Docker is an open platform (available since 2013) for developing, shipping, and running applications as containers.

### Key Characteristics

* **Written in:** Go programming language
* **Uses:** Linux kernel features, including namespaces
* **Isolation:** Separates applications from hardware, OS, and container runtime

### How It Works

* Uses **namespaces** to isolate environments into containers
* Each container has a unique set of namespaces
* Each component (process, network, mount, etc.) runs within its own namespace

### Core Benefits

* Stable deployments through consistent, isolated environments
* Faster deployments—often within seconds
* Small, reusable Docker images speed up development
* Automation reduces errors and simplifies maintenance
* Supports Agile, CI/CD, and DevOps methodologies
* Easy versioning enables faster testing, rollback, and redeployment
* Promotes collaboration and scalability
* Platform-independent—highly portable across systems

### Ecosystem and Tools

* Docker CLI
* Docker Compose
* Prometheus (for monitoring)
* Various storage and functionality plugins
* Supports orchestration tools: Docker Swarm and Kubernetes
* Encourages microservices and serverless architecture

### Limitations

Docker is **not suitable** for applications that:

* Require **high performance** or **high security**
* Use **monolithic architecture**
* Depend heavily on **rich GUI features**
* Are intended for **standard desktop or limited functions**

## Docker Container Development Process

### Steps to Create and Run a Docker Container

1. **Create a Dockerfile**

   * Contains instructions for building a container image
   * Example:

     ```Dockerfile
     FROM alpine
     CMD ["echo", "hello world"]
     ```

2. **Build the Docker Image**

   * Command:

     ```bash
     docker build -t my-app:v1 .
     ```
   * Output includes:

     * `Sending build context to Docker Daemon`
     * `Successfully built <image_id>`
     * `Successfully tagged my-app:v1`

3. **Verify Image Creation**

   * Command:

     ```bash
     docker images
     ```
   * Output includes:

     * Repository (`my-app`)
     * Tag (`v1`)
     * Image ID
     * Created date
     * Image size

4. **Run the Container**

   * Command:

     ```bash
     docker run my-app:v1
     ```
   * Output:

     ```
     hello world
     ```

5. **Check Running Containers**

   * Command:

     ```bash
     docker ps -a
     ```

### Key Docker CLI Commands

| Command         | Description                                |
| --------------- | ------------------------------------------ |
| `docker build`  | Builds an image from a Dockerfile          |
| `docker images` | Lists available images                     |
| `docker run`    | Creates and runs a container from an image |
| `docker ps -a`  | Lists all containers (running and exited)  |
| `docker push`   | Uploads an image to a Docker registry      |
| `docker pull`   | Downloads an image from a Docker registry  |

## Docker Core Concepts Summary

* **Docker Objects**:
  Includes Dockerfiles, images, containers, networks, storage volumes, plugins, and add-ons.

* **Dockerfile**:
  A text file with instructions to build an image.

  * `FROM`: Base image (e.g., OS, language like Go/Node.js)
  * `RUN`: Executes commands
  * `CMD`: Defines the default command (only the last CMD takes effect if multiple are present)

* **Docker Image**:

  * Read-only template used to create containers
  * Built from Dockerfile instructions, where each instruction adds a new layer
  * Layers can be shared across images (efficient disk and bandwidth usage)
  * On image instantiation, a **writable layer** is added on top for container changes

* **Image Naming Convention**:
  Format: `hostname/repository:tag`
  Example: `docker.io/ubuntu:18.04`

  * `docker.io`: Host (Docker Hub, optional in CLI)
  * `ubuntu`: Repository (image name)
  * `18.04`: Tag (version)

* **Docker Container**:

  * Runnable instance of an image
  * Managed via Docker CLI or API
  * Supports networking, persistent storage, and creating new images from current state
  * Isolated from other containers and host
  * Ephemeral by default (data lost unless persisted)

* **Persistence and Storage**:

  * Use **volumes** or **bind mounts** to retain data after container shutdown
  * **Plugins** (e.g., storage plugins) enable integration with external storage platforms

* **Networking**:

  * Used to isolate communication between containers
  * Each container can connect to multiple networks

## Docker Architecture Overview

### Key Components
- **Docker Client**: Interfaces via CLI or REST API to send commands.
- **Docker Host**: Runs the **Docker daemon (`dockerd`)**, which:
  - Listens for API requests
  - Builds, runs, and distributes containers
  - Manages:
    - Images
    - Containers
    - Namespaces
    - Networks
    - Storage plugins
    - Add-ons
- **Registry**: Stores and distributes container images.
  - Can be **public** (e.g., Docker Hub) or **private** (e.g., IBM Cloud Container Registry)

### Client-Server Interaction
- The client communicates with:
  - Local or remote Docker hosts
  - Docker daemons (which can also interact with other daemons)

### Image Lifecycle
1. **Build**: Use a base image or Dockerfile to create a container image.
2. **Push**: Send the image to a registry.
3. **Pull**: If an image is not found locally, the host pulls it from the registry.
4. **Run**: The daemon uses the image to create a running container.

### Summary
- Docker uses a **client-server model** with:
  - A client that sends commands
  - A daemon that executes them
  - A registry to store images
- The **containerization process** involves:
  - Building an image
  - Pushing it to a registry
  - Pulling it as needed
  - Running it as a container

## Container Orchestration Overview

### The Need for Orchestration
- One container often grows into many as applications scale globally.
- Managing and connecting hundreds or thousands of containers becomes complex and overwhelming.
- **Container orchestration** automates:
  - Deployment
  - Management
  - Scaling
  - Networking
  - Availability

### Why Orchestration Matters
- Streamlines container management in large, dynamic environments.
- Enables hands-off deployments and scaling.
- Integrates with CI/CD workflows and DevOps practices.
- Increases speed, agility, and resource efficiency.
- Supports on-premises, public, private, or multi-cloud environments.
- Meets **SOAR** (Security, Orchestration, Automation, and Response) needs.

### Key Features of Orchestration Tools
- Define container images and their registries.
- Automate provisioning and deployment.
- Secure network connections between containers.
- Ensure availability by relocating containers during outages or resource shortages.
- Scale containers and balance loads.
- Schedule and allocate resources.
- Perform rolling updates and rollbacks.
- Conduct health checks and act on failures.

### Configuration and Operation
- Uses **YAML** or **JSON** configuration files.
- Defines:
  - Resource requirements (CPU, memory)
  - File parameters (metadata, proximity)
  - Logging
  - Networking
- Automatically schedules deployment and selects appropriate hosts.
- Manages the container's entire lifecycle per configuration.

### Popular Orchestration Tools
- **Marathon** (Apache Mesos): Open-source, automates management/monitoring.
- **Nomad** (HashiCorp): Supports Docker and others across all OS/infrastructure.
- **Docker Swarm**: Built for Docker Engine; popular for Docker-centric teams.
- **Kubernetes (K8s)**:
  - Maintained by CNCF
  - Industry standard
  - Automates deployment, scaling, storage, discovery, and self-healing
  - Widely supported by major cloud providers with managed services

### Benefits of Container Orchestration
- **Productivity**: Frees dev teams from manual management.
- **Speed**: Faster feature releases and deployments.
- **Cost-efficiency**: Lower overhead vs. VMs or traditional servers.
- **Security**: Improved isolation and resource sharing.
- **Scalability**: Easily scale apps with simple commands.
- **Error recovery**: Auto-resolve infrastructure issues for high availability.

### Summary
- Container orchestration solves the complexity of managing many containers.
- Automates full container lifecycle.
- Tools like Kubernetes, Nomad, Docker Swarm, and Marathon are widely used.
- Major benefits include speed, scalability, security, reliability, and reduced cost.

## Kubernetes Overview

### What is Kubernetes?
- An **open-source system** for automating the **deployment, scaling, and management** of containerized applications.
- Developed by **Google**, now maintained by the **Cloud Native Computing Foundation (CNCF)**.
- Widely recognized as the **de facto standard** for container orchestration.
- **Portable** across public clouds, private clouds, and on-premises infrastructure.
- Supports **declarative management**: automatically ensures actual system state matches desired state.

### What Kubernetes Is Not
- **Not** a full Platform-as-a-Service (PaaS).
- **Not** prescriptive about:
  - CI/CD pipelines
  - Logging, monitoring, or alerting
  - Middleware, databases, or built-in services
- **Not** rigid; supports a wide range of workloads (stateless, stateful, batch, data processing).

---

## Kubernetes Core Concepts

### Compute & Workloads
- **Pods**: Smallest deployable compute unit; a group of containers sharing storage/network.
- **Workloads**: Higher-level abstractions for managing Pods (Deployments, StatefulSets, etc.).

### Services & Networking
- **Services**: Expose Pods as a network service with a stable IP and DNS name.
- **IPv4/IPv6** dual-stack support.

### Storage
- Supports **temporary and persistent** volumes.
- Can mount **local, network, or cloud-based** storage systems.

### Configuration & Security
- **Configuration**: Resource provisioning and management for Pods.
- **Security**:
  - Pod and API access control
  - Secrets management (e.g., passwords, tokens, SSH keys)
  - Secure config updates without rebuilding images

### Scheduling & Policies
- **Scheduling**: Matches Pods to Nodes based on resource needs.
- **Eviction**: Proactively removes Pods on overloaded Nodes.
- **Preemption**: Terminates low-priority Pods to run higher-priority ones.

### Cluster Administration
- Tools and capabilities for setting up and managing Kubernetes clusters.

---

## Kubernetes Capabilities

### Automation
- **Automated rollouts/rollbacks** of application and configuration changes.
- **Self-healing**: Restarts, replaces, or reschedules failed containers.

### Scaling & Load Balancing
- **Horizontal scaling** based on metrics or commands.
- **Service discovery** and **load balancing** for high availability.

### Storage Orchestration
- Automates storage provisioning and volume mounts.

### Resource Optimization
- **Automated bin packing**:
  - Efficient resource allocation
  - High utilization without sacrificing availability

---

## Kubernetes Ecosystem

### Public Cloud Providers
- **AWS**, **Google Cloud**, **IBM**, **Prisma**

### Open Source Frameworks
- **Red Hat**, **VMware**, **SUSE**, **Docker**, **Mesosphere**, **Cloud Foundry**

### Cluster Management Platforms
- **DigitalOcean**, **loodse**, **SUPERGIANT**, **CloudSoft**, **Techtonic**, **Weaveworks**

### Tooling
- **CI/CD & Dev Tools**: JFrog, Bitnami, Univa, Aspen Mesh, Cloud 66
- **Monitoring & Logging**: Grafana, DataDog, New Relic, Sysdig, Dynatrace, SignalFX, Sumo Logic
- **Security**: Aqua, Black Duck, TwistLock, Alcide, Cilium, Yubico, Guardicore
- **Load Balancing**: NGINX, VMware, AVI Networks

---

### Summary

- Kubernetes is a **flexible**, **scalable**, and **extensible** orchestration platform.
- Key concepts: Pods, Services, Scheduling, Storage, Security, and Configuration.
- Capabilities include:
  - Automated rollouts & healing
  - Storage orchestration
  - Horizontal scaling
  - Load balancing
  - Secret/config management
- Backed by a massive, growing **ecosystem of tools, providers, and integrations**.

## Kubernetes Architecture Overview

### Kubernetes Cluster
- A **Kubernetes cluster** is a group of nodes running containerized applications.
- It consists of:
  - **Control Plane**: Manages the cluster.
  - **Worker Nodes**: Run application workloads (containers).

---

## Control Plane Components

### kube-apiserver
- **Front-end** of the Kubernetes control plane.
- Exposes the **Kubernetes API**.
- Handles all communication and operations via API requests.
- **Horizontally scalable**—multiple instances can run simultaneously.

### etcd
- A **highly available key-value store**.
- Stores **cluster configuration and state**.
- Defines the **desired state** of the cluster (e.g., deployments, replicas).

### kube-scheduler
- Assigns **new Pods** to appropriate Nodes.
- Makes decisions based on **resource availability**, **policies**, and **scheduling principles**.

### kube-controller-manager
- Runs various **controllers** that:
  - Monitor the state of cluster resources.
  - Ensure the **actual state** matches the **desired state**.
  - Examples: node controller, replica set controller.

### cloud-controller-manager
- Integrates with **underlying cloud provider APIs**.
- Manages cloud resources (e.g., load balancers, storage volumes).
- Enables **cloud-agnostic** architecture by decoupling cloud-specific logic.

---

## Worker Node Components

### Nodes
- **Worker machines** (virtual or physical) that run user workloads.
- Managed by the control plane.
- Each node runs Kubernetes components and application containers.

### Pods
- **Smallest deployable unit** in Kubernetes.
- A Pod can contain **one or more containers** that:
  - Share networking and storage.
  - Run on the same Node.

### kubelet
- **Primary agent** on each Node.
- Communicates with **kube-apiserver**.
- Ensures containers are **running correctly** as defined by Pod specs.
- Reports Pod status back to the control plane.

### Container Runtime
- Downloads images and runs containers in Pods.
- Pluggable via Kubernetes’ **Container Runtime Interface (CRI)**.
- Common runtimes:
  - **Docker**
  - **Podman**
  - **CRI-O**

### kube-proxy
- A **network proxy** running on each node.
- Maintains **network rules** for Pod communication.
- Enables **service discovery and load balancing** across Pods.

---

### Summary

- **Control Plane** handles cluster-level decisions:
  - Components: `kube-apiserver`, `etcd`, `kube-scheduler`, `kube-controller-manager`, `cloud-controller-manager`.
- **Worker Plane** runs user applications:
  - Components: `kubelet`, `container runtime`, `kube-proxy`, `Pods`.
- **Pods** are the smallest unit of deployment.
- Kubernetes architecture allows **flexibility, scalability**, and **cloud agnosticism**.

## Kubernetes Objects and Configuration

### Software Objects and Persistence
- A **software object** has:
  - **Identity**: Uniquely identifiable.
  - **State**: Represents current data or configuration.
  - **Behavior**: Defines what it does or how it reacts.
- **Entity**: Domain-specific object with identity and data (e.g., bank account).
- **Persistent**: Survives crashes or reboots (e.g., persistent storage).
- **Kubernetes Objects** are **persistent entities** that define the desired and current state of Kubernetes-managed resources.

---

## Kubernetes Object Structure

### Two Main Fields
- **spec**: Desired state (defined by the user).
- **status**: Current state (reported by Kubernetes).
- Kubernetes works to **match the current state to the desired state**.

### Interacting with Objects
- Use the **Kubernetes API**, **client libraries**, and/or the **kubectl** CLI tool.

---

## Labels and Namespaces

### Labels
- **Key-value pairs** attached to objects.
- Used to **identify and group** resources.
- Multiple objects can share the same labels.

### Label Selectors
- Identify sets of objects with matching labels.
- Core mechanism for **grouping and selection**.

### Namespaces
- **Isolate groups of resources** in the same cluster.
- Useful for **multi-team** or **multi-project** environments.
- Examples:
  - `default`: Holds user applications.
  - `kube-system`: Used by Kubernetes system components.
- Object names must be **unique within a namespace**.

---

## Pods

### Overview
- **Smallest deployable unit** in Kubernetes.
- Represents a **process or instance of an application**.
- Typically wraps **one or more containers**.
- Used for **horizontal scaling** by creating multiple replicas.

### Pod Definition (YAML)
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx
  labels:
    app: nginx
spec:
  containers:
    - name: nginx
      image: nginx:1.14.2
      ports:
        - containerPort: 80
```

---

## Replica Sets

### Purpose

* Ensures a **specified number of pod replicas** are running at all times.
* Can **create or delete pods** to meet the desired count.

### ReplicaSet Definition (YAML)

```yaml
apiVersion: apps/v1
kind: ReplicaSet
metadata:
  name: nginx-rs
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
        - name: nginx
          image: nginx:1.14.2
          ports:
            - containerPort: 80
```

> ⚠️ Creating ReplicaSets directly is not recommended.

---

## Deployments

### Purpose

* **Higher-level abstraction** managing ReplicaSets.
* Supports **rolling updates**, **rollbacks**, and **scaling**.
* Ideal for **stateless applications**.
* For **stateful workloads**, use **StatefulSets**.

### Deployment Definition (YAML)

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
        - name: nginx
          image: nginx:1.14.2
          ports:
            - containerPort: 80
```

### Rolling Updates

* Deployments update applications **without downtime**:

  * **Scale up** new version.
  * **Scale down** old version.

---

## Summary

* Kubernetes objects are **persistent entities** with `spec` and `status`.
* **Namespaces** isolate resource groups within a cluster.
* **Pods** are the simplest deployable units.
* **ReplicaSets** manage the number of running Pods.
* **Deployments** orchestrate ReplicaSets and provide enhanced update and scaling features.

## 🔗 Kubernetes Services

### What is a Service?

* A **Service** is a **REST object** in Kubernetes, just like Pods.
* It is a **logical abstraction** that defines a set of Pods and a policy by which to access them.
* Provides:

  * A **stable IP address** or **DNS name**.
  * **Load balancing** across Pods.
  * **Service discovery**, eliminating the need for external systems.

### Why Services Are Needed

* Pods are **ephemeral**—they can be created/destroyed at any time.
* This causes issues with changing IPs.
* Services **track** Pods using **selectors** and expose a **stable endpoint**.

---

## ⚙️ Service Types

| Service Type            | Description                                                                                                                                       |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| **ClusterIP** (default) | Internal-only access. Provides communication **within the cluster** (e.g., frontend ↔ backend).                                                   |
| **NodePort**            | Exposes service on **static port** on each node's IP. Extends ClusterIP. Not recommended for production.                                          |
| **LoadBalancer**        | Integrates with **cloud ELBs**. Automatically creates NodePort + ClusterIP and exposes via an **external IP**.                                    |
| **ExternalName**        | Maps a service to a **DNS name**. No selectors; returns a **CNAME record**. Good for **external resources** or **cross-namespace** communication. |

---

## 🌐 Ingress

* An **Ingress** is an API object + controller used for **HTTP/HTTPS routing** to Services.
* Typically used to expose applications via **port 80/443**.
* More cost-effective than external load balancers.
* Allows **centralized access control**, **TLS**, and **path-based routing**.

---

## 🧱 Workload Controllers

### 🟡 DaemonSet

* Ensures that a **Pod runs on every (or selected) node**.
* Good for:

  * Logging agents
  * Monitoring daemons
  * Node-level storage
* Pods are **garbage collected** when nodes are removed.
* Deleting the DaemonSet removes all associated Pods.

### 🟢 StatefulSet

* Used for **stateful applications**.
* Guarantees:

  * **Stable network identities** (`pod-0`, `pod-1`, etc.)
  * **Persistent storage**
  * **Ordered deployment and scaling**
* Common for:

  * Databases (e.g., PostgreSQL, MongoDB)
  * Queues (e.g., Kafka)

### 🔄 Job

* **Runs Pods to completion** (not continuously).
* Pods are retried until they **succeed**.
* Deleting a Job deletes its Pods.
* You can:

  * Run **parallel Pods**
  * Use **suspension/resume**
  * Use a **CronJob** to schedule Jobs.

---

## 🔑 Summary

* **Service**: Exposes a stable endpoint to a dynamic set of Pods.
* **ClusterIP**: Default internal communication.
* **NodePort**: Adds external access via static port.
* **LoadBalancer**: External access via cloud provider’s load balancer.
* **ExternalName**: DNS alias to external service.
* **Ingress**: Manages external HTTP(S) traffic to services with routing rules.
* **DaemonSet**: Runs a Pod on each node—ideal for node-level utilities.
* **StatefulSet**: Manages Pods with stable identity and persistent storage.
* **Job**: Runs tasks to completion; CronJobs schedule Jobs at intervals.

## 🛠️ Kubernetes with `kubectl`

### What is `kubectl`?
- The **Kubernetes CLI**.
- Stands for **"kube control"**.
- Used for:
  - Deploying applications
  - Managing resources
  - Viewing logs
  - Cluster inspection

---

## 📐 `kubectl` Command Structure

```

kubectl \[command] \[type] \[name] \[flags]

```

- **command**: `create`, `get`, `apply`, `delete`, etc.
- **type**: Resource type — e.g. `pod`, `deployment`, `service`
- **name**: Specific object name (optional)
- **flags**: Options/modifiers to customize behavior

---

## ⚡ Types of `kubectl` Configuration Approaches

### 1. Imperative Commands
- Run live operations directly via the CLI.
- **Example**:
```sh
  kubectl run nginx --image=nginx
```

* ✅ Easy and quick for dev/test
* ❌ No audit trail, not reusable, not scalable
* ❌ Not suitable for teams or production

---

### 2. Imperative Object Configuration

* Uses configuration **files** with full object definitions.
* **Example**:

  ```sh
  kubectl create -f nginx.yaml
  ```
* ✅ Enables reuse across environments
* ✅ Can store configs in Git for version control
* ❌ Must manually track and update changes
* ❌ Can lead to config drift if updates are not committed

---

### 3. Declarative Object Configuration (Best Practice)

* Define the **desired state** in config files.
* Kubernetes reconciles actual state with desired state.
* **Example**:

```sh
  kubectl apply -f ./configs/
```
* ✅ Ideal for production
* ✅ Supports automation, versioning, GitOps
* ✅ Centralized source of truth

---

## 🧰 Common `kubectl` Commands

| Command             | Description                       |
| ------------------- | --------------------------------- |
| `kubectl get`       | List resources                    |
| `kubectl delete`    | Delete resources                  |
| `kubectl apply -f`  | Apply config file (YAML/JSON)     |
| `kubectl autoscale` | Add autoscaling to a deployment   |
| `kubectl scale`     | Manually scale number of replicas |

---

## 📄 `kubectl get` Examples

| Command                             | Description                        |
| ----------------------------------- | ---------------------------------- |
| `kubectl get svc`                   | List services in current namespace |
| `kubectl get pods --all-namespaces` | List all pods                      |
| `kubectl get deployment my-dep`     | Get specific deployment            |
| `kubectl get pods`                  | List pods in current namespace     |

---

## 📈 `kubectl scale` Examples

* Scale a ReplicaSet:

```sh
  kubectl scale rs/foo --replicas=3
```

* Scale using a config file:

```sh
  kubectl scale -f resourceinfo.yaml --replicas=3
```

---

## 📌 Deployment Example

1. Create a deployment with 3 replicas:

```sh
   kubectl apply -f my-deployment.yaml
```

2. Verify:

```sh
   kubectl get deployment my-dep
```

   Sample output:

```bash
   NAME     READY   UP-TO-DATE   AVAILABLE   AGE
   my-dep   3/3     3            3           1m
```

---

## ✅ Summary

* `kubectl` is the primary CLI for Kubernetes operations.
* Use **imperative** for quick tasks, **imperative config** for reusability, and **declarative config** for production.
* Declarative is the **recommended approach** for version control, team collaboration, and automation.

## 🤖 Kubernetes ReplicaSet & Deployment

### 🚫 Why a Single Pod is Insufficient
- **Cannot handle increased traffic** or surges in request volume
- **Single point of failure** — No redundancy
- **No fault tolerance** — Cannot recover from pod crashes
- ❌ No load balancing or scaling capabilities

---

### ✅ Solution: ReplicaSet

#### What is a ReplicaSet?
- Ensures **a specified number of pod replicas** are running at all times
- **Maintains desired state** by:
  - Replacing failed pods
  - Scaling pods up/down
  - Deleting excess pods
- **Uses pod labels** to identify pods it manages
- Supersedes the older `ReplicationController`

---

#### How ReplicaSets Work
- Created **automatically** when a **Deployment** is created
- Managed **indirectly** via **Deployments** (best practice)
- ReplicaSets themselves do **not "own" pods** — they match pods using **labels**
- ReplicaSets created manually require `.spec.replicas` and `.selector.matchLabels`

---

### 📦 Deployment + ReplicaSet

#### Benefits of Deployment:
- Manages ReplicaSets
- Sends **declarative updates**
- Automatically:
  - Rolls out updates
  - Rolls back changes
  - Maintains availability

---

## 🧪 Creating a ReplicaSet (YAML)

```yaml
apiVersion: apps/v1
kind: ReplicaSet
metadata:
  name: my-replicaset
spec:
  replicas: 1
  selector:
    matchLabels:
      app: my-app
  template:
    metadata:
      labels:
        app: my-app
    spec:
      containers:
      - name: nginx
        image: nginx
```

* Run: `kubectl apply -f replicaset.yaml`
* Confirm:

```sh
  kubectl get pods
  kubectl get rs
```

---

### 📈 Scaling Deployments

1. **Create a deployment**:

```sh
   kubectl create deployment hello-kubernetes --image=nginx
```

2. **Scale it**:

```sh
   kubectl scale deployment hello-kubernetes --replicas=3
```

3. **Confirm**:

```sh
   kubectl get pods
```

   Example output:

```
   hello-kubernetes-5mflw
   hello-kubernetes-hbt7v
   hello-kubernetes-xxxxxx
```

---

### 🔄 Maintaining Desired State

#### When a Pod is Deleted:

* Run:

  ```sh
  kubectl delete pod hello-kubernetes-5mflw
  ```
* ReplicaSet **automatically creates a replacement** pod
* Confirm:

```sh
  kubectl get pods
```

---

### When a Pod is Created Manually:

* Manually add a pod:

```sh
  kubectl apply -f newpod.yaml
```
* ReplicaSet notices the **extra pod** and **deletes it**
* Desired state of 3 pods is restored

---

### 🧠 Key Learnings

* A **ReplicaSet** provides:

  * **High availability**
  * **Fault tolerance**
  * **Scaling**
* Best practice: **Use a Deployment to manage ReplicaSets**
* ReplicaSet uses **labels** to track and maintain pods
* Kubernetes always **reconciles desired state with actual state**
