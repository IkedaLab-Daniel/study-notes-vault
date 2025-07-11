# Lab 2: Add CI/CD value with Docker images

## Docker Image
Summary
The lab focuses on creating custom Docker images using Dockerfiles. A Docker image is essentially a compressed file system archive used to create containers, enabling easy sharing and distribution across environments. Docker Hub serves as the default public registry for pulling and pushing images, but private registries are also important for enterprise use. Dockerfiles contain instructions to build images, with each line forming a separate cached layer. This layering system optimizes build and push processes by reusing unchanged layers, significantly speeding up continuous integration and deployment (CI/CD) pipelines. Docker images use a union filesystem with a copy-on-write mechanism to maintain read-only layers while allowing containers to have writable layers on top, saving disk space and improving efficiency. The lab includes hands-on exercises to build, run, and push custom images, demonstrating the benefits of layer caching through incremental updates.

Highlights
🐳 Docker images are file system archives that enable container creation and distribution.
📦 Docker Hub is the default public registry for sharing images, with private registries used in enterprises.
📝 Dockerfiles instruct Docker on building images with each line creating a cached image layer.
⚡ Layer caching speeds up builds and pushes by reusing unchanged layers, enhancing CI/CD efficiency.
🔄 Union filesystem and copy-on-write enable read-only image layers with writable container layers on top.
💾 Layer reuse saves significant disk space by sharing base layers across containers and images.
🚀 Lab exercises focus on creating, running, pushing images, and demonstrating layer caching benefits.
Key Insights
🐳 Docker Image Architecture: Docker images are structured as layered tar archives, which represent the file system for containers. This abstraction allows for easy sharing and consistent execution environments across different hosts and environments. Understanding this helps in effective image management and troubleshooting.
🗄️ Layered Caching Mechanism: Each Dockerfile instruction creates a new immutable layer, which Docker caches. When building or pushing images, Docker reuses these cached layers if unchanged, drastically reducing build times and network usage—critical for efficient CI/CD workflows.
🔐 Private vs Public Registries: While Docker Hub is great for publicly available images and learning, private registries are essential for enterprise security and control. Enterprises can self-host registries using Docker images, offering flexibility and integration with internal infrastructure.
📂 Union Filesystem & Copy-On-Write: Docker’s union filesystem merges multiple read-only image layers into a single unified view in containers. Copy-on-write ensures that container-specific changes do not alter the base image, enabling safe reuse and sharing of image layers among multiple containers.
💡 Optimizing Dockerfile for Caching: Ordering Dockerfile instructions from least to most frequently changing improves build efficiency. For example, placing source code additions at the end allows earlier layers to be cached and reused, minimizing rebuild times when code changes.
💾 Storage Efficiency: Because image layers are shared and read-only, running thousands of containers from the same image consumes minimal additional disk space—only a small writable layer per container—maximizing host resource utilization.
🚀 Practical Lab Application: The hands-on lab reinforces theoretical concepts by guiding users through creating a Dockerfile, building and running images, pushing to Docker Hub, and observing caching effects during updates, providing practical understanding of Docker image layering and optimization.

Notes:

Docker Image
- TAR file containing a container's filesystem + metadata
- For sharing and redistribution

Docker Registry
- push and pull image from registry
- default registry: Docker Hub
    - Public and free for public image
    - many pre-packaged images available
- Private registry
    - self-host or cloud provider options

Create a Docker image - with docker build
- Create a "Dockerfile"
    - list of instructions for how to construct the container
```bash
docker build -f Dockerfile
```
```bash
$ cat Dockerfile
FROM ubuntu
ADD myapp /
EXPOSE 80
ENTRYPOINT /myapp
```

Secret sauce: Docker image layer

Docker image layer
- Union file system
    - merge image layer into single file system for each container
- copy-on-write
    - copies file that are edited up to top writable layer 
- Advantages
    - more container per host
    - faster start-up/download time - base layers are cached

## Lab overview
In this lab, build on your knowledge from Lab 1 where you used Docker commands to run containers. Create a custom Docker image built from a Dockerfile. After you build the image, you will push it to a central registry where it can be pulled to be deployed on other environments.

Also, you'll get a brief understanding of image layers and how Docker incorporates copy-on-write and the union file system to efficiently store images and run containers. You will use a few Docker commands in this lab. See the documentation on for information on available commands.