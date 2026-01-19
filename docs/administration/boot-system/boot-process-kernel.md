---
title: "Boot Process: Kernel"
layout: default
parent: Boot System
grand_parent: Administration
nav_order: 4
---

## Lesson Content

Once the bootloader has loaded the kernel into memory and passed the necessary parameters, the kernel takes control of the system. Let's explore what happens next.

### Kernel Initialization and the Initramfs

A classic challenge during boot-up is that the kernel needs drivers to access hardware devices, but those drivers often reside on a storage device that the kernel can't access yet. To solve this, Linux uses a temporary root filesystem.

In older systems, this was handled by an `initrd` (initial RAM disk). The kernel would load this disk image, find the necessary drivers, and then switch to the real root filesystem. Modern systems, including distributions like Ubuntu, use `initramfs` (initial RAM filesystem). Unlike `initrd`, `initramfs` is a `cpio` archive that is unpacked into a temporary filesystem directly in memory. This approach is more efficient as it avoids the overhead of creating and mounting a block device. The `initramfs` contains just the essential modules the kernel needs to access the actual `boot partition` and other hardware.

### Mounting the Boot Root Filesystem

With the drivers loaded from `initramfs`, the kernel can now locate and mount the main `boot root` filesystem. The location of this filesystem is typically passed as a parameter by the bootloader, which can be configured in files like `/etc/default/grub`.

First, the kernel mounts the `boot root` partition in read-only mode. This is a safety measure that allows the `fsck` (file system check) utility to run and verify the integrity of the filesystem without risking data corruption. After the check completes successfully, the kernel remounts the filesystem in read-write mode.

Finally, with the root filesystem fully available, the kernel starts the very first user-space program: `init`. This program is responsible for bringing the rest of the system online.

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

What is used in modern systems to load a temporary root filesystem? Please answer in English, using only lowercase letters.

