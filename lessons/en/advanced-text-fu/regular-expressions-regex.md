---
index: 1
lang: "en"
title: "regex (Regular Expressions)"
meta_title: "regex (Regular Expressions) - Advanced Text-Fu"
meta_description: "Master the basics of Linux with our guide to regular expressions (regex). Learn pattern matching with grep, using syntax like ^, $, and []. This is one of the best ways to learn Linux text manipulation and advance your skills."
meta_keywords: "regular expression linux, regex, basics of linux, pattern matching, grep, text processing, learn linux, linux tutorial, quickest way to linux advanced"
---

## Lesson Content

Regular expressions, often shortened to regex, are a powerful tool for pattern-based text selection. Understanding them is fundamental to mastering text manipulation in Linux. While there are many apps to learn Linux, diving into core concepts like `regular expression linux` is the quickest way to linux advanced proficiency. They use special notations, some of which are similar to wildcards like `*`.

Let's explore some of the most common regex operators, which are nearly universal across programming languages. We will use the following text as our example:

```plaintext
sally sells seashells
by the seashore
```

### Anchoring to the Start of a Line

The caret `^` symbol matches the beginning of a line. It ensures that your pattern appears only at the start.

```plaintext
^by
```

This pattern would match the line "by the seashore" but not "sally sells seashells".

### Anchoring to the End of a Line

The dollar `$` symbol matches the end of a line. It is the counterpart to the `^` anchor.

```plaintext
seashore$
```

This pattern would match the line "by the seashore" because it ends with "seashore".

### Matching Any Single Character

The period `.` is a wildcard that matches any single character.

```plaintext
b.
```

In our example, this would match "by".

### Using Brackets for Character Sets

Brackets `[]` allow you to specify a set of characters to match. This provides more control than the `.` wildcard.

```plaintext
s[ae]lls
```

This would match "sells" and would also match "salls".

You can also use brackets to specify what _not_ to match. When the caret `^` is the first character inside brackets, it negates the set, matching any character _except_ those listed.

```plaintext
s[^e]lls
```

This would match "salls" but not "sells".

Finally, brackets support ranges to define a large set of characters efficiently.

```plaintext
d[a-c]g
```

This pattern will match "dag", "dbg", and "dcg". Be aware that ranges are case-sensitive. For example, `[a-c]` will not match `A`, `B`, or `C`.

Learning these operators is one of the best ways to learn Linux command-line efficiency.

## Exercise

Follow these steps in your Ubuntu VM terminal to practice the concepts from this lesson:

1. **Practice the concepts using a text editor of your choice**
   ```bash
   # Follow the instructions from the lesson
   ```

2. **Create a test file**: Try this command
   ```bash
   touch practice.txt
   ```
   Expected output:
   ```
   (Output will vary based on your system)
   ```

3. **Edit the file following the lesson instructions**
   ```bash
   # Follow the instructions from the lesson
   ```

4. **Save and verify changes**: Try this command
   ```bash
   cat practice.txt
   ```
   Expected output:
   ```
   (Output will vary based on your system)
   ```

## Quiz Question

What regular expression would you use to match any single character?

