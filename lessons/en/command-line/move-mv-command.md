---
index: 11
lang: "en"
title: "mv (Move)"
meta_title: "mv (Move) - Command Line"
meta_description: "A comprehensive guide to the mv command in Linux. Learn how to use the bash mv command to move and rename files and directories, use options like linux mv -t, and prevent accidental overwrites."
meta_keywords: "mv command, mv command in linux, linux mv, bash mv, mv -r linux, linux mv -t, move files, rename files, linux command line"
---

## Lesson Content

The `mv` command, short for "move," is a fundamental utility in any Linux environment. It serves two primary purposes: renaming files or directories and moving them to a different location. Its functionality is similar in many ways to the `cp` command.

### Renaming Files and Directories

One of the most common uses of the `mv command in linux` is for renaming. The syntax is straightforward: you specify the old name and the new name.

To rename a file:

```bash
mv oldfile newfile
```

This same logic applies to renaming directories:

```bash
mv old_directory_name new_directory_name
```

### Moving Files and Directories

The other core function of the `mv` command is to move items from one location to another.

To move a single file into a different directory:

```bash
mv file2 /home/pete/Documents
```

You can also move multiple files at once. Simply list all the source files followed by the target directory:

```bash
mv file_1 file_2 /somedirectory
```

A useful option for this is `linux mv -t`, which allows you to specify the target directory first. This can be clearer when moving many files.

```bash
mv -t /somedirectory file_1 file_2
```

Unlike the `cp` command, you do not need a `-r` flag to move a directory. The `bash mv` command handles directories by default. While some users search for `mv -r linux`, this option is not necessary for moving directories with `mv`.

### Important Options for the mv Command

By default, if you move a file to a destination where a file with the same name already exists, `mv` will overwrite it without warning. To prevent accidental data loss, you can use the following options:

- **-i (interactive)**: This is a crucial safety feature. It will prompt you for confirmation before overwriting any existing file.

  ```bash
  mv -i source_file destination_directory
  ```

- **-b (backup)**: If you intend to overwrite a file but want to keep the old version, this option creates a backup of the destination file. The backup is typically renamed with a tilde (`~`) suffix.

  ```bash
  mv -b file1 directory_with_file1
  ```

- **-v (verbose)**: This option makes the `mv` command print out what it is doing, showing each file being moved or renamed.

  ```bash
  mv -v file1 file2 /somedirectory
  ```

Mastering the `mv command` is essential for efficient file management on the command line.

## Exercise

Practice the commands in your Ubuntu VM terminal. Experiment with different options and variations to deepen your understanding.

## Quiz Question

Using the `mv` command, how would you rename a file named `cat` to `dog`? Please provide the full command. Note: The answer is case-sensitive and should be entered in lowercase English.

## Quiz Answer

mv cat dog
