---
index: 6
lang: "en"
title: "file"
meta_title: "file - Command Line"
meta_description: "Learn how to use the Linux 'file' command to identify file types and contents. Understand Linux file naming conventions with this beginner-friendly guide."
meta_keywords: "Linux file command, identify file type, Linux tutorial, file naming, beginner Linux, Linux guide"
---

## Lesson Content

In the previous lesson, we learned about `touch`. Let's revisit that for a bit. Did you notice that the filename didn't conform to standard naming conventions, like you've probably seen with other operating systems such as Windows? Normally, you would expect a file called `banana.jpeg` to be a JPEG picture file.

In Linux, filenames aren't required to represent the contents of the file. You can create a file called `funny.gif` that isn't actually a GIF.

To find out what kind of file a file is, you can use the `file` command. It will show you a description of the file's contents.

```bash
file banana.jpg
```

## Exercise

Follow these steps in your Ubuntu VM terminal to practice the concepts from this lesson:

1. **Check the type of a text file**: Identify what kind of file .bashrc is
   ```bash
   file ~/.bashrc
   ```
   Expected output:
   ```
   /home/user/.bashrc: ASCII text
   ```

2. **Check a binary file**: See the type of a system binary
   ```bash
   file /bin/ls
   ```
   Expected output:
   ```
   /bin/ls: ELF 64-bit LSB executable
   ```

3. **Check a directory**: Use file on a directory
   ```bash
   file /etc
   ```
   Expected output:
   ```
   /etc: directory
   ```

4. **Create and check different file types**: Make files and check them
   ```bash
   echo "Hello World" > test.txt
   file test.txt
   rm test.txt
   ```

## Quiz Question

What command can you use to find the file type of a file?

