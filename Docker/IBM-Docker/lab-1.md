# Lab 1

## What are containers?
Container
- a process, or a group of processes run in isolation
    - all process must be able to run on shared kernel

Each container has its own set of "namespace" (isolated view)
- PID - process ID
- USER - user and group IDs
- UTS - hostname and domain  name
- NS - mount points
- NET - network devices, stacks, ports
- IPC - inter-process communication, message queues

- cgroups - controls limits and monitoring resources

VM vs Container

|VM | Container|
|-|-|
|Runs in hypervisor|Run on shared Kernel|
|Each have its own OS|No full-brown OS, Has OS specific Files
|Heavy, Slow to start|Light-weight, Very fast|

What is Docker?
- As its core, Docker is tooling to manage containers
    - simplified existing technology to enable it for the masses
- Enable developers to use container for their application
    - package dependencies with containers: "build once, run anywhere"

Why containers are appealing to users
- No more "Works on my machine"
- Lightweight and fast
- Better resource utilization
    - can fit far more containers than VMs into a host
- Standard developer to operations interface 
- Ecosystem and tooling

## Lab Overview

Containers are just a process (or a group of processes) running in isolation, which is achieved with Linux namespaces and control groups. Linux namespaces and control groups are features that are built into the Linux kernel. Other than the Linux kernel itself, there is nothing special about containers.

What makes containers useful is the tooling that surrounds them. The labs in this course use Docker, which has been the understood standard tool for using containers to build applications. Docker provides developers and operators with a friendly interface to build, ship, and run containers on any environment.

In the first part of this lab, run your first container, and learn how to inspect it. You will be able to witness the namespace isolation that you acquire from the Linux kernel.

After you run your first container, you can explore other uses of docker containers. You can find many examples of these on the Docker Store and can run several different types of containers on the same host, which allows you to see the benefit of isolation—where you can run multiple containers on the same host without conflicts.

You will use a few Docker commands in this lab. If interested, see the full documentation on available commands.

## Run a container 
Run a container
Use the Docker CLI to run your first container.

Open a terminal on your local computer and run this command:

```bash
$ docker container run -t ubuntu top
```
You use the docker container run command to run a container with the Ubuntu image by using the top command. The -t flag allocates a pseudo-TTY, which you need for the top command to work correctly.

The docker run command first starts a docker pull to download the Ubuntu image onto your host. After it is downloaded, it will start the container. The output for the running container should look like this:

top is a Linux utility that prints the processes on a system and orders them by resource consumption. Notice that there is only a single process in this output: it is the top process itself. You don't see other processes from the host in this list because of the PID namespace isolation.

Containers use Linux namespaces to provide isolation of system resources from other containers or the host. The PID namespace provides isolation for process IDs. If you run top while inside the container, you will notice that it shows the processes within the PID namespace of the container, which is much different than what you can see if you ran top on the host.

Even though we are using the Ubuntu image, it is important to note that the container does not have its own kernel. It uses the kernel of the host and the Ubuntu image is used only to provide the file system and tools available on an Ubuntu system.

Open a new terminal. To open a new terminal connected to node1 by using Play-With-Docker.com, click Add New Instance on the left and then ssh from node2 into node1 by using the IP that is listed by node1, for example:

In the new terminal, get the ID of the running container that you just created:

docker container ls 
 
Use that container ID to run bash inside that container by using the docker container exec command. Because you are using bash and want to interact with this container from your terminal, use the -it flag to run using interactive mode while allocating a psuedo-terminal:
```bash
$ docker container exec -it b3ad2a23fab3 bash 
root@b3ad2a23fab3:/#
```
You just used the docker container exec command to enter the container's namespaces with the bash process. Using docker container exec with bash is a common way to inspect a Docker container.

Notice the change in the prefix of your terminal, for example,  root@b3ad2a23fab3:/. This is an indication that you are running bash inside the container.

Tip: This is not the same as using ssh to a separate host or a VM. You don't need an ssh server to connect with a bash process. Remember that containers use kernel-level features to achieve isolation and that containers run on top of the kernel. Your container is just a group of processes running in isolation on the same host, and you can use the command docker container exec to enter that isolation with the bash process. After you run the command docker container exec, the group of processes running in isolation (in other words, the container) includes top and bash.

From the same terminal, inspect the running processes:
```bash
$ ps -ef
```

You should see only the top process, bash process, and your ps process. PID is just one of the Linux namespaces that provides containers with isolation to system resources.

Other Linux namespaces include:

MNT: Mount and unmount directories without affecting other namespaces.
NET: Containers have their own network stack.
IPC: Isolated interprocess communication mechanisms such as message queues.
User: Isolated view of users on the system.
UTC: Set hostname and domain name per container.
These namespaces provide the isolation for containers that allow them to run together securely and without conflict with other containers running on the same system.

