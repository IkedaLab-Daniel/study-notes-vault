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

---

# `alias`

Used **inside a `location` block only**. It maps a URL path to a completely different directory on disk.

```nginx
location /admin/ {
    alias /var/www/locked/;
}
```

* Request: `/admin/report.html`
* File served: `/var/www/locked/report.html`

Notice that `/admin/` is replaced entirely by the alias path.

### Important

* `alias` should usually end with a trailing slash when mapping directories.
* It differs from `root`.

With `root`:

```nginx
location /admin/ {
    root /var/www;
}
```

Request `/admin/report.html` becomes:
`/var/www/admin/report.html`

With `alias`:
`/var/www/locked/report.html`

Think of it this way: `root` appends; `alias` replaces.

---

## `error_page`

Defines custom pages or actions for HTTP errors.

```nginx
error_page 404 /not_found.html;
error_page 500 502 503 504 /50x.html;
```

You can also:

* Redirect elsewhere
* Jump to a named location
* Change the response code

```nginx
error_page 404 =200 /index.html;
```

This is commonly used in Single Page Applications so client-side routing works.

---

## `if_modified_since`

Controls how NGINX handles the `If-Modified-Since` request header.

```nginx
if_modified_since exact;
```

Possible values:

* `off` – ignore the header
* `exact` – only return `304 Not Modified` if timestamps match exactly
* `before` – return `304` if the file has not changed since that time

Default:

```nginx
if_modified_since exact;
```

Useful for browser caching and reducing bandwidth.

---

## `index`

Specifies the default file served when a directory is requested.

```nginx
index index.php index.html;
```

If someone visits:

```text
https://example.com/
```

NGINX looks for:

1. `index.php`
2. `index.html`

and serves the first one it finds.

---

## `recursive_error_pages`

Allows error pages themselves to trigger other error pages.

```nginx
recursive_error_pages on;
```

Normally off. Mostly useful in advanced custom error handling setups.

---

## `try_files`

One of the most useful directives. It checks for files in order and serves the first one found.

```nginx
location / {
    try_files $uri $uri/ /index.html;
}
```

How it works:

1. Try exact file (`$uri`)
2. Try directory (`$uri/`)
3. Fallback to `/index.html`

This is the standard setup for React, Vue, and other SPAs.

### Example for reverse proxy fallback

```nginx
location / {
    try_files $uri $uri.html $uri.xml @backend;
}
```

If none exist, request is passed to `@backend`.

### Security warning

Never do this:

```nginx
try_files $uri $uri.php @backend;
```

That can accidentally expose PHP source code. A spectacularly bad surprise.

---

# Connection Handling Directives

## `keepalive_requests`

Maximum number of requests allowed on one persistent connection.

```nginx
keepalive_requests 100;
```

Default: `100`

---

## `keepalive_timeout`

How long to keep an idle connection open.

```nginx
keepalive_timeout 75;
```

Or:

```nginx
keepalive_timeout 75 60;
```

* First value: server timeout
* Second value: sent to client in the `Keep-Alive` header

---

## `keepalive_disable`

Disable keepalive for certain browsers.

```nginx
keepalive_disable msie6;
```

Default is already `msie6` because, well, Internet Explorer liked to keep life interesting.

---

## `send_timeout`

Closes a connection if the client stops receiving data.

```nginx
send_timeout 60;
```

Default: `60s`

---

# Request Body Handling

## `client_body_in_file_only`

Stores incoming request bodies (such as POST data) in files.

```nginx
client_body_in_file_only clean;
```

Options:

* `off` – default
* `clean` – store temporarily, then delete
* `on` – store permanently (mainly for debugging)

Use `on` cautiously, unless you enjoy mystery files multiplying.

---

## `client_body_in_single_buffer`

Stores the entire request body in one memory buffer.

```nginx
client_body_in_single_buffer on;
```

Useful for some performance optimizations or modules that prefer contiguous data.

Default:

```nginx
off
```

---

# Quick Practical Example

```nginx
server {
    listen 80;
    server_name example.com;
    root /var/www/example;

    index index.php index.html;

    location / {
        try_files $uri $uri/ /index.html;
    }

    location /admin/ {
        alias /var/www/admin-panel/;
    }

    error_page 404 /404.html;

    keepalive_timeout 65;
    send_timeout 60;
}
```

This setup:

* Serves files from `/var/www/example`
* Falls back to `index.html` for SPA routes
* Maps `/admin/` to a separate directory
* Uses a custom 404 page
* Optimizes connection handling

---

# Request Body Handling

## `client_body_buffer_size`

Sets how much of the request body NGINX keeps in memory before spilling over to disk.

```nginx
client_body_buffer_size 16k;
```

* Small uploads stay in RAM (faster).
* Larger uploads are written to temporary files.

Default:

* `8k` on 32-bit systems
* `16k` on 64-bit systems

### When to adjust

* Increase for APIs receiving medium-sized JSON payloads.
* Leave default unless you have a specific reason.

---

## `client_body_temp_path`

Defines where temporary uploaded request bodies are stored.

```nginx
client_body_temp_path /var/cache/nginx/client_temp;
```

You can also create a hashed directory structure:

```nginx
client_body_temp_path /var/cache/nginx/client_temp 1 2;
```

This creates nested folders, which helps performance when handling many temporary files.

Example layout:

```text
/var/cache/nginx/client_temp/a/3f/
```

Very handy for high-traffic upload systems.

---

## `client_body_timeout`

How long NGINX waits while reading the request body.

```nginx
client_body_timeout 60s;
```

If the client stops sending data for longer than this, NGINX returns:

```text
408 Request Timeout
```

Useful for defending against slow upload attacks.

---

# Request Header Handling

## `client_header_buffer_size`

Initial buffer size for request headers.

```nginx
client_header_buffer_size 2k;
```

Default: `1k`

This stores:

* HTTP headers
* Cookies
* Request line

If headers exceed this, NGINX uses larger fallback buffers.

---

## `large_client_header_buffers`

Number and size of extra header buffers.

```nginx
large_client_header_buffers 4 8k;
```

Meaning:

* Up to 4 large buffers
* Each buffer is 8 KB

### Important limits

* Request URI too large → `414 Request-URI Too Large`
* Header line too large → `400 Bad Request`

