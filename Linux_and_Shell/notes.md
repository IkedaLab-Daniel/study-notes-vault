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
