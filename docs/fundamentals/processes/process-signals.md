---
title: "Signals"
layout: default
parent: Processes
grand_parent: Fundamentals
nav_order: 6
---

## Lesson Content

In Linux, a signal is a software interrupt sent to a process to notify it that an important event has occurred. Understanding **linux signals** is fundamental to managing processes and system behavior effectively.

### The Purpose of Signals

Signals serve as a primary method of inter-process communication (IPC). They have many uses:

- **User Interaction**: A user can type special terminal characters, like `Ctrl-C` (SIGINT) or `Ctrl-Z` (SIGTSTP), to interrupt or suspend foreground processes.
- **Kernel Notifications**: The kernel can send signals to a process to notify it of hardware or software issues, such as an illegal memory access (SIGSEGV).
- **Process Management**: System administrators and other processes use signals to manage the lifecycle of other processes, such as requesting termination or a configuration reload.

### The Signal Lifecycle

When an event generates a signal, it is first delivered to a target process. The signal remains in a "pending" state until the kernel runs the process. When the process is scheduled, the signal is delivered. However, processes have signal masks, which can be configured to block the delivery of specific signals.

When a signal is delivered, the process can take one of several actions:

- **Ignore the signal**: The process simply discards the signal and continues execution.
- **Catch the signal**: The process executes a custom function called a signal handler to respond to the event.
- **Perform the default action**: If not caught or ignored, the default action is taken. For many signals, this means terminating the process.
- **Block the signal**: If the signal is in the process's signal mask, it remains pending until it is unblocked.

### Common Linux Process Signals

Each signal is defined by an integer, but they are almost always referred to by their symbolic names (the **os sig code**), which start with `SIG`. While the numbers can vary slightly between architectures, the names are consistent. Here are some of the most common **linux process signals**:

- **SIGHUP (1)**: Hangup. Often used to tell a daemon to reload its configuration.
- **SIGINT (2)**: Interrupt. Sent by `Ctrl-C`. It's a request to terminate the process.
- **SIGKILL (9)**: Kill. This is an immediate, forceful termination. The process cannot catch, ignore, or block this signal.
- **SIGSEGV (11)**: Segmentation Fault. Indicates the process made an invalid memory reference.
- **SIGTERM (15)**: Termination. This is the standard, polite way to ask a process to terminate. It is the default signal sent by the `kill` command. A process can catch this signal to perform cleanup before exiting. This is often referred to as **signal 15 linux**.
- **SIGSTOP**: Stop. Pauses the process. Like SIGKILL, it cannot be caught or ignored.

The key difference between `SIGTERM` (**linux signal 15**) and `SIGKILL` is that `SIGTERM` is a request that can be handled, while `SIGKILL` is a command that destroys the process immediately.

## Exercise

Follow these steps in your Ubuntu VM terminal to practice the concepts from this lesson:

1. **List all available signals**: View signal numbers and names
   ```bash
   kill -l
   ```
   Expected output:
   ```
    1) SIGHUP       2) SIGINT       3) SIGQUIT      4) SIGILL
    5) SIGTRAP      6) SIGABRT      7) SIGBUS       8) SIGFPE
    9) SIGKILL     10) SIGUSR1     11) SIGSEGV     12) SIGUSR2
   (and more signals)
   ```

2. **Start a process and send SIGSTOP**: Pause a process
   ```bash
   sleep 100 &
   SLEEPPID=$!
   kill -STOP $SLEEPPID
   ps -p $SLEEPPID -o pid,state,cmd
   ```
   Expected output:
   ```
     PID S CMD
    5678 T sleep 100
   (T = stopped)
   ```

3. **Resume the process with SIGCONT**: Continue a stopped process
   ```bash
   kill -CONT $SLEEPPID
   ps -p $SLEEPPID -o pid,state,cmd
   ```
   Expected output:
   ```
     PID S CMD
    5678 S sleep 100
   (S = sleeping/running)
   ```

4. **Terminate with SIGTERM**: Send termination signal
   ```bash
   kill -TERM $SLEEPPID
   ```

5. **Try SIGINT with Ctrl+C**: Start a foreground process
   ```bash
   sleep 60
   (Press Ctrl+C to send SIGINT)
   ```
   Expected output:
   ```
   ^C
   (Process interrupted)
   ```

## Quiz Question

What signal is unblockable? Please answer in English, using the exact signal name and paying attention to capitalization.

