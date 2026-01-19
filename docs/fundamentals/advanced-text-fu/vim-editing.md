---
title: "Vim Editing"
layout: default
parent: Advanced Text-Fu
grand_parent: Fundamentals
nav_order: 7
---

## Lesson Content

Editing text in Vim is a powerful feature that relies on combining operators and motions from Normal mode. This approach allows you to efficiently delete, change, copy (yank), and paste (put) text. Before executing any commands, press `Esc` to ensure you are in Normal mode.

### Understanding Vim Operators and Motions

The core of Vim editing is the formula: `operator + motion`. An operator is an action (like `d` for delete), and a motion is a movement (like `w` for word). For example, `dw` combines the delete operator with the word motion to delete a word. You can also use counts to repeat an action, such as `2dw` to delete two words.

### Deleting Text in Vim

The delete operator is `d`. It's one of the most common Vim commands for text manipulation.

- `x` – Deletes the character directly under the cursor.
- `dw` – Deletes from the cursor to the beginning of the next word.
- `d$` – Deletes from the cursor to the end of the current line.
- `dd` – The `dd` command deletes the entire current line.
- `3dd` – Deletes three lines, starting from the current line.

### Changing Text

The change operator, `c`, works similarly to delete but places you into Insert mode after performing the action. This is useful for replacing text.

- `cw` – Changes the text from the cursor to the end of the word.
- `c$` – Changes text from the cursor to the end of the line.
- `cc` – Changes the entire current line.

### Copying and Pasting in Vim

In Vim, copying is called "yanking" (operator `y`), and pasting is called "putting."

- `yw` – Yanks (copies) a word.
- `yy` – Yanks the entire current line.
- `p` – Puts (pastes) the yanked text after the cursor or on the line below.
- `P` – Puts the text before the cursor or on the line above.

### Other Useful Editing Commands

This Vim guide wouldn't be complete without a few other handy commands.

- `r{char}` – Replaces the single character under the cursor with the specified character.
- `R` – Enters Replace mode, allowing you to overwrite text continuously until you press `Esc`.
- `J` – Joins the current line with the next one.
- `.` – Repeats the last change you made, a very powerful and efficient command.

Combining operators with different motions unlocks the full potential of this Linux text editor. For instance, `d}` deletes to the next paragraph, and `caw` changes "a word" (the word under the cursor including any surrounding space).

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

Which command deletes the current line in Vim? (Please answer in English, paying attention to case sensitivity).

