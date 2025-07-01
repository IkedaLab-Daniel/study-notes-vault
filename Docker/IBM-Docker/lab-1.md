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