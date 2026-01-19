---
title: "Authentication Logging"
layout: default
parent: Logging
grand_parent: Administration
nav_order: 5
---

## Lesson Content

In Linux, keeping track of who accesses a system and how they do it is crucial for security and troubleshooting. This process is managed through authentication logging, which records all authorization-related events, such as user logins and the methods used.

### The auth.log File

On Debian-based systems like Ubuntu, the primary file for tracking this activity is `/var/log/auth.log`. This log file contains system authorization information, including successful and failed user login attempts, and any authentication mechanisms that were triggered. Reviewing this file is a key step in diagnosing login problems or investigating security incidents.

Here is a sample snippet from an `auth.log` file:

```plaintext
Jan 31 10:37:50 icebox pkexec: pam_unix(polkit-1:session): session opened for user root by (uid=1000)
```

### Understanding Log Entries

Each line in the log provides valuable details. In the example above:

- **`Jan 31 10:37:50`**: The timestamp of the event.
- **`icebox`**: The hostname of the machine where the event occurred.
- **`pkexec`**: The program that initiated the event.
- **`pam_unix(polkit-1:session)`**: The authentication module and service used.
- **`session opened for user root by (uid=1000)`**: The action taken—a session was opened for the `root` user by a user with UID `1000`.

### Alternative Log Files

It's important to note that the location for authentication logs can vary between Linux distributions. For example, on Red Hat-based systems like CentOS and Fedora, these events are typically recorded in `/var/log/secure` instead of `/var/log/auth.log`.

## Exercise

Follow these steps in your Ubuntu VM terminal to practice the concepts from this lesson:

1. **View system logs**: Try this command
   ```bash
   journalctl -n 20` or `tail -20 /var/log/syslog
   ```
   Expected output:
   ```
   (Output will vary based on your system)
   ```

2. **Check auth logs**: Try this command
   ```bash
   sudo tail -20 /var/log/auth.log` (if available)
   ```
   Expected output:
   ```
   (Output will vary based on your system)
   ```

3. **View kernel logs**: Try this command
   ```bash
   dmesg | tail -20
   ```
   Expected output:
   ```
   (Output will vary based on your system)
   ```

4. **Check log directory**: Try this command
   ```bash
   ls -lh /var/log/ | head -15
   ```
   Expected output:
   ```
   (Output will vary based on your system)
   ```

## Quiz Question

On Debian-based systems, what is the name of the log file used for user authentication? Please answer using the filename only. The answer is case-sensitive.

