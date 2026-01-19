---
index: 1
lang: "en"
title: "Filesystem Hierarchy"
meta_title: "Filesystem Hierarchy - The Filesystem"
meta_description: "Explore the standard Linux file system hierarchy (FHS). This guide explains the purpose of key directories like /bin, /etc, /home, and /var, providing a clear overview of the file system hierarchy in Linux."
meta_keywords: "linux file system hierarchy, file system hierarchy in linux, linux file hierarchy structure, linux file hierarchy, FHS, linux directory structure"
---

## Lesson Content

You are likely becoming familiar with the directory structure on your system. Most Linux distributions organize their filesystems according to the **Linux File System Hierarchy** (FHS) Standard. This standard ensures that files are stored in predictable locations, making systems more consistent.

To see the top-level directories, run the command `ls -l /`. While your system might have minor differences, the core **linux file hierarchy structure** will be very similar to the one described below.

### The Root Directory

- `/` - This is the root directory, the starting point for the entire filesystem. Every single file and directory on your system is located under this directory.

### Essential System Directories

The **file hierarchy in linux** includes several directories critical for the system's operation.

- `/bin` - Contains essential command-line programs (binaries) available to all users, such as `ls`, `cp`, and `mv`.
- `/sbin` - Holds essential system binaries, which are primarily intended for system administration and can typically only be run by the root user.
- `/etc` - This is the core system configuration directory. It contains configuration files for the operating system and installed applications, but it should not contain any executable binaries.
- `/lib` - Contains essential shared library files that system binaries in `/bin` and `/sbin` depend on to function correctly.
- `/boot` - Stores the files required for the system's boot process, including the Linux kernel and the boot loader files.

### User and Application Data

- `/home` - Contains personal directories for each user. This is where you store your documents, application settings, and other personal files.
- `/root` - The home directory for the root user, separate from the `/home` directory to ensure the root user can log in even if `/home` is unavailable.
- `/opt` - Reserved for optional or third-party application software packages.
- `/usr` - This directory contains user-installed software and utilities. Despite its name, it generally does not hold individual user's home files. It has its own sub-directory structure, such as `/usr/bin` for non-essential user binaries and `/usr/local` for software compiled from source.

### Dynamic and Temporary Data

- `/var` - Stands for "variable" and stores files that are expected to change in size and content, such as system logs (`/var/log`), caches, and spool files.
- `/tmp` - A world-writable space for storing temporary files. Files in this directory are often deleted upon system reboot.
- `/run` - Contains information about the running system since the last boot, such as process IDs (PIDs) and other runtime data.

### Device and Mount Points

- `/dev` - Contains special device files that represent hardware components like hard drives, terminals, and input devices.
- `/media` - A standard mount point for removable media like USB drives, SD cards, and CD-ROMs.
- `/mnt` - A generic mount point for temporarily mounting filesystems.

### System Information

- `/proc` - A virtual filesystem that provides real-time information about currently running processes and kernel parameters.
- `/srv` - Intended for site-specific data served by the system, such as files for a web server.

## Exercise

Follow these steps in your Ubuntu VM terminal to practice the concepts from this lesson:

1. **Check disk usage**: Try this command
   ```bash
   df -h
   ```
   Expected output:
   ```
   (Output will vary based on your system)
   ```

2. **View directory usage**: Try this command
   ```bash
   du -sh /home
   ```
   Expected output:
   ```
   (Output will vary based on your system)
   ```

3. **Check filesystem type**: Try this command
   ```bash
   df -T
   ```
   Expected output:
   ```
   (Output will vary based on your system)
   ```

4. **View mounted filesystems**: Try this command
   ```bash
   mount | column -t
   ```
   Expected output:
   ```
   (Output will vary based on your system)
   ```

## Quiz Question

What directory is used to store logs? (Please provide the full path. The answer is case-sensitive and must be in English.)