This is especially useful for:

* Applications with large cookies
* Complex authentication tokens (JWTs)
* Long URLs

---

## `client_header_timeout`

How long NGINX waits for request headers.

```nginx
client_header_timeout 60s;
```

If the client pauses too long while sending headers:

```text
408 Request Timeout
```

A nice little shield against slowloris-style attacks.

---

# Upload Limits

## `client_max_body_size`

Maximum allowed request body size.

```nginx
client_max_body_size 50m;
```

If exceeded:

```text
413 Request Entity Too Large
```

### Common values

* File uploads: `50m`, `100m`, or higher
* APIs with JSON only: `1m` to `10m`

Default: `1m`

This is one of the first settings you'll tweak for upload features.

---

# Connection Closing Behavior

## `lingering_close`

Controls how NGINX closes connections after a response.

```nginx
lingering_close on;
```

Options:

* `on` (default) – wait briefly for extra client data
* `off` – close immediately
* `always` – always linger before closing

Usually, keep the default.

---

## `lingering_time`

Maximum total time spent reading leftover client data.

```nginx
lingering_time 30s;
```

Default: `30s`

---

## `lingering_timeout`

Maximum pause between reads while lingering.

```nginx
lingering_timeout 5s;
```

Default: `5s`

Together, these directives help NGINX shut connections gracefully without abruptly cutting off clients.

---

# Header Validation

## `ignore_invalid_headers`

Controls whether malformed headers are ignored.

```nginx
ignore_invalid_headers on;
```

* `on` (default): invalid headers are ignored
* `off`: malformed headers trigger errors

Best practice: leave it `on`.

---

# Transfer Encoding

## `chunked_transfer_encoding`

Enables HTTP/1.1 chunked responses.

```nginx
chunked_transfer_encoding on;
```

Default: `on`

This allows NGINX to send data in chunks when the total size isn't known upfront.

Turn it off only for compatibility with very old or broken clients.

---

# Partial Content Requests

## `max_ranges`

Limits the number of byte ranges allowed in a single request.

```nginx
max_ranges 5;
```

* `0` = disable range requests entirely
* unset = unlimited

Useful for mitigating certain abuse patterns involving excessive range requests.

---

# MIME Type Handling

## `types`

Maps file extensions to MIME types.

```nginx
types {
    text/html  html;
    text/css   css;
    application/javascript js;
}
```

Usually, you simply include the standard file:

```nginx
include mime.types;
```

This gives NGINX a full list of common file types.

---

## `default_type`

Used when no matching file extension is found.

```nginx
default_type application/octet-stream;
```

Default:

```nginx
default_type text/plain;
```

### Common use case: force downloads

```nginx
location /downloads/ {
    types { }
    default_type application/octet-stream;
    add_header Content-Disposition 'attachment';
}
```

This tells browsers:
"Don't try to display this—just download it."

---

# Practical Example

```nginx
server {
    listen 80;
    server_name example.com;

    client_max_body_size 50m;
    client_body_buffer_size 16k;
    client_body_timeout 60s;

    client_header_buffer_size 2k;
    large_client_header_buffers 4 8k;
    client_header_timeout 60s;

    lingering_close on;
    lingering_time 30s;
    lingering_timeout 5s;

    include mime.types;
    default_type application/octet-stream;
}
```

This configuration is ideal for:

* File uploads
* API servers
* Modern web applications

---

# 🧾 MIME Types (What the browser *thinks* a file is)

## `default_type`

When NGINX can’t figure out a file’s type, it falls back here:

```nginx id="m1n8qx"
default_type text/plain;
```

### What this really means

If you request something like:

```
/file.unknown
```

NGINX asks:

* “Do I know this extension from `types {}` or `mime.types`?”
* If NO → it uses `default_type`

### Common real-world setting

```nginx id="z7kq3t"
default_type application/octet-stream;
```

👉 This forces unknown files to be treated as “downloadable binary”

So instead of:

* browser trying to display garbage

You get:

* clean download behavior

---

# ⚡ MIME Hash Tables (Performance internals)

NGINX doesn’t search MIME types line-by-line. It uses hash tables.

## `types_hash_max_size`

Controls how big that lookup structure can grow:

```nginx id="h3p9aa"
types_hash_max_size 4096;
```

* Bigger = more entries allowed
* Helps when you have many file types

Default:

* `4k` or `8k` depending on system

👉 You usually only touch this when NGINX literally warns you during startup.

---

## `types_hash_bucket_size`

Controls how data is grouped inside the hash table:

```nginx id="b2v7lm"
types_hash_bucket_size 64;
```

Think of it like:

> how NGINX organizes MIME types for fast lookup

Default:

* `64`

### When it matters

Only change if you see startup warnings like:

> “could not build types_hash, you should increase types_hash_bucket_size”

Otherwise: leave it alone.

---

# 🚫 LIMITING & SECURITY CONTROL

This is where NGINX starts behaving like a gatekeeper.

---

## `limit_except` (HTTP method control)

This is basically:

> “What HTTP methods are allowed here?”

```nginx id="k9x0dd"
location /admin/ {
    limit_except GET {
        deny all;
    }
}
```

### What this means:

* Only `GET` allowed
* `POST`, `PUT`, `DELETE` → blocked

### Why this is powerful

You can lock down:

* admin panels
* APIs
* sensitive endpoints

And optionally allow exceptions:

```nginx id="q8p1zz"
limit_except GET {
    allow 192.168.1.0/24;
    deny all;
}
```

👉 So internal network gets more freedom

---

## `limit_rate` (bandwidth throttling)

```nginx id="r4v7ee"
limit_rate 500k;
```

This limits download speed per connection.

### Important detail:

It’s **per connection**, not per user.

So:

* 2 connections = double speed

---

## `limit_rate_after` (burst then slow down)

```nginx id="t6m2pp"
limit_rate_after 10m;
```

Meaning:

* First 10MB → full speed
* After that → apply `limit_rate`

### Real use case

Good for:

* letting pages load fast
* slowing down large downloads afterward

---

## `satisfy` (security logic mode)

This is a big one.

```nginx id="n8a1ss"
satisfy any;
```

or

```nginx id="c3d9kk"
satisfy all;
```

