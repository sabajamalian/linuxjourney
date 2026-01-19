---
index: 3
lang: "en"
title: "Process Threads"
meta_title: "Process Threads - Process Utilization"
meta_description: "A guide to Linux process threads. Learn the difference between single-threaded and multi-threaded processes and how to use the ps command to show threads."
meta_keywords: "Linux threads, process threads, ps show threads, ps m, multi-threaded, single-threaded, lightweight process, Linux process management"
---

## Lesson Content

### What Are Process Threads?

You may have heard the terms single-threaded and multi-threaded. Threads are units of execution within a process and are often called "lightweight processes." While processes operate with their own isolated system resources, threads within the same process can share these resources, such as memory. This shared-resource model makes communication between threads much faster and more efficient than communication between separate processes.

### Single-Threaded vs. Multi-Threaded

Every process has at least one thread. A process with only one thread is called single-threaded, while a process with more than one is multi-threaded.

For example, when you use a modern text editor, it might run as a single process. However, within that process, one thread could be managing your keyboard input, while another thread runs in the background to perform spell-checking or auto-saving. This concurrent execution makes the application feel more responsive. Using multiple threads is often more efficient than launching multiple processes for related tasks.

### How to Show Threads with ps

To inspect running processes and their threads, you can use the `ps` command. While `ps` has many options, a common way to **show threads** is with the `m` flag.

```plaintext
pete@icebox:~$ ps m
  PID TTY      STAT   TIME COMMAND
 2207 pts/2    -      0:01 bash
    - -        Ss     0:01 -
 5252 pts/2    -      0:00 ps m
    - -        R+     0:00 -
```

### Interpreting the Output

In the output above, the lines with a `PID` (Process ID) represent the main process. The lines directly underneath, which have a dash (`-`) instead of a `PID`, represent the threads belonging to that process. In this example, both the `bash` and `ps m` processes are single-threaded, as each has only one main thread listed.

## Exercise

Follow these steps in your Ubuntu VM terminal to practice the concepts from this lesson:

1. **View top processes**: Try this command
   ```bash
   top -b -n 1 | head -20
   ```
   Expected output:
   ```
   (Output will vary based on your system)
   ```

2. **Check memory usage**: Try this command
   ```bash
   free -h
   ```
   Expected output:
   ```
   (Output will vary based on your system)
   ```

3. **View CPU info**: Try this command
   ```bash
   cat /proc/cpuinfo | grep 'model name' | head -1
   ```
   Expected output:
   ```
   (Output will vary based on your system)
   ```

4. **Check load average**: Try this command
   ```bash
   uptime
   ```
   Expected output:
   ```
   (Output will vary based on your system)
   ```

## Quiz Question

True or false, all processes start out single-threaded.

