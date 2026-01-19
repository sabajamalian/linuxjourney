---
index: 9
lang: "en"
title: "history"
meta_title: "history - Command Line"
meta_description: "Master the history command in Linux to efficiently recall and manage your command line activity. Learn about viewing history, using shortcuts like Ctrl-R, and managing your history with options like history -c and history -d."
meta_keywords: "history in linux, history -c linux, history -d linux, history -w linux, history command unix, bash history, command line, Ctrl-R, clear command"
---

## Lesson Content

Your shell keeps a record of the commands you've previously entered. You can access this list, which is incredibly useful when you want to find and reuse a command without retyping it. The `history` command is a fundamental tool in most Unix and Linux environments.

### Viewing Your Command History

To see the list of commands you have used, simply type the `history` command. This feature provides a detailed log of your activity, making it easy to track your `history in linux`.

```bash
history
```

### Re-running Previous Commands

The shell provides several shortcuts to make re-running commands easier.

- **Up Arrow**: Want to run the same command you just did? Just press the up arrow key to cycle backward through your history.
- **The `!!` Shortcut**: To execute the most recent command again, you can use `!!`. For example, if you just ran `cat file1`, typing `!!` and pressing Enter will run `cat file1` again.

### Searching Your History

One of the most powerful history shortcuts is `Ctrl-R`. This initiates a reverse search. After pressing `Ctrl-R`, start typing any part of the command you're looking for, and the shell will display the most recent match. You can press `Ctrl-R` repeatedly to cycle through older matches. Once you find the command you want, just press Enter to execute it.

### Managing the History List

Beyond just viewing your history, you can also manage it directly.

- **Clearing History**: If you want to clear the command history for your current session, you can use the `history -c linux` command. This removes all entries from the history list in memory.
- **Writing to File**: To save the current session's history to your history file (usually `~/.bash_history`), you can use `history -w linux`. This is useful for preserving commands before closing a session.
- **Deleting a Specific Entry**: You can remove a single command from your history using `history -d <offset>`. The offset is the number shown next to the command in the `history` output. For example, `history -d 101` would delete the 101st entry. This is a key function of `history -d linux`.

### Other Useful Terminal Tools

As your terminal window fills up, you might want to clean it. Use the `clear` command to wipe your display and start with a fresh screen.

```bash
clear
```

Another indispensable feature is tab completion. If you start typing the beginning of a command, filename, or directory and press the Tab key, the shell will attempt to autocomplete it. If there are multiple possibilities, it may show you the options or do nothing. Pressing Tab a second time will often list all possible completions.

## Exercise

Follow these steps in your Ubuntu VM terminal to practice the concepts from this lesson:

1. **View your command history**: Display recently executed commands
   ```bash
   history
   ```
   Expected output:
   ```
   1  pwd
   2  ls -la
   3  cd /etc
   4  history
   ```

2. **Repeat a specific command**: Run a command from history
   ```bash
   !-2
   ```

3. **Search history**: Use reverse search
   ```bash
   Press Ctrl+R, then type "ls"
   ```

4. **View last 10 commands**: Limit history output
   ```bash
   history 10
   ```

5. **Clear history**: Remove all history entries
   ```bash
   history -c
   history
   ```

## Quiz Question

What is the command to clear the terminal? (Please answer in lowercase English letters only)

## Quiz Answer

clear
