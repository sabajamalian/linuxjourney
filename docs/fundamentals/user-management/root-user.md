---
title: "root"
layout: default
parent: User Management
grand_parent: Fundamentals
nav_order: 2
---

## Lesson Content

In Linux, certain administrative tasks require elevated privileges. These privileges belong to a special account known as the **root user in Linux**. While you can log in directly as root, it is often safer and more manageable to gain superuser access temporarily.

### The `su` Command

Besides the `sudo` command, you can use `su` (substitute user) to gain superuser privileges. When run without a username, `su` attempts to open a new shell session for the **linux root user**, prompting you for the root password.

```bash
su
```

You can also use this command to switch to any other user on the system, provided you know their password.

### Risks of a Persistent Root Shell

Using `su` to open a root shell has significant downsides. Operating continuously as the root user increases the risk of making a critical, system-altering mistake. Furthermore, actions performed in a root shell are not logged under your personal user account, making it difficult to audit system changes. For these reasons, it is best practice to use `sudo` for individual commands that require superuser access.

### The `sudoers` File

So, how does the system determine who is allowed to use `sudo`? Access is controlled by a configuration file located at `/etc/sudoers`. This file lists the users and groups who are granted permission to run commands as the superuser.

To edit this file safely, you should always use the `visudo` command. This utility opens the `sudoers` file in a text editor and performs a syntax check before saving, which helps prevent configuration errors that could lock you out of administrative access.

## Exercise

Follow these steps in your Ubuntu VM terminal to practice the concepts from this lesson:

1. **Check if you are root**: Verify your current user
   ```bash
   whoami
   ```
   Expected output:
   ```
   your-username
   (not root - which is correct for safety)
   ```

2. **Run a command as root**: Use sudo to execute with elevated privileges
   ```bash
   sudo whoami
   ```
   Expected output:
   ```
   root
   ```

3. **View a root-only file**: Try to access shadow file
   ```bash
   sudo cat /etc/shadow | head -3
   ```
   Expected output:
   ```
   root:*:18000:0:99999:7:::
   (encrypted password entries)
   ```

4. **Check sudo privileges**: See what commands you can run as sudo
   ```bash
   sudo -l
   ```
   Expected output:
   ```
   User your-username may run the following commands:
       (ALL : ALL) ALL
   ```

5. **View root's home directory**: List contents of /root
   ```bash
   sudo ls -la /root
   ```
   Expected output:
   ```
   drwx------  5 root root 4096 (root's home directory contents)
   ```

## Quiz Question

What file lists the users and groups with `sudo` privileges? Please provide the full path. (Note: Your answer must be in English and is case-sensitive).

