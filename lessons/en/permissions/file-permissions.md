---
index: 1
lang: "en"
title: "File Permissions"
meta_title: "File Permissions - Permissions"
meta_description: "A key part of our complete linux tutorial. Learn about Linux file permissions, including the rwx bits for user, group, and other. Master the `ls -l` output and understand file modes."
meta_keywords: "file permissions, linux file permissions, best way to learn linux, complete linux tutorial, rwx permissions, ls -l command, file modes, linux guide"
---

## Lesson Content

In Linux, everything is a file, and managing access to these files is a critical skill. Understanding **file permissions** is fundamental for system security and administration. Let's explore how to read and interpret these permissions.

### Introduction to File Permissions

When we list files in a detailed format, we see a string of characters that define their permissions. Let's look at an example using the `ls -l` command:

```bash
$ ls -l Desktop/
drwxr-xr-x 2 pete penguins 4096 Dec 1 11:45 .
```

This output provides a wealth of information, but we will focus on the first column, `drwxr-xr-x`, which represents the file type and its permissions.

### Decoding the Permission String

The permission string has four main parts. The first character indicates the file type. In our example, the **d** signifies that `Desktop` is a directory. For a regular file, you would see a hyphen (`-`).

The next nine characters represent the actual **file permissions**. These are divided into three sets of three characters each. To make it clearer, we can visualize them like this:

```plaintext
d | rwx | r-x | r-x
```

Each character in these sets corresponds to a specific permission:

- **r**: Read permission.
- **w**: Write permission.
- **x**: Execute permission.
- **-**: No permission granted.

The meaning of these permissions can change slightly depending on whether it's a file or a directory. For example, execute (`x`) permission on a directory allows you to enter it, while on a file, it allows you to run it as a program.

### User, Group, and Other Permissions

The three sets of permissions apply to different levels of access:

1. **User (Owner)**: The first set (`rwx`) applies to the owner of the file, which is `pete` in our example. The owner has read, write, and execute permissions.
2. **Group**: The second set (`r-x`) applies to the group associated with the file, which is `penguins`. Members of this group have read and execute permissions but cannot write to the file.
3. **Other**: The final set (`r-x`) applies to all other users on the system. They have read and execute permissions.

Mastering **file permissions** is a core concept, and this foundation is essential as you continue through this **complete linux tutorial**.

## Exercise

Follow these steps in your Ubuntu VM terminal to practice the concepts from this lesson:

1. **Create a test file and check permissions**: Make a file and view its permissions
   ```bash
   touch testfile.txt
   ls -l testfile.txt
   ```
   Expected output:
   ```
   -rw-rw-r-- 1 user user 0 Jan 19 10:30 testfile.txt
   ```

2. **Understand permission notation**: Break down the permission string
   - First character: file type (- for regular file, d for directory)
   - Next 9 characters: rwxrwxrwx (owner, group, others)
   - rw-rw-r-- means: owner can read/write, group can read/write, others can only read

3. **Check directory permissions**: View permissions of a directory
   ```bash
   ls -ld /home
   ```
   Expected output:
   ```
   drwxr-xr-x 3 root root 4096 Jan 15 10:30 /home
   ```

4. **View permissions in octal**: Use stat to see numeric permissions
   ```bash
   stat -c "%a %n" testfile.txt
   ```
   Expected output:
   ```
   664 testfile.txt
   ```

5. **Clean up**: Remove test file
   ```bash
   rm testfile.txt
   ```

## Quiz Question

What permission bit is used for executable? Please answer in English, paying close attention to case sensitivity.

