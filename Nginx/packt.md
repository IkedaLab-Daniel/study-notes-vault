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

# Basic NGINX Configuration

## Overview

Now that NGINX is installed, the next step is learning how to configure it. NGINX uses a clean, modular configuration system that is both powerful and relatively easy to understand.

In this section, you will learn:

* How NGINX configuration files are structured
* The syntax used in configuration files
* How directives and blocks work
* How configuration files can include other files
* How to test your configuration for errors

A solid understanding of these basics is essential before moving on to advanced topics such as virtual hosts, reverse proxying, load balancing, and SSL/TLS.

---

# Where Is the Main Configuration File?

The location depends on how NGINX was installed.

## Package Manager Installation

```text id="b2z6wr"
/etc/nginx/nginx.conf
```

## Source Installation (Default)

```text id="n7pnux"
/usr/local/nginx/conf/nginx.conf
```

---

# Understanding NGINX Configuration Syntax

NGINX configuration files are made up of:

* **Directives**
* **Blocks (contexts)**
* **Comments**
* **Include statements**

---

# 1. Directives

A directive is a configuration instruction.

### Syntax

```nginx id="lyx2sp"
directive_name value;
```

Every directive:

* Begins with a directive name
* Followed by one or more values
* Ends with a semicolon (`;`)

### Example

```nginx id="oz8k77"
worker_processes 1;
```

This tells NGINX to run with one worker process.

---

# 2. Comments

Comments are ignored by NGINX and are used for documentation.

### Syntax

```nginx id="zh9yjv"
# This is a comment
```

You can place comments:

* On their own line
* After a directive

### Example

```nginx id="vb8v8t"
worker_processes 4;  # Number of worker processes
```

---

# 3. Blocks (Contexts)

Blocks group related directives together.

### Syntax

```nginx id="ojc3g4"
context_name {
    directive value;
}
```

### Example

```nginx id="ok9ajx"
events {
    worker_connections 1024;
}
```

The `events` block contains settings related to connection handling.

---

# Common Top-Level Contexts

| Context    | Purpose                           |
| ---------- | --------------------------------- |
| `main`     | Global settings                   |
| `events`   | Connection processing             |
| `http`     | HTTP server settings              |
| `server`   | Virtual host configuration        |
| `location` | URL matching and request handling |

---

# Example Basic Configuration Structure

```nginx id="7xg2kr"
user nginx;
worker_processes auto;

events {
    worker_connections 1024;
}

http {
    include       mime.types;
    default_type  application/octet-stream;

    server {
        listen 80;
        server_name localhost;

        location / {
            root   /usr/share/nginx/html;
            index  index.html index.htm;
        }
    }
}
```

---

# Important Core Directives

## `worker_processes`

Determines how many worker processes NGINX will use.

```nginx id="e9l6j7"
worker_processes auto;
```

Using `auto` allows NGINX to match the number of CPU cores automatically.

---

## `user`

Specifies which system user runs worker processes.

```nginx id="z4izkq"
user nginx;
```

---

## `pid`

Defines the location of the process ID file.

```nginx id="x5ldfx"
pid /run/nginx.pid;
```

---

## `error_log`

Specifies where error logs are written.

```nginx id="ehgxy0"
error_log /var/log/nginx/error.log;
```

---

# The `include` Directive

The `include` directive inserts the contents of another file into the current configuration.

### Example

```nginx id="m7uww2"
include mime.types;
```

This imports MIME type definitions.

---

# Why Use Include Files?

Benefits include:

* Better organization
* Easier maintenance
* Modular configuration
* Separation of concerns
* Simpler troubleshooting

---

# Example of File Inclusion

## Main Configuration

```nginx id="63b9dj"
user nginx;
worker_processes auto;
include other_settings.conf;
```

## Included File (`other_settings.conf`)

```nginx id="80t7yo"
error_log /var/log/nginx/error.log;
pid /run/nginx.pid;
```

NGINX processes this as if all content were in one file.

---

# Wildcard Includes

NGINX supports file globbing.

```nginx id="knk5gk"
include /etc/nginx/conf.d/*.conf;
```

This includes all `.conf` files in the specified directory.

This is commonly used for:

* Virtual hosts
* Site-specific configurations
* Modular service definitions

---

# Common Included Files

| File              | Purpose                               |
| ----------------- | ------------------------------------- |
| `mime.types`      | MIME type mappings                    |
| `fastcgi.conf`    | FastCGI settings                      |
| `proxy.conf`      | Reverse proxy settings                |
| `conf.d/*.conf`   | Additional configurations             |
| `sites-enabled/*` | Enabled virtual hosts (Debian/Ubuntu) |