### Think of it like logic gates:

### `all`

User must pass:

* IP rule AND password

### `any`

User passes if:

* IP rule OR password

### Example scenario

Admin panel:

* internal IPs OR login required

---

## `internal` (hidden routes)

```nginx id="u2w5qq"
location /admin/ {
    internal;
}
```

### What it does:

* Blocks direct browser access
* Only allows internal redirects

So users can’t just type:

```
/admin/
```

But NGINX can still route there internally via:

* `rewrite`
* `try_files`
* backend logic

---

# 📂 FILE SYSTEM BEHAVIOR

---

## `disable_symlinks` (security control)

```nginx id="s1l3yy"
disable_symlinks on;
```

### Why this exists

Symlinks can be abused to:

* escape web root
* expose sensitive files

### Modes:

#### `on`

* block all symlinks

#### `if_not_owner`

* allow only if same owner

#### `from=`

* partial trust zone

Example:

```nginx id="p7x8zz"
disable_symlinks on from=$document_root;
```

👉 Only trust symlinks inside your web root

---

## `directio` (bypass cache for big files)

```nginx id="d9k2ll"
directio 4m;
```

### What it does:

* Large files skip OS cache
* read directly from disk

### Why that matters:

Good for:

* video streaming
* large downloads

Bad for:

* small files (adds overhead)

---

## `directio_alignment`

```nginx id="a8v4mm"
directio_alignment 4k;
```

### Why it exists

Storage systems (like XFS) prefer aligned reads.

So:

* reduces disk inefficiency
* improves throughput

---

# 🧠 Big picture (this section in one idea)

This whole chapter is basically NGINX saying:

> “I don’t just serve files. I decide *how*, *when*, *who*, and *at what speed* they are served.”

---

# ⚡ Open File Cache (BIG performance feature)

## `open_file_cache`

This is one of the most important optimizations in high-traffic NGINX setups.

```nginx id="ofc1"
open_file_cache max=5000 inactive=180;
```

### What it actually does

Instead of constantly checking disk for files, NGINX caches:

* file existence (does it exist?)
* file metadata (size, modified time)
* directory existence
* permission errors (optional)

👉 It does NOT cache file content — only file *info*

---

## Parameters explained

### `max=5000`

Maximum cached entries.

* More entries = more RAM usage
* Too low = frequent disk checks
* Too high = wasted memory

---

### `inactive=180`

Time before an entry is removed if unused.

* Default is **60 seconds**
* In your example: **180 seconds**

BUT:

* If a file is frequently accessed, its timer resets
* So “hot files” stay cached longer

---

## Why this matters

Without it:

* every request may hit disk metadata lookup

With it:

* requests become mostly memory lookups ⚡

---

## `open_file_cache_errors`

```nginx id="ofc2"
open_file_cache_errors on;
```

Controls whether NGINX caches errors like:

* file not found (404)
* permission denied (403)

### Why disable it sometimes?

If your filesystem changes often, caching errors may “stick” too long.

Default:

```text id="ofc2a"
off
```

---

## `open_file_cache_min_uses`

```nginx id="ofc3"
open_file_cache_min_uses 3;
```

Meaning:

> If a file is accessed 3+ times, treat it as “important”

So it won’t be evicted easily.

---

## `open_file_cache_valid`

```nginx id="ofc4"
open_file_cache_valid 60s;
```

This controls freshness.

Every 60 seconds:

* NGINX re-checks cached file info

👉 Prevents serving stale metadata forever

---

# 📖 File read optimization

## `read_ahead`

```nginx id="ra1"
read_ahead 0;
```

* Linux may prefetch file data automatically
* NGINX mostly ignores your value on Linux

So:

* `0` = disable control
* anything else = “let OS decide”

👉 Honestly: rarely touched in real deployments

---

# 📄 Logging behavior tweaks

## `log_not_found`

```nginx id="log1"
log_not_found off;
```

* `on`: log every 404
* `off`: ignore missing files

### Why disable it?

Because bots LOVE hitting:

* `/favicon.ico`
* `/robots.txt`

Your logs get spammed fast.

---

## `log_subrequest`

```nginx id="log2"
log_subrequest off;
```

Logs internal requests like:

* SSI includes
* internal redirects

Usually:

* `off` (default)
* only enable for debugging

---

# 🧼 URI cleanup behavior

## `merge_slashes`

```nginx id="ms1"
merge_slashes on;
```

Turns this:

```
/images//logo.png
```

into:

```
/images/logo.png
```

### Why this matters

Without it:

* weird URLs may fail matching
* inconsistent routing issues

Default:

* `off` (surprisingly)

---

# 🧓 Browser compatibility hacks (legacy stuff)

These exist mainly for old Internet Explorer quirks.

---

## `msie_padding`

```nginx id="ms1a"
msie_padding on;
```

* Pads small error pages to 512 bytes
* Prevents IE from showing its own ugly error page

👉 Mostly irrelevant today, but still in NGINX

---

## `msie_refresh`

```nginx id="ms2"
msie_refresh on;
```

* Sends HTML refresh redirect instead of HTTP redirect
* Only for old IE behavior

Modern usage:

* basically never needed

---

# 🌐 DNS RESOLUTION (VERY IMPORTANT in dynamic setups)

## `resolver`

```nginx id="dns1"
resolver 8.8.8.8 1.1.1.1 valid=1h;
```

### What it does

NGINX needs DNS when:

* using `proxy_pass` with domain names
* upstreams change dynamically

---

## Key parts

### DNS servers

* 127.0.0.1 (local resolver = best practice)
* Google DNS: `8.8.8.8`
* Cloudflare: `1.1.1.1`

---

### `valid=1h`

Cache DNS results for 1 hour

Without this:

* every request may trigger DNS lookup (bad performance)

---

## Why local resolver is recommended

Using something like:

* dnsmasq
* systemd-resolved

Benefits:

* faster DNS
* cached locally
* avoids external latency
* more stable under load

---

## `resolver_timeout`

```nginx id="dns2"
resolver_timeout 30s;
```

If DNS lookup takes longer than 30 seconds:

* request fails

Default:

* `30s`

---

# 🧠 Big mental model for this whole section

This part of NGINX is about 3 things:

### 1. Avoid disk work

