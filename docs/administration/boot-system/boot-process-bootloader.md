---
title: "Boot Process: Bootloader"
layout: default
parent: Boot System
grand_parent: Administration
nav_order: 3
---

## Lesson Content

### What is a Bootloader in Linux

After the BIOS/UEFI finishes its tasks, it hands over control to the next stage of the boot process: the bootloader. A **bootloader in Linux** is a small program that loads the operating system's kernel into memory and then executes it. It acts as the bridge between the system's firmware and the Linux kernel.

### The Role of the Linux Boot Loader

The primary responsibilities of a **Linux boot loader** are straightforward but critical:

- **Operating System Selection**: It can present a menu to boot into various operating systems, including non-Linux systems, if you have a multi-boot setup.
- **Kernel Selection**: It allows you to choose which version of the Linux kernel to load, which is useful for troubleshooting or testing.
- **Passing Kernel Parameters**: It specifies crucial parameters that the kernel needs to start correctly.

The most common **Linux bootloader** is GRUB (GRand Unified Bootloader), which you are most likely using. While other bootloaders like LILO, SYSLINUX, and Coreboot exist, this lesson will focus on GRUB.

### Common Kernel Parameters in GRUB

The main goal of the bootloader is to load the kernel, but it needs instructions on how and where to find it. These instructions are provided as kernel parameters. You can typically view or edit these parameters by pressing the 'e' key in the **GRUB** menu during startup.

Here are some of the most common parameters you will encounter:

- `initrd` - Specifies the location of the initial RAM disk, a temporary root filesystem loaded into memory. We will cover this in more detail in the next lesson.
- `BOOT_IMAGE` - Defines the path to the kernel image file that should be loaded.
- `root` - Points to the location of the actual root filesystem. The kernel uses this path to find the `init` process. This is often represented by a device name (e.g., `/dev/sda1`) or a UUID.
- `ro` - A standard parameter that instructs the kernel to mount the root filesystem in read-only mode initially. This is a safety measure to allow filesystem checks to run before any changes are made.
- `quiet` - This parameter suppresses most of the detailed boot messages, providing a cleaner, less verbose startup screen.
- `splash` - Enables a graphical splash screen to be displayed during the boot process instead of text messages.

## Exercise

Follow these steps in your Ubuntu VM terminal to practice the concepts from this lesson:

1. **View boot messages**: Try this command
   ```bash
   dmesg | head -20
   ```
   Expected output:
   ```
   (Output will vary based on your system)
   ```

2. **Check bootloader**: Try this command
   ```bash
   ls -l /boot/
   ```
   Expected output:
   ```
   (Output will vary based on your system)
   ```

3. **View system uptime**: Try this command
   ```bash
   uptime
   ```
   Expected output:
   ```
   (Output will vary based on your system)
   ```

4. **Check boot time**: Try this command
   ```bash
   who -b
   ```
   Expected output:
   ```
   (Output will vary based on your system)
   ```

## Quiz Question

What kernel parameter makes it so you don't see bootup messages? Please answer with the single-word parameter in lowercase English.