---

# Configuration Testing

Always test your configuration before reloading or restarting NGINX.

```bash id="iydx6r"
sudo nginx -t
```

Successful output:

```text id="o3i8ly"
nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
nginx: configuration file /etc/nginx/nginx.conf test is successful
```

---

# Common Configuration Errors

## Missing Included File

```text id="a0wlkd"
open() "/etc/nginx/missing.conf" failed
```

This occurs when a referenced file does not exist.

---

# Wildcard Include Behavior

If no files match a wildcard pattern, NGINX does **not** generate an error.

```nginx id="k9m5vn"
include /etc/nginx/sites/*.conf;
```

If the directory is empty, configuration testing still succeeds.

---

# Best Practices

* Keep configuration modular using `include`.
* Use separate files for each site or service.
* Always test configuration changes with `nginx -t`.
* Comment your configuration for clarity.
* Use `worker_processes auto` for most systems.

---

# Recommended Directory Layout

```text id="7a5a14"
/etc/nginx/
├── nginx.conf
├── mime.types
├── conf.d/
│   ├── default.conf
│   └── api.conf
└── sites-enabled/
    ├── example.com.conf
    └── app.example.com.conf
```

---

# Key Takeaways

* NGINX configuration is based on directives and blocks.
* Every directive ends with a semicolon.
* Blocks organize related settings.
* `include` makes configuration modular and manageable.
* Always validate your configuration before applying changes.

---

# Next Steps

With the syntax mastered, you're ready to learn:

* HTTP module configuration
* Virtual host setup
* Reverse proxy configuration
* SSL/TLS implementation
* Performance optimization

Understanding the configuration structure is the foundation for all advanced NGINX administration.

---

# Understanding NGINX Configuration Syntax

NGINX configuration is built around **directives** and **blocks**. Each directive belongs to a specific module, and when that module is enabled, its directives become available.

## Directives and Modules

A directive is a configuration instruction. For example:

```nginx
worker_processes auto;
```

Some directives are simple single-line instructions, while others create blocks.

Modules can also introduce **directive blocks**, which group related settings.

For example:

```nginx
events {
    worker_connections 1024;
}
```

Here:

* `events` is a block directive provided by the Events module.
* `worker_connections` is only valid inside the `events` block.

Trying to place `worker_connections` outside of `events` would cause an error.

---

# The Main Block

The top level of the configuration file is called the **main block**.

Directives placed here affect the entire NGINX server.

Example:

```nginx
user nginx;
worker_processes auto;
error_log /var/log/nginx/error.log;
```

These settings apply globally.

---

# Nested Blocks

NGINX allows blocks to be nested in a logical hierarchy.

A typical structure looks like this:

```nginx
http {
    server {
        listen 80;
        server_name example.com;

        location / {
            root /var/www/html;
            index index.html;
        }
    }
}
```

## Block Hierarchy

* **main**

  * **http**

    * **server**

      * **location**

Each level has a specific purpose:

* `http`: Global HTTP settings
* `server`: Configuration for a virtual host (website)
* `location`: Rules for specific URIs or paths

---

# Example Explained

```nginx
http {
    server {
        listen 80;
        server_name example.com;
        access_log /var/log/nginx/example.com.log;

        location ^~ /admin/ {
            index index.php;
        }
    }
}
```

### What this does:

* Handles HTTP traffic
* Hosts a website for `example.com`
* Listens on port 80
* Logs requests to a custom log file
* Applies special settings for URLs starting with `/admin/`

---

# Configuration Inheritance

Child blocks inherit settings from parent blocks unless explicitly overridden.

Example:

```nginx
server {
    access_log /var/log/nginx/access.log;

    location /admin/ {
        access_log off;
    }
}
```

### Result:

* Logging is enabled for the entire server
* Logging is disabled for `/admin/`

The child block overrides the parent setting.

---

# Directive-Specific Syntax

Each directive has its own syntax rules.

Simple example:

```nginx
root /var/www/html;
```

Complex example:

```nginx
rewrite ^/(.*)\.(png|jpg|gif)$ /image.php?file=$1&format=$2 last;
```

This uses a regular expression to rewrite image requests.

Not all directives are this fancy, but some can get surprisingly spicy.

---

# Size Units

NGINX supports shorthand units for file sizes:

* `k` or `K` = Kilobytes
* `m` or `M` = Megabytes
* `g` or `G` = Gigabytes

These are equivalent:

```nginx
client_max_body_size 2G;
client_max_body_size 2048M;
client_max_body_size 2097152k;
```

---

# Time Units

NGINX also supports shorthand for time values:

* `ms` = Milliseconds
* `s` = Seconds
* `m` = Minutes
* `h` = Hours
* `d` = Days
* `w` = Weeks
* `M` = Months (30 days)
* `y` = Years (365 days)

Examples:

```nginx
client_body_timeout 3m;
client_body_timeout 180s;
client_body_timeout 180;
```

All three are equivalent because the default unit is seconds.

You can also combine units:

```nginx
client_body_timeout 1m30s;
client_body_timeout '1m 30s 500ms';
```

---

# Variables

NGINX provides built-in variables, which always begin with `$`.

Example:

```nginx
log_format main '$pid - $nginx_version - $remote_addr';
```

Common variables include:

* `$remote_addr` – Client IP address
* `$request_uri` – Requested URI
* `$status` – Response status code
* `$host` – Host header
* `$nginx_version` – NGINX version

---

# Important Note About Variables

Not every directive supports variable expansion.

For example:

```nginx
error_log logs/error-$nginx_version.log;
```

This will literally create a file named:

```text
error-$nginx_version.log
```

—not one containing the actual version number.

---

# String Values

Strings can be written in three ways.

## Without quotes

```nginx
root /var/www/html;
```

## With single quotes

```nginx
root '/var/www/my website';
```

## With double quotes

```nginx
root "/var/www/my website";
```

Use quotes when the value contains:

* spaces
* semicolons (`;`)
* curly braces (`{}`)

Alternatively, you can escape special characters with a backslash.

---

# Duplicate Directives

Most directives can only appear once per block.

Invalid:

```nginx
server {
    root /var/www/site1;
    root /var/www/site2;
}
```

This will cause NGINX to reject the configuration.

### Exceptions

Some directives, such as:

* `allow`
* `deny`

can appear multiple times.

---

# Key Takeaways

* NGINX configuration is modular.
* Directives belong to modules.
* Blocks organize configuration hierarchically.
* Child blocks inherit parent settings.
* Each directive has its own syntax.
* Shorthand units simplify size and time values.
* Variables are powerful, but not universally supported.
* Most directives cannot be repeated in the same block.

NGINX configuration may look intimidating at first, but once you understand its block-based structure, it becomes surprisingly elegant—like LEGO for web servers, only with fewer chances of stepping on it.

# NGINX Base Modules: The Foundation of Everything

Before diving into virtual hosts, reverse proxies, or fancy load balancing, it helps to understand the three **base modules** that power every NGINX installation. These modules are always available—you can't disable them during compilation. Think of them as NGINX's built-in operating system.

---

# The Three Base Modules

## 1. Core Module

The **Core module** provides the essential directives that control how NGINX itself runs.

It handles:

* Process management
* Security settings
* Logging
* Worker processes
* User permissions

Examples of core directives:

```nginx
user www-data www-data;
worker_processes auto;
pid /run/nginx.pid;
error_log /var/log/nginx/error.log;
```

---

## 2. Events Module

The **Events module** controls how NGINX handles network connections.

This is where you configure:

* Maximum simultaneous connections
* Event handling method (`epoll`, `kqueue`, etc.)
* Connection acceptance behavior

Example:

```nginx
events {
    worker_connections 1024;
    use epoll;
}
```

---

## 3. Configuration Module

The **Configuration module** provides the `include` directive, which lets you split your configuration into multiple files.

Example:

```nginx
include mime.types;
include sites-enabled/*.conf;
```

This keeps your configuration organized and manageable—because one giant config file is nobody's idea of a good time.

---

# NGINX Process Architecture

NGINX uses a **master-worker architecture**.

## Master Process

* Starts first
* Usually runs as `root`
* Reads the configuration
* Manages worker processes
* Handles signals (reload, restart, upgrade)

Importantly, the master process does **not** handle client requests directly.

## Worker Processes

* Handle all incoming client requests
* Serve content
* Process connections
* Run under a less-privileged user (such as `www-data`)

This design improves both **security** and **performance**.

---

# Typical Process Flow

```text
Master Process (root)
        │
        ├── Worker Process (www-data)
        ├── Worker Process (www-data)
        ├── Worker Process (www-data)
        └── Worker Process (www-data)
```

Each worker can process many connections simultaneously.

---

# Important Core Directives

## `daemon`

Controls whether NGINX runs in the background.

```nginx
daemon on;
```

* `on` (default): Run as a background service
* `off`: Run in the foreground

Useful for debugging:

```nginx
daemon off;
```

---

# Essential Performance Settings

## `user`

Never run workers as `root`.

Bad idea:

```nginx
user root;
```

Recommended:

```nginx
user www-data www-data;
```

This limits damage if something goes wrong.

---

## `worker_processes`

Determines how many worker processes NGINX creates.

Recommended:

```nginx
worker_processes auto;
```

This automatically matches the number of CPU cores.

For example:

* 4 CPU cores → 4 workers
* 8 CPU cores → 8 workers

---

## `worker_priority`

Controls the scheduling priority of worker processes.

```nginx
worker_priority -5;
```

Range:

* `-20` = highest priority
* `19` = lowest priority

Usually, the default (`0`) is perfectly fine.

---

# Events Module Directives

All of these must be placed inside the `events` block.

```nginx
events {
    worker_connections 1024;
}
```

---

## `worker_connections`

Defines the maximum simultaneous connections per worker.

```nginx
worker_connections 1024;
```

Total connection capacity is:

```text
worker_processes × worker_connections
```

Example:

* 4 workers
* 1024 connections each

Total:

```text
4 × 1024 = 4096 simultaneous connections
```

---

## `use`

Selects the event handling method.

```nginx
use epoll;
```

Common options:

* `epoll` – Linux (best choice)
* `kqueue` – FreeBSD/macOS
* `select` – fallback, less efficient
* `poll` – older alternative

Usually, NGINX automatically picks the best option.

---

## `multi_accept`

Controls whether a worker accepts multiple new connections at once.

```nginx
multi_accept on;
```

* `on`: Accept as many as possible
* `off`: Accept one at a time

Default is `off`.

---

## `accept_mutex`

Prevents all workers from trying to accept the same connection simultaneously (the classic "thundering herd" problem).

```nginx
accept_mutex on;
```

Modern systems often work well with the default setting.

---

# Configuration Module: `include`

This directive allows modular configuration.

```nginx
include /etc/nginx/mime.types;
include /etc/nginx/sites-enabled/*.conf;
```

Benefits:

* Cleaner organization
* Easier maintenance
* Separation of concerns
* Simpler troubleshooting

---

# Recommended Initial Configuration

```nginx
user www-data www-data;
worker_processes auto;
pid /run/nginx.pid;

events {
    worker_connections 1024;
}

http {
    include mime.types;
    default_type application/octet-stream;

    sendfile on;
    keepalive_timeout 65;

    server {
        listen 80;
        server_name localhost;

        location / {
            root /usr/share/nginx/html;
            index index.html;
        }
    }
}
```

---

# Testing Your Configuration

Always test before reloading:

```bash
nginx -t
```

If successful, you'll see:

```text
syntax is ok
test is successful
```

Then reload:

```bash
sudo systemctl reload nginx
```

Or:

```bash
sudo nginx -s reload
```

---

# Graceful Binary Upgrade (Zero Downtime)

One of NGINX's coolest tricks is upgrading without dropping connections.

## Steps

1. Replace the old binary.
2. Find the master process PID:

```bash
cat /run/nginx.pid
```

3. Send `USR2`:

```bash
kill -USR2 <pid>
```

4. Gracefully stop old workers:

```bash
kill -WINCH <old_pid>
```

5. After confirming old workers are gone:

```bash
kill -QUIT <old_pid>
```

Boom—zero downtime. Your users won't even notice.

---

# Key Best Practices

* Run workers as a non-root user
* Set `worker_processes auto`
* Tune `worker_connections` based on hardware
* Use `include` for modular configs
* Always test with `nginx -t`
* Use graceful reloads and upgrades

---

## Quick Summary

* **Core module**: Controls NGINX itself
* **Events module**: Controls connection handling
* **Configuration module**: Organizes configuration files

Together, these modules form the backbone of every NGINX server.

Master these, and the rest of NGINX becomes much easier to understand.

# Exploring the HTTP Configuration in NGINX

Now we're getting to the fun part: actually serving websites.

The **HTTP Core Module** is the heart of NGINX's web-serving functionality. It provides the blocks, directives, and variables that make it possible to host websites, route requests, and control how content is delivered.

Without this module, NGINX would be a very efficient... nothing. Fast, but nothing.

---

# The Three Core HTTP Blocks

The HTTP module introduces three essential blocks:

```nginx
http {
    server {
        location / {
            # Configuration here
        }
    }
}
```

Think of them as a hierarchy:

* **http** → Global HTTP settings
* **server** → One website (virtual host)
* **location** → Rules for specific URLs or paths

---

# 1. `http` Block

This is the top-level container for all web-related configuration.

It must appear in the main configuration file.

```nginx
http {
    include mime.types;
    default_type application/octet-stream;
}
```

Typical settings here include:

* MIME types
* Logging formats
* Compression
* Timeouts
* Default behaviors

