# Day 1 — Docker Fundamentals

## Objective

The goal of Day 1 was to understand the basic Docker workflow through hands-on experimentation rather than passive learning.

The main concepts explored were:

* Docker images
* Docker containers
* Running vs. stopped containers
* `docker run`
* `docker ps`
* `docker ps -a`
* `docker stop`
* `docker start`
* Docker port mapping
* Host ports vs. container ports
* Basic Docker troubleshooting

The learning approach used throughout the session was:

> **Predict → Experiment → Observe → Explain**

---

# 1. Docker Images

## What I initially thought

I initially thought an image might be an already-available container in Docker. I also understood that images could be used to package software so that other people could run it without dealing with dependency and version conflicts.

## What I understand now

A **Docker image** is a packaged, read-only artifact containing the filesystem, application code/dependencies, and metadata needed to create a container.

An image is **not a container**.

An image can be used as the basis for creating one or more containers.

For example:

```text
nginx image
     │
     ├── Container 1
     │
     ├── Container 2
     │
     └── Container 3
```

The same image can therefore be used to create multiple containers.

### Important distinction

```text
Image = packaged artifact / template

Container = runtime instance created from an image
```

---

# 2. Docker Containers

## Initial understanding

I initially thought of a container as a running instance of an image.

The analogy I used was:

> Image = blueprint of a house
> Container = house created from that blueprint

This is a useful analogy, but it needed one correction.

## What I understand now

A container is an **isolated runtime environment created from a Docker image**.

A container does not necessarily have to be running.

It can exist in different states, including:

```text
Created
Running
Exited / Stopped
```

For example, I observed stopped containers using:

```powershell
docker ps -a
```

This showed that a container can still exist even after its process has stopped.

A stopped container can subsequently be started again:

```powershell
docker start <container_id>
```

---

# 3. `docker ps`

The command:

```powershell
docker ps
```

shows currently running containers.

Example use:

```text
docker ps
    ↓
Which containers are running right now?
```

This is useful when checking the current runtime state of Docker containers.

---

# 4. `docker ps -a`

The command:

```powershell
docker ps -a
```

shows all containers, including containers that are currently stopped.

The `-a` flag means to include all containers rather than only currently running containers.

This became useful during the Day 1 experiments because several Nginx containers had been stopped but still existed.

Example states observed:

```text
Running
Exited (0)
Created
```

This demonstrated the difference between a container **existing** and a container **currently running**.

---

# 5. Running an Nginx Container

The first real application container was started with:

```powershell
docker run -d -p 8080:80 nginx
```

This started an Nginx container in detached mode.

The application was then accessible through:

```text
http://localhost:8080
```

This was my first practical demonstration of running a web server inside a Docker container.

---

# 6. Understanding `docker run`

The command:

```powershell
docker run -d -p 8080:80 nginx
```

can be understood as:

```text
docker run
    ↓
Create and start a container from the nginx image
```

### `-d`

Runs the container in detached mode, allowing the terminal to remain available while the container runs in the background.

### `-p 8080:80`

Maps a port on the host machine to a port inside the container.

The general format is:

```text
-p HOST_PORT:CONTAINER_PORT
```

Therefore:

```text
-p 8080:80
```

means:

```text
Host machine port 8080
        │
        ▼
Container port 80
        │
        ▼
Nginx
```

---

# 7. Host Port vs. Container Port

This was one of the most important concepts learned during Day 1.

Initially, I was thinking about port `80` as a standard TCP port and was not clearly distinguishing it from port `8080`.

After experimentation, I understood that the two numbers have different meanings.

For:

```powershell
-p 8080:80
```

the meanings are:

```text
8080 = port on the host machine

80 = port inside the container
```

Therefore, accessing:

```text
http://localhost:8080
```

causes traffic to reach the host's port `8080`, which Docker forwards to port `80` inside the Nginx container.

Conceptually:

```text
Browser
   │
   ▼
localhost:8080
   │
   ▼
Host port 8080
   │
   │ Docker port mapping
   ▼
Container port 80
   │
   ▼
Nginx
```

---

# 8. Multiple Containers Can Use the Same Container Port

I tested this by running another Nginx container:

```powershell
docker run -d -p 5000:80 nginx
```

This container was accessible through:

```text
http://localhost:5000
```

At this point, two Nginx containers were running:

```text
localhost:8080 → Container 1 → port 80

localhost:5000 → Container 2 → port 80
```

