## Example: Shared Development Environment

There are two developers, **Sarah** and **John**, working in a shared development environment.

Both developers pull, modify, commit, and push code to the same shared environment.

One day, **John updates a library** and pushes his changes to the shared environment.

Sarah then pulls the latest changes.

Suddenly, **Sarah's application stops working**.

The library update may have introduced an **incompatibility** or a **version mismatch** with Sarah's code or dependencies.

```text
John
  ↓
Updates Library
  ↓
Pushes Changes
  ↓
Shared Environment
  ↓
Sarah Pulls Changes
  ↓
💥 Application Breaks
```

## Example: Containers and Consistent Environments

Sarah has a **container** containing the application code, dependencies, libraries, and required environment configuration.

She pushes the container image to a **shared container registry**.

John pulls the same image and runs it in his environment.

Now, both developers are working with the **same application environment**.

If John updates the application or its dependencies, he can build a **new version of the container image** and push it to the shared registry.

When Sarah pulls the new image, she gets the **same updated code, dependencies, and environment** that John built.

```text
Sarah
  ↓
Code + Dependencies + Environment
  ↓
Build Container Image
  ↓
Shared Container Registry
  ↓
John pulls the same image
  ↓
Same Environment
```

Instead of everyone manually configuring their own environment, the **container image acts as a consistent, reproducible package** for the application.

## What is Docker?

**Docker** is an open-source platform that allows you to **build, deploy, scale, and manage applications using containers**.

### What is Containerization?

**Containerization** is a lightweight technology that packages an application together with everything it needs to run, such as:

* Application code
* Dependencies
* Libraries
* Configuration
* Required runtime components

This package can then run consistently across different environments.

> **Think of a container as a standardized package that contains the application and its required environment.**

### What Can a Container Contain?

A container can contain:

* Application code
* Runtime
* Libraries
* System tools
* Dependencies
* Configuration

This helps ensure **consistency across different developers and environments**.

## Containers vs Virtual Machines

### Virtual Machines (VMs)

A **virtual machine** acts like a separate computer running inside a physical computer.

Each VM behaves like an independent computer with its own:

* Operating system
* Applications
* Libraries
* Resources

VMs are created and managed using **virtualization software**, such as **Oracle VirtualBox** or **VMware**.

```text
Physical Computer
│
├── VM 1 → Guest OS + Application
│
├── VM 2 → Guest OS + Application
│
└── VM 3 → Guest OS + Application
```

Each VM includes a **full guest operating system**, which makes VMs generally heavier than containers.