→ `open_file_cache`

### 2. Clean request handling

→ slashes, logging, headers

### 3. Avoid slow dependencies

→ DNS resolver optimization

---

## 🧠 1. Big Idea: HTTP Core Module = “How web traffic is handled”

Everything you’re seeing here (server_tokens, client_body, open_file_cache, variables, etc.) belongs to the **HTTP layer**, which controls:

* how requests come in
* how files are served
* how headers behave
* how performance is optimized
* how responses are shaped

So instead of random directives, think:

> “This is everything NGINX uses to *understand, process, and respond to HTTP requests*.”

---

## 🧩 2. The 3 HTTP blocks (super important mental model)

You’ve basically got a hierarchy:

```
http {
    server {
        location {
        }
    }
}
```

### 🔵 http block (global web rules)

Applies to ALL websites on NGINX:

* caching behavior
* MIME types
* resolver (DNS)
* global limits
* default settings

---

### 🟢 server block (one website / domain)

Applies per domain:

* example.com vs api.example.com
* ports (80 / 443)
* SSL / HTTP2
* server_name routing

---

### 🟣 location block (per URL path)

Applies per route:

* `/admin`
* `/api`
* `/downloads`

This is where most “behavior tweaks” happen:

* auth
* caching rules
* redirects
* file routing (`root` vs `alias`)
* rate limits

---

## ⚙️ 3. The 5 major directive categories you just covered

Instead of memorizing hundreds of directives, group them like this:

---

### 📦 A. Request limits & safety

Controls abuse, uploads, performance stability:

* `client_max_body_size`
* `client_body_timeout`
* `limit_rate`
* `limit_except`
* `satisfy`

👉 Think: *“How much and what kind of traffic do I allow?”*

---

### 📁 B. File handling & caching (VERY important for performance)

* `open_file_cache`
* `open_file_cache_valid`
* `open_file_cache_min_uses`
* `directio`
* `sendfile`

👉 Think: *“How fast can I read files from disk without redoing work?”*

---

### 🌐 C. Routing / serving logic

* `root` vs `alias`
* `index`
* `try_files`
* `error_page`
* `internal`

👉 This is the “brain” of URL → file mapping.

Example idea:

* `/admin` → different folder
* missing file → fallback logic (`try_files`)

---

### 🧾 D. Headers, MIME, and browser behavior

* `types`
* `default_type`
* `server_tokens`
* `ignore_invalid_headers`
* `chunked_transfer_encoding`

👉 Think: *“What does the browser think this response is?”*

---

### 🔌 E. Connection behavior (performance + stability)

* `keepalive_timeout`
* `keepalive_requests`
* `send_timeout`
* `reset_timedout_connection`

👉 Think: *“How long should connections stay alive?”*

---

## 🧠 4. The most important concept: variables

This is where NGINX becomes “script-like”.

Variables like:

* `$remote_addr` → client IP
* `$request_uri` → requested path
* `$status` → response code
* `$http_user_agent` → browser info

### 💡 Key idea:

Variables are *dynamic values that change per request*

So you can do things like:

```nginx
log_format main '$remote_addr - $request_uri - $status';
```

That means:

> “Every request logs real-time values.”

---

## ⚠️ 5. One critical rule people miss

> If a directive does NOT support variables, NGINX will NOT error — it will just print raw text.

Example:

```nginx
error_log logs/error-$nginx_version.log;
```

Result:

```
error-$nginx_version.log   ❌ (not expanded)
```

So NGINX is powerful—but not always “helpful” with mistakes.

---

## 🚀 6. HTTP/2 section in one sentence

HTTP/2 in NGINX is basically:

> “Same website, but faster multiplexed connections over SSL.”

Enabled by:

```nginx
listen 443 ssl http2;
```

And the rest of the directives mostly tune:

* buffering
* stream limits
* header size limits
* idle timeouts

👉 You usually don’t tweak these unless optimizing high traffic systems.

---

## 🧩 7. The big mental takeaway

If you strip everything down:

* `http` = global web engine
* `server` = website identity (domain)
* `location` = route behavior (/admin, /api)
* directives = rules
* variables = dynamic data per request


# Understanding and Exploring the Location Block

# 🧭 1. What the location block really is

A `location` block is just:

> “If the request URL matches this pattern, do THIS.”

Example:

```nginx
location /admin/ {
    # rules for /admin/*
}
```

So every request like:

* `/admin`
* `/admin/dashboard`
* `/admin/users`

gets handled differently from the rest of the site.

---

# 🧩 2. The 5 location types (the real mental model)

Instead of memorizing symbols, think of them as **priority levels + matching style**.

---

## 🟢 1. `=` (Exact match — highest priority)

```nginx
location = /login
```

✔ Only matches:

* `/login`

❌ Does NOT match:

* `/login/`
* `/login?x=1`

👉 Think:

> “THIS EXACT URL ONLY. No variations.”

---

## 🔵 2. No modifier (prefix match)

```nginx
location /admin
```

Matches anything starting with `/admin`:

* `/admin`
* `/admin/users`
* `/admin123`

👉 Think:

> “Anything that starts like this.”

---

## 🟣 3. `^~` (prefix match, but STOP searching)

```nginx
location ^~ /static/ {
```

If matched:

* NGINX **stops checking regex locations**

👉 Think:

> “If it matches this, don’t overthink it—use it immediately.”

This is a performance + control tool.

---

## 🔴 4. `~` (case-sensitive regex)

```nginx
location ~ ^/user/[0-9]+$ {
```

Matches:

* `/user/123`

Does NOT match:

* `/user/abc`
* `/User/123`

👉 Think:

> “Power mode matching (strict + case-sensitive)”

---

## 🟠 5. `~*` (case-insensitive regex)

```nginx
location ~* \.(jpg|png|gif)$ {
```

Matches:

* `image.JPG`
* `image.png`
* `IMAGE.Gif`

👉 Think:

> “Flexible regex matching”

---

## ⚫ 6. `@name` (internal only)

```nginx
location @fallback {
    proxy_pass http://backend;
}
```

Cannot be accessed directly by browser.

Used for:

* `try_files`
* `error_page`
* internal routing

👉 Think:

> “Private helper route inside NGINX”

---

