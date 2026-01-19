---
title: "Emacs Editing"
layout: default
parent: Advanced Text-Fu
grand_parent: Fundamentals
nav_order: 12
---

## Lesson Content

Emacs is a powerful and extensible text editor widely used on Linux and other Unix-like systems. This beginner Emacs guide will introduce you to some fundamental editing commands. In Emacs terminology, `C-` refers to the `Ctrl` key, and `M-` refers to the `Meta` key, which is usually the `Alt` key.

### Emacs Text Navigation

While standard navigation keys like Home, End, and the arrow keys work as expected, Emacs offers more efficient commands for moving through your text, which Emacs holds in a "buffer". Mastering Emacs navigation is a key step in becoming proficient.

Here are some essential Emacs commands for moving the cursor:

```
C-up arrow: move up one paragraph
C-down arrow: move down one paragraph
C-left arrow: move one word left
C-right arrow: move one word right
M->: move to the end of the buffer
```

### Cutting and Pasting

In Emacs, cutting is called "killing" and pasting is called "yanking". To perform these actions, you first need to select a region of text.

To begin selecting text, move your cursor to the start of the desired region and press `C-space`. This sets the "mark". Then, use any navigation commands to move the cursor to the end of the region you want to select. The area between the mark and your current cursor position will be highlighted.

Once you have selected a region, you can use the following commands:

```
C-w: kill (cut) the selected region
C-y: yank (paste) the last killed text
```

These basic commands form the foundation of editing in the Emacs text editor.

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

How do you move to the end of the buffer? Please answer using only the key combination format shown in the lesson (e.g., C-w). The answer is case-sensitive.

