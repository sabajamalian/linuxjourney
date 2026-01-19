---
index: 4
lang: "en"
title: "pipe and tee"
meta_title: "pipe and tee - Text-Fu"
meta_description: "Explore the powerful pipe and tee command in Linux. Learn how to chain commands with the Linux pipe tee combination and redirect output to both the screen and a file. This guide covers how to pipe to tee for advanced command-line data flow."
meta_keywords: "pipe and tee command in linux, linux pipe tee, pipe to tee, Linux pipe, tee command, stdout, stdin, command line redirection, Linux tutorial"
---

## Lesson Content

In Linux, the command line becomes incredibly powerful when you start connecting commands. Instead of running one command, saving its output, and then running another, you can create a pipeline to pass data directly between them.

### Understanding the Pipe Operator

Let's start with a command that produces a lot of output:

```bash
ls -la /etc
```

The list of items is likely too long to fit on your screen, making it difficult to read. While you could redirect this output to a file, a more efficient method is to send it directly to another command, like `less`, for easy viewing.

```bash
ls -la /etc | less
```

The pipe operator `|`, represented by a vertical bar, is the key to this process. It takes the standard output (`stdout`) of the command on its left and uses it as the standard input (`stdin`) for the command on its right. In this case, we _piped_ the output of `ls -la /etc` directly into the `less` command. The pipe is a fundamental tool you will use constantly.

### Splitting Output with the Tee Command

What if you want to see the output on your screen _and_ save it to a file simultaneously? This is where the `tee` command comes in. The `pipe and tee command in linux` is a classic combination for logging and monitoring.

```bash
ls | tee peanuts.txt
```

After running this, you will see the output of `ls` on your terminal. If you also check the contents of `peanuts.txt`, you will find the exact same information. The `tee` command effectively splits the output stream into two directions: one to standard output and another to a specified file.

### Combining Pipe and Tee

You can create even more advanced workflows by chaining these commands. A common pattern is to `pipe to tee` in the middle of a longer command chain. This allows you to save an intermediate result while continuing to process the data.

For example, you can use the `linux pipe tee` combination to view and save output before further filtering:

```bash
ls -la /etc | tee etc_listing.txt | grep "conf"
```

This command does three things:

1. It lists the contents of the `/etc` directory.
2. It pipes that output to `tee`, which saves a copy to `etc_listing.txt` and also passes it along.
3. The output from `tee` is then piped to `grep`, which filters for lines containing "conf".

Mastering these commands will significantly improve your efficiency on the command line.

## Exercise

Follow these steps in your Ubuntu VM terminal to practice the concepts from this lesson:

1. **Use pipe to chain commands**: List files and count them
   ```bash
   ls /etc | wc -l
   ```
   Expected output:
   ```
   (Number of files in /etc directory)
   ```

2. **Use tee to view and save output**: See output and save to file
   ```bash
   ls /etc | tee filelist.txt | head -10
   ```
   Expected output:
   ```
   (First 10 files displayed and all saved to filelist.txt)
   ```

3. **Chain multiple pipes**: Filter and sort results
   ```bash
   ls -l /etc | grep ".conf" | wc -l
   ```
   Expected output:
   ```
   (Number of .conf files in /etc)
   ```

4. **Use tee to append**: Append to file instead of overwriting
   ```bash
   echo "New entry" | tee -a filelist.txt
   cat filelist.txt | tail -5
   ```

5. **Complex pipe chain**: Combine multiple text processing tools
   ```bash
   cat /etc/passwd | cut -d: -f1 | sort | head -10
   ```
   Expected output:
   ```
   (First 10 usernames sorted alphabetically)
   ```

6. **Clean up**: Remove test file
   ```bash
   rm filelist.txt
   ```

## Quiz Question

What single character represents the pipe operator in a Linux command? Please answer with only the symbol.

## Quiz Answer

|
