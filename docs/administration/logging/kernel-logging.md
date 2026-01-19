---
title: "Kernel Logging"
layout: default
parent: Logging
grand_parent: Administration
nav_order: 4
---

## Lesson Content

The Linux kernel is the core of the operating system, and it generates messages about its operations, hardware status, and potential issues. Accessing this information is crucial for system administration and troubleshooting. This is where the kernel log comes in.

### The Kernel Ring Buffer and dmesg

During boot-time, your system logs a wealth of information from the kernel ring buffer. This buffer contains messages about hardware drivers being loaded, kernel status updates, and other events that occur during the startup process.

This log can be viewed using the `dmesg` command. The contents are also often written to `/var/log/dmesg`, but be aware that this file is typically cleared and rewritten on every reboot. While you might not need it daily, the `dmesg` output is the first place to check if you encounter a hardware issue or a problem during bootup.

### The Primary Kernel Log File

For a more persistent record of kernel activity, you can turn to `/var/log/kern.log`. This file is the primary destination for the `kernel log linux` systems use. It captures kernel information and events as they happen on your running system.

The `kern.log` file also includes the output from `dmesg`, making it a comprehensive source for kernel-related messages. If you need to investigate a `kernel log` from a past event that is no longer in the ring buffer, the `kern log` is the correct place to look.

### Why Kernel Logs Matter

Understanding how to read the `kernel log` is a fundamental skill. These logs provide deep insights into your system's interaction with its hardware. By examining `kern.log` or the output of `dmesg`, you can diagnose driver problems, investigate unexpected hardware behavior, and monitor the overall health of the kernel.

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

What command can be used to view kernel bootup messages? Please answer using only the lowercase English command.

