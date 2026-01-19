---
index: 7
lang: "en"
title: "cat"
meta_title: "cat - Command Line"
meta_description: "Master the linux cat command to view, create, and concatenate files. This guide covers basic usage, common options, and how to use cat linux with redirection like linux cat >."
meta_keywords: "linux cat command, cat linux, cat manual linux, linux cat >, view file contents, concatenate files, linux commands, command line"
---

## Lesson Content

After learning to navigate the filesystem, the next step is to view the contents of files. A fundamental and versatile tool for this is the `linux cat command`. The name `cat` is short for "concatenate," which hints at its ability to link files together.

### Viewing File Contents

The most basic use of the `cat` command is to display the content of a single file directly in your terminal.

```bash
cat myfile.txt
```

This command will print the entire content of `myfile.txt` to the screen. While this is perfect for short configuration files or text snippets, it's not ideal for viewing large files, as the text will scroll by very quickly. We will cover tools better suited for large files in a later lesson.

### Concatenating Files

True to its name, `cat` can combine, or concatenate, multiple files and display their combined output. The `cat linux` utility reads the files in the order they are provided and prints them sequentially.

```bash
cat dogfile birdfile
```

This command will first display the contents of `dogfile`, immediately followed by the contents of `birdfile`.

### Creating Files with Redirection

You can also use `cat` with the output redirection operator (`>`) to create new files. The `linux cat >` combination is a quick way to write text into a file directly from your terminal.

```bash
cat > newfile.txt
```

After running this command, you can type your text. Press `Ctrl+D` on a new line to save and exit. This will create `newfile.txt` with the text you entered. Be careful, as using `>` on an existing file will overwrite it completely.

### Common cat Command Options

The `cat` command has several options to modify its behavior. Here are a couple of common ones:

- `-n`: This option numbers all output lines, starting from 1.
- `-b`: This option numbers only the non-empty output lines.

For a complete list of functionalities, you can always refer to the `cat manual linux` page by typing `man cat` in your terminal.

## Exercise

Follow these steps in your Ubuntu VM terminal to practice the concepts from this lesson:

1. **View a simple file**: Display the contents of /etc/hostname
   ```bash
   cat /etc/hostname
   ```
   Expected output:
   ```
   ubuntu
   ```

2. **Create a file with cat**: Use cat to create and write content
   ```bash
   cat > mytext.txt
   This is line 1
   This is line 2
   (Press Ctrl+D to save)
   ```

3. **View your created file**: Display what you just created
   ```bash
   cat mytext.txt
   ```

4. **Concatenate multiple files**: Create another file and combine them
   ```bash
   echo "File 2 content" > file2.txt
   cat mytext.txt file2.txt
   ```

5. **Clean up**: Remove test files
   ```bash
   rm mytext.txt file2.txt
   ```

## Quiz Question

What command is used to display the contents of a file on the command line? (Note: Your answer should be a single, lowercase English word.)