# 🧠 3. The REAL priority order (important correction)

NGINX does NOT follow a simple list—it follows this logic:

### Step 1: Exact match (`=`)

If found → STOP immediately

---

### Step 2: Prefix match (`^~` or normal `/path`)

* If `^~` matches → STOP regex checking
* If normal prefix → continue checking regex

---

### Step 3: Regex (`~` / `~*`)

Evaluated in order of appearance

---

### Step 4: Best prefix match fallback

---

# ⚡ 4. Simple flow diagram (how NGINX chooses)

```
Request URL
   ↓
Exact match (=) found?
   → YES → use it immediately

   ↓ NO
Prefix match (^~)?
   → YES → use it, skip regex

   ↓ NO
Check regex (~ / ~*)

   ↓ NO MATCH
Use best normal prefix match (/admin, /docs, etc.)
```

---

# 🧪 5. Real-world example (this is where it clicks)

```nginx
location /static/ {
    # normal files
}

location ^~ /static/images/ {
    # optimized image handling
}

location ~* \.(jpg|png|gif)$ {
    # image processing rules
}
```

### What happens?

Request:

```
/static/images/cat.png
```

👉 Matches `^~ /static/images/`
✔ Stops immediately
❌ regex is NOT checked

---

Request:

```
/assets/photo.jpg
```

👉 skips prefix `/static/images/`
👉 matches regex `~* \.(jpg|png|gif)$`

---

# 🧠 6. The easiest way to remember modifiers

Think of them like “personality types”:

* `=` → perfectionist (exact only)
* `/path` → general worker (prefix match)
* `^~` → decisive boss (stop searching)
* `~` → strict detective (case-sensitive regex)
* `~*` → relaxed detective (case-insensitive regex)
* `@` → internal assistant (not public)

---

# ⚠️ 7. Common beginner mistake

People think:

> “NGINX reads top to bottom”

❌ Not true.

# PHP and Python wiuth NGINX

# 🧠 The Big Picture

For static content:

```text
Browser → NGINX → HTML/CSS/JS file
```

For dynamic content:

```text
Browser → NGINX → Application Server → NGINX → Browser
```

Examples:

* PHP → PHP-FPM
* Python → Gunicorn / uWSGI / Daphne
* Ruby → Puma / Unicorn
* Perl → FastCGI daemon

NGINX does not execute application code itself. It delegates that responsibility.

---

# 📜 Why CGI Wasn't Enough

Traditional CGI worked like this:

```text
Request arrives
→ Web server starts a new process
→ Script runs
→ Process exits
```

That’s fine for low traffic, but under load it’s a disaster:

* expensive process creation
* no memory reuse
* poor scalability
* high latency

Every request starts from scratch. That's like hiring a new chef for every sandwich.

---

# ⚡ Why FastCGI Changed Everything

FastCGI keeps application processes alive.

```text
Request arrives
→ NGINX sends request to existing worker process
→ Worker handles it
→ Worker stays alive for next request
```

Benefits:

* much faster
* lower CPU overhead
* better memory efficiency
* supports high concurrency
* can run locally or remotely

---

# 🔌 How NGINX Communicates with Applications

Using sockets:

### Unix socket (faster, local only)

```text
/run/php/php8.2-fpm.sock
```

### TCP socket (network-capable)

```text
127.0.0.1:9000
```

Unix sockets are typically preferred when the app runs on the same server.

---

# 🐘 PHP + NGINX = PHP-FPM

PHP-FPM stands for:

> **PHP FastCGI Process Manager**

It maintains a pool of PHP worker processes.

Request flow:

```text
Browser
   ↓
NGINX
   ↓
PHP-FPM
   ↓
PHP script executes
   ↓
NGINX
   ↓
Browser
```

Typical configuration:

```nginx
location ~ \.php$ {
    include fastcgi_params;
    fastcgi_pass unix:/run/php/php8.2-fpm.sock;
    fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
}
```

### Key directives

* `fastcgi_pass` → where PHP-FPM is listening
* `include fastcgi_params` → passes standard CGI variables
* `fastcgi_param SCRIPT_FILENAME` → tells PHP which file to execute

Without `SCRIPT_FILENAME`, PHP would have a bit of an existential crisis.

---

# 🐍 Python + NGINX

For Python web apps (like Django or Flask), NGINX usually sits in front of an application server such as:

* Gunicorn
* uWSGI
* Daphne
* Uvicorn

Architecture:

```text
Browser → NGINX → Gunicorn/uWSGI → Django/Flask
```

Example using uWSGI:

```nginx
location / {
    include uwsgi_params;
    uwsgi_pass unix:/run/uwsgi/app.sock;
}
```

Example using Gunicorn:

```nginx
location / {
    proxy_pass http://127.0.0.1:8000;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
}
```

---

# 🔄 FastCGI vs uWSGI vs SCGI

All serve the same purpose: connecting NGINX to an application server.

| Protocol | Common Use                | Directive      |
| -------- | ------------------------- | -------------- |
| FastCGI  | PHP                       | `fastcgi_pass` |
| uWSGI    | Python                    | `uwsgi_pass`   |
| SCGI     | Specialized / legacy apps | `scgi_pass`    |

The syntax is intentionally very similar.

---

# 🚀 Why This Architecture Is So Popular

NGINX handles what it does best:

* SSL/TLS termination
* static files
* caching
* compression
* rate limiting
* connection management

Application servers handle:

* business logic
* database access
* templating
* session management

This separation is elegant and highly scalable.

---

# 🧩 Real-World Deployment Pattern

```text
Internet
   ↓
NGINX
   ├── Static files (served directly)
   ├── PHP requests → PHP-FPM
   └── Python requests → Gunicorn/uWSGI
```

NGINX acts like a smart receptionist:

* static files? “I’ve got this.”
* dynamic PHP? “Forwarding to PHP.”
* Python app? “Right this way.”

## Main FastCGI, uWSGI, and SCGI Directives in NGINX

NGINX includes built-in support for FastCGI, uWSGI, and SCGI, so no additional compilation is required. These modules allow NGINX to forward requests to backend applications such as PHP, Python, or other dynamic web frameworks.

## Core Connection Directives

### `fastcgi_pass`

Specifies the backend FastCGI server.

