---
index: 2
lang: "en"
title: "stdin (Standard In)"
meta_title: "stdin (Standard In) - Text-Fu"
meta_description: "Master Linux command-line operations by learning how to redirect stdin (standard input). This guide covers the relationship between stdin and stdout, using the '<' operator, and practical examples like 'cat stdin' to manage data streams effectively."
meta_keywords: "stdin, standardin, redirect stdin, cat stdin, stdin and stdout, standard input, Linux redirection, command line, input stream"
---

## Lesson Content

In our previous lesson, we learned about redirecting the standard output (stdout) stream. Similarly, we can also manage the standard input (`stdin`) stream. By default, a program receives its `stdin` from the keyboard, but we can also use files or the output from other processes as an input source.

### Understanding stdin and stdout

Every command-line process in Linux operates with at least two fundamental data streams: standard input (`stdin`) and standard output (`stdout`). A program reads data from `stdin` and writes its results to `stdout`. Understanding how to control both `stdin and stdout` is crucial for effective command-line work.

### How to Redirect stdin

Just as we use `>` for stdout redirection, we use the `<` operator to `redirect stdin`. This powerful feature allows you to tell a command to read its input from a file instead of waiting for you to type it on the keyboard. This is a core concept of input redirection.

### Practical Example with cat stdin

Let's revisit the `peanuts.txt` file from the previous lesson, which contains the text "Hello World". Consider the following command:

```bash
cat < peanuts.txt > banana.txt
```

Here’s a breakdown of what happens:

1. The `< peanuts.txt` part tells the shell to `redirect stdin` for the `cat` command, making it read from `peanuts.txt` instead of the keyboard.
2. The `cat` command processes its input. In this case, using `cat stdin` means it reads the content of `peanuts.txt`.
3. The `> banana.txt` part redirects the standard output of `cat` to a new file named `banana.txt`.

Ultimately, the content of `peanuts.txt` is copied to `banana.txt`. This example effectively demonstrates how to manage both `stdin and stdout` in a single, efficient command.

## Exercise

Follow these steps in your Ubuntu VM terminal to practice the concepts from this lesson:

1. **Create a test file**: Make a file to use as input
   ```bash
   cat > input.txt << EOF
   Line 1
   Line 2
   Line 3
   EOF
   ```

2. **Redirect file as input**: Use < to provide input to a command
   ```bash
   cat < input.txt
   ```
   Expected output:
   ```
   Line 1
   Line 2
   Line 3
   ```

3. **Use stdin with sort**: Sort contents of a file via stdin
   ```bash
   sort < input.txt
   ```
   Expected output:
   ```
   Line 1
   Line 2
   Line 3
   ```

4. **Combine input and output redirection**: Read from one file, write to another
   ```bash
   tr 'a-z' 'A-Z' < input.txt > output.txt
   cat output.txt
   ```
   Expected output:
   ```
   LINE 1
   LINE 2
   LINE 3
   ```

5. **Clean up**: Remove test files
   ```bash
   rm input.txt output.txt
   ```

## Quiz Question

What operator is used to redirect stdin? Please answer with only the required symbol.

