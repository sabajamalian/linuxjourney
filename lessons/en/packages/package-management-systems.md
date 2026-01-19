---
index: 6
lang: "en"
title: "yum and apt"
meta_title: "yum and apt - Packages"
meta_description: "Explore the key differences in the yum vs apt debate. This guide covers how to use yum and apt for installing, removing, and updating packages on RPM and Debian-based Linux systems."
meta_keywords: "yum vs apt, yum apt, linux package management, apt, yum, debian, red hat, install packages, update packages, linux commands"
---

## Lesson Content

Package managers are essential tools in Linux that simplify installing, updating, and removing software. They automatically handle dependencies, ensuring that all required libraries and components are installed correctly. Two of the most prominent package management systems are **yum** and **apt**.

### Yum vs Apt

The primary difference between these two systems lies in the Linux distributions they serve. The `yum` (Yellowdog Updater, Modified) package manager is used by RPM-based distributions like Red Hat, CentOS, and Fedora. In contrast, `apt` (Advanced Package Tool) is the standard for Debian-based distributions, including Ubuntu. While both `yum` and `apt` achieve the same goals, their command syntax differs.

### Installing and Removing Packages

To install a new piece of software from a repository, you use the `install` command.

```bash
Debian: $ apt install package_name
RPM: $ yum install package_name
```

To remove a package, the commands are also straightforward. `apt` uses `remove`, while `yum` uses `erase`.

```bash
Debian: $ apt remove package_name
RPM: $ yum erase package_name
```

### Updating and Inspecting Packages

It is a best practice to update your local package index before installing or upgrading software. This ensures you are getting the latest available versions.

For Debian systems, this is a two-step process: `apt update` refreshes the package list, and `apt upgrade` installs the new versions. For RPM systems, `yum update` handles both actions with a single command.

```bash
Debian: $ apt update; apt upgrade
RPM: $ yum update
```

If you need to get more details about a specific package, you can use the following commands to display information like its version, size, and description.

```bash
Debian: $ apt show package_name
RPM: $ yum info package_name
```

## Exercise

Follow these steps in your Ubuntu VM terminal to practice the concepts from this lesson:

1. **Check your package management system**: Identify which system you're using
   ```bash
   which apt apt-get dpkg
   ```
   Expected output:
   ```
   /usr/bin/apt
   /usr/bin/apt-get
   /usr/bin/dpkg
   (Debian-based system)
   ```

2. **Update package database**: Refresh available packages
   ```bash
   sudo apt update
   ```
   Expected output:
   ```
   Hit:1 http://archive.ubuntu.com/ubuntu focal InRelease
   Reading package lists... Done
   Building dependency tree       
   ```

3. **Search for a package**: Find available packages
   ```bash
   apt search tree 2>/dev/null | grep "^tree/"
   ```
   Expected output:
   ```
   tree/focal 1.8.0-1 amd64
   ```

4. **Simulate package installation**: Dry-run to see what would happen
   ```bash
   apt install --simulate tree 2>/dev/null | head -10
   ```
   Expected output:
   ```
   Reading package lists... Done
   Building dependency tree       
   The following NEW packages will be installed:
     tree
   ```

5. **List upgradable packages**: Check for available updates
   ```bash
   apt list --upgradable 2>/dev/null | head -10
   ```
   Expected output:
   ```
   Listing... Done
   (Shows packages that can be upgraded)
   ```

## Quiz Question

What command is used to show package information on a Debian system? Please answer in English, paying attention to case sensitivity.

## Quiz Answer

apt show
