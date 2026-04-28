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

## Summary

A proper NGINX installation lays the groundwork for a stable, high-performance web server. Whether you choose a simple package installation or a fully customized source build, understanding the installation process ensures you can deploy and manage NGINX confidently.

In the next section, you'll learn how to configure NGINX, manage virtual hosts, and optimize it for production workloads.

---

# Downloading and Compiling the NGINX Source Code

## Overview

Compiling NGINX from source gives you full control over your installation. You can:

* Use the latest NGINX release
* Enable only the modules you need
* Optimize performance for your environment
* Include third-party modules
* Build a lightweight, custom web server

This approach is ideal for advanced users, production environments with specific requirements, and systems where maximum performance or customization is important.

---

## NGINX Resources and Community

Before compiling, it's helpful to know where to find documentation, support, and updates.

## Official Resources

* NGINX Official Website: [https://nginx.org](https://nginx.org)
* Official Documentation
* Source Code Downloads
* Release Notes and Changelogs

## Additional Learning Resources

* NGINX Documentation Wiki
* Community Forums
* Mailing Lists
* IRC Channel: `#nginx` on Libera.Chat

These resources are invaluable when troubleshooting or learning advanced configurations.

---

## Understanding NGINX Version Branches

NGINX offers three release branches:

## 1. Mainline Version (Recommended for Most Users)

* Latest features
* Latest bug fixes
* Actively developed
* Production-ready for most environments

Despite being the newest branch, mainline releases are highly stable and widely used in production.

## 2. Stable Version

* Receives critical bug fixes only
* More conservative release cycle
* Preferred by organizations prioritizing maximum stability

## 3. Legacy Versions

* Older releases
* Maintained primarily for compatibility
* Generally not recommended for new deployments

---

## Which Version Should You Choose?

| Use Case                   | Recommended Version |
| -------------------------- | ------------------- |
| New deployments            | Mainline            |
| Enterprise environments    | Stable              |
| Legacy application support | Legacy              |

For most modern deployments, **mainline** is the best choice.

---

# Key NGINX Features

NGINX is far more than just a web server.

## Core Web Features

* High-performance static file serving
* Reverse proxying
* Load balancing
* HTTP caching
* Gzip compression
* SSL/TLS termination
* HTTP/2 and HTTP/3 support
* Fault tolerance
* Auto indexing
* Connection multiplexing

## Application Gateway Support

* FastCGI
* uWSGI
* SCGI
* Memcached

## Additional Capabilities

* Mail proxy (IMAP, POP3, SMTP)
* Stream proxying (TCP/UDP)
* Image transformation
* SSI (Server Side Includes)
* XSLT filtering

---

# Downloading NGINX Source Code

First, create a working directory:

```bash
mkdir -p ~/src
cd ~/src
```

Download the desired version from the official website.

For example:

```bash
wget https://nginx.org/download/nginx-1.25.2.tar.gz
```

> Replace the version number with the latest available release.

---

## Extracting the Source Code

Once downloaded, extract the archive:

```bash
tar -zxf nginx-1.25.2.tar.gz
```

This creates a new directory containing the NGINX source files.

Move into the extracted directory:

```bash
cd nginx-1.25.2
```

---

## Verifying the Download

You can confirm the contents with:

```bash
ls
```

You should see directories such as:

* `auto`
* `conf`
* `contrib`
* `html`
* `man`
* `src`

These contain the build scripts, default configuration files, documentation, and source code.

---

## Why Compile from Source?

Compiling from source allows you to:

* Select specific modules
* Exclude unnecessary features
* Improve security by minimizing attack surface
* Optimize binaries for your hardware
* Integrate third-party modules

This is especially useful for:

* High-performance production servers
* Embedded systems
* Specialized reverse proxies
* Security-hardened deployments

---

## Next Step: Configure the Build

After extraction, the next phase is configuring the build options.

Typical configuration includes:

* Installation path
* Enabled modules
* SSL support
* Compression support
* User and group settings
* Logging locations

A common example:

```bash
./configure \
  --prefix=/etc/nginx \
  --sbin-path=/usr/sbin/nginx \
  --conf-path=/etc/nginx/nginx.conf \
  --pid-path=/var/run/nginx.pid \
  --with-http_ssl_module \
  --with-http_v2_module \
  --with-http_gzip_static_module
```

---

## Build and Install

After configuration:

```bash
make
sudo make install
```

This compiles and installs NGINX using your selected options.

---

## Verify Installation

Check the installed version:

```bash
nginx -v
```

For detailed build information:

```bash
nginx -V
```

This shows:

* Version number
* Compiler used
* Enabled modules
* Configuration arguments

---

## Best Practices

* Always download from the official NGINX website.
* Prefer the mainline release unless strict stability requirements exist.
* Keep track of your compile options for future upgrades.
* Regularly update source installations for security patches.
* Test configurations before deploying to production.

---

## Summary

Compiling NGINX from source gives you maximum flexibility, performance, and control. The process involves:

1. Selecting the appropriate version
2. Downloading the source archive
3. Extracting the files
4. Configuring build options
5. Compiling and installing

This approach is perfect for administrators who need a customized, optimized NGINX installation tailored to their exact requirements.

---

# Configuring NGINX Before Compilation

## Overview

When building NGINX from source, there are three standard steps:

1. **Configure**
2. **Compile**
3. **Install**

Of these, the **configuration step is the most important**. It determines:

* Which modules are included
* Where files are installed
* Which libraries are used
* How NGINX behaves at runtime

Once compiled, these options cannot be changed without rebuilding NGINX.

---

## The Three Build Steps

## 1. Configure

The `configure` script examines your system and prepares the build environment.

```bash id="9gzj6h"
./configure
```

It checks for:

* Compiler availability
* Required libraries
* Optional dependencies
* System compatibility

---

## 2. Compile

```bash id="epj5f9"
make
```

This compiles the NGINX source code into executable binaries.

---

## 3. Install

```bash id="6yq1zr"
sudo make install
```

By default, NGINX is installed to:

```text id="h8b2g0"
/usr/local/nginx
```

---

## The Easy Way

If you want a quick installation using default settings, simply run:

```bash id="5i4o6x"
./configure
make
sudo make install
```

This creates a working NGINX installation with standard modules and default paths.

Good for:

* Testing
* Learning
* Development environments
* Quick prototypes

Not ideal for:

* Production deployments
* Custom module requirements
* Standardized system integration

---

## Why Configuration Matters

Skipping customization may result in:

* Missing required modules
* Incorrect file locations
* Inconvenient log paths
* Limited functionality
* Difficult maintenance later

Think of `./configure` as choosing the blueprint before building the house.

---

## Viewing Available Configuration Options

Each NGINX version may support different options.

To list all available switches:

```bash id="krkk2i"
./configure --help
```

This command displays every configurable option supported by your specific NGINX version.

---

## Common Path Configuration Options

Path options allow you to control where NGINX stores its files.

## Example

```bash id="syv8hx"
./configure --conf-path=/etc/nginx/nginx.conf
```

This tells NGINX to use:

```text id="k3mkku"
/etc/nginx/nginx.conf
```

as its main configuration file.

---

## Commonly Customized Paths

| Option             | Purpose                     |
| ------------------ | --------------------------- |
| `--prefix`         | Installation root directory |
| `--sbin-path`      | NGINX executable location   |
| `--conf-path`      | Main configuration file     |
| `--error-log-path` | Error log file              |
| `--http-log-path`  | Access log file             |
| `--pid-path`       | Process ID file             |
| `--lock-path`      | Lock file                   |
| `--modules-path`   | Dynamic modules directory   |

---

## Recommended Production Configuration

A typical production-ready configuration might look like:

```bash id="7h5yl8"
./configure \
  --prefix=/etc/nginx \
  --sbin-path=/usr/sbin/nginx \
  --modules-path=/usr/lib/nginx/modules \
  --conf-path=/etc/nginx/nginx.conf \
  --error-log-path=/var/log/nginx/error.log \
  --http-log-path=/var/log/nginx/access.log \
  --pid-path=/var/run/nginx.pid \
  --lock-path=/var/run/nginx.lock \
  --with-http_ssl_module \
  --with-http_v2_module \
  --with-http_gzip_static_module
```

This layout closely matches packages provided by major Linux distributions.

---

## Troubleshooting Configuration Errors

If `./configure` fails, don't panic—it's usually one of a few common issues.

## Step 1: Check the Error Log

```bash id="7aq60p"
cat objs/autoconf.err
```

This file contains detailed diagnostic information.

---

## Common Causes of Failure

## Missing Prerequisites

Ensure these are installed:

* GCC
* PCRE and development headers
* zlib and development headers
* OpenSSL and development headers

Optional modules may require:

* LibXML2
* LibXSLT
* GeoIP libraries

---

## Required Core Dependencies

| Dependency | Required For                          |
| ---------- | ------------------------------------- |
| GCC        | Compilation                           |
| PCRE       | Regular expressions and rewrite rules |
| zlib       | Gzip compression                      |
| OpenSSL    | HTTPS/TLS support                     |

---

## Specifying Library Paths Manually

If the configure script cannot locate a library, specify its path explicitly.

## Example: OpenSSL

```bash id="ca7pw4"
./configure --with-openssl=/usr/lib64
```

This tells NGINX where to find the OpenSSL source or library files.

---

## File and Directory Permissions

Before running `configure`, verify:

* Source directory is readable
* Build directory is writable
* Installation target directories exist
* You have sufficient permissions

Check permissions:

```bash id="gjdq56"
ls -ld .
```

If necessary:

```bash id="4fey53"
chmod -R u+rw .
```

---

## Best Practices

* Always review `./configure --help` before building.
* Use explicit paths for production installations.
* Match package-manager directory layouts when possible.
* Keep a copy of your configure command for future upgrades.
* Review `objs/autoconf.err` when errors occur.

---

## Example Full Build Process

```bash id="3zjrbv"
./configure \
  --prefix=/etc/nginx \
  --sbin-path=/usr/sbin/nginx \
  --conf-path=/etc/nginx/nginx.conf \
  --with-http_ssl_module \
  --with-http_v2_module

make
sudo make install
```

---

## Verify the Build

After installation:

```bash id="9ah9hy"
nginx -V
```

This displays:

* NGINX version
* Compiler version
* Enabled modules
* Full configure arguments

---

## Key Takeaways

* Configuration is the most critical build step.
* Default settings are fine for testing, but not ideal for production.
* Use `./configure --help` to explore all available options.
* Missing dependencies are the most common cause of errors.
* `objs/autoconf.err` is your best troubleshooting resource.
* Save your configure command for future upgrades and consistency.

---

## Summary

The `configure` step determines exactly how NGINX will be built and installed. Taking the time to configure NGINX properly ensures:

* Better performance
* Cleaner system integration
* Required module availability
* Easier maintenance
* Fewer surprises later

A carefully configured build is the foundation of a reliable NGINX deployment.
