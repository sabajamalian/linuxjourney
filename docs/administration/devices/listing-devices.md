---
title: "lsusb, lspci, lssci"
layout: default
parent: Devices
grand_parent: Administration
nav_order: 6
---

## Lesson Content

Just as you use the `ls` command to list files, Linux provides similar tools for listing hardware devices. These commands are essential for identifying the hardware connected to your system.

### Listing USB Devices with lsusb

To see all the USB devices connected to your system, you can use the `lsusb` command. This command scans the USB hubs and reports information about the devices it finds, such as webcams, keyboards, and external drives.

```bash
lsusb
```

For a more structured view, you can use the `lsusb -t` command. This option displays the USB devices in a tree-like structure, which is helpful for understanding how devices are physically connected to the USB controllers and hubs.

### Listing PCI Devices with lspci

The `lspci` command is used to list all PCI (Peripheral Component Interconnect) devices. These are typically internal components connected to the motherboard, such as graphics cards, network adapters, and sound cards. This command provides a quick overview of your system's core hardware.

```bash
lspci
```

### Listing SCSI and SATA Devices with lssci

For storage devices, the `lssci` command is particularly useful. It lists all connected SCSI and SATA devices, which commonly include hard drives, SSDs, and optical drives (CD/DVD/Blu-ray). While other commands might show the storage controller, `lssci` provides direct information about the storage devices themselves, making it a valuable tool for system administrators and users managing storage.

```bash
lssci
```

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

What command is used to view a list of connected USB devices? (Please answer in lowercase English characters only.)

