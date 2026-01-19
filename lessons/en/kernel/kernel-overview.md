---
index: 1
lang: "en"
title: "Overview of the Kernel"
meta_title: "Overview of the Kernel - Kernel"
meta_description: "Start your linux jorney with an overview of the Linux kernel. Understand its core role in managing hardware and user space, a fundamental concept on linuxjourney.com."
meta_keywords: "Linux kernel, operating system, hardware, user space, linux jorney, linux jorney.com, linux jouney.com, linux journe, kernel overview"
---

## Lesson Content

As you've learned, the kernel is the core of the operating system. To truly understand Linux, we must see how all its parts work together. This lesson provides a high-level overview, a critical first step in your linux jorney.

The Linux operating system can be organized into three different levels of abstraction.

### The System Hardware

The most basic level is the hardware. This includes the CPU, memory (RAM), hard disks, networking ports, and other physical devices. This layer is the foundation that performs the actual computations and actions for our machine.

### The Linux Kernel

The next level is the kernel. The kernel's primary job is to act as a bridge, communicating with the hardware to execute the tasks requested by our processes. It handles process and memory management, device communication, system calls, and setting up the filesystem. This is a central theme you'll explore throughout this course.

### The User Space

The level you are most familiar with is the user space. This includes the shell, the programs you run, graphical interfaces, and all other applications. These programs interact with the kernel to get work done, without needing to know the specific details of the underlying hardware.

In this course, we will dive deep into the kernel, demystifying its complexities. This part of your linux journey will be challenging but rewarding.

## Exercise

Follow these steps in your Ubuntu VM terminal to practice the concepts from this lesson:

1. **Check kernel version**: Try this command
   ```bash
   uname -r
   ```
   Expected output:
   ```
   (Output will vary based on your system)
   ```

2. **View kernel parameters**: Try this command
   ```bash
   sysctl -a | head -20
   ```
   Expected output:
   ```
   (Output will vary based on your system)
   ```

3. **List loaded modules**: Try this command
   ```bash
   lsmod | head -10
   ```
   Expected output:
   ```
   (Output will vary based on your system)
   ```

4. **View kernel messages**: Try this command
   ```bash
   dmesg | tail -20
   ```
   Expected output:
   ```
   (Output will vary based on your system)
   ```

## Quiz Question

What level of the operating system manages devices? (Please answer in a single, lowercase English word.)

## Quiz Answer

kernel