For comparison, exit the container and run ps -ef or top on the host. These commands will work on Linux or Mac. For Windows, you can inspect the running processes by using tasklist.
```bash
root@b3ad2a23fab3:/# exit 
exit
```
In the next lab, you'll see different uses of containers and the benefit of isolation as you run multiple containers on the same host.

Tip: Namespaces are a feature of the Linux kernel. However, Docker allows you to run containers on Windows and Mac. The secret is that embedded in the Docker product is a Linux subsystem. Docker open-sourced this Linux subsystem to a new project: LinuxKit. Being able to run containers on many different platforms is one advantage of using the Docker tooling with containers.

In addition to running Linux containers on Windows by using a Linux subsystem, native Windows containers are now possible because of the creation of container primitives on the Windows operating system. Native Windows containers can be run on Windows 10 or Windows Server 2016 or later.

Clean up the container running the top processes:
```bash
<ctrl>-c
```

## Run Multiple containers
Explore the Docker Hub.

The Docker Hub is the public central registry for Docker images. Anyone can share images here publicly. The Docker Store contains community and official images that can also be found on the Docker Hub.

When searching for images, you will find filters for Store and Community images. Store images include content that has been verified and scanned for security vulnerabilities by Docker. Go one step further and search for Certified images that are deemed enterprise-ready and are tested with Docker Enterprise Edition.

It is important to avoid using unverified content from the Docker Store when you develop your own images that are intended to be deployed into the production environment. These unverified images might contain security vulnerabilities or possibly even malicious software.

In the next step of this lab, you will start a couple of containers by using some verified images from the Docker Store: NGINX web server and Mongo database.

Run an NGINX server by using the official NGINX image from the Docker Store:
```bash
$ docker container run --detach --publish 8080:80 --name nginx nginx
```

You are using a couple of new flags here. The --detach flag will run this container in the background. The publish flag publishes port 80 in the container (the default port for NGINX) by using port 8080 on your host. Remember that the NET namespace gives processes of the container their own network stack. The --publish flag is a feature that can expose networking through the container onto the host.

How do you know port 80 is the default port for NGINX? Because it is listed in the documentation on the Docker Store. In general, the documentation for the verified images is very good, and you will want to refer to it when you run containers using those images.

You are also specifying the --name flag, which names the container. Every container has a name. If you don't specify one, Docker will randomly assign one for you. Specifying your own name makes it easier to run subsequent commands on your container because you can reference the name instead of the id of the container. For example, you can specify docker container inspect nginx instead of docker container inspect 5e1.

Because this is the first time you are running the NGINX container, it will pull down the NGINX image from the Docker Store. Subsequent containers created from the NGINX image will use the existing image located on your host.

NGINX is a lightweight web server. You can access it on port 8080 on your localhost.

Access the NGINX server on http://localhost:8080.


Run a MongoDB server. You will use the official MongoDB image from the Docker Store. Instead of using the latest tag (which is the default if no tag is specified), use a specific version of the Mongo image: 3.4.
```bash
$ docker container run --detach --publish 8081:27017 --name mongo mongo:3.4
```

Again, because this is the first time you are running a Mongo container, pull the Mongo image from the Docker Store. You use the --publish flag to expose the 27017 Mongo port on your host. You must use a port other than 8080 for the host mapping because that port is already exposed on your host. See the documentation on the Docker Store to get more information about using the Mongo image.

Access http://localhost:8081 to see some output from Mongo.


Check your running containers:
```bash
$ docker container ls 
```

You should see that you have an NGINX web server container and a MongoDB container running on your host. Note that you have not configured these containers to talk to each other.

You can see the nginx and mongo names that you gave to the containers and the random name (in this example, priceless_kepler) that was generated for the Ubuntu container. You can also see that the port mappings that you specified with the --publish flag. For more information on these running containers, use the docker container inspect [container id] command.

One thing you might notice is that the Mongo container is running the docker-entrypoint command. This is the name of the executable that is run when the container is started. The Mongo image requires some prior configuration before kicking off the DB process. You can see exactly what the script does by looking at it on GitHub. Typically, you can find the link to the GitHub source from the image description page on the Docker Store website.

Containers are self-contained and isolated, which means you can avoid potential conflicts between containers with different system or runtime dependencies. For example, you  can deploy an app that uses Java 7 and another app that uses Java 8 on the same host. Or you can run multiple NGINX containers that all have port 80 as their default listening ports. (If you're exposing on the host by using the --publish flag, the ports selected for the host must be unique.) Isolation benefits are possible because of Linux namespaces.

Remember: You didn't have to install anything on your host (other than Docker) to run these processes! Each container includes the dependencies that it needs within the container, so you don't need to install anything on your host directly.

Running multiple containers on the same host gives us the ability to use the resources (CPU, memory, and so on) available on single host. This can result in huge cost savings for an enterprise.

Although running images directly from the Docker Store can be useful at times, it is more useful to create custom images and refer to official images as the starting point for these images. You'll learn to build your own custom images in the next lab.