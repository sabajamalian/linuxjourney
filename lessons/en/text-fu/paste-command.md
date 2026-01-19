---
index: 7
lang: "en"
title: "paste"
meta_title: "paste - Text-Fu"
meta_description: "Learn how to use the Linux paste command to merge file lines. Discover delimiters and combine files with this essential Linux command tutorial."
meta_keywords: "Linux paste command, paste command tutorial, merge file lines, Linux commands, beginner Linux, Linux guide"
---

## Lesson Content

The `paste` command is similar to the `cat` command; it merges lines together in a file. Let's create a new file with the following contents:

```
sample2.txt
The
quick
brown
fox
```

Let's combine all these lines into one line:

```bash
paste -s sample2.txt
```

The default delimiter for `paste` is TAB, so now there is one line with TABs separating each word.

Let's change this delimiter (`-d`) to something a little more readable:

```bash
paste -d ' ' -s sample2.txt
```

Now everything should be on one line delimited by spaces.

## Exercise

Follow these steps in your Ubuntu VM terminal to practice the concepts from this lesson:

1. **Create two test files**: Make files to paste together
   ```bash
   echo -e "A
B
C" > file1.txt
   echo -e "1
2
3" > file2.txt
   ```

2. **Paste files side by side**: Merge files horizontally
   ```bash
   paste file1.txt file2.txt
   ```
   Expected output:
   ```
   A       1
   B       2
   C       3
   ```

3. **Use custom delimiter**: Paste with comma delimiter
   ```bash
   paste -d',' file1.txt file2.txt
   ```
   Expected output:
   ```
   A,1
   B,2
   C,3
   ```

4. **Paste serially**: Use -s to paste one file per line
   ```bash
   paste -s file1.txt
   ```
   Expected output:
   ```
   A       B       C
   ```

5. **Clean up**: Remove test files
   ```bash
   rm file1.txt file2.txt
   ```

## Quiz Question

What flag do you use with `paste` to make everything go on one line?

