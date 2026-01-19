---
title: "niceness"
layout: default
parent: Processes
grand_parent: Fundamentals
nav_order: 8
---

## Lesson Content

When you run multiple applications on your computer, it seems like they are all running simultaneously. In reality, the CPU is rapidly switching between them, giving each process a small amount of processing time.

### How the CPU Manages Processes

Each process is allocated a small amount of CPU time called a "time slice". After its time slice, a process is paused, and the CPU moves to the next one. By default, the Linux kernel schedules processes in a round-robin fashion, ensuring every process gets a fair share of CPU time until it completes. The kernel's scheduler is highly efficient at managing these rapid switches.

### What is Niceness in Linux

While processes cannot directly control their CPU time, you can influence the kernel's scheduling decisions. This is done by adjusting the **linux niceness** value of a process. The term "niceness" refers to how "nice" a process is to other processes on the system.

The **niceness of a process** is represented by a number ranging from -20 (highest priority) to 19 (lowest priority).

- A high niceness value (e.g., 19) means the process is very "nice" and has a low priority, yielding CPU time to others.
- A low or negative niceness value (e.g., -20) means the process is not "nice" and demands more CPU time, giving it a higher priority.

Understanding **linux process niceness** is key to managing system resources effectively.

### Adjusting Process Priority

You can view the current niceness level of running processes using the `top` command. Look for the `NI` column, which displays the niceness value.

```bash
top
```

To control the **niceness linux** value, you can use the `nice` and `renice` commands.

Use the `nice` command to start a new process with a specific niceness level. For example, the following command starts `apt upgrade` with a niceness of 5.

```bash
nice -n 5 apt upgrade
```

To change the priority of an already running process, use the `renice` command. The following command changes the niceness of a process with PID 3245 to 10.

```bash
renice 10 -p 3245
```

## Exercise

Follow these steps in your Ubuntu VM terminal to practice the concepts from this lesson:

1. **Check niceness of current shell**: View the nice value
   ```bash
   ps -o pid,ni,cmd -p $$
   ```
   Expected output:
   ```
     PID  NI CMD
    1234   0 bash
   ```

2. **Start a process with nice**: Launch process with lower priority
   ```bash
   nice -n 10 sleep 100 &
   ps -o pid,ni,cmd | grep sleep
   ```
   Expected output:
   ```
    5678  10 sleep 100
   ```

3. **Change niceness with renice**: Adjust priority of running process
   ```bash
   sleep 100 &
   SLEEPPID=$!
   renice +5 $SLEEPPID
   ps -o pid,ni,cmd -p $SLEEPPID
   ```
   Expected output:
   ```
    5679   5 sleep 100
   ```

4. **View nice values of all processes**: List processes by priority
   ```bash
   ps -eo pid,ni,cmd | head -15
   ```
   Expected output:
   ```
     PID  NI CMD
       1   0 /sbin/init
       2   0 [kthreadd]
   (Shows nice values for all processes)
   ```

5. **Clean up**: Kill test processes
   ```bash
   killall sleep
   ```

## Quiz Question

If you want a process to get more CPU priority, should you use a lower or higher nice number? Please answer in a single English word, all lowercase.