* TCP socket:

  ```nginx
  fastcgi_pass 127.0.0.1:9000;
  ```
* Unix socket:

  ```nginx
  fastcgi_pass unix:/tmp/fastcgi.socket;
  ```
* Upstream block:

  ```nginx
  upstream fastcgi_backend {
      server 127.0.0.1:9000;
      server 127.0.0.1:9001;
  }

  location ~ \.php$ {
      fastcgi_pass fastcgi_backend;
  }
  ```

## Passing Request Parameters

### `fastcgi_param`

Defines parameters sent to the FastCGI application.

Essential parameters include:

```nginx
fastcgi_param SCRIPT_FILENAME /path/to/site$fastcgi_script_name;
fastcgi_param QUERY_STRING    $query_string;
```

For POST requests, these are also required:

```nginx
fastcgi_param REQUEST_METHOD  $request_method;
fastcgi_param CONTENT_TYPE    $content_type;
fastcgi_param CONTENT_LENGTH  $content_length;
```

The standard `fastcgi_params` file already includes most required parameters, except `SCRIPT_FILENAME`, which must be set manually.

## Request and Response Handling

### `fastcgi_index`

Defines the default script when a directory is requested.

```nginx
fastcgi_index index.php;
```

### `fastcgi_split_path_info`

Splits URLs containing extra path information.

```nginx
fastcgi_split_path_info ^(.+\.php)(.*)$;
fastcgi_param SCRIPT_FILENAME /path/to/site$fastcgi_script_name;
fastcgi_param PATH_INFO       $fastcgi_path_info;
```

Useful for URLs like:

```text
/page.php/param1/param2
```

## Timeout Controls

### `fastcgi_connect_timeout`

Maximum time to establish a connection to the backend.

Default: 60 seconds

### `fastcgi_send_timeout`

Maximum delay between successive writes to the backend.

Default: 60 seconds

### `fastcgi_read_timeout`

Maximum time to wait for a response from the backend.

Default: 60 seconds

If exceeded, NGINX returns:

```text
504 Gateway Timeout
```

## Header Management

### `fastcgi_pass_header`

Allows specific headers to be forwarded.

```nginx
fastcgi_pass_header Authorization;
```

### `fastcgi_hide_header`

Prevents certain headers from being forwarded.

```nginx
fastcgi_hide_header X-Forwarded-For;
```

### `fastcgi_ignore_headers`

Ignores selected response headers from the backend, such as:

* `Cache-Control`
* `Expires`
* `X-Accel-Redirect`
* `X-Accel-Buffering`

## Error Handling

### `fastcgi_intercept_errors`

Allows NGINX to process backend-generated errors using `error_page`.

```nginx
fastcgi_intercept_errors on;
```

### `fastcgi_catch_stderr`

Captures matching backend stderr output into the NGINX error log.

```nginx
fastcgi_catch_stderr "PHP Fatal error:";
```

## Client Abort Behavior

### `fastcgi_ignore_client_abort`

Controls whether NGINX continues processing if the client disconnects.

* `on`: continue processing
* `off`: stop processing (default)

## Upstream Failover

### `fastcgi_next_upstream`

Specifies when to retry another backend server.

Common conditions:

* `error`
* `timeout`
* `invalid_header`
* `http_500`
* `http_503`
* `http_404`
* `http_429`

Example:

```nginx
fastcgi_next_upstream error timeout invalid_header;
```

Related directives:

* `fastcgi_next_upstream_timeout`
* `fastcgi_next_upstream_tries`

## Connection Optimization

### `fastcgi_keep_conn`

Keeps FastCGI connections open for reuse.

```nginx
fastcgi_keep_conn on;
```

Reduces connection overhead.

## Request Forwarding Controls

### `fastcgi_pass_request_body`

Controls whether the request body is sent.

Default: `on`

### `fastcgi_pass_request_headers`

Controls whether request headers are sent.

Default: `on`

## Temporary File and Storage Settings

### `fastcgi_temp_path`

Specifies the directory for temporary files.

```nginx
fastcgi_temp_path /tmp/nginx_fastcgi;
```

### `fastcgi_max_temp_file_size`

Limits temporary file size.

```nginx
fastcgi_max_temp_file_size 5m;
```

Set to `0` to disable temporary files.

### `fastcgi_temp_file_write_size`

Defines write buffer size for temporary files.

## Performance Controls

### `fastcgi_limit_rate`

Limits download speed from the FastCGI backend.

```nginx
fastcgi_limit_rate 100k;
```

### `fastcgi_force_ranges`

Enables byte-range support for FastCGI responses.

```nginx
fastcgi_force_ranges on;
```

## FastCGI Caching

FastCGI caching can dramatically improve performance by storing backend responses.

### Example Configuration

```nginx
fastcgi_cache phpcache;
fastcgi_cache_key "$scheme$host$request_uri";
fastcgi_cache_min_uses 2;

fastcgi_cache_path /tmp/cache
    levels=1:2
    keys_zone=phpcache:10m
    inactive=30m
    max_size=500m;

fastcgi_cache_use_stale updating timeout;
fastcgi_cache_valid 404 1m;
fastcgi_cache_valid 500 502 504 5m;
```

## Example PHP Location with Caching

```nginx
location ~ \.php$ {
    fastcgi_pass 127.0.0.1:9000;
    fastcgi_param SCRIPT_FILENAME /home/website.com/www$fastcgi_script_name;
    fastcgi_param PATH_INFO $fastcgi_script_name;
    include fastcgi_params;
    include fastcgi_cache;
}
```

## Key Benefits of FastCGI Caching and Buffering

* Reduces backend load
* Improves response times
* Serves repeated requests faster
* Allows stale content during backend outages
* Buffers responses for more efficient client delivery

## Equivalent Directives in uWSGI and SCGI

Most FastCGI directives have direct counterparts:

| FastCGI             | uWSGI             | SCGI             |
| ------------------- | ----------------- | ---------------- |
| `fastcgi_pass`      | `uwsgi_pass`      | `scgi_pass`      |
| `fastcgi_cache`     | `uwsgi_cache`     | `scgi_cache`     |
| `fastcgi_temp_path` | `uwsgi_temp_path` | `scgi_temp_path` |

