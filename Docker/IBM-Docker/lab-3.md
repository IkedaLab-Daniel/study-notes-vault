# Lab 3 - Intro to container orchestration

## Container orchestration overview
Containers have advantages, but also have major problems
- Automated scheduling and scaling
- Service discovery
- Zero downtime deployments
- High availability and fault tolerance
- A/B Delopments

Container Orchestration:
- Cluster management
- scheduling
- service discovery
- replication
- health management
- declare desired state
    - active reconciliation

## Overview
Lab 3 overview
So far, you have learned how to run applications by using Docker on your local machine. But what about running Dockerized applications in production? A number of problems come with building an application for production, for example:

Scheduling services across distributed nodes
Maintaining high availability
Implementing reconciliation
Scaling
Logging
Several orchestration solutions are available to help you solve some of these problems. One example is the IBM Cloud Kubernetes Service, which uses Kubernetes to run containers in production.

Before you learn about Kubernetes, you will learn how to orchestrate applications by using Docker Swarm. Docker Swarm is the orchestration tool that is built into the Docker Engine.

This lab uses a few Docker commands. For a complete list of commands, see the Docker documentation.

To complete a lab about orchestrating an application that is deployed across multiple hosts, you need multiple hosts. To make things easier, this lab uses the multi-node support provided by Play-with-Docker. This is the easiest way to test Docker Swarm without having to install Docker on multiple hosts.

Be sure you have a Docker Hub account.