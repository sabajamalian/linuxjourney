---
index: 5
lang: "en"
title: "Authentication Logging"
meta_title: "Authentication Logging - Logging"
meta_description: "Explore Linux authentication logging by examining the /var/log/auth.log file. This guide helps beginners understand user login events, authentication methods, and how to troubleshoot access issues for better Linux security."
meta_keywords: "Linux authentication, auth.log, Linux logging, user login, Linux security, system authorization, troubleshoot login, authentication methods, beginner, tutorial, guide, secure log"
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

Practice the commands in your Ubuntu VM terminal. Experiment with different options and variations to deepen your understanding.

## Quiz Question

On Debian-based systems, what is the name of the log file used for user authentication? Please answer using the filename only. The answer is case-sensitive.

## Quiz Answer

auth.log
