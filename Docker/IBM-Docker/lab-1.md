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

