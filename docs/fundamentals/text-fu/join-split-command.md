---
title: "join and split"
layout: default
parent: Text-Fu
grand_parent: Fundamentals
nav_order: 11
---

## Lesson Content

In Linux, managing and manipulating text files is a common task. Two powerful utilities for this are `join` and `split`. The `join` command merges lines from two files based on a common field, while `split` breaks a large file into smaller, more manageable pieces.

### Joining Files by a Common Field

The `join` command is a fundamental tool when you need to **linux join files**. By default, it combines lines from two sorted files based on an identical first field.

For example, imagine you have two files you want to merge:

```plaintext
file1.txt
1 John
2 Jane
3 Mary

file2.txt
1 Doe
2 Doe
3 Sue
```

Using the `join` command, you can combine them easily:

```bash
$ join file1.txt file2.txt
1 John Doe
2 Jane Doe
3 Mary Sue
```

As you can see, the files were joined using the common first field (1, 2, 3). For `join` to work correctly, the join fields in both files must be sorted.

### Specifying Different Join Fields

What if the common field is not the first column? You can tell `join` which fields to use. Consider these files:

```plaintext
file1.txt
John 1
Jane 2
Mary 3

file2.txt
1 Doe
2 Doe
3 Sue
```

Here, we need to join on the second field of `file1.txt` and the first field of `file2.txt`. The command would be:

```bash
$ join -1 2 -2 1 file1.txt file2.txt
1 John Doe
2 Jane Doe
3 Mary Sue
```

The `-1 2` flag specifies field 2 of the first file, and `-2 1` specifies field 1 of the second file.

### Splitting Large Files

The `split` command does the opposite of joining; it divides a large file into smaller ones.

```bash
split somefile
```

By default, this command splits `somefile` into new files once a 1000-line limit is reached. The output files are named `xaa`, `xab`, and so on. You can customize this behavior, for example, by specifying a different line count with the `-l` flag or splitting by file size with the `-b` flag.

## Exercise

Follow these steps in your Ubuntu VM terminal to practice the concepts from this lesson:

1. **Create files with common fields**: Make two files to join
   ```bash
   echo -e "1 John
2 Jane
3 Bob" > names.txt
   echo -e "1 Engineer
2 Designer
3 Manager" > jobs.txt
   ```

2. **Join files on common field**: Merge based on first column
   ```bash
   join names.txt jobs.txt
   ```
   Expected output:
   ```
   1 John Engineer
   2 Jane Designer
   3 Bob Manager
   ```

3. **Create a large file to split**: Make a file with multiple lines
   ```bash
   seq 1 100 > bigfile.txt
   ```

4. **Split file into smaller files**: Use split command
   ```bash
   split -l 25 bigfile.txt part_
   ls part_*
   ```
   Expected output:
   ```
   part_aa  part_ab  part_ac  part_ad
   ```

5. **View one of the split files**: Check the content
   ```bash
   head part_aa
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

6. **Clean up**: Remove all test files
   ```bash
   rm names.txt jobs.txt bigfile.txt part_*
   ```

## Quiz Question

What command would you use to join files named `cat`, `dog`, `cow`? Please provide the full command in English. The command and filenames should be in lowercase.

