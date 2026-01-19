---
title: "cut"
layout: default
parent: Text-Fu
grand_parent: Fundamentals
nav_order: 6
---

## Lesson Content

We're going to learn a couple of useful commands for processing text. Before we begin, let's create a file to work with. Copy and paste the following command. After pasting, you will need to add a literal TAB character between "lazy" and "dog" (you can often do this by pressing Ctrl-v then TAB).

```bash
echo 'The quick brown; fox jumps over the lazy  dog' > sample.txt
```

The first command we'll explore is `cut`, which extracts portions of text from a file.

### Cutting by Character

You can extract content based on character position using the `-c` flag.

```bash
cut -c 5 sample.txt
```

This command outputs the 5th character from each line of the file. In our case, the output is "q". Note that spaces also count as characters.

### Cutting by Field with cut f

A more powerful feature is cutting by fields. The `cut f` syntax, using the `-f` flag, allows you to extract text based on field position. By default, `cut` uses the TAB character as a delimiter, meaning everything separated by a TAB is considered a distinct field.

Let's see how to cut f based on fields:

```bash
cut -f 2 sample.txt
```

Since we inserted a TAB between "lazy" and "dog", this command treats "dog" as the second field. Your output should be "dog".

### Using Custom Delimiters

You can also combine the field flag with the delimiter flag (`-d`) to specify a custom delimiter. This is useful when working with files that use characters like commas or semicolons to separate data.

```bash
cut -f 1 -d ";" sample.txt
```

This command changes the delimiter from a TAB to a semicolon (`;`). Since we are cutting the first field (`-f 1`), the result will be "The quick brown".

## Exercise

Follow these steps in your Ubuntu VM terminal to practice the concepts from this lesson:

1. **Create a test file with delimited data**: Make a CSV-style file
   ```bash
   cat > data.txt << EOF
   John,Doe,30,Engineer
   Jane,Smith,25,Designer
   Bob,Johnson,35,Manager
   EOF
   ```

2. **Extract first column**: Use cut with delimiter
   ```bash
   cut -d',' -f1 data.txt
   ```
   Expected output:
   ```
   John
   Jane
   Bob
   ```

3. **Extract multiple columns**: Get first and last columns
   ```bash
   cut -d',' -f1,4 data.txt
   ```
   Expected output:
   ```
   John,Engineer
   Jane,Designer
   Bob,Manager
   ```

4. **Extract by character position**: Get first 5 characters of each line
   ```bash
   cut -c1-5 data.txt
   ```
   Expected output:
   ```
   John,
   Jane,
   Bob,J
   ```

5. **Clean up**: Remove test file
   ```bash
   rm data.txt
   ```

## Quiz Question

What command would you use to get the first character of every line in a file?

