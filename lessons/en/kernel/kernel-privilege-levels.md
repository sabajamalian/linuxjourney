---
index: 2
lang: "en"
title: "Privilege Levels"
meta_title: "Privilege Levels - Kernel"
meta_description: "Explore the core concepts of Linux privilege levels. This lesson explains the difference between kernel mode and user mode, the role of protection rings, and how system calls provide privileged access to hardware. Understand how the kernel manages security and kernel privileges."
meta_keywords: "Linux privilege levels, kernel mode, user mode, protection rings, system calls, privileged access, kernel privileges, what is the difference between kernel mode and user mode, Linux security"
---

## Lesson Content

The next few lessons cover more theoretical concepts. If you prefer hands-on practice, feel free to skip ahead and return to these topics later.

A fundamental aspect of the Linux architecture is the separation between user space and the kernel. But why can't we combine their powers into a single layer? The reason is security and stability, which is achieved by having them operate in different modes.

### What is the Difference Between Kernel Mode and User Mode

The system operates in two distinct modes: kernel mode and user mode. This separation is crucial for protecting the system's hardware and resources from direct, uncontrolled access by applications.

In **kernel mode**, the kernel has complete and unrestricted access to the hardware; it controls everything. This is the highest level of privilege.

In **user mode**, applications have very limited access to a small, safe portion of memory and CPU resources.

When a user application needs to perform an action involving hardware—such as reading from a disk, sending data over the network, or accessing a peripheral—it cannot do so directly. These operations must be handled by the kernel in kernel mode. This design prevents a malfunctioning or malicious program from compromising the entire system. For example, you wouldn't want spyware to have direct hardware access, as it could read all your data or control your webcam.

### Protection Rings and Privileged Access

These different modes are often described as **privilege levels** or **protection rings**. Imagine a fortress with concentric walls: the innermost area is the most secure and has the highest authority. The protection rings in a computer work similarly, with the innermost ring corresponding to the highest privilege level.

On a standard x86 computer architecture, there are two primary levels:

- **Ring 0:** This is where the kernel runs. It has the highest level of **kernel privileges**, can execute any system instruction, and is given full trust to manage the hardware. This is the core of **privileged access**.
- **Ring 3:** This is the level where user-mode applications run. It is the least privileged ring and has no direct access to hardware.

This ring-based security model ensures that user applications are isolated from critical system components. But if applications are always in a different mode than the kernel, how can they perform necessary hardware operations?

### System Calls and Kernel Privileges

The bridge between user mode and kernel mode is the **system call**. When a user application needs to perform a privileged task, it makes a system call to request that the kernel perform the action on its behalf.

This process allows the application to temporarily and safely transition from user mode to kernel mode to execute a specific, controlled instruction. Once the task is complete, the system switches back to user mode. This mechanism ensures that applications can get the services they need without gaining dangerous, direct **privileged access** to the hardware.

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

What ring number has the highest privileges?

## Quiz Answer

0
