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

$ docker container run -t ubuntu top
You use the docker container run command to run a container with the Ubuntu image by using the top command. The -t flag allocates a pseudo-TTY, which you need for the top command to work correctly.



The docker run command first starts a docker pull to download the Ubuntu image onto your host. After it is downloaded, it will start the container. The output for the running container should look like this:



top is a Linux utility that prints the processes on a system and orders them by resource consumption. Notice that there is only a single process in this output: it is the top process itself. You don't see other processes from the host in this list because of the PID namespace isolation.

Containers use Linux namespaces to provide isolation of system resources from other containers or the host. The PID namespace provides isolation for process IDs. If you run top while inside the container, you will notice that it shows the processes within the PID namespace of the container, which is much different than what you can see if you ran top on the host.

Even though we are using the Ubuntu image, it is important to note that the container does not have its own kernel. It uses the kernel of the host and the Ubuntu image is used only to provide the file system and tools available on an Ubuntu system.

Open a new terminal. To open a new terminal connected to node1 by using Play-With-Docker.com, click Add New Instance on the left and then ssh from node2 into node1 by using the IP that is listed by node1, for example:



In the new terminal, get the ID of the running container that you just created:

docker container ls 
 


Use that container ID to run bash inside that container by using the docker container exec command. Because you are using bash and want to interact with this container from your terminal, use the -it flag to run using interactive mode while allocating a psuedo-terminal:

$ docker container exec -it b3ad2a23fab3 bash 
root@b3ad2a23fab3:/#
You just used the docker container exec command to enter the container's namespaces with the bash process. Using docker container exec with bash is a common way to inspect a Docker container.

Notice the change in the prefix of your terminal, for example,  root@b3ad2a23fab3:/. This is an indication that you are running bash inside the container.

Tip: This is not the same as using ssh to a separate host or a VM. You don't need an ssh server to connect with a bash process. Remember that containers use kernel-level features to achieve isolation and that containers run on top of the kernel. Your container is just a group of processes running in isolation on the same host, and you can use the command docker container exec to enter that isolation with the bash process. After you run the command docker container exec, the group of processes running in isolation (in other words, the container) includes top and bash.

From the same terminal, inspect the running processes:

$ ps -ef
 


You should see only the top process, bash process, and your ps process. PID is just one of the Linux namespaces that provides containers with isolation to system resources.

Other Linux namespaces include:

MNT: Mount and unmount directories without affecting other namespaces.
NET: Containers have their own network stack.
IPC: Isolated interprocess communication mechanisms such as message queues.
User: Isolated view of users on the system.
UTC: Set hostname and domain name per container.
These namespaces provide the isolation for containers that allow them to run together securely and without conflict with other containers running on the same system.

For comparison, exit the container and run ps -ef or top on the host. These commands will work on Linux or Mac. For Windows, you can inspect the running processes by using tasklist.

root@b3ad2a23fab3:/# exit 
exit
In the next lab, you'll see different uses of containers and the benefit of isolation as you run multiple containers on the same host.

Tip: Namespaces are a feature of the Linux kernel. However, Docker allows you to run containers on Windows and Mac. The secret is that embedded in the Docker product is a Linux subsystem. Docker open-sourced this Linux subsystem to a new project: LinuxKit. Being able to run containers on many different platforms is one advantage of using the Docker tooling with containers.

In addition to running Linux containers on Windows by using a Linux subsystem, native Windows containers are now possible because of the creation of container primitives on the Windows operating system. Native Windows containers can be run on Windows 10 or Windows Server 2016 or later.

Clean up the container running the top processes:

<ctrl>-c

