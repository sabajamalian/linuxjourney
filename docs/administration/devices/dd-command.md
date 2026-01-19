---
title: "dd"
layout: default
parent: Devices
grand_parent: Administration
nav_order: 7
---

## Lesson Content

The `dd` command is a versatile and powerful utility for converting and copying data. It operates by reading from an input file or data stream and writing to an output file or data stream, making it an essential `dd tool` for many system administration tasks.

### Understanding the dd Command

At its core, `dd` copies data byte by byte. Consider the following command:

```bash
dd if=/home/pete/backup.img of=/dev/sdb bs=1024
```

This command copies the contents of the file `backup.img` to the block device `/dev/sdb`. It performs this operation by copying the data in blocks of 1024 bytes until the entire input file has been read.

### Essential dd Options

The behavior of the `dd` command is controlled by several key options:

- `if=file`: Specifies the **input file**. `dd` will read from this file instead of standard input.
- `of=file`: Specifies the **output file**. `dd` will write to this file instead of standard output.
- `bs=bytes`: Sets the **block size**. `dd` reads and writes this many bytes at a time. You can use suffixes for larger units, such as `k` for kilobytes (1024 bytes), `M` for megabytes, and `G` for gigabytes. For example, `bs=1M`.
- `count=number`: Copies only this specified **number of blocks**.

### Using bs and count Together

The `count` option is useful when you need to copy a specific amount of data. The total data copied will be `bs` multiplied by `count`. For example, if you run the following command on a 10M file:

```bash
dd if=/home/pete/backup.img of=/dev/sdb bs=1M count=2
```

Even though `backup.img` is 10M, this command instructs `dd` to copy 2 blocks, each 1M in size. As a result, only 2M of data will be copied, leading to an incomplete transfer. While `count` is valuable in certain scenarios, you can often omit it if your goal is to copy an entire file. Optimizing `bs` can significantly improve transfer speeds, but the default settings are often sufficient.

### The Power and Danger of dd

The `dd linux` command is extremely powerful. You can use it to create backups of entire disk drives, restore disk images, and securely wipe data. However, this power comes with a risk. A small mistake, such as swapping the `if` and `of` values, can result in irreversible data loss. Always double-check your commands before executing them, especially when writing to a device like `/dev/sda`.

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

What is the `dd` option for block size? Please answer using only lowercase English letters.

