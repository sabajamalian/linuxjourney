---
index: 3
lang: "en"
title: "Device Names"
meta_title: "Device Names - Devices"
meta_description: "Explore common Linux device names for storage and peripherals. This guide explains the naming convention for SCSI disks (like sda), what sda stands for, and pseudo-devices like /dev/null."
meta_keywords: "linux device names, linux device name, what does sda stand for, sd element name, what would commonly be the device name for the first partition on the second scsi disk, /dev, SCSI devices, pseudo devices, PATA devices"
---

## Lesson Content

In Linux, every device is represented by a file in the `/dev` directory. Understanding the naming conventions for these files is crucial for system administration. Here are the most common types of Linux device names you will encounter.

### SCSI and Modern Storage Devices

Even if your machine uses modern storage like SATA, NVMe, or USB drives, the Linux kernel often manages them through its SCSI (Small Computer System Interface) subsystem. This is why the most common prefix for storage devices is `sd`, which originally stood for "SCSI disk".

The `sd element name` follows a clear pattern:

- The `sd` prefix indicates a mass storage device.
- The next letter represents the drive itself, assigned in the order of detection (`a` for the first, `b` for the second, and so on).
- A number at the end indicates the partition on that drive.

Common SCSI device files include:

- `/dev/sda`: The first storage drive.
- `/dev/sdb`: The second storage drive.
- `/dev/sda3`: The third partition on the first storage drive.

So, what would commonly be the device name for the first partition on the second SCSI disk? Following the pattern, the second disk is `sdb`, and its first partition is `1`. Therefore, the device name is `/dev/sdb1`.

### Pseudo-Devices

Pseudo-devices are special files that do not correspond to any physical hardware but provide useful system functions. They are typically character devices.

- `/dev/zero`: Accepts and discards all input. When read, it produces a continuous stream of NULL (zero value) bytes.
- `/dev/null`: Accepts and discards all input written to it, and produces no output when read.
- `/dev/random`: Produces a stream of random numbers generated from environmental noise.

### Legacy PATA Devices

On older systems, you might encounter hard drives that use the Parallel ATA (PATA) interface. The Linux device name for these drives uses an `hd` prefix.

- `/dev/hda`: The first PATA hard disk.
- `/dev/hdd2`: The second partition on the fourth PATA hard disk.

## Exercise

Follow these steps in your Ubuntu VM terminal to practice the concepts from this lesson:

1. **List block devices**: Try this command
   ```bash
   lsblk
   ```
   Expected output:
   ```
   (Output will vary based on your system)
   ```

2. **View device information**: Try this command
   ```bash
   ls -l /dev/
   ```
   Expected output:
   ```
   (Output will vary based on your system)
   ```

3. **Check device types**: Try this command
   ```bash
   file /dev/sda` (if available)
   ```
   Expected output:
   ```
   (Output will vary based on your system)
   ```

4. **View USB devices**: Try this command
   ```bash
   lsusb
   ```
   Expected output:
   ```
   (Output will vary based on your system)
   ```

## Quiz Question

What would commonly be the device name for the first partition on the second SCSI disk? Please provide the answer in English, paying attention to the correct case.

## Quiz Answer

/dev/sdb1