Directive syntax and behavior are nearly identical across all three modules.

## Summary

The FastCGI module is central to integrating NGINX with dynamic web applications. Its key responsibilities include:

* Forwarding requests to backend applications
* Passing required request parameters
* Managing timeouts and errors
* Handling upstream failover
* Optimizing connections
* Enabling response buffering
* Providing powerful caching capabilities

These same concepts largely apply to uWSGI and SCGI, making NGINX a flexible and high-performance gateway for a wide range of application platforms.

## Setting Up PHP with NGINX Using FastCGI and PHP-FPM

PHP works especially well with NGINX through **FastCGI**, thanks to **PHP-FPM** (PHP FastCGI Process Manager), which has been bundled with PHP since version 5.3.3.

Unlike SCGI or uWSGI, FastCGI is the native and recommended protocol for PHP deployments.

## Why Use PHP-FPM?

PHP itself can process FastCGI requests, but PHP-FPM adds a dedicated process manager that greatly improves performance, scalability, and administration.

Key advantages include:

* Automatic daemonization (runs as a background service)
* Efficient process management
* Support for multiple worker pools
* Improved logging
* IP-based access controls
* Optional chroot sandboxing
* Better security and resource isolation

## How the Architecture Works

The communication flow is:

```text
Client Browser → NGINX → PHP-FPM → PHP Interpreter
```

* **NGINX** acts as the FastCGI client.
* **PHP-FPM** acts as the FastCGI server and process manager.
* **PHP workers** execute the requested scripts.

Communication occurs over either:

* TCP sockets (for example, `127.0.0.1:9000`)
* Unix domain sockets (for example, `/run/php/php-fpm.sock`)

## Installing PHP-FPM

### On Red Hat / CentOS / Fedora

```bash
dnf install php-fpm
```

### On Ubuntu / Debian

```bash
apt install php-fpm
```

Most modern repositories provide packages such as:

* `php-fpm`
* `php8-fpm`

## Important PHP Security Setting

Edit your `php.ini` file and ensure the following setting is disabled:

```ini
cgi.fix_pathinfo=0
```

This is an important security measure that helps prevent unintended script execution vulnerabilities.

## Key PHP-FPM Configuration Options

The main configuration file is typically:

```text
/etc/php-fpm.conf
```

Or pool-specific files such as:

```text
/etc/php-fpm.d/www.conf
```

Important settings to review:

* Worker process user and group
* Socket or IP/port to listen on
* Maximum number of child processes
* Allowed client IP addresses
* Optional Unix socket ownership and permissions

## Managing PHP-FPM

### Start or Restart

```bash
systemctl restart php-fpm
```

### Start (if not already running)

```bash
systemctl start php-fpm
```

### Check Status

```bash
systemctl status php-fpm
```

This command helps monitor:

* Service health
* Active processes
* Current workload
* Error messages

## NGINX Configuration for PHP

A basic NGINX server block for PHP looks like this:

```nginx
server {
    listen 80;
    server_name .website.com;
    root /home/website/www;
    index index.php index.html;

    location ~* \.php$ {
        fastcgi_pass 127.0.0.1:9000;
        fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
        fastcgi_param PATH_INFO $fastcgi_script_name;
        include fastcgi_params;
    }
}
```

## Explanation of Key Directives

* `fastcgi_pass`: Specifies the PHP-FPM backend
* `SCRIPT_FILENAME`: Full filesystem path to the PHP script
* `PATH_INFO`: Additional path information for the script
* `include fastcgi_params`: Loads standard FastCGI parameters

## Reload NGINX

After updating the configuration:

```bash
systemctl reload nginx
```

## Testing PHP Integration

Create a simple test file:

```bash
echo "<?php phpinfo(); ?>" > /home/website/www/index.php
```

Then visit:

```text
http://localhost/
```

Or your configured domain.

If everything is working correctly, you'll see the PHP information page.

## Common Issues

### 403 Forbidden

Usually caused by incorrect file permissions or ownership.

Verify that:

* Website files are readable by the PHP-FPM user
* Directory permissions allow traversal
* PHP-FPM is running under the correct user and group

### Connection Refused

Possible causes:

* PHP-FPM is not running
* Wrong socket or port configured
* Firewall blocking TCP connections

## Best Practices

* Use Unix sockets for local communication when possible
* Set `cgi.fix_pathinfo=0`
* Separate applications into different PHP-FPM pools
* Restrict access to PHP-FPM using allowed client settings
* Monitor PHP-FPM status regularly
* Tune worker limits based on server resources

## Summary

Integrating PHP with NGINX is straightforward using PHP-FPM and FastCGI.

The setup provides:

* High performance
* Efficient process management
* Strong security
* Excellent scalability
* Flexible configuration options

PHP-FPM is the standard and recommended way to run PHP applications with NGINX in production environments.

## Python and NGINX with Django

Python is a widely used object-oriented programming language available across many platforms, including Linux, Unix, Windows, Java, and .NET. When paired with NGINX, it becomes a powerful platform for building dynamic web applications.

In this setup, Python is used as a **server-side web language** through the **Django framework**.

## What Is Django?

Django is a popular open-source web framework for Python designed to simplify and accelerate web development.

Its well-known slogan is:

> *The web framework for perfectionists with deadlines.*

Django provides many built-in features, including:

* Automatic administrative interface
* Powerful URL routing
* Built-in caching framework
* Unit testing tools
* Security protections
* Database ORM (Object-Relational Mapping)

## Why Use Django with NGINX?

Django applications are commonly deployed using **WSGI**, which is the standard Python web interface. However, Django also supports **FastCGI**, which integrates smoothly with NGINX and is simpler to configure for FastCGI-based deployments.

This makes it an excellent choice for learning how NGINX communicates with Python applications.

## Architecture Overview

```text id="nzwv0s"
Client Browser → NGINX → Django FastCGI → Python Application
```

* **NGINX** receives client requests.
* Requests for dynamic content are forwarded via FastCGI.
* **Django's FastCGI handler** processes the request.
* Python executes the application logic.
* The response is returned through NGINX to the client.

## Installing Python

Python is typically available through your system's package manager.

### Red Hat / CentOS / Fedora

```bash id="k2p8xg"
dnf install python python-devel
```

