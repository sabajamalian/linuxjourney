---
title: "ps (Processes)"
layout: default
parent: Processes
grand_parent: Fundamentals
nav_order: 1
---

## Lesson Content

### Understanding Linux Processes

Processes are the programs currently running on your machine. The Linux kernel manages them, and each process is assigned a unique number called the **process ID (PID)**. PIDs are typically assigned sequentially as new processes are created.

### Basic ps Command Usage

To get a glimpse of your active processes, simply run the `ps` command. This provides a quick snapshot of the processes associated with your current terminal session.

```plaintext
$ ps

PID        TTY     STAT   TIME          CMD
41230    pts/4    Ss        00:00:00     bash
51224    pts/4    R+        00:00:00     ps
```

This output shows a few key details:

- **PID**: The unique Process ID.
- **TTY**: The controlling terminal for the process.
- **STAT**: The current status of the process.
- **TIME**: The total CPU time the process has used.
- **CMD**: The command that started the process.

### Exploring ps with BSD-Style Options

The `ps` command is highly versatile, with many options that fall into different syntax styles (BSD, System V, GNU). The BSD style, which doesn't use a dash for options, is quite common. A popular combination is `ps aux`:

```bash
ps aux
```

Here's what these options mean:

- **a**: Displays all processes for all users.
- **u**: Provides a detailed, user-oriented format.
- **x**: Includes processes not attached to any terminal. These often include system daemons that start at boot and show a `?` in the TTY column.

This command gives a much richer output with additional columns like `USER`, `%CPU`, `%MEM`, `VSZ`, and `RSS`. For now, we'll focus on PID, STAT, and COMMAND.

### Using the ps -ef Command in Linux

Another extremely popular syntax is the System V style. You will frequently see the **ps -ef command** used by system administrators. This is a powerful way to get a full picture of everything running on your system.

```bash
ps -ef
```

The **ps -ef linux** command provides a full listing of all processes.

- **-e**: Selects every process on the system.
- **-f**: Displays a "full-format" listing, which includes details like UID, PPID (Parent Process ID), C (CPU utilization), and STIME (start time).

Many users prefer `ps -ef` over `ps aux` for its clear, hierarchical view and detailed information. When troubleshooting on a Linux system, running **linux ps -ef** is often one of the first steps to diagnose issues. A simpler variation, `ps -e linux`, will also list all processes but in a less detailed format.

### Real-Time Monitoring with top

While `ps` gives you a snapshot, the `top` command provides a real-time, dynamic view of the processes on your system. It's an excellent tool for identifying which processes are consuming the most CPU or memory. By default, the display refreshes every few seconds.

```bash
top
```

## Exercise

Follow these steps in your Ubuntu VM terminal to practice the concepts from this lesson:

1. **View your current processes**: See processes in your terminal session
   ```bash
   ps
   ```
   Expected output:
   ```
     PID TTY          TIME CMD
    1234 pts/0    00:00:00 bash
    5678 pts/0    00:00:00 ps
   ```

2. **View all processes**: Use ps aux to see all running processes
   ```bash
   ps aux | head -10
   ```
   Expected output:
   ```
   USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
   root         1  0.0  0.1 225848  9476 ?        Ss   Jan19   0:03 /sbin/init
   root         2  0.0  0.0      0     0 ?        S    Jan19   0:00 [kthreadd]
   ```

3. **Filter processes by name**: Find all bash processes
   ```bash
   ps aux | grep bash
   ```
   Expected output:
   ```
   user      1234  0.0  0.1  21536  5124 pts/0    Ss   10:30   0:00 /bin/bash
   ```

4. **View processes in tree format**: See process hierarchy
   ```bash
   ps auxf | head -20
   ```
   Expected output:
   ```
   (Shows processes in tree structure with parent-child relationships)
   ```

5. **Use ps with System V style**: Try the ps -ef command
   ```bash
   ps -ef | head -10
   ```
   Expected output:
   ```
   UID        PID  PPID  C STIME TTY          TIME CMD
   root         1     0  0 Jan19 ?        00:00:03 /sbin/init
   ```

## Quiz Question

What `ps` flag, when used with the `a` and `x` flags, is used to view detailed, user-oriented information about processes? Please answer with a single lowercase English letter.

