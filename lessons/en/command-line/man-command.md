---
index: 16
lang: "en"
title: "man"
meta_title: "man - Command Line"
meta_description: "Learn how to use the 'man' command in Linux to access detailed manuals for commands like 'ls'. Understand the man ls page to master the command line."
meta_keywords: "man, man ls, ls man, ls -l man, Linux man pages, command manual, Linux documentation, command line help"
---

## Lesson Content

In Linux, nearly every command comes with its own instruction manual. These are called "man pages" (short for manual pages), and they are an essential resource for learning how to use the system effectively.

### Understanding Man Pages

Man pages are the built-in documentation for Linux commands, utilities, and system calls. They provide a detailed description of what a command does, its available options (or flags), and how to use it. They are your first and best source for command-line help.

### Accessing a Manual with man

To view the manual for any command, you use the `man` command itself, followed by the name of the command you want to learn about. For example, to read the manual for the `ls` command, you would type:

```bash
man ls
```

This will open the `ls man` page, a comprehensive document detailing all of its features. You can scroll through the manual using the arrow keys and press `q` to quit and return to the command line.

### Finding Details on Command Options

Man pages are particularly useful for understanding command options. For instance, if you've seen the `ls -l` command and want to know what the `-l` flag does or what each column in the output means, the `man ls` page provides a complete explanation. It's the definitive guide for any variations of a command, making it an indispensable tool.

## Exercise

Follow these steps in your Ubuntu VM terminal to practice the concepts from this lesson:

1. **Read the manual for ls**: Open the comprehensive manual page
   ```bash
   man ls
   ```
   Expected output:
   ```
   (Opens manual - press 'q' to quit)
   ```

2. **Search within a man page**: Look for specific information
   ```bash
   man ls
   ```
   Then type **/recursive** and press Enter

3. **View manual for a configuration file**: Check passwd file docs
   ```bash
   man 5 passwd
   ```

4. **Search all manual pages**: Find commands related to "copy"
   ```bash
   man -k copy | head -10
   ```

5. **View man page sections**: Check available sections for passwd
   ```bash
   man -wa passwd
   ```

## Quiz Question

How do you see the manual for a command? (Please answer using only the command name in lowercase English letters).