### Ubuntu / Debian

```bash id="tnexy0"
apt install python python-dev
```

The package manager automatically installs all required dependencies.

## Installing Django

Although Django can be installed from system repositories, the recommended approach is to use **pip**, Python's package manager. This ensures you get the latest stable version and simplifies dependency management.

### Why Use pip?

* Access to the latest Django release
* Easier upgrades
* Better dependency handling
* Consistent installation across platforms

Before installing Django, you must first install `pip`.

## Next Step

After installing `pip`, Django can be installed using:

```bash id="o8fdg4"
pip install django
```

This will download and install Django along with any required Python packages.

## Summary

To run Python applications with NGINX:

* Install Python and development libraries
* Install Django using `pip`
* Use Django's FastCGI support for integration with NGINX
* Configure NGINX to forward requests to the Django application

While WSGI is the modern standard for production deployments, FastCGI provides a simpler and effective way to understand how NGINX interacts with Python web applications.

## NGINX as a Reverse Proxy

NGINX was designed not only as a fast web server but also as a powerful **reverse proxy**. In modern web architectures, it commonly sits in front of backend application servers such as Node.js, Apache, Django, or microservices.

## How Reverse Proxy Works

```text id="e5x2gb"
Client → NGINX → Backend Server(s)
```

* Clients communicate directly with **NGINX**
* NGINX serves static files itself
* Dynamic requests are forwarded to backend servers
* Backend servers respond only to NGINX, not directly to the public internet

This architecture improves:

* Performance
* Security
* Scalability
* Load balancing
* Resource utilization

## Benefits of Using NGINX as a Reverse Proxy

* Efficient handling of static content
* Offloads traffic from backend servers
* Supports load balancing across multiple servers
* Improves security by hiding backend infrastructure
* Simplifies SSL/TLS termination
* Enables advanced routing and caching
* Supports modern protocols like WebSockets

## Reverse Proxy vs FastCGI

Unlike FastCGI, reverse proxying uses standard **HTTP or HTTPS** between NGINX and backend servers.

* **FastCGI**: Used for applications like PHP-FPM
* **HTTP Proxying**: Used for web servers and application servers such as Node.js, Apache, or Django

No special protocol is required beyond HTTP.

## Core Proxy Module

NGINX includes the **proxy module** by default. It provides directives for:

* Forwarding requests
* Managing headers
* Handling redirects
* Configuring failover
* Controlling retries
* Buffering and caching responses

## Main Directives

### `proxy_pass`

Specifies the backend server to which requests are forwarded.

#### TCP Backend

```nginx id="3c4gby"
proxy_pass http://127.0.0.1:8080;
```

#### HTTPS Backend

```nginx id="lnw0zt"
proxy_pass https://192.168.0.1;
```

#### Unix Socket

```nginx id="q6ngul"
proxy_pass http://unix:/tmp/nginx.sock;
```

#### With URI Rewriting

```nginx id="n58e1x"
proxy_pass http://localhost:8080/uri/;
```

#### Using Variables

```nginx id="94u8ww"
proxy_pass http://$server_name:8080;
```

## Load Balancing with Upstream

```nginx id="o8t85n"
upstream backend {
    server 127.0.0.1:8080;
    server 127.0.0.1:8081;
}

location / {
    proxy_pass http://backend;
}
```

This distributes requests among multiple backend servers.

## Overriding the HTTP Method

### `proxy_method`

Forces all proxied requests to use a specific HTTP method.

```nginx id="vbwjlwm"
proxy_method POST;
```

Useful in specialized integration scenarios.

## Header Management

### `proxy_hide_header`

Prevents specific response headers from being sent to the client.

```nginx id="aqxv3z"
proxy_hide_header Cache-Control;
```

By default, NGINX already hides some headers, including:

* `Date`
* `Server`
* `X-Pad`
* `X-Accel-*`

### `proxy_pass_header`

Allows otherwise hidden headers to be passed to the client.

```nginx id="v99dri"
proxy_pass_header Date;
```

## Forwarding Request Data

### `proxy_pass_request_body`

Controls whether the request body is sent to the backend.

Default: `on`

### `proxy_pass_request_headers`

Controls whether request headers are sent to the backend.

Default: `on`

## Rewriting Redirects

### `proxy_redirect`

Rewrites `Location` headers returned by the backend.

#### Disable Rewriting

```nginx id="u1m75c"
proxy_redirect off;
```

#### Automatic Rewriting

```nginx id="mf4kmg"
proxy_redirect default;
```

#### Custom Rewrite

```nginx id="j2fykf"
proxy_redirect http://localhost:8080/ http://example.com/;
```

This is especially useful when backend servers generate redirects using internal URLs.

## Upstream Failover

### `proxy_next_upstream`

Specifies when NGINX should retry another upstream server.

Supported conditions include:

* `error`
* `timeout`
* `invalid_header`
* `http_500`
* `http_502`
* `http_503`
* `http_504`
* `http_404`

Example:

```nginx id="vz8qsk"
proxy_next_upstream error timeout invalid_header;
```

## Retry Controls

### `proxy_next_upstream_timeout`

Limits the total retry duration.

```nginx id="36g1aj"
proxy_next_upstream_timeout 30s;
```

Set to `0` to disable.

### `proxy_next_upstream_tries`

Limits the number of retry attempts.

```nginx id="2mvjkx"
proxy_next_upstream_tries 3;
```

## Typical Reverse Proxy Configuration

```nginx id="v2kfb2"
server {
    listen 80;
    server_name example.com;

    location / {
        proxy_pass http://backend;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_next_upstream error timeout invalid_header http_500 http_502 http_503 http_504;
    }
}
```

## Common Use Cases

* Proxying Node.js applications
* Fronting Apache or Tomcat servers
* Serving Django or Flask apps
* Load balancing microservices
* SSL termination
* WebSocket proxying
* API gateway functionality

## Summary

NGINX excels as a reverse proxy by acting as an intelligent intermediary between clients and backend servers.

Its reverse proxy capabilities provide:

* High performance
* Flexible routing
* Load balancing
* Failover handling
* Header manipulation
* Redirect rewriting
* Enhanced security

This makes NGINX an essential component in modern web application architectures, especially for distributed systems and microservices.
