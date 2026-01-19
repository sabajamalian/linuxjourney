---
title: "expand and unexpand"
layout: default
parent: Text-Fu
grand_parent: Fundamentals
nav_order: 10
---

## Lesson Content

Inconsistent spacing can make text files difficult to read. While tabs are meant to create uniform indentation, their display width can vary across different editors and systems. This can disrupt text formatting and alignment. Fortunately, Linux provides simple tools to manage this by converting between tabs and spaces. This beginner Linux guide will walk you through the process.

### Converting Tabs to Spaces with the expand Command

When you need to ensure consistent spacing, you can convert tabs into a standard number of spaces using the `expand` command. This command reads a file and replaces each tab character with a set of space characters, printing the result to standard output.

```bash
expand sample.txt
```

By default, the `expand command` converts each tab into 8 spaces. This simple utility is a powerful tool for improving text formatting.

### Saving the Converted Output

The `expand` command only prints the converted text to your terminal. To save the changes, you must redirect the output to a new file.

```bash
expand sample.txt > result.txt
```

This command takes the output of `expand sample.txt` and writes it into `result.txt`, giving you a new file with spaces instead of tabs.

### Converting Spaces to Tabs with the unexpand Command

The reverse operation, converting spaces back into tabs, is handled by the `unexpand` command. This can be useful for reducing file size or adhering to coding standards that require tabs.

```bash
unexpand -a result.txt
```

By default, `unexpand` only converts leading spaces on each line. The `-a` option tells the `unexpand command` to convert all instances of 8 spaces into a tab, not just those at the beginning of a line, providing more comprehensive control over your Linux spaces and tabs.

## Exercise

Follow these steps in your Ubuntu VM terminal to practice the concepts from this lesson:

1. **Create a file with tabs**: Make a test file with tab characters
   ```bash
   echo -e "Col1	Col2	Col3" > tabbed.txt
   cat tabbed.txt
   ```

2. **Convert tabs to spaces**: Use expand command
   ```bash
   expand tabbed.txt
   ```
   Expected output:
   ```
   Col1    Col2    Col3
   (Tabs converted to spaces)
   ```

3. **Specify tab width**: Use -t flag to set tab width
   ```bash
   expand -t 4 tabbed.txt
   ```
   Expected output:
   ```
   Col1 Col2 Col3
   (Tabs converted to 4 spaces)
   ```

4. **Convert spaces back to tabs**: Use unexpand command
   ```bash
   expand tabbed.txt | unexpand
   ```
   Expected output:
   ```
   (Spaces converted back to tabs)
   ```

5. **Clean up**: Remove test file
   ```bash
   rm tabbed.txt
   ```

## Quiz Question

What command is used to convert tabs to spaces? (Please answer using the lowercase English command name.)