Anything defined here is inherited by all `server` and `location` blocks unless overridden.

---

# 2. `server` Block

A `server` block defines a **virtual host**—a website.

```nginx
server {
    listen 80;
    server_name example.com www.example.com;
}
```

Each `server` block can represent:

* A domain
* A subdomain
* A specific IP/port combination

You can host multiple websites on a single NGINX server using multiple server blocks.

---

# 3. `location` Block

A `location` block applies rules to specific URIs.

```nginx
location /images/ {
    root /var/www/assets;
}
```

This lets you customize behavior for:

* Static files
* API routes
* Admin panels
* Downloads
* Proxied applications

You can even nest location blocks in some cases.

---

# Configuration Inheritance

Settings flow downward.

```nginx
http {
    gzip on;

    server {
        location /downloads/ {
            gzip off;
        }
    }
}
```

Result:

* Compression is enabled everywhere
* Except inside `/downloads/`

Child blocks override parent settings.

---

# The `listen` Directive

Defines which IP address and port the server listens on.

```nginx
server {
    listen 80;
}
```

## Common Examples

```nginx
listen 80;
listen 443 ssl;
listen 443 ssl http2;
listen 127.0.0.1:8080;
listen [::]:80;
```

---

# Useful `listen` Options

* `default_server` – Fallback server
* `ssl` – Enable HTTPS
* `http2` – Enable HTTP/2
* `reuseport` – Improve performance under heavy load

Example:

```nginx
listen 443 ssl http2 default_server;
```

---

# The `server_name` Directive

Specifies which hostnames this server block handles.

```nginx
server_name example.com www.example.com;
```

NGINX matches the request's `Host` header against this list.

---

## Wildcards

```nginx
server_name *.example.com;
```

Matches:

* `blog.example.com`
* `shop.example.com`

---

## Combined Root + Subdomains

```nginx
server_name .example.com;
```

Matches both:

* `example.com`
* `www.example.com`
* Any subdomain

Very handy.

---

## Regular Expressions

```nginx
server_name ~^(www)\.example\.com$;
```

Use regex only when necessary—they're more expensive to process.

---

# Default Server Behavior

If no `server_name` matches, NGINX uses:

1. The server block marked with `default_server`
2. Otherwise, the first matching `listen` block

Example:

```nginx
listen 80 default_server;
```

---

# Important HTTP Directives

## `root`

Defines the document root.

```nginx
root /var/www/example.com;
```

This is where NGINX looks for files.

---

## `index`

Specifies default index files.

```nginx
index index.html index.htm index.php;
```

When a directory is requested, NGINX tries these files in order.

---

## `error_page`

Custom error pages.

```nginx
error_page 404 /404.html;
error_page 500 502 503 504 /50x.html;
```

A nice touch for production sites.

---

# Performance-Related Directives

## `sendfile`

Enables zero-copy file transfers.

```nginx
sendfile on;
```

This usually improves performance for static files.

---

## `sendfile_max_chunk`

Limits the amount of data per sendfile call.

```nginx
sendfile_max_chunk 1m;
```

Useful for preventing a single large file transfer from monopolizing a worker.

---

## `reset_timedout_connection`

Frees resources immediately after client timeout.

```nginx
reset_timedout_connection on;
```

Helps reduce memory usage under abusive or broken connections.

---

# A Basic Website Configuration

```nginx
http {
    include mime.types;
    default_type application/octet-stream;

    sendfile on;
    keepalive_timeout 65;

    server {
        listen 80;
        server_name example.com www.example.com;

        root /var/www/example.com;
        index index.html index.htm;

        location / {
            try_files $uri $uri/ =404;
        }
    }
}
```

---

# How Request Matching Works

When a request arrives:

1. NGINX matches the IP and port (`listen`)
2. It checks the `Host` header (`server_name`)
3. It finds the best matching `location`

This three-step process is incredibly fast.

---

# Simple Example

Request:

```text
http://example.com/images/logo.png
```

NGINX will:

* Match `listen 80`
* Match `server_name example.com`
* Match `location /images/` (if present)

Otherwise, it falls back to the best available match.

---

# Why This Matters

These three blocks are the backbone of all NGINX HTTP configuration.

Once you understand them, you can build:

* Static websites
* Reverse proxies
* API gateways
* Load balancers
* SSL-enabled applications
* Multi-domain hosting

---

# Quick Summary

* `http` = Global HTTP settings
* `server` = One website or virtual host
* `location` = Rules for specific URIs

Together, they form NGINX's request-handling pipeline.

Master these, and you're officially speaking fluent NGINX.
