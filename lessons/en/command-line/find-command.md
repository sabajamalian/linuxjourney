---
index: 14
lang: "en"
title: "find"
meta_title: "find - Command Line"
meta_description: "A comprehensive guide to the find command in linux. Learn how to use the find command line to locate files and directories by name, type, and more. Enhance your file management skills with the powerful command linux find utility."
meta_keywords: "find command line, find command in linux, find command, find command linux, command linux find, file search, directory search, linux tutorial"
---

## Lesson Content

With countless files on a system, it can be challenging to locate a specific one. Fortunately, there's a powerful utility we can use for that: the `find` command. This tool is essential for efficient file management.

### Using the Find Command Line

The basic syntax for the `find command line` is `find [path] [expression]`. You must specify the directory to search in and the criteria for what you're looking for.

For example, to search for a file named `puppies.jpg` within the `/home` directory and all its subdirectories, you would use:

```bash
find /home -name puppies.jpg
```

The `find command in linux` is highly flexible, allowing for many different search expressions.

### Searching by Name and Type

One of the most common uses of the `find command` is searching by filename. As seen above, the `-name` option allows you to specify the exact name of the file you want to find.

You can also specify the type of item you are searching for. The `-type` option is used for this purpose. For instance, if you want to find a directory instead of a file, you can use `d`.

```bash
find /home -type d -name MyFolder
```

In this command, we set the type to `d` for directory and are searching for an item named `MyFolder`. To search specifically for regular files, you would use `-type f`.

### Recursive Searching

A key feature of the `find command linux` users appreciate is its recursive nature. When you specify a starting directory, `find` doesn't just look in that single directory; it automatically searches through all subdirectories contained within it. This makes it an incredibly thorough tool for locating items anywhere in a directory tree.

## Exercise

Follow these steps in your Ubuntu VM terminal to practice the concepts from this lesson:

1. **Find files by name**: Search for files in your home directory
   ```bash
   find ~ -name "*.txt" 2>/dev/null | head -5
   ```

2. **Find files by type**: Look for all directories
   ```bash
   find /etc -type d 2>/dev/null | head -10
   ```

3. **Find recently modified files**: Search for files modified in last 7 days
   ```bash
   find ~ -type f -mtime -7 2>/dev/null | head -5
   ```

4. **Find empty files**: Create and find empty files
   ```bash
   touch empty1.txt empty2.txt
   find . -name "empty*.txt" -type f -empty
   ```

5. **Clean up**: Remove test files
   ```bash
   rm empty1.txt empty2.txt
   ```

## Quiz Question

What option should you specify for the `find` command to search by name? Please answer using only the English option, paying attention to the required format (e.g., -option).

