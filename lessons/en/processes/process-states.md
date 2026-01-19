---
index: 9
lang: "en"
title: "Process States"
meta_title: "Process States - Processes"
meta_description: "A comprehensive guide to Linux process states. Learn about the different process states in Linux (R, S, D, Z, T) and how to interpret them using the `ps` command."
meta_keywords: "linux process states, process states in linux, linux process state, process state in linux, linux process states explained, ps command, STAT codes, process management"
---

## Lesson Content

When you inspect running processes, for example with the `ps aux` command, you'll notice a STAT column. Understanding the codes in this column is key to mastering process management. Each code represents a specific **linux process state**.

```bash
ps aux
```

A **process state in Linux** provides a snapshot of what a process is currently doing. Is it actively using the CPU, waiting for input, or has it terminated? Let's explore the most common states you will encounter.

### Decoding Common Process State Codes

The STAT column reveals the current **linux process state**. While there are many possible states, the following are the ones you will see most often. Having these **linux process states explained** will help you diagnose system behavior.

- **R (Running or Runnable)**: A process in this state is either actively executing on a CPU core or is in the run queue, ready to be executed as soon as a CPU core becomes available.

- **S (Interruptible Sleep)**: This is one of the most common **process states in Linux**. The process is waiting for an event to complete, such as user input from the terminal or a network packet to arrive. It is "interruptible," meaning it can be woken up by signals.

- **D (Uninterruptible Sleep)**: This process is also sleeping, but it's in a state where it cannot be interrupted by a signal. This is typically used for short periods during I/O operations where interrupting the process could lead to a corrupted state. If a process remains in this state for a long time, it may indicate a problem with hardware or a driver.

- **Z (Zombie)**: A zombie process has finished execution, but it still has an entry in the process table. It is waiting for its parent process to read its exit status. A few zombies are normal, but a large number may indicate a bug in the parent application.

- **T (Stopped)**: A process enters this state when it has been suspended by a job control signal (like pressing `Ctrl+Z`) or because it is being traced by a debugger. It can be resumed with the `SIGCONT` signal.

By understanding these fundamental **linux process states**, you can gain deeper insight into your system's activity and more effectively manage running applications.

## Exercise

Follow these steps in your Ubuntu VM terminal to practice the concepts from this lesson:

1. **View process states**: See STAT column in ps output
   ```bash
   ps aux | head -15
   ```
   Expected output:
   ```
   USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
   root         1  0.0  0.1 225848  9476 ?        Ss   Jan19   0:03 /sbin/init
   root         2  0.0  0.0      0     0 ?        S    Jan19   0:00 [kthreadd]
   (Note STAT column: S=sleeping, R=running, Z=zombie, etc.)
   ```

2. **Find running processes**: Filter for running state
   ```bash
   ps aux | awk '$8 ~ /R/ {print $0}' | head -5
   ```
   Expected output:
   ```
   (Shows processes in Running state)
   ```

3. **Find sleeping processes**: Look for interruptible sleep
   ```bash
   ps aux | awk '$8 ~ /S/ {print $0}' | head -5
   ```
   Expected output:
   ```
   (Shows processes in Sleeping state)
   ```

4. **Check zombie processes**: Look for defunct processes
   ```bash
   ps aux | grep Z
   ```
   Expected output:
   ```
   (Usually no output if system is healthy)
   ```

## Quiz Question

What STAT code is used to represent an uninterruptible sleep? (Please provide the single, uppercase English letter for the state code.)

## Quiz Answer

D
