---
index: 9
lang: "en"
title: "tail"
meta_title: "tail - Text-Fu"
meta_description: "A beginner Linux guide to the tail command. Learn how to use Linux tail to view the end of files and monitor logs in real-time with the powerful tail -f option."
meta_keywords: "tail command, Linux tail, tail -f, view logs, monitor logs, Linux tutorial, beginner Linux, Linux guide, file monitoring"
---

## Lesson Content

The `tail` command is a fundamental utility for anyone learning Linux. As its name suggests, it allows you to view the "tail" or end of a file. This is particularly useful for checking the most recent entries in rapidly changing files, such as system logs.

### Viewing the End of a File

By default, the `tail` command displays the last 10 lines of a specified file. It functions as the counterpart to the `head` command.

```bash
tail /var/log/syslog
```

Just like with `head`, you can customize the number of lines you want to see by using the `-n` option. For example, to see the last 20 lines, you would use the following command:

```bash
tail -n 20 /var/log/syslog
```

This flexibility makes the `Linux tail` command an essential tool for quickly inspecting file endings without opening the entire file.

### Real-Time File Monitoring with tail -f

One of the most powerful features of the `tail` command is its ability to monitor files in real-time. This is achieved with the `-f` (follow) flag. When you use `tail -f`, the command doesn't exit after displaying the last few lines. Instead, it waits for new data to be appended to the file and prints it to the screen as it arrives.

```bash
tail -f /var/log/syslog
```

Try running this command. As you continue to use your system, you will see new lines appear in your terminal. This makes `tail -f` an indispensable tool for system administrators and developers who need to `view logs` and monitor application output as it happens.

## Exercise

Follow these steps in your Ubuntu VM terminal to practice the concepts from this lesson:

1. **View last 10 lines of a file**: Use default tail behavior
   ```bash
   tail /etc/passwd
   ```
   Expected output:
   ```
   (Last 10 lines of the passwd file)
   ```

2. **View last 5 lines**: Use the -n flag
   ```bash
   tail -n 5 /etc/passwd
   ```
   Expected output:
   ```
   (Last 5 lines of the passwd file)
   ```

3. **Create a test file**: Make a file with numbered lines
   ```bash
   seq 1 100 > numbers.txt
   tail numbers.txt
   ```
   Expected output:
   ```
   91
   92
   93
   94
   95
   96
   97
   98
   99
   100
   ```

4. **Follow a file in real-time**: Monitor a log file (press Ctrl+C to stop)
   ```bash
   tail -f /var/log/syslog
   ```
   Expected output:
   ```
   (Real-time log output - press Ctrl+C to exit)
   ```

5. **Clean up**: Remove the test file
   ```bash
   rm numbers.txt
   ```

## Quiz Question

What is the flag used to follow a file in `tail`? (Please answer in English, paying attention to case sensitivity).

## Quiz Answer

-f
