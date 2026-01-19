---
title: "User Management Tools"
layout: default
parent: User Management
grand_parent: Fundamentals
nav_order: 6
---

## Lesson Content

While many enterprise environments rely on dedicated systems for identity management, understanding the fundamentals of **Linux user management** directly on a single machine is a crucial skill. Several utilities serve as **the command-line tool for managing accounts in Linux**, allowing for efficient administration from the terminal.

### Adding Users

To create a new user, you can use the `useradd` command. It is a low-level utility that creates a new user account based on default values found in `/etc/default/useradd`. While some systems also offer `adduser`, a more interactive and user-friendly script, `useradd` is the universal standard.

```bash
sudo useradd bob
```

Executing this command adds an entry for the user "bob" in the `/etc/passwd` file, sets up default group memberships, and creates a corresponding entry in the `/etc/shadow` file to store password information securely.

### Removing Users

To remove a user account, you can use the `userdel` command. This command effectively reverses the changes made by `useradd` by removing the user's entries from the system account files.

```bash
sudo userdel bob
```

By default, this command may not remove the user's home directory. You can use the `-r` flag (`userdel -r bob`) to ensure the home directory and mail spool are also deleted.

### Changing Passwords

The `passwd` command is used to set or change a user's password. A regular user can run this command to change their own password. The root user can run it to change any user's password.

```bash
passwd bob
```

When run by an administrator, the system will prompt for a new password for the specified user without asking for the old one. This is a fundamental task in **Linux user management**.

## Exercise

Follow these steps in your Ubuntu VM terminal to practice the concepts from this lesson:

1. **Create a new user (requires sudo)**: Add a test user
   ```bash
   sudo useradd -m testuser
   grep testuser /etc/passwd
   ```
   Expected output:
   ```
   testuser:x:1001:1001::/home/testuser:/bin/sh
   ```

2. **Set password for the new user**: Assign a password
   ```bash
   sudo passwd testuser
   ```
   Expected output:
   ```
   Enter new UNIX password:
   Retype new UNIX password:
   passwd: password updated successfully
   ```

3. **View user information**: Use finger or id command
   ```bash
   id testuser
   ```
   Expected output:
   ```
   uid=1001(testuser) gid=1001(testuser) groups=1001(testuser)
   ```

4. **Create a new group**: Add a test group
   ```bash
   sudo groupadd testgroup
   grep testgroup /etc/group
   ```
   Expected output:
   ```
   testgroup:x:1002:
   ```

5. **Add user to group**: Modify group membership
   ```bash
   sudo usermod -aG testgroup testuser
   id testuser
   ```
   Expected output:
   ```
   uid=1001(testuser) gid=1001(testuser) groups=1001(testuser),1002(testgroup)
   ```

6. **Clean up**: Remove test user and group
   ```bash
   sudo userdel -r testuser
   sudo groupdel testgroup
   ```

## Quiz Question

What command is used to change a password? Please answer with the command name in lowercase English letters only.

