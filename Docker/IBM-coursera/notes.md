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
