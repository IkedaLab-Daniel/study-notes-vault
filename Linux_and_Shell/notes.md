# Hands on Linux Commands and Shell

## Introduction to Linux and Unix

### Operating System (OS)

* Software that manages computer hardware/resources and enables interaction to perform tasks.

### Unix

* Family of operating systems (e.g., Oracle Solaris, FreeBSD, HPUX, IBM AIX, macOS).
* Originated in **1960s** at AT\&T Bell Labs for PDP-7 hardware.
* Rewritten in **C** in the 1970s → portable across architectures.
* **BSD** (Berkeley Software Distribution) developed at UC Berkeley added capabilities.
* macOS derived from BSD.

### Linux

* Unix-like OS family, often referring to specific distributions.
* Free and open-source; highly secure due to public source code.
* **Features:** multi-user, multitasking, portable.
* Origin:

  * 1980s: GNU project (MIT) created free Unix-like tools.
  * 1991: Linus Torvalds created Linux kernel.
  * 1992: GNU tools + Linux kernel merged → popular Linux OS.
  * 1996: Tux the penguin adopted as mascot.

### Common Uses of Linux

* **Mobile:** Android OS (Linux kernel) powers billions of smartphones.
* **Supercomputers:** clusters for high-performance computing.
* **Enterprise & Cloud:** millions of Linux servers for apps, web, databases.
* **PC OS:** popular with developers and learners (e.g., Ubuntu).

### Key Takeaways

* Unix: OS family since 1960s; portable after rewrite in C.
* Linux: free, open-source Unix alternative since 1991.
* Supports multi-user, multitasking, portability.
* Widely used in mobile, supercomputing, cloud, and desktops.

## Linux Distributions

### Definition

* A **Linux distribution** (distro) is a specific flavor of the Linux OS.
* All distros use the **Linux kernel**.
* Tailored for specific audiences or tasks.

### Differentiating Factors

* **Default utilities**: prepackaged commands and apps.
* **GUI**: graphical interface for user interaction.
* **Shell commands**: supported command sets.
* **Support model**: community-backed or commercial; long-term support (LTS) or rolling release.

### Common Distributions & Use Cases

* **Debian**

  * First release: 1993 (v0.01), stable release 1996 (v1.1).
  * Stable, reliable, fully open-source.
  * Supports many architectures; popular in servers.
  * Largest community-run distro.

* **Ubuntu**

  * First release: 2004.
  * Based on Debian; developed by Canonical.
  * Editions: Desktop, Server, Core (IoT).

* **Red Hat Enterprise Linux (RHEL)**

  * Independent (not based on another distro).
  * Stable, reliable, open-source.
  * Maintained by Red Hat (IBM subsidiary).
  * Focused on enterprise customers.

* **Fedora**

  * Stable, reliable, secure; supports many architectures.
  * Sponsored by Red Hat; acts as a testing ground for RHEL.
  * Known for unique firewall and security features.

* **SUSE Linux Enterprise (SLE)**

  * Editions: SLES (Server), SLED (Desktop).
  * Supports architectures like ARM (Raspberry Pi).
  * Uses SUSE Package Hub for additional software.
  * Maintained by SUSE (Germany).

* **Arch Linux**

  * DIY, highly configurable.
  * Requires strong Linux/system knowledge.
  * Rolling release with newest software, less focus on stability.

### Key Takeaways

* Distros differ by UI, shell commands, support model, and target audience.
* Debian: server stability; Ubuntu: user-friendly, versatile; RHEL: enterprise; Fedora: innovation; SUSE: architecture versatility; Arch: customization freedom.


## Overview of Linux Architecture

### Layers of a Linux System

1. **User Interface (UI)**

   * Enables user interaction via keyboard, mouse, or GUI.
   * Desktop versions provide GUI similar to Windows.

2. **Application Layer**

   * Includes system tools, shells, programming languages, and user applications (e.g., browsers, text editors, games).
   * Communicates with the OS to perform tasks.

