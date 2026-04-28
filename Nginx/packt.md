# NGINX HTTP Server

## Installing NGINX: A Complete Beginner-Friendly Guide

## Overview

NGINX (pronounced "Engine-X") is one of the world's most popular web servers, known for its high performance, scalability, and security. Originally released in 2004, it was designed to handle heavy web traffic more efficiently than traditional web servers.

Setting up NGINX correctly is the first step toward building a reliable, secure, and scalable web infrastructure.

By the end of this section, you will be able to:

* Install NGINX using your operating system's package manager
* Install NGINX from official NGINX repositories
* Prepare your system for compiling NGINX from source
* Understand the required dependencies
* Configure NGINX to start automatically at boot
* Choose the best installation method for your needs

---

# Installation Methods

There are three main ways to install NGINX:

1. **Using your operating system's default package manager** (recommended for most users)
2. **Using official NGINX repositories** (recommended for newer versions)
3. **Compiling from source** (recommended for advanced customization)

---

# Method 1: Install via Package Manager

This is the simplest and fastest installation method.

## For Red Hat / CentOS / Rocky Linux / AlmaLinux

First, enable the EPEL repository:

```bash
sudo yum install epel-release
```

Search for available NGINX packages:

```bash
sudo yum search nginx
```

View package details:

```bash
sudo yum info nginx
```

Install NGINX:

```bash
sudo yum install nginx
```

---

## For Debian / Ubuntu

Search available packages:

```bash
apt-cache search nginx
```

View package information:

```bash
apt-cache show nginx
```

Install NGINX:

```bash
sudo apt update
sudo apt install nginx
```

---

# Method 2: Install from Official NGINX Repositories

Use this method if your distribution provides an outdated version.

## Red Hat / CentOS

Create the repository file:

```bash
sudo nano /etc/yum.repos.d/nginx.repo
```

Add the following content:

```ini
[nginx]
name=nginx repo
baseurl=http://nginx.org/packages/centos/$releasever/$basearch/
gpgcheck=0
enabled=1
```

For RHEL, replace `centos` with `rhel`.

Install NGINX:

```bash
sudo yum install nginx
```

---

## Debian

Download the signing key:

```bash
wget http://nginx.org/keys/nginx_signing.key
sudo apt-key add nginx_signing.key
```

Add the repository to `/etc/apt/sources.list`:

```bash
deb http://nginx.org/packages/debian/ bookworm nginx
deb-src http://nginx.org/packages/debian/ bookworm nginx
```

Replace `bookworm` with your Debian codename if necessary.

Install NGINX:

```bash
sudo apt update
sudo apt install nginx
```

---

## Ubuntu

Add these lines to `/etc/apt/sources.list`:

```bash
deb http://nginx.org/packages/ubuntu/ noble nginx
deb-src http://nginx.org/packages/ubuntu/ noble nginx
```

Replace `noble` with your Ubuntu version codename (`focal`, `bionic`, etc.).

Install:

```bash
sudo apt update
sudo apt install nginx
```

---

# Method 3: Compile NGINX from Source

Compiling from source gives you:

* Maximum flexibility
* Access to the latest features
* Custom module selection
* Optimized builds for specific environments

Best for:

* Advanced users
* Custom deployments
* Performance tuning
* Embedded systems

---

# Required Build Dependencies

Before compiling NGINX, install the following tools and libraries.

---

## 1. GCC (GNU Compiler Collection)

### Verify Installation

```bash
gcc --version
```

If GCC is not installed:

### On Red Hat-based Systems

```bash
sudo yum groupinstall "Development Tools"
```

### On Debian/Ubuntu

```bash
sudo apt install build-essential
```

---

## 2. PCRE Library

Required for regular expression support (used by rewrite rules).

### Red Hat-based Systems

```bash
sudo yum install pcre pcre-devel
```

### Debian/Ubuntu

```bash
sudo apt install libpcre3 libpcre3-dev
```

---

## 3. zlib Library

Required for gzip compression support.

### Red Hat-based Systems

```bash
sudo yum install zlib zlib-devel
```

### Debian/Ubuntu

```bash
sudo apt install zlib1g zlib1g-dev
```

---

## 4. OpenSSL Library

Required for HTTPS and TLS support.

### Red Hat-based Systems

```bash
sudo yum install openssl openssl-devel
```

### Debian/Ubuntu

```bash
sudo apt install openssl libssl-dev
```

---

# Why These Dependencies Matter

| Dependency | Purpose                                        |
| ---------- | ---------------------------------------------- |
| GCC        | Compiles NGINX source code                     |
| PCRE       | Supports regular expressions and URL rewriting |
| zlib       | Enables gzip compression                       |
| OpenSSL    | Provides HTTPS/TLS encryption                  |

---

# Next Steps After Installation

Once NGINX is installed, you should:

1. Start the NGINX service
2. Enable it to start at boot
3. Verify it is running

## Using systemd

```bash
sudo systemctl start nginx
sudo systemctl enable nginx
sudo systemctl status nginx
```

---

# Verify Installation

Open a browser and visit:

```text
http://your-server-ip
```

You should see the default NGINX welcome page.

You can also test from the command line:

```bash
curl http://localhost
```

---

# Which Installation Method Should You Choose?

| Scenario                | Recommended Method        |
| ----------------------- | ------------------------- |
| Quick setup             | OS package manager        |
| Latest stable version   | Official NGINX repository |
| Custom modules/features | Compile from source       |

---

# Key Takeaways

* Package manager installation is the easiest option.
* Official repositories provide newer, better-maintained versions.
* Compiling from source offers the greatest flexibility.
* Essential dependencies include GCC, PCRE, zlib, and OpenSSL.
* Always enable NGINX to start automatically on boot.

---

# Summary

A proper NGINX installation lays the groundwork for a stable, high-performance web server. Whether you choose a simple package installation or a fully customized source build, understanding the installation process ensures you can deploy and manage NGINX confidently.

In the next section, you'll learn how to configure NGINX, manage virtual hosts, and optimize it for production workloads.

---