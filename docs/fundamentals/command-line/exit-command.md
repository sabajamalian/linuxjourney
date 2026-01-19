---
title: "exit"
layout: default
parent: Command Line
grand_parent: Fundamentals
nav_order: 19
---

## Lesson Content

Congratulations on completing the foundational lessons of your Linux journey! You've covered essential Linux basics, and now it's time to learn how to properly end your session. Exiting the Linux shell is a simple but important final step.

### The Exit Command

The most common way to end a shell session is with the `exit` command. When you type `exit` and press Enter, the current shell process terminates. This is a universal command that works in virtually any shell environment, making it a fundamental part of any beginner Linux tutorial.

```bash
exit
```

### The Logout Command

Another command you can use for a terminal exit is `logout`. This command is specifically designed to terminate a login shell. While in many modern systems it behaves similarly to `exit`, it's good practice to know both commands.

```bash
logout
```

### Closing the Terminal Window

If you are working within a graphical user interface (GUI), you also have the option to simply close the terminal window. This action typically sends a signal that terminates the shell session running inside it, providing a quick way to perform a terminal exit.

You've successfully learned how to navigate, work with files, and now, how to exit the shell. Take a well-deserved break, and we'll see you in the next course to continue your learning!

## Exercise

Follow these steps in your Ubuntu VM terminal to practice the concepts from this lesson:

1. **Check exit status of successful command**: Run a command and check status
   ```bash
   ls /home
   echo $?
   ```
   Expected output:
   ```
   0
   ```

2. **Check exit status of failed command**: Run a failing command
   ```bash
   ls /nonexistent 2>/dev/null
   echo $?
   ```
   Expected output:
   ```
   2
   ```

3. **Exit with custom status code**: Test exit codes
   ```bash
   bash -c 'exit 5'
   echo $?
   ```
   Expected output:
   ```
   5
   ```

4. **Chain commands based on success**: Use && operator
   ```bash
   mkdir tempdir && cd tempdir && pwd
   cd .. && rmdir tempdir
   ```

## Quiz Question

What is the most common command to exit from the Linux shell? Please answer using only a single lowercase English word.