3. **Operating System (OS)**

   * Manages essential system functions: job scheduling, file management, error detection, user assignment.
   * Ensures system stability and performance.

4. **Linux Kernel**

   * Core, lowest-level software with full system control.
   * Starts at boot, stays in memory.
   * Bridges apps and hardware via system calls.
   * Key functions: memory management, process management, device driver management, system security.

5. **Hardware Layer**

   * Physical/electronic components: CPU, RAM, storage, display, USB devices.

### Linux Filesystem

* Organized as a tree with **root directory** `/` at the top.
* Key directories:

  * `/bin` – user binary files (programs, commands).
  * `/usr` – user programs.
  * `/home` – personal files and directories.
  * `/boot` – system boot files.
  * `/media` – temporary media (CD, USB).
* Assigns access rights to files and directories.

### Key Takeaways

* **5 layers**: UI → Applications → OS → Kernel → Hardware.
* Filesystem: hierarchical structure starting from `/`, organizing system, application, and user files.

## Creating and Editing Text Files

### Categories of Text Editors in Linux

1. **Command-line Editors**

   * **GNU nano** – Friendly, modeless editor with undo/redo, search/replace, syntax highlighting, automatic indentation, multiple buffers.
   * **vi** – Traditional Unix-based editor.
   * **vim** – Mode-based, powerful editor based on vi.

2. **GUI Editors**

   * **gedit** – Default GNOME editor, general-purpose, simple GUI, supports syntax highlighting, file browser, search/replace, and plugins.
   * **emacs** – One of the oldest open-source editors; can be used in GUI or terminal.

---

### gedit Features

* Integrated file browser.
* Undo/redo support.
* Search and replace (supports regular expressions).
* Plugin extensibility (`gedit-plugins`).
* Syntax color coding for better code readability.

---

### GNU nano Basics

* Open file: `nano filename`
* Navigation: arrow keys, Page Up/Down, Home/End.
* Search: `Ctrl + W` (“Where Is”).
* Common commands shown at bottom; use `Ctrl + <key>` to activate.

---

### vim Basics

* Start: `vim filename`
* **Modes**:

  * *Insert mode*: Press `i` to type text.
  * *Command mode*: Press `Esc` to run commands.
* Save: `:w` or `:save filename`
* Quit: `:q`
* Quit without saving: `:q!`
* Highly configurable with extensive commands for navigation, editing, and text manipulation.

---

### Key Takeaways

* Linux offers both **command-line** and **GUI-based** text editors.
* **gedit** simplifies editing for beginners and general-purpose work.
* **nano** provides command-line editing with intuitive shortcuts.
* **vim** offers powerful, fast editing through a two-mode system, suited for experienced users.

## Overview of Common Linux Shell Commands — Summary

### 1. **What is a Shell?**

* User interface for Unix-like operating systems.
* Interprets commands and runs programs.
* Functions as:

  * **Interactive language**
  * **Scripting language** (can automate tasks)
* Common shells: **Bash** (default in most Linux systems), sh, ksh, tcsh, zsh, fish.
* Check default shell:

  ```bash
  printenv SHELL
  ```
* Switch to Bash:

  ```bash
  bash
  ```

---

### 2. **Applications of Shell Commands**

* **Getting information** about the system and user.
* **Navigating** and working with files/directories.
* **Printing contents** of files or strings.
* **File compression & archiving**.
* **Networking operations**.
* **System monitoring**.
* **Batch job automation** (e.g., ETL).

---

### 3. **Common Shell Commands**

#### **Getting Information**

| Command  | Purpose                    |
| -------- | -------------------------- |
| `whoami` | Username of current user   |
| `id`     | User ID and group IDs      |
| `uname`  | OS name                    |
| `ps`     | Running processes & IDs    |
| `top`    | Processes + resource usage |
| `df`     | Mounted file system info   |
| `man`    | Manual for a command       |
| `date`   | Current date               |

---

#### **Working with Files**

