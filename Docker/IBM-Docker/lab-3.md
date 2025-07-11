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

## 1 - Create your first swarm
In this section, you will create your first swarm by using Play-with-Docker.

1. Navigate to Play-with-Docker. You're going to create a swarm with three nodes.

2. Click Add new instance on the left side three times to create three nodes.
3. Initialize the swarm on node 1:
```bash
$ docker swarm init --advertise-addr eth0
Swarm initialized: current node (vq7xx5j4dpe04rgwwm5ur63ce) is now a manager.

To add a worker to this swarm, run the following command:

    docker swarm join \
    --token SWMTKN-1-50qba7hmo5exuapkmrj6jki8knfvinceo68xjmh322y7c8f0pj-87mjqjho30uue43oqbhhthjui \
    10.0.120.3:2377
```
To add a manager to this swarm, run 'docker swarm join-token manager' and follow the instructions.
You can think of Docker Swarm as a special mode that is activated by the command: docker swarm init. The --advertise-addr option specifies the address in which the other nodes will use to join the swarm.

This docker swarm init command generates a join token. The token makes sure that no malicious nodes join the swarm. You need to use this token to join the other nodes to the swarm. For convenience, the output includes the full command docker swarm join, which you can just copy/paste to the other nodes.

On both node2 and node3, copy and run the docker swarm join command that was outputted to your console by the last command.
You now have a three-node swarm!

Back on node1, run docker node ls to verify your three-node cluster:
```bash
$ docker node ls
ID                            HOSTNAME            STATUS              AVAILABILITY        MANAGER STATUS
7x9s8baa79l29zdsx95i1tfjp     node3               Ready               Active
x223z25t7y7o4np3uq45d49br     node2               Ready               Active
zdqbsoxa6x1bubg3jyjdmrnrn *   node1               Ready               Active              Leader
```
This command outputs the three nodes in your swarm. The asterisk (*) next to the ID of the node represents the node that handled that specific command (docker node ls in this case).

Your node consists of one manager node and two workers nodes. Managers handle commands and manage the state of the swarm. Workers cannot handle commands and are simply used to run containers at scale. By default, managers are also used to run containers.

All docker service commands for the rest of this lab need to be executed on the manager node (Node1).

Note: Although you control the swarm directly from the node in which its running, you can control a Docker swarm remotely by connecting to the Docker Engine of the manager by using the remote API or by activating a remote host from your local Docker installation (using the $DOCKER_HOST and $DOCKER_CERT_PATH environment variables). This will become useful when you want to remotely control production applications, instead of using SSH to directly control production servers.

## 2 - Deploy your first service
Now that you have your three-node Swarm cluster initialized, you'll deploy some containers. To run containers on a Docker Swarm, you need to create a service. A service is an abstraction that represents multiple containers of the same image deployed across a distributed cluster.

Let's do a simple example using NGINX. For now, you will create a service with one running container, but you will scale up later.

1. On Node1 (manager node), deploy a service by using NGINX:
```bash
$ docker service create --detach=true --name nginx1 --publish 80:80  --mount source=/etc/hostname,target=/usr/share/nginx/html/index.html,type=bind,ro nginx:1.12 pgqdxr41dpy8qwkn6qm7vke0q
```
This command statement is declarative, and Docker Swarm will try to maintain the state declared in this command unless explicitly changed by another docker service command. This behavior is useful when nodes go down, for example, and containers are automatically rescheduled on other nodes. You will see a demonstration of that a little later in this lab.

The --mount flag is useful to have NGINX print out the hostname of the node it's running on. You will use this later in this lab when you start load balancing between multiple containers of NGINX that are distributed across different nodes in the cluster and you want to see which node in the swarm is serving the request.

You are using NGINX tag 1.12 in this command. You will see a rolling update with version 1.13 later in this lab.

The --publish command uses the swarm's built-in routing mesh. In this case, port 80 is exposed on every node in the swarm. The routing mesh will route a request coming in on port 80 to one of the nodes running the container.

2. Inspect the service.  Use the command docker service ls to inspect the service you just created:
```bash
$ docker service ls
ID                  NAME                MODE                REPLICAS            IMAGE               PORTS
pgqdxr41dpy8        nginx1              replicated          1/1                 nginx:1.12          *:80->80/tcp
```
3. Check the running container of the service.

To take a deeper look at the running tasks, use the command docker service ps. A task is another abstraction in Docker Swarm that represents the running instances of a service. In this case, there is a 1-1 mapping between a task and a container.
```bash
$ docker service ps nginx1
ID                  NAME                IMAGE               NODE                DESIRED STATE       CURRENT STATE           ERROR               PORTS
iu3ksewv7qf9        nginx1.1            nginx:1.12          node1               Running             Running 8 minutes ago
```
If you know which node your container is running on (you can see which node based on the output from docker service ps), you can use the command docker container ls to see the container running on that specific node.

4. Test the service.

Because of the routing mesh, you can send a request to any node of the swarm on port 80. This request will be automatically routed to the one node that is running the NGINX container.

Try this command on each node:
```bash
$ curl localhost:80
node1
```
Curling will output the hostname where the container is running. For this example, it is running on node1, but yours might be different.

## 3 - Scale your service
Update your service with an updated number of replicas.

Use the docker service command to update the NGINX service that you created previously to include 5 replicas. This is defining a new state for the service.
```bash
$ docker service update --replicas=5 --detach=true nginx1
nginx1
```
When this command is run, the following events occur:

The state of the service is updated to 5 replicas, which is stored in the swarm's internal storage.
Docker Swarm recognizes that the number of replicas that is scheduled now does not match the declared state of 5.
Docker Swarm schedules 5 more tasks (containers) in an attempt to meet the declared state for the service.
This swarm is actively checking to see if the desired state is equal to actual state and will attempt to reconcile if needed.

Check the running instances.

After a few seconds, you should see that the swarm did its job and successfully started 9 more containers. Notice that the containers are scheduled across all three nodes of the cluster. The default placement strategy that is used to decide where new containers are to be run is the emptiest node, but that can be changed based on your needs.
```bash
$ docker service ps nginx1
```

Send a lot of requests to http://localhost:80.

The --publish 80:80 parameter is still in effect for this service; that was not changed when you ran the docker service update command. However, now when you send requests on port 80, the routing mesh has multiple containers in which to route requests to. The routing mesh acts as a load balancer for these containers, alternating where it routes requests to.

Try it out by curling multiple times. Note that it doesn't matter which node you send the requests. There is no connection between the node that receives the request and the node that that request is routed to.
```bash
$ curl localhost:80
node3
$ curl localhost:80
node3
$ curl localhost:80
node2
$ curl localhost:80
node1
$ curl localhost:80
node1
```
You should see which node is serving each request because of the useful --mount command you used earlier.

Limits of the routing mesh: The routing mesh can publish only one service on port 80. If you want multiple services exposed on port 80, you can use an external application load balancer outside of the swarm to accomplish this.

Check the aggregated logs for the service.

Another easy way to see which nodes those requests were routed to is to check the aggregated logs. You can get aggregated logs for the service by using the command docker service logs [service name]. This aggregates the output from every running container, that is, the output from docker container logs [container name].
```bash
$ docker service logs nginx1
```

Based on these logs, you can see that each request was served by a different container.

In addition to seeing whether the request was sent to node1, node2, or node3, you can also see which container on each node that it was sent to. For example, nginx1.5 means that request was sent to a container with that same name as indicated in the output of the command docker service ps nginx1.