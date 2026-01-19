---
index: 1
lang: "en"
title: "stdout (Standard Out)"
meta_title: "stdout (Standard Out) - Text-Fu"
meta_description: "Start your journey to learn Linux by mastering standard output (stdout) and I/O redirection. This lesson covers how to redirect command output to files using the > and >> operators, a fundamental skill for any Linux user."
meta_keywords: "Linux, learn linux, stdout, I/O redirection, standard output, redirect output, bash, shell scripting, Linux commands, Linux tutorial"
---

## Lesson Content

As you continue to learn Linux, you've seen how commands produce output. This brings us to the important topic of I/O (input/output) streams, specifically standard output or **stdout**. Let's explore this concept by running the following command:

```bash
echo Hello World > peanuts.txt
```

After running this, you will find a new file named `peanuts.txt` in your current directory. If you view its contents, you'll see the text "Hello World". Let's break down what happened.

### Understanding Standard Output (stdout)

First, consider the command without the special character:

```bash
echo Hello World
```

By default, many commands send their results to **stdout**, which is your terminal screen. This is why `echo Hello World` displays the text directly in your shell. Processes use I/O streams to receive input (standard input or stdin) and send output. I/O redirection allows us to change this default behavior, giving us greater control over our data.

### Redirecting stdout with >

The `>` character is a redirection operator. It intercepts the data heading to **stdout** and sends it to a new destination.

```bash
>
```

In our example, it sends the output of `echo Hello World` to a file instead of the screen. If the file doesn't exist, it will be created. **Be careful**, as if the file already exists, this operator will completely overwrite its contents.

### Appending stdout with >>

What if you want to add to a file without erasing its contents? For that, we use the `>>` operator.

```bash
echo Hello World >> peanuts.txt
```

This operator appends the output to the end of the specified file. If the file doesn't already exist, it will be created, just like the `>` operator. Mastering **stdout** redirection is a fundamental step in your Linux journey.

## Exercise

Follow these steps in your Ubuntu VM terminal to practice the concepts from this lesson:

1. **Redirect output to a file**: Save command output to a file
   ```bash
   echo "Hello World" > output.txt
   cat output.txt
   ```
   Expected output:
   ```
   Hello World
   ```

2. **Append to a file**: Add more content without overwriting
   ```bash
   echo "Second line" >> output.txt
   cat output.txt
   ```
   Expected output:
   ```
   Hello World
   Second line
   ```

3. **Redirect ls output**: Save directory listing to a file
   ```bash
   ls -la ~ > homelist.txt
   head -5 homelist.txt
   ```
   Expected output:
   ```
   (First 5 lines of your home directory listing)
   ```

4. **Overwrite existing file**: Use > to replace file contents
   ```bash
   echo "New content" > output.txt
   cat output.txt
   ```
   Expected output:
   ```
   New content
   ```

5. **Clean up**: Remove test files
   ```bash
   rm output.txt homelist.txt
   ```

## Quiz Question

What redirector do you use to append output to a file?