| Command | Purpose                        |
| ------- | ------------------------------ |
| `cp`    | Copy files                     |
| `mv`    | Move/rename files              |
| `rm`    | Delete files                   |
| `touch` | Create/update empty file       |
| `chmod` | Change file permissions        |
| `wc`    | Count lines, words, characters |
| `grep`  | Search file for patterns       |

---

#### **Navigating Directories**

| Command | Purpose                |
| ------- | ---------------------- |
| `ls`    | List files/directories |
| `find`  | Search for files       |
| `pwd`   | Show current directory |
| `mkdir` | Create directory       |
| `cd`    | Change directory       |
| `rmdir` | Remove directory       |

---

#### **Printing File/String Contents**

| Command | Purpose                  |
| ------- | ------------------------ |
| `cat`   | Print entire file        |
| `more`  | View file page-by-page   |
| `head`  | First N lines            |
| `tail`  | Last N lines             |
| `echo`  | Print string or variable |

---

#### **Compression & Archiving**

| Command | Purpose        |
| ------- | -------------- |
| `tar`   | Archive files  |
| `zip`   | Compress files |
| `unzip` | Extract files  |

---

#### **Networking**

| Command    | Purpose                           |
| ---------- | --------------------------------- |
| `hostname` | Show hostname                     |
| `ping`     | Send test packets to host         |
| `ifconfig` | Show/configure network interfaces |
| `curl`     | Show URL contents                 |
| `wget`     | Download file from URL            |

---

### 4. **Running Linux on Windows**

* **Dual boot** (separate partition).
* **Virtual machine** installation.
* **Linux emulators** (e.g., CygWin).
* **Windows Subsystem for Linux (WSL)** — run Linux binaries natively.

---

### **Key Takeaways**

* Shell = interactive + scripting environment for running commands.
* Used for file management, system monitoring, networking, and automation.
* `echo` prints strings/variables, `cat` and `tail` display file contents.
* `curl` and `wget` work with files from the web.

## File and Directory Navigation Commands

### Commands Overview

* **ls**: Lists files and directories in a given directory.

  * `ls` → lists current directory contents.
  * `ls Downloads` → lists contents of `Downloads`.
  * `ls -l` → detailed list with permissions, owner, and modification date.

* **pwd**: Prints the current working directory.

* **cd**: Changes the current working directory.

  * **Relative path**: `cd Documents` (moves into Documents from current location).
  * **Parent directory**: `cd ..` (moves up one level).
  * **Home directory**: `cd ~` (absolute path to home).
  * **Absolute path**: `cd /path/to/Notes` (direct path navigation).

* **find**: Searches for files matching a specified pattern.

  * `find . -name "a.txt"` → case-sensitive search in current directory.
  * `find . -iname "a.txt"` → case-insensitive search.

### Key Takeaways

* **ls** → list directory contents.
* **pwd** → see current location.
* **cd** → navigate directories using relative or absolute paths.
* **find** → locate files matching specific names or patterns.

## File and Directory Management Commands

### Creating and Deleting

* **mkdir** → create a new directory.

  * Example: `mkdir test` → creates folder `test`.
* **rm file** → remove a file.
* **rm -r folder** → remove a directory and all its contents (use with caution).
* **rmdir folder** → remove an empty directory safely.
* **touch file.txt** → create an empty file, or update timestamp of an existing file.

### Copying and Moving

* **cp source dest** → copy file to destination.
* **cp -r source\_folder dest\_folder** → copy entire directory.
* **mv source dest** → move (or rename) file/directory.

### File Permissions

* **chmod +x file.sh** → make a file executable.
* Use `ls -l` to view permissions (`r` = read, `w` = write, `x` = execute).

### Key Takeaways

* **touch** → create/update files.
* **mkdir / rmdir** → create/remove empty directories.
* **rm / rm -r** → delete files/directories (recursive deletion is dangerous).
* **cp / mv** → copy or move files and directories.
* **chmod** → adjust read/write/execute permissions.
