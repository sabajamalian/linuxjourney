---
title: "Umask"
layout: default
parent: Permissions
grand_parent: Fundamentals
nav_order: 4
---

## Lesson Content

Every file that gets created comes with a default set of permissions. If you ever want to change that default set of permissions, you can do so with the `umask` command. This command uses the 3-bit permission set we see in numerical permissions.

Instead of adding these permissions, however, `umask` takes away these permissions.

```bash
umask 021
```

In the above example, we are stating that we want the default permissions of new files to allow users access to everything, but for groups, we want to take away their write permission, and for others, we want to take away their executable permission. The default `umask` on most distributions is `022`, meaning full user access, but no write access for group and other users.

When you run the `umask` command, it will apply that default set of permissions to any new file you create. However, if you want it to persist, you'll have to modify your startup file (`.profile`), but we'll discuss that in a later lesson.

## Exercise

Follow these steps in your Ubuntu VM terminal to practice the concepts from this lesson:

1. **Check current umask value**: View your default umask
   ```bash
   umask
   ```
   Expected output:
   ```
   0002
   (Common default umask value)
   ```

2. **Create a file and check default permissions**: See umask in action
   ```bash
   touch testfile1.txt
   ls -l testfile1.txt
   ```
   Expected output:
   ```
   -rw-rw-r-- 1 user user 0 Jan 19 10:30 testfile1.txt
   (666 - 002 = 664 permissions)
   ```

3. **Change umask temporarily**: Set a more restrictive umask
   ```bash
   umask 0077
   umask
   ```
   Expected output:
   ```
   0077
   ```

4. **Create a file with new umask**: See how permissions change
   ```bash
   touch testfile2.txt
   ls -l testfile2.txt
   ```
   Expected output:
   ```
   -rw------- 1 user user 0 Jan 19 10:30 testfile2.txt
   (666 - 077 = 600 permissions)
   ```

5. **Create a directory with current umask**: Check directory permissions
   ```bash
   mkdir testdir
   ls -ld testdir
   ```
   Expected output:
   ```
   drwx------ 2 user user 4096 Jan 19 10:30 testdir
   (777 - 077 = 700 permissions)
   ```

6. **Restore default umask and clean up**: Reset umask
   ```bash
   umask 0002
   rm testfile1.txt testfile2.txt
   rmdir testdir
   ```

## Quiz Question

What command is used to change default file permissions?

