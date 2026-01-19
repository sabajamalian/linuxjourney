---
index: 2
lang: "en"
title: "Controlling Terminal"
meta_title: "Controlling Terminal - Processes"
meta_description: "Explore the concept of a controlling terminal in Linux. Learn what a TTY is, the difference between TTY and PTS, and how to use the `ps tty` output to identify processes without a controlling terminal, like daemons."
meta_keywords: "controlling terminal, ps tty, what is tty, how to use ps, TTY, PTS, Linux terminal, daemon process, Linux processes"
---

## Lesson Content

When you inspect running processes, you'll notice a `TTY` field in the `ps` command's output. This field is important as it indicates the **controlling terminal** that executed the command. Understanding this concept is key to managing processes effectively.

### What is a TTY

TTY is an abbreviation for "Teletype," which historically was a physical device for interacting with a computer. In modern Linux systems, a TTY refers to the terminal that provides the standard input and output for a process.

There are two main types of terminals you will encounter: terminal devices and pseudo-terminal devices.

### Terminal Devices vs Pseudo-Terminals

A true terminal device is a native console that allows you to type commands and see output directly. You can experience this by switching to a virtual console. On many systems, you can press `Ctrl-Alt-F1` to access TTY1. You'll see a login prompt in a purely text-based environment, with no graphical interface. This is a classic terminal device. To return to your graphical session, you can typically use `Ctrl-Alt-F7` (the exact key combination may vary).

A pseudo-terminal (PTS), on the other hand, is what you most commonly use. When you open a terminal application within your graphical desktop environment, you are using a PTS. These emulate a terminal within a window. If you check the `ps tty` output for your shell, you will see its TTY listed as `pts/*`.

### The Role of the Controlling Terminal

Most processes are bound to a **controlling terminal**. This means the process's lifecycle is tied to the terminal session that started it. For example, if you run a program like `find` in your terminal window and then close that window, the `find` process will also be terminated.

### Processes Without a Controlling Terminal

Some processes, known as daemons, are designed to run in the background and manage system services. These processes often start when the system boots and stop only when it shuts down.

To prevent them from being accidentally terminated, daemons are not attached to a **controlling terminal**. When you learn **how to use ps** to examine these processes, you will see a question mark (`?`) in the TTY column. This `?` signifies that the process does not have a controlling terminal and is running independently of any user session.

## Exercise

Practice the commands in your Ubuntu VM terminal. Experiment with different options and variations to deepen your understanding.

## Quiz Question

What value is given for a process that does not have a controlling terminal?

## Quiz Answer

?
