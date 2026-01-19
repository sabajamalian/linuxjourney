---
index: 17
lang: "en"
title: "whatis"
meta_title: "whatis - Command Line"
meta_description: "Discover the whatis command in Linux. Learn how the linux whatis command provides one-line descriptions of other commands, making it a vital tool for navigating the command line."
meta_keywords: "whatis command in linux, whatis linux, linux whatis command, whatis command linux, linux whatis, command line, linux commands"
---

## Lesson Content

As you explore the Linux command line, you'll encounter a vast number of commands. It's natural to forget what a specific command does. Fortunately, there's a simple utility to help you out.

### What is the whatis Command in Linux

The `whatis` command in Linux displays a concise, one-line description of a command directly from its manual (man) page. It's a quick way to get a reminder of a command's primary function without reading the entire man page. Think of the **linux whatis** command as a quick dictionary for your terminal.

### How to Use the whatis Command

Using the **whatis command linux** is straightforward. Simply type `whatis` followed by the name of the command you want to know about. For example, if you're unsure about the `cat` command, you can run:

```bash
whatis cat
```

This will return a short description, such as "cat - concatenate files and print on the standard output".

### Understanding the Output

The description provided by the **linux whatis command** is sourced directly from the NAME section of the command's manual page. This ensures the information is accurate and consistent with the system's documentation. If a command has multiple manual pages in different sections, `whatis` may display a line for each, helping you understand its various contexts.

## Exercise

Follow these steps in your Ubuntu VM terminal to practice the concepts from this lesson:

1. **Get brief description of ls**: See one-line summary
   ```bash
   whatis ls
   ```
   Expected output:
   ```
   ls (1)               - list directory contents
   ```

2. **Look up multiple commands**: Check several commands
   ```bash
   whatis ls pwd mkdir
   ```

3. **Check a system file**: Get info about passwd
   ```bash
   whatis passwd
   ```

4. **Use with wildcards**: Find commands starting with "net"
   ```bash
   whatis net* | head -5
   ```

## Quiz Question

What command can you use to see a small description of a command? Please answer in English, paying attention to lowercase.

