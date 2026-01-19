---
title: "Software Distribution"
layout: default
parent: Packages
grand_parent: Fundamentals
nav_order: 1
---

## Lesson Content

A Linux system is composed of many software components, such as web browsers, text editors, and media players. These components are known as packages, and they are typically managed by a package manager, which handles the installation, update, and removal of software. Understanding this process is a fundamental part of the **best way to learn linux**.

### What Are Linux Packages

You might know software by names like Chrome or Firefox, but on a technical level, they are packages. A package is essentially an archive of files, including the application's executables, configuration files, and documentation, all bundled together. This organized structure simplifies software management.

### The Software Supply Chain

The journey of a software package involves two key roles:

- **Upstream Providers**: These are the developers who write the software. They compile the source code, create installation instructions, and release new versions and updates.
- **Package Maintainers**: When a new version is ready, upstream providers send it to package maintainers. These maintainers review, manage, and distribute the software to end-users in the form of packages tailored for specific Linux distributions.

### Common Package Formats

While you can install software directly from its source code, using a package manager is far more common and efficient. It's one of the **best ways to learn linux commands** for system administration. There are two predominant package formats:

- **Debian (.deb)**: Used by Debian and its derivatives, such as Ubuntu and Linux Mint.
- **Red Hat Package Manager (.rpm)**: Used by Red Hat Enterprise Linux (RHEL), Fedora, and CentOS.

Mastering the tools to manage these packages is the **best way to learn linux command line** and is a skill you will use constantly. These tools are some of the **best resources to learn linux** system administration.

## Exercise

Follow these steps in your Ubuntu VM terminal to practice the concepts from this lesson:

1. **Check your Linux distribution**: Identify which distro you're using
   ```bash
   cat /etc/os-release
   ```
   Expected output:
   ```
   NAME="Ubuntu"
   VERSION="20.04.5 LTS (Focal Fossa)"
   ID=ubuntu
   ID_LIKE=debian
   ```

2. **Check package management system**: Verify what package manager is available
   ```bash
   which apt
   which dpkg
   ```
   Expected output:
   ```
   /usr/bin/apt
   /usr/bin/dpkg
   ```

3. **View system architecture**: Check if 32-bit or 64-bit
   ```bash
   uname -m
   ```
   Expected output:
   ```
   x86_64
   (64-bit system)
   ```

4. **Check kernel version**: View Linux kernel information
   ```bash
   uname -r
   ```
   Expected output:
   ```
   5.4.0-150-generic
   ```

## Quiz Question

What package format is used by Ubuntu and Debian?

