---
index: 3
lang: "en"
title: "Ownership Permissions"
meta_title: "Ownership Permissions - Permissions"
meta_description: "Master Linux file ownership by learning how to use the chown and chgrp Linux commands. This Linux tutorial explains how to change user and group ownership for files, a key skill for managing Linux permissions."
meta_keywords: "chown, chgrp, linux file ownership, change file owner, change file group, linux permissions, linux commands, linux tutorial, linux guide, user ownership, group ownership"
---

## Lesson Content

In a Linux system, every file and directory is assigned an owner and a group. Managing **Linux file ownership** is a fundamental task for controlling access and permissions. You can modify both the user and group ownership of a file using specific **Linux commands**.

### Changing User Ownership

To transfer the ownership of a file to a different user, you use the `chown` (change owner) command. This is useful when a user's responsibilities change or when you need to assign file control to someone else. You typically need superuser privileges (`sudo`) to change the owner of a file you don't own.

```bash
sudo chown patty myfile
```

This command changes the user owner of `myfile` to the user `patty`.

### Changing Group Ownership

Similarly, you can change the group associated with a file using the `chgrp` (change group) command. This allows all members of the new group to have access based on the group's **Linux permissions**.

```bash
sudo chgrp whales myfile
```

This command sets the group ownership of `myfile` to the group `whales`.

### Changing Both User and Group

For efficiency, the `chown` command allows you to change both the user and group ownership in a single step. By separating the user and group name with a colon, you can update both attributes simultaneously.

```bash
sudo chown patty:whales myfile
```

This single command assigns user ownership to `patty` and group ownership to `whales` for the file `myfile`. This is the most common method for managing **Linux file ownership**.

## Exercise

Follow these steps in your Ubuntu VM terminal to practice the concepts from this lesson:

1. **Create a test file and check ownership**: Make a file and see who owns it
   ```bash
   touch testfile.txt
   ls -l testfile.txt
   ```
   Expected output:
   ```
   -rw-rw-r-- 1 your-username your-username 0 Jan 19 10:30 testfile.txt
   ```

2. **View file ownership details**: Use stat command
   ```bash
   stat testfile.txt
   ```
   Expected output:
   ```
   File: testfile.txt
   Size: 0           Blocks: 0          IO Block: 4096   regular empty file
   Device: 802h/2050d  Inode: 123456      Links: 1
   Access: (0664/-rw-rw-r--)  Uid: ( 1000/your-username)   Gid: ( 1000/your-username)
   ```

3. **Create a directory and check ownership**: Make a directory
   ```bash
   mkdir testdir
   ls -ld testdir
   ```
   Expected output:
   ```
   drwxrwxr-x 2 your-username your-username 4096 Jan 19 10:30 testdir
   ```

4. **View numeric user and group IDs**: Check IDs with stat
   ```bash
   stat -c "Owner UID: %u, Owner GID: %g" testfile.txt
   ```
   Expected output:
   ```
   Owner UID: 1000, Owner GID: 1000
   ```

5. **Clean up**: Remove test files
   ```bash
   rm testfile.txt
   rmdir testdir
   ```

## Quiz Question

What command is used to change the user ownership of a file? Please provide only the command name in lowercase English letters.

## Quiz Answer

chown
