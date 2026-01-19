---
index: 2
lang: "en"
title: "Modifying Permissions"
meta_title: "Modifying Permissions - Permissions"
meta_description: "Learn how to change permissions in Linux using the chmod command. This guide covers both symbolic and numerical methods to help you manage file and directory access securely. Master the linux change permission process for better system administration."
meta_keywords: "linux change permission, change permission linux, how to change permissions in linux, how to change file permissions linux, chmod, file permissions, linux security, symbolic permissions, numerical permissions"
---

## Lesson Content

When you need to modify file or directory access rights, the primary tool you'll use is the `chmod` (change mode) command. Understanding **how to change permissions in Linux** is a fundamental skill for any user. The `chmod` command offers two main methods for this task: symbolic and numerical mode.

### Using Symbolic Mode

Symbolic mode is often considered more readable because it uses letters to represent users and permissions. You first specify which permission set you want to change (user, group, or other), then use a `+` to add a permission or a `-` to remove it.

- `u` (user/owner)
- `g` (group)
- `o` (others)
- `a` (all: user, group, and others)

Let's see **how to change file permissions linux** style with some examples.

To add the execute permission for the user on a file, you would use:

```bash
chmod u+x myfile
```

This command adds (`+`) the executable (`x`) permission for the user (`u`) on `myfile`.

To remove a permission, you use the `-` operator. For instance, to remove the write permission for the group:

```bash
chmod g-w myfile
```

You can also modify multiple permissions at once. The following command adds write permission for both the user and the group:

```bash
chmod ug+w myfile
```

### Using Numerical (Octal) Mode

Another powerful way to **change permission linux** offers is through numerical, or octal, mode. This method allows you to set all permissions for the user, group, and others simultaneously with a three-digit number.

The permissions are represented by the following values:

- `4`: read (r)
- `2`: write (w)
- `1`: execute (x)

To set a permission set, you add the numbers together. For example, to grant read, write, and execute permissions, you would use `4 + 2 + 1 = 7`.

Let's look at a common example:

```bash
chmod 755 myfile
```

How does this `linux change permission` command work? Let's break down the number `755`:

- **7 (User):** `4 + 2 + 1` -> The user gets read, write, and execute permissions (`rwx`).
- **5 (Group):** `4 + 0 + 1` -> The group gets read and execute permissions (`r-x`).
- **5 (Others):** `4 + 0 + 1` -> All other users get read and execute permissions (`r-x`).

### Security Considerations

While `chmod` is essential, it's crucial to use it carefully. Changing permissions without understanding the implications can expose sensitive files to unauthorized modification or viewing. For example, recursively setting `777` permissions (`chmod -R 777 /some/directory`) is a common but dangerous practice that gives everyone full read, write, and execute access. Always apply the principle of least privilege, granting only the permissions that are strictly necessary.

## Exercise

Follow these steps in your Ubuntu VM terminal to practice the concepts from this lesson:

1. **Create a test file**: Make a file to modify permissions
   ```bash
   touch myfile.txt
   ls -l myfile.txt
   ```
   Expected output:
   ```
   -rw-rw-r-- 1 user user 0 Jan 19 10:30 myfile.txt
   ```

2. **Add execute permission for owner**: Use chmod with symbolic notation
   ```bash
   chmod u+x myfile.txt
   ls -l myfile.txt
   ```
   Expected output:
   ```
   -rwxrw-r-- 1 user user 0 Jan 19 10:30 myfile.txt
   ```

3. **Remove write permission for group**: Use chmod to remove permissions
   ```bash
   chmod g-w myfile.txt
   ls -l myfile.txt
   ```
   Expected output:
   ```
   -rwxr--r-- 1 user user 0 Jan 19 10:30 myfile.txt
   ```

4. **Set permissions with octal notation**: Use numeric mode
   ```bash
   chmod 755 myfile.txt
   ls -l myfile.txt
   ```
   Expected output:
   ```
   -rwxr-xr-x 1 user user 0 Jan 19 10:30 myfile.txt
   ```

5. **Set restrictive permissions**: Make file owner-only accessible
   ```bash
   chmod 600 myfile.txt
   ls -l myfile.txt
   ```
   Expected output:
   ```
   -rw------- 1 user user 0 Jan 19 10:30 myfile.txt
   ```

6. **Clean up**: Remove test file
   ```bash
   rm myfile.txt
   ```

## Quiz Question

What number represents the read permission when using numerical format?

