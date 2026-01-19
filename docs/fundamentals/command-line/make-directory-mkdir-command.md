---
title: "mkdir (Make Directory)"
layout: default
parent: Command Line
grand_parent: Fundamentals
nav_order: 12
---

## Lesson Content

As you work with files, you'll need to organize them into directories. The primary tool for this task is the `mkdir` command, which stands for "Make Directory". This command allows you to **create a directory in Linux** right from your terminal or **command prompt**.

### Creating a Single Directory

The most basic use of the **mkdir command in Linux** is to create a single new directory. If the directory doesn't already exist, this command will create it in your current location. For example, to create a directory named `documents`:

```bash
mkdir documents
```

### Creating Multiple Directories

You can also create several directories at once by listing their names, separated by spaces. This is an efficient way to set up multiple folders quickly.

```bash
mkdir books paintings
```

### Creating Nested Directories

Sometimes you need to create a directory and its parent directories simultaneously. The `-p` (parent) option is perfect for this. This powerful feature of the **create folder Linux command** prevents errors if parent directories don't exist. For instance, to create the directory `favorites` inside `hemmingway`, which is inside `books`:

```bash
mkdir -p books/hemmingway/favorites
```

This single command creates `books`, `hemmingway`, and `favorites` if they don't already exist, demonstrating a key capability when you need to **create a directory in Linux**.

## Exercise

Follow these steps in your Ubuntu VM terminal to practice the concepts from this lesson:

1. **Create a single directory**: Make a new directory
   ```bash
   mkdir testdir
   ls -ld testdir
   ```

2. **Create multiple directories at once**: Make several directories
   ```bash
   mkdir dir1 dir2 dir3
   ls -d dir*
   ```

3. **Create nested directories**: Use -p flag to create parents
   ```bash
   mkdir -p parent/child/grandchild
   ls -R parent/
   ```

4. **Create directory with verbose output**: See confirmation
   ```bash
   mkdir -v myproject
   ```

5. **Clean up**: Remove all test directories
   ```bash
   rm -r testdir dir1 dir2 dir3 parent myproject
   ```

## Quiz Question

What command is used to make a directory? Please answer using only the lowercase English command.