Both containers were able to use **container port 80**.

There was no conflict because each container has its own isolated networking environment.

The host ports were different:

```text
8080 → Container 1:80
5000 → Container 2:80
```

---

# 9. Port Conflict

I then tested what happens when another container attempts to use an already-occupied host port.

If a container is already using:

```text
localhost:5000 → Container 2:80
```

and I attempt:

```powershell
docker run -d -p 5000:80 nginx
```

Docker cannot bind the new container to host port `5000`.

The important point is that the conflict is with the **host port**, not with container port `80`.

Conceptually:

```text
Host port 5000
      │
      ├── Container 2
      │
      └── Container 3
```

Both cannot claim the same host port in this configuration.

However, this is perfectly valid:

```text
Host 8080 → Container 1:80

Host 5000 → Container 2:80
```

because the host ports are different.

---

# 10. Stopping One Container

I stopped one of the Nginx containers while leaving the other running.

The result was:

```text
localhost:8080 → unavailable

localhost:5000 → still available
```

This demonstrated that the two containers were independently running.

Stopping one container did not stop the other.

This helped reinforce the relationship:

```text
Host port
    ↓
Specific container
    ↓
Application
```

---

# 11. Useful Docker Commands Learned

### Check running containers

```powershell
docker ps
```

### Check all containers

```powershell
docker ps -a
```

### Start a container

```powershell
docker start <container_id>
```

### Stop a container

```powershell
docker stop <container_id>
```

### View container logs

```powershell
docker logs <container_id>
```

### Inspect container configuration

```powershell
docker inspect <container_id>
```

### Run a container

```powershell
docker run -d -p 8080:80 nginx
```

---

# 12. Troubleshooting Approach

The most important lesson from Day 1 was not a specific Docker command.

It was the troubleshooting process.

When the observed behavior does not match the expected behavior, I should not assume the system is wrong or blindly repeat commands.

Instead:

```text
1. Predict
      ↓
2. Run the experiment
      ↓
3. Observe actual behavior
      ↓
4. Inspect the system
      ↓
5. Form a hypothesis
      ↓
6. Test the hypothesis
      ↓
7. Fix the problem
      ↓
8. Document the result
```

This is a mindset I want to carry forward into DevOps.

---

# 13. Key Lessons From Day 1

### Lesson 1

An **image is not a container**.

An image is used to create containers.

### Lesson 2

A container can exist without currently running.

```text
Running ≠ Existing
```

### Lesson 3

Docker port mappings follow:

```text
HOST_PORT:CONTAINER_PORT
```

### Lesson 4

Multiple containers can use the same internal port.

For example:

```text
8080 → Container A:80
5000 → Container B:80
```

### Lesson 5

The host port is what creates the port-binding conflict in this scenario.

### Lesson 6

Stopping one container does not automatically stop another independent container.

### Lesson 7

The best way for me to learn DevOps is through experimentation and troubleshooting rather than memorizing commands.

---

# 14. Day 1 Reflection

At the beginning of the session, I had some prior knowledge of Docker and Linux commands, but several concepts were mixed together.

The biggest improvement was understanding Docker port mapping through actual experimentation.

Instead of simply memorizing:

```text
-p HOST_PORT:CONTAINER_PORT
```

I tested multiple containers and observed:

```text
localhost:8080 → Nginx container 1

localhost:5000 → Nginx container 2
```

I also intentionally tested what happens when the same host port is requested twice.

This made the concept much easier to understand than simply reading the definition.

---

# 15. Current Mental Model

My current simplified model of Docker is:

```text
Docker Image
     │
     │ create
     ▼
Docker Container
     │
     ├── Running
     │
     └── Stopped
     
Host Machine
     │
     │ port mapping
     ▼
Host Port ─────────→ Container Port
   8080                  80
   5000                  80
```

The key relationship is:

```text
-p HOST_PORT:CONTAINER_PORT
```

---

## Day 1 Status

**Completed**

* [x] Docker installed
* [x] `hello-world` container executed
* [x] Nginx container deployed
* [x] Images and containers investigated
* [x] Running and stopped containers observed
* [x] Port mapping tested
* [x] Multiple containers tested
* [x] Port conflict investigated
* [x] Container independence tested
* [x] Troubleshooting performed
* [x] Initial Docker mental model established

**Next:** Continue to Docker fundamentals and move from individual containers toward containerized applications and Dockerfiles.
