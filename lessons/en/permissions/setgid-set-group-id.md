---
index: 6
lang: "en"
title: "Setgid"
meta_title: "Setgid - Permissions"
meta_description: "Learn about Linux SGID (Set Group ID) permissions, how they work, and how to modify them. Understand this crucial Linux security concept."
meta_keywords: "Linux SGID, Set Group ID, Linux permissions, chmod g+s, Linux security, beginner Linux, Linux tutorial"
---

## Lesson Content

Similar to the set user ID permission bit, there is a set group ID (SGID) permission bit. This bit allows a program to run as if it were a member of that group.

Let's look at one example:

```bash
$ ls -l /usr/bin/wall
-rwxr-sr-x 1 root tty 19024 Dec 14 11:45 /usr/bin/wall
```

We can now see that the permission bit is in the group permission set.

### Modifying SGID

```bash
sudo chmod g+s myfile
sudo chmod 2555 myfile
```

The numerical representation for SGID is 2.

## Exercise

Follow these steps in your Ubuntu VM terminal to practice the concepts from this lesson:

1. **Find files with setgid bit**: Look for SGID files
   ```bash
   find /usr/bin -perm -2000 2>/dev/null | head -5
   ```
   Expected output:
   ```
   /usr/bin/ssh-agent
   /usr/bin/wall
   (SGID executables on system)
   ```

2. **Create a directory with SGID**: Make a directory for testing
   ```bash
   mkdir testdir
   chmod g+s testdir
   ls -ld testdir
   ```
   Expected output:
   ```
   drwxrwsr-x 2 user user 4096 Jan 19 10:30 testdir
   (Note the 's' in group execute permission)
   ```

3. **Create a file in SGID directory**: Test inheritance
   ```bash
   touch testdir/newfile.txt
   ls -l testdir/newfile.txt
   ```
   Expected output:
   ```
   -rw-rw-r-- 1 user user 0 Jan 19 10:30 testdir/newfile.txt
   (File inherits the group from parent directory)
   ```

4. **Check SGID in octal notation**: View numeric permissions
   ```bash
   stat -c "%a" testdir
   ```
   Expected output:
   ```
   2775
   (2 prefix indicates SGID bit is set)
   ```

5. **Clean up**: Remove test directory
   ```bash
   rm -r testdir
   ```

## Quiz Question

What number represents the SGID?

