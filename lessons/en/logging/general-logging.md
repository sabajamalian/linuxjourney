---
index: 3
lang: "en"
title: "General Logging"
meta_title: "General Logging - Logging"
meta_description: "A beginner's guide to general Linux logs. Learn about /var/log/messages and syslog for effective system monitoring, log analysis, and Linux troubleshooting."
meta_keywords: "Linux logs, syslog, var/log/messages, Linux troubleshooting, system logs, log analysis, system monitoring, Linux guide, Linux beginner, /var/log"
---

## Lesson Content

Your Linux system diligently records events, errors, and operational information in files known as **system logs**. These logs are invaluable for **Linux troubleshooting** and understanding system behavior. For any **Linux beginner**, learning to read these logs is a crucial step. Most important log files are stored in the `/var/log` directory. In this lesson, we'll explore two of the most common general-purpose logs.

### The General Messages Log

On many Linux distributions, `/var/log/messages` serves as a central repository for a wide range of system events. It captures non-critical, informational messages from the kernel, daemons, and various services. This makes it an excellent starting point for getting a general overview of your system's activity and for initial **Linux troubleshooting**. Think of it as the default inbox for your system's daily chatter.

### The Comprehensive System Log

The `/var/log/syslog` file often contains a more comprehensive collection of **system logs**. While its content can overlap with `/var/log/messages`, it typically includes a broader range of information, everything except for authentication-related messages. This detailed log is particularly useful for in-depth debugging and **log analysis** when you need to trace a specific problem from start to finish.

### Effective System Monitoring with Logs

While these two files are powerful tools for **system monitoring**, remember that the `/var/log` directory contains many other specialized logs (e.g., for authentication, package management, or specific applications). The exact logging behavior can also vary depending on your Linux distribution and its configuration, with some modern systems using `systemd-journald`. However, understanding `/var/log/messages` and `syslog` provides a solid foundation for any aspiring Linux user and is a key part of any **Linux guide**.

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

Which log file typically records everything except authentication messages? (Please answer in English, using only lowercase letters.)

