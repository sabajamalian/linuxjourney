---
index: 8
lang: "en"
title: "head"
meta_title: "head - Text-Fu"
meta_description: "A beginner Linux guide on using the head command to view the beginning of a file. Learn how to use the head -n option to control line count, an essential skill for any Linux tutorial."
meta_keywords: "head command, Linux head, view file beginning, Linux tutorial, Linux commands, beginner Linux, head -n, Linux guide, text files, command line"
---

## Lesson Content

In Linux, you often need to inspect the contents of very large files, such as system logs. For example, if you run `cat /var/log/syslog`, you'll see pages of text scroll by, making it difficult to get a quick overview. So, what if you only want to **view the beginning of a file**? The `head` command is the perfect tool for this job.

### Default Behavior of the head Command

By default, the `head` command displays the first 10 lines of any given file. This is a fundamental part of our **beginner Linux guide** for handling text. To see it in action, simply provide a filename as an argument:

```bash
head /var/log/syslog
```

This command will output the first 10 lines from `/var/log/syslog`, allowing you to quickly check the file's initial content without opening it in an editor.

### Customizing the Line Count

The **Linux head** command is flexible. You can easily change the number of lines it displays using the `-n` flag, which stands for "number of lines". For instance, if you want to see the first 15 lines of a file, you would use the `head -n` option like this:

```bash
head -n 15 /var/log/syslog
```

This makes `head` one of the most useful **Linux commands** for quickly inspecting file headers or log entries.

## Exercise

Follow these steps in your Ubuntu VM terminal to practice the concepts from this lesson:

1. **View first 10 lines of a system file**: Use default head behavior
   ```bash
   head /etc/passwd
   ```
   Expected output:
   ```
   (First 10 lines of the passwd file)
   ```

2. **View first 5 lines**: Use the -n flag to specify line count
   ```bash
   head -n 5 /etc/passwd
   ```
   Expected output:
   ```
   (First 5 lines of the passwd file)
   ```

3. **Create a test file and view it**: Make a file with numbered lines
   ```bash
   seq 1 100 > numbers.txt
   head numbers.txt
   ```
   Expected output:
   ```
   1
   2
   3
   4
   5
   6
   7
   8
   9
   10
   ```

4. **View first 15 lines**: Use head -n with a larger number
   ```bash
   head -n 15 numbers.txt
   ```
   Expected output:
   ```
   (Numbers 1 through 15)
   ```

5. **Clean up**: Remove the test file
   ```bash
   rm numbers.txt
   ```

## Quiz Question

What flag would you use with the `head` command to change the number of lines you want to view? Please answer using only the English flag, paying attention to case sensitivity.

