---
index: 4
lang: "en"
title: "/etc/shadow"
meta_title: "/etc/shadow - User Management"
meta_description: "Explore the /etc/shadow file in Linux, a critical component for user authentication. Learn how to view it with 'cat /etc/shadow' and understand the structure of the etc shadow file, which stores encrypted passwords and policy information."
meta_keywords: "etc shadow, etc/shadow file in linux, cat /etc/shadow, etc shadow in linux, /etc/shadow, user authentication, password security, Linux system administration"
---

## Lesson Content

The `/etc/shadow` file is a critical component in Linux systems for storing sensitive user authentication information. Unlike the world-readable `/etc/passwd` file, it requires superuser privileges to access, providing a secure location for password data.

### The Role of the etc/shadow File in Linux

The primary purpose of the **etc/shadow file in Linux** is to store encrypted user passwords and password aging policies. By separating this sensitive data from the general user information in `/etc/passwd`, the system enhances security. If a non-privileged user could read the password hashes, they could attempt to crack them offline.

### Viewing the File with cat /etc/shadow

To inspect the contents of this file, you must use a command with superuser privileges, such as `sudo`. The `cat /etc/shadow` command is commonly used for this purpose.

```bash
$ sudo cat /etc/shadow

root:MyEPTEa$6Nonsense:15000:0:99999:7:::
```

The output format of the **etc shadow** file is a series of colon-separated fields, with each line representing a single user.

### Understanding the File Structure

Each line in `/etc/shadow` contains nine fields, separated by colons:

1. **Username**: The user's login name.
2. **Encrypted password**: The hashed user password. An asterisk (`*`) or exclamation mark (`!`) here means the account is locked.
3. **Date of last password change**: The number of days since January 1, 1970, that the password was last changed. A value of `0` forces a password change at the next login.
4. **Minimum password age**: The minimum number of days that must pass before the user can change their password again.
5. **Maximum password age**: The maximum number of days the password is valid. After this period, the user must change it.
6. **Password warning period**: The number of days before the password expires that the user will receive a warning message.
7. **Password inactivity period**: The number of days after a password expires that the account is disabled.
8. **Account expiration date**: An absolute date, expressed as days since January 1, 1970, when the user account will be disabled.
9. **Reserved field**: This field is reserved for future use.

While the `/etc/shadow` file is fundamental, most modern distributions supplement it with other authentication mechanisms, such as Pluggable Authentication Modules (PAM), which offer more flexible and advanced authentication schemes.

## Exercise

Follow these steps in your Ubuntu VM terminal to practice the concepts from this lesson:

1. **View the shadow file (requires sudo)**: Display encrypted passwords
   ```bash
   sudo cat /etc/shadow | head -5
   ```
   Expected output:
   ```
   root:*:18000:0:99999:7:::
   daemon:*:18000:0:99999:7:::
   (encrypted password hashes)
   ```

2. **Check your own shadow entry**: Find your user's password info
   ```bash
   sudo grep "$USER" /etc/shadow
   ```
   Expected output:
   ```
   your-username:$6$randomhash...:18500:0:99999:7:::
   ```

3. **View shadow file permissions**: See why sudo is needed
   ```bash
   ls -l /etc/shadow
   ```
   Expected output:
   ```
   -rw-r----- 1 root shadow 1234 Jan 15 10:30 /etc/shadow
   (Only root and shadow group can read)
   ```

4. **Count password entries**: Count lines in shadow file
   ```bash
   sudo wc -l /etc/shadow
   ```
   Expected output:
   ```
   45 /etc/shadow
   ```

## Quiz Question

No questions, move along!

## Quiz Answer
