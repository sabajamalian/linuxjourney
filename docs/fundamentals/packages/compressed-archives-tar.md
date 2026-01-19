---
title: "tar and gzip"
layout: default
parent: Packages
grand_parent: Fundamentals
nav_order: 3
---

## Lesson Content

Before diving into package managers, it's essential to understand file archiving and compression. When you download software online, you'll often find it packaged in archived and compressed formats. This lesson focuses on two fundamental utilities for this purpose: `tar` and `gzip`.

### Understanding Archiving vs. Compression

It's important to distinguish between archiving and compression. **Archiving** is the process of combining multiple files and directories into a single file, known as an archive. This makes it easier to manage and transfer a group of files. **Compression**, on the other hand, is the process of reducing the size of a file to save disk space and speed up transfers. The `tar` utility is used for archiving, while `gzip` is used for compression. Often, you will see `gzip and tar` used together.

### Compressing Single Files with gzip

The `gzip` program is used to compress individual files in Linux. When you compress a file with `gzip`, it is replaced by a file with a `.gz` extension.

To compress a file:

```bash
gzip mycoolfile
```

This will create `mycoolfile.gz` and remove the original. To decompress the file, you can use `gunzip`:

```bash
gunzip mycoolfile.gz
```

### Creating Archives with tar

While `gzip` is great for compression, it cannot bundle multiple files into a single archive. For that, we use the `tar` (Tape Archive) utility. A file created with `tar` is often called a "tarball" and has a `.tar` extension.

To create a new archive containing multiple files:

```bash
tar cvf myarchive.tar file1 file2 directory1
```

Let's break down the options:

- `c`: **c**reate a new archive.
- `v`: **v**erbose mode, which lists the files as they are processed.
- `f`: **f**ile, which specifies that the next argument is the name of the archive file.

### The Power of tar and gzip Combined

The true power comes from using `tar and gzip` together. You can first create a `.tar` archive and then compress it with `gzip`, resulting in a `.tar.gz` file. However, `tar` provides a convenient way to handle `tar compression` in a single step using the `z` option. This process is sometimes referred to as creating a `gzip tar` archive.

To create a compressed archive, which is a common way to `compress tar gz` files:

```bash
tar czvf myarchive.tar.gz file1 file2 directory1
```

Here, the `z` option tells `tar` to use `gzip` for compression.

### Extracting tar and gzip Archives

To extract files from an archive, you use the `x` option.

To extract a simple `.tar` archive:

```bash
tar xvf myarchive.tar
```

To uncompress and extract a `.tar.gz` archive in one command, simply add the `z` option again:

```bash
tar xzvf myarchive.tar.gz
```

Let's review the extraction options:

- `x`: **e**xtract files from an archive.
- `z`: Decompress the archive using `g**z**ip`.
- `v`: **v**erbose mode, listing files as they are extracted.
- `f`: **f**ile, specifying the archive file to extract.

A helpful mnemonic for this is: e**X**tract **Z**ee **V**ery **F**ast!

`tar` is a command so essential yet often forgotten. Relevant xkcd: `https://xkcd.com/1168`

### Other Utilities

While `tar` and `gzip` are extremely common, you will encounter other archiving and compression formats on your Linux journey. These include `bzip2` (which creates `.bz2` files and uses the `j` flag in `tar`), `xz` (creating `.xz` files with the `J` flag), and the familiar `zip`/`unzip` utilities. Each has its own set of commands and compression ratios, but the underlying concepts remain the same.

## Exercise

Follow these steps in your Ubuntu VM terminal to practice the concepts from this lesson:

1. **Create test files for archiving**: Make some files to practice with
   ```bash
   mkdir test_archive
   echo "File 1" > test_archive/file1.txt
   echo "File 2" > test_archive/file2.txt
   echo "File 3" > test_archive/file3.txt
   ```

2. **Create a tar archive**: Bundle files together
   ```bash
   tar -cvf myarchive.tar test_archive/
   ls -lh myarchive.tar
   ```
   Expected output:
   ```
   test_archive/
   test_archive/file1.txt
   test_archive/file2.txt
   test_archive/file3.txt
   -rw-rw-r-- 1 user user 10K Jan 19 10:30 myarchive.tar
   ```

3. **List contents of tar archive**: View what's inside without extracting
   ```bash
   tar -tvf myarchive.tar
   ```
   Expected output:
   ```
   drwxrwxr-x user/user         0 2024-01-19 10:30 test_archive/
   -rw-rw-r-- user/user         7 2024-01-19 10:30 test_archive/file1.txt
   -rw-rw-r-- user/user         7 2024-01-19 10:30 test_archive/file2.txt
   ```

4. **Create compressed tar.gz archive**: Use gzip compression
   ```bash
   tar -czvf myarchive.tar.gz test_archive/
   ls -lh myarchive.tar.gz
   ```
   Expected output:
   ```
   test_archive/
   test_archive/file1.txt
   test_archive/file2.txt
   -rw-rw-r-- 1 user user 1.2K Jan 19 10:30 myarchive.tar.gz
   ```

5. **Extract tar archive**: Unpack the archive
   ```bash
   rm -r test_archive
   tar -xzvf myarchive.tar.gz
   ls test_archive/
   ```
   Expected output:
   ```
   test_archive/
   test_archive/file1.txt
   file1.txt  file2.txt  file3.txt
   ```

6. **Clean up**: Remove test files
   ```bash
   rm -r test_archive myarchive.tar myarchive.tar.gz
   ```

## Quiz Question

What tar flag is used to create archives? Please answer with a single lowercase English letter.

