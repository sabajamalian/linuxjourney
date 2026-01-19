---
title: "cp (Copy)"
layout: default
parent: Command Line
grand_parent: Fundamentals
nav_order: 10
---

## Lesson Content

The `cp` command is the standard tool for copying files and directories in Linux. Its basic syntax is `cp [SOURCE] [DESTINATION]`.

### Basic File Copying

To copy a file, you specify the source file and the destination directory or path.

```bash
cp mycoolfile /home/pete/Documents/cooldocs
```

In this example, `mycoolfile` is the source file, and `/home/pete/Documents/cooldocs` is the destination directory. You can also copy a file and give it a new name in the destination.

```bash
cp mycoolfile /home/pete/Documents/mycoolfile_backup
```

### Using Wildcards for Bulk Copying

Wildcards are special characters that help you select multiple files based on patterns, providing great flexibility.

- `*`: Matches any sequence of characters.
- `?`: Matches any single character.
- `[]`: Matches any one of the characters enclosed in the brackets.

For example, to copy all JPEG images from your current location to the `Pictures` directory:

```bash
cp *.jpg /home/pete/Pictures
```

### Copying Directories Recursively

If you try to copy a directory using `cp` without any options, you will receive an error. To copy a directory and all of its contents, including subdirectories, you must use the `-r` (recursive) flag.

```bash
cp -r Pumpkin/ /home/pete/Documents
```

This command copies the `Pumpkin` directory and everything inside it to your `Documents` directory.

### Handling File Overwrites

By default, `cp` will overwrite a file at the destination if it has the same name. To prevent accidental data loss, use the `-i` (interactive) flag, which prompts for confirmation before overwriting.

```bash
cp -i mycoolfile /home/pete/Pictures
```

Conversely, if you want to force an overwrite without any prompts, you can use the `cp -f flag`. This is useful in scripts where user interaction is not possible.

```bash
cp -f mycoolfile /home/pete/Pictures
```

### Preserving File Attributes with cp -p

When you copy a file, its metadata, such as modification time and ownership, is typically updated. To preserve these original attributes, the `cp -p` flag is essential. Using `cp -p in linux` ensures that the copy is an exact replica, not just in content but also in its metadata.

The `cp -p flag` is particularly useful for backups or when migrating files where preserving timestamps is critical.

```bash
cp -p mycoolfile /home/pete/backups/
```

This command demonstrates how to use `linux cp -p` to copy `mycoolfile` while preserving its mode, ownership, and timestamps.

## Exercise

Follow these steps in your Ubuntu VM terminal to practice the concepts from this lesson:

1. **Create a test file and copy it**: Make a file and create a copy
   ```bash
   echo "Original content" > original.txt
   cp original.txt copy.txt
   ls -l *.txt
   ```

2. **Copy with verbose output**: Use -v flag
   ```bash
   cp -v original.txt another_copy.txt
   ```
   Expected output:
   ```
   'original.txt' -> 'another_copy.txt'
   ```

3. **Create a directory and copy files into it**: Make a test directory
   ```bash
   mkdir test_dir
   cp *.txt test_dir/
   ls test_dir/
   ```

4. **Copy a directory recursively**: Copy entire directory with -r flag
   ```bash
   cp -r test_dir test_dir_backup
   ls test_dir_backup/
   ```

5. **Clean up**: Remove test files and directories
   ```bash
   rm -r test_dir test_dir_backup *.txt
   ```

## Quiz Question

What flag do you need to specify to copy over a directory?

