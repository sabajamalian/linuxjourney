---
index: 8
lang: "en"
title: "The Sticky Bit"
meta_title: "The Sticky Bit - Permissions"
meta_description: "Explore the purpose of the sticky bit in Linux and Unix file permissions. Learn how the sticky bit protects files in shared directories like /tmp and how to set it using chmod."
meta_keywords: "sticky bit, sticky bit linux, unix file permissions sticky bit, chmod +t, /tmp directory, file permissions, linux security"
---

## Lesson Content

Beyond the standard read, write, and execute permissions, Linux offers special permissions for advanced access control. The last of these special permissions we will cover is the **sticky bit**.

### What is the Sticky Bit?

The sticky bit is a permission setting that can be applied to a directory. When a directory has the sticky bit set, files within that directory can only be deleted or renamed by the file's owner, the directory's owner, or the root user. This is particularly useful for shared directories where multiple users need to create and manage their own files without interfering with others. This concept is a key part of **Unix file permissions sticky bit** management.

### A Practical Example: The /tmp Directory

A common use case for the **sticky bit in Linux** is the `/tmp` directory, which is a world-writable location for temporary files. Let's examine its permissions:

```bash
$ ls -ld /tmp
drwxrwxrwt 17 root root 4096 Dec 15 11:45 /tmp
```

Notice the `t` at the end of the permission string (`rwxrwxrwt`). This `t` indicates that the sticky bit is set. Because of this, while any user can create files in `/tmp`, they cannot delete or move files created by other users. This prevents one user from disrupting another's work in this shared space.

### How to Set the Sticky Bit

You can set the sticky bit using the `chmod` command in two ways: symbolic mode or octal (numeric) mode.

To add the sticky bit using symbolic mode:

```bash
chmod +t my_shared_dir
```

To set permissions using octal mode, you prepend a `1` to the standard three-digit permission code. The numerical representation for the sticky bit is **1**.

```bash
# This sets permissions to rwxr-xr-x with the sticky bit
chmod 1755 my_shared_dir
```

Understanding the sticky bit is essential for managing multi-user environments and securing shared directories effectively.

## Exercise

Follow these steps in your Ubuntu VM terminal to practice the concepts from this lesson:

1. **Check /tmp directory sticky bit**: View the sticky bit on /tmp
   ```bash
   ls -ld /tmp
   ```
   Expected output:
   ```
   drwxrwxrwt 15 root root 4096 Jan 19 10:30 /tmp
   (Note the 't' at the end - sticky bit)
   ```

2. **Create a directory and set sticky bit**: Make a test directory
   ```bash
   mkdir testshared
   chmod +t testshared
   ls -ld testshared
   ```
   Expected output:
   ```
   drwxrwxr-t 2 user user 4096 Jan 19 10:30 testshared
   ```

3. **Set sticky bit with octal notation**: Use numeric mode
   ```bash
   chmod 1777 testshared
   ls -ld testshared
   ```
   Expected output:
   ```
   drwxrwxrwt 2 user user 4096 Jan 19 10:30 testshared
   (1 prefix indicates sticky bit)
   ```

4. **Test sticky bit behavior**: Create a file in the directory
   ```bash
   touch testshared/myfile.txt
   ls -l testshared/
   ```
   Expected output:
   ```
   -rw-rw-r-- 1 user user 0 Jan 19 10:30 myfile.txt
   (Only owner can delete this file, even though dir is world-writable)
   ```

5. **Clean up**: Remove test directory
   ```bash
   rm -r testshared
   ```

## Quiz Question

In a long directory listing (ls -l), what single character in the permissions string represents that the sticky bit is set? Please answer with a single lowercase English letter.

