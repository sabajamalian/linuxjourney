---
index: 5
lang: "en"
title: "/etc/group"
meta_title: "/etc/group - User Management"
meta_description: "Explore the /etc/group file in Linux to understand group management. Learn how to view group data with cat /etc/group, and understand the structure including GID and user lists. This guide covers the essentials of the etc group linux file."
meta_keywords: "/etc/group, /etc/group linux, /etc/group file in linux, cat /etc/group, etc group linux, group management, GID, Linux permissions, Linux groups"
---

## Lesson Content

In Linux, managing permissions for multiple users is streamlined through the use of groups. The central file for this is `/etc/group`, which defines the groups on the system and their members.

### What is the /etc/group file?

The `/etc/group` file in Linux is a plain text file that contains the list of all user groups. Each group can be assigned specific permissions to files and directories, allowing administrators to manage access rights efficiently for multiple users at once. Understanding this file is crucial for proper user and permission management in any `etc group linux` environment.

### Viewing Group Information

To inspect the contents of this file, you can use a simple command. Running `cat /etc/group` in your terminal will display all the group definitions on your system.

```bash
$ cat /etc/group

root:*:0:pete
```

### Structure of the /etc/group File

Similar to the `/etc/passwd` file, each line in the `/etc/group` file represents a single group and contains four fields separated by colons (`:`).

1. **Group Name**: The unique name of the group.
2. **Group Password**: This field is a legacy feature and is rarely used. Modern systems use tools like `sudo` for elevated privileges instead of group passwords. You will typically see a placeholder like an asterisk (`*`) or an 'x'.
3. **Group ID (GID)**: A unique numerical identifier for the group. The system often uses the GID internally instead of the group name.
4. **List of Users**: A comma-separated list of usernames that are members of this group.

In the example `root:*:0:pete`, the group name is `root`, there is no password, the GID is `0`, and the user `pete` is a member.

## Exercise

Practice the commands in your Ubuntu VM terminal. Experiment with different options and variations to deepen your understanding.

## Quiz Question

What is the GID of root?

## Quiz Answer

0
