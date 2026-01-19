---
title: "Creating Filesystems"
layout: default
parent: Filesystem
grand_parent: Administration
nav_order: 5
---

## Lesson Content

After you have successfully partitioned a disk, the next crucial step in Linux disk management is to create a filesystem. This process, often called formatting, organizes the partition so it can store files and directories.

### The mkfs Command

The primary tool for this task is `mkfs` (make filesystem). It's a versatile command that allows you to create a wide variety of filesystems.

Let's look at a typical example:

```bash
sudo mkfs -t ext4 /dev/sdb2
```

Here is a breakdown of the command:

- **`sudo`**: Executes the command with administrative privileges, which is required for disk management tasks.
- **`mkfs`**: The command to create a filesystem.
- **`-t ext4`**: The `-t` flag specifies the filesystem type. In this case, we are creating an `ext4` filesystem.
- **`/dev/sdb2`**: This is the target partition where the filesystem will be created.

### Common Filesystem Types

While `ext4` is a robust and widely used default for many Linux distributions, `mkfs` supports others. You might encounter different types depending on the use case, such as XFS, which is known for high performance with large files, or Btrfs, which offers modern features like snapshots. For general use, `ext4` is an excellent choice.

### A Word of Caution

You should only create a filesystem on a newly created partition or on a disk you intend to completely erase. Running the `mkfs` command on a partition that already contains data is a destructive operation. It will permanently delete all existing data, and you will likely corrupt the filesystem if you attempt to create a new one on top of an existing one without proper preparation. Always double-check your target device to avoid accidental data loss.

## Exercise

Follow these steps in your Ubuntu VM terminal to practice the concepts from this lesson:

1. **Check disk usage**: Try this command
   ```bash
   df -h
   ```
   Expected output:
   ```
   (Output will vary based on your system)
   ```

2. **View directory usage**: Try this command
   ```bash
   du -sh /home
   ```
   Expected output:
   ```
   (Output will vary based on your system)
   ```

3. **Check filesystem type**: Try this command
   ```bash
   df -T
   ```
   Expected output:
   ```
   (Output will vary based on your system)
   ```

4. **View mounted filesystems**: Try this command
   ```bash
   mount | column -t
   ```
   Expected output:
   ```
   (Output will vary based on your system)
   ```

## Quiz Question

What command is used to create a filesystem? Please answer in English.

