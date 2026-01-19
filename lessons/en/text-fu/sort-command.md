---
index: 12
lang: "en"
title: "sort"
meta_title: "sort - Text-Fu"
meta_description: "Learn how to use the Linux sort command for sorting text files. Discover options like reverse and numerical sorting. Improve your Linux command line skills!"
meta_keywords: "Linux sort command, sort -r, sort -n, Linux tutorial, command line, beginner Linux, sort guide"
---

## Lesson Content

The `sort` command is useful for sorting lines.

```plaintext
file1.txt
dog
cow
cat
elephant
bird

$ sort file1.txt
bird
cat
cow
dog
elephant
```

You can also do a reverse sort:

```bash
$ sort -r file1.txt
elephant
dog
cow
cat
bird
```

And also sort by numerical value:

```bash
$ sort -n file1.txt
bird
cat
cow
elephant
dog
```

## Exercise

Follow these steps in your Ubuntu VM terminal to practice the concepts from this lesson:

1. **Create a test file with unsorted data**: Make a file to practice sorting
   ```bash
   cat > animals.txt << EOF
   dog
   cow
   cat
   elephant
   bird
   EOF
   ```

2. **Sort the file alphabetically**: Use basic sort
   ```bash
   sort animals.txt
   ```
   Expected output:
   ```
   bird
   cat
   cow
   dog
   elephant
   ```

3. **Sort in reverse order**: Use the -r flag
   ```bash
   sort -r animals.txt
   ```
   Expected output:
   ```
   elephant
   dog
   cow
   cat
   bird
   ```

4. **Sort numbers**: Create a file with numbers and sort numerically
   ```bash
   echo -e "10
2
30
1
20" > numbers.txt
   sort -n numbers.txt
   ```
   Expected output:
   ```
   1
   2
   10
   20
   30
   ```

5. **Clean up**: Remove test files
   ```bash
   rm animals.txt numbers.txt
   ```

## Quiz Question

What flag do you use to perform a reverse sort?

## Quiz Answer

-r
