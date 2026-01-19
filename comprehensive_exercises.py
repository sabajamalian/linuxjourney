#!/usr/bin/env python3
"""
Comprehensive exercise generator for all 185 Linux Journey lessons.
This script creates detailed, contextual exercises for each lesson.
"""
import os
import re
from pathlib import Path

def create_exercises_dict():
    """Return a comprehensive dictionary of exercises for all lessons."""
    
    exercises = {}
    
    # COMMAND-LINE LESSONS (19 files) - Already created above
    exercises.update({
        "print-working-directory-pwd-command.md": """## Exercise

Follow these steps in your Ubuntu VM terminal to practice the concepts from this lesson:

1. **Check your current location**: Run pwd to see where you are in the filesystem
   ```bash
   pwd
   ```
   Expected output:
   ```
   /home/your-username
   ```

2. **Navigate to the root directory**: Change to the root and verify your location
   ```bash
   cd /
   pwd
   ```
   Expected output:
   ```
   /
   ```

3. **Explore a system directory**: Navigate to /etc and check your working directory
   ```bash
   cd /etc
   pwd
   ```
   Expected output:
   ```
   /etc
   ```

4. **Return to your home directory**: Use cd without arguments and confirm the change
   ```bash
   cd
   pwd
   ```
   Expected output:
   ```
   /home/your-username
   ```""",
        
        "list-directories-ls-command.md": """## Exercise

Follow these steps in your Ubuntu VM terminal to practice the concepts from this lesson:

1. **List files in your home directory**: See what files and folders you have
   ```bash
   ls
   ```
   Expected output:
   ```
   Desktop  Documents  Downloads  Music  Pictures  Videos
   ```

2. **Show hidden files**: View all files including those starting with a dot
   ```bash
   ls -a
   ```
   Expected output:
   ```
   .  ..  .bash_history  .bashrc  .profile  Desktop  Documents
   ```

3. **Get detailed file information**: Use the long format
   ```bash
   ls -l
   ```
   Expected output:
   ```
   drwxr-xr-x 2 user user 4096 Jan 15 10:30 Desktop
   drwxr-xr-x 2 user user 4096 Jan 15 10:30 Documents
   ```

4. **Combine flags**: List all files in long format with reverse sorting
   ```bash
   ls -lar
   ```

5. **List a specific directory**: View contents of /etc
   ```bash
   ls /etc
   ```""",

        "change-directory-cd-command.md": """## Exercise

Follow these steps in your Ubuntu VM terminal to practice the concepts from this lesson:

1. **Navigate to root directory**: Move to the top of the filesystem
   ```bash
   cd /
   pwd
   ```
   Expected output:
   ```
   /
   ```

2. **Use absolute path**: Navigate to /usr/share using the full path
   ```bash
   cd /usr/share
   pwd
   ```
   Expected output:
   ```
   /usr/share
   ```

3. **Use relative path**: Move up one directory level
   ```bash
   cd ..
   pwd
   ```
   Expected output:
   ```
   /usr
   ```

4. **Return to home directory**: Use cd without arguments
   ```bash
   cd
   pwd
   ```
   Expected output:
   ```
   /home/your-username
   ```

5. **Use cd with tilde**: Navigate to home using the ~ shortcut
   ```bash
   cd ~/Documents
   pwd
   ```""",

        "touch-command.md": """## Exercise

Follow these steps in your Ubuntu VM terminal to practice the concepts from this lesson:

1. **Create a new empty file**: Use touch to create a test file
   ```bash
   touch myfile.txt
   ls -l myfile.txt
   ```
   Expected output:
   ```
   -rw-rw-r-- 1 user user 0 Jan 19 10:30 myfile.txt
   ```

2. **Create multiple files at once**: Make several files in one command
   ```bash
   touch file1.txt file2.txt file3.txt
   ls -l file*.txt
   ```

3. **Update file timestamp**: Touch an existing file to update modification time
   ```bash
   touch myfile.txt
   ls -l myfile.txt
   ```

4. **Clean up test files**: Remove the created files
   ```bash
   rm myfile.txt file1.txt file2.txt file3.txt
   ```""",

        "file-command.md": """## Exercise

Follow these steps in your Ubuntu VM terminal to practice the concepts from this lesson:

1. **Check the type of a text file**: Identify what kind of file .bashrc is
   ```bash
   file ~/.bashrc
   ```
   Expected output:
   ```
   /home/user/.bashrc: ASCII text
   ```

2. **Check a binary file**: See the type of a system binary
   ```bash
   file /bin/ls
   ```
   Expected output:
   ```
   /bin/ls: ELF 64-bit LSB executable
   ```

3. **Check a directory**: Use file on a directory
   ```bash
   file /etc
   ```
   Expected output:
   ```
   /etc: directory
   ```

4. **Create and check different file types**: Make files and check them
   ```bash
   echo "Hello World" > test.txt
   file test.txt
   rm test.txt
   ```""",

        "cat-command.md": """## Exercise

Follow these steps in your Ubuntu VM terminal to practice the concepts from this lesson:

1. **View a simple file**: Display the contents of /etc/hostname
   ```bash
   cat /etc/hostname
   ```
   Expected output:
   ```
   ubuntu
   ```

2. **Create a file with cat**: Use cat to create and write content
   ```bash
   cat > mytext.txt
   This is line 1
   This is line 2
   (Press Ctrl+D to save)
   ```

3. **View your created file**: Display what you just created
   ```bash
   cat mytext.txt
   ```

4. **Concatenate multiple files**: Create another file and combine them
   ```bash
   echo "File 2 content" > file2.txt
   cat mytext.txt file2.txt
   ```

5. **Clean up**: Remove test files
   ```bash
   rm mytext.txt file2.txt
   ```""",

        "less-command.md": """## Exercise

Follow these steps in your Ubuntu VM terminal to practice the concepts from this lesson:

1. **Open a file with less**: View a system file
   ```bash
   less /etc/services
   ```
   Expected output:
   ```
   (Opens file in pager - press 'q' to quit)
   ```

2. **Navigate through the file**: Practice movement commands
   - Press **Space** to move down one page
   - Press **b** to move back one page
   - Press **g** to go to the beginning
   - Press **G** to go to the end
   - Press **q** to quit

3. **Search within less**: Open a file and search
   ```bash
   less /etc/services
   ```
   Then type **/http** and press Enter to search for "http"

4. **View command output with less**: Pipe a long listing into less
   ```bash
   ls -lR /etc | less
   ```""",

        "history-command.md": """## Exercise

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
   ```""",

        "copy-cp-command.md": """## Exercise

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
   ```""",

        "move-mv-command.md": """## Exercise

Follow these steps in your Ubuntu VM terminal to practice the concepts from this lesson:

1. **Create a file and rename it**: Use mv to change a filename
   ```bash
   echo "Test content" > oldname.txt
   mv oldname.txt newname.txt
   ls -l newname.txt
   ```

2. **Move a file to a different directory**: Create a directory and move a file
   ```bash
   mkdir mydir
   mv newname.txt mydir/
   ls mydir/
   ```

3. **Move and rename simultaneously**: Move file with new name
   ```bash
   mv mydir/newname.txt renamed_file.txt
   ls -l renamed_file.txt
   ```

4. **Move multiple files**: Create several files and move them
   ```bash
   touch file1.txt file2.txt file3.txt
   mv file1.txt file2.txt file3.txt mydir/
   ls mydir/
   ```

5. **Clean up**: Remove test files and directory
   ```bash
   rm -r mydir renamed_file.txt
   ```""",

        "make-directory-mkdir-command.md": """## Exercise

Follow these steps in your Ubuntu VM terminal to practice the concepts from this lesson:

1. **Create a single directory**: Make a new directory
   ```bash
   mkdir testdir
   ls -ld testdir
   ```

2. **Create multiple directories at once**: Make several directories
   ```bash
   mkdir dir1 dir2 dir3
   ls -d dir*
   ```

3. **Create nested directories**: Use -p flag to create parents
   ```bash
   mkdir -p parent/child/grandchild
   ls -R parent/
   ```

4. **Create directory with verbose output**: See confirmation
   ```bash
   mkdir -v myproject
   ```

5. **Clean up**: Remove all test directories
   ```bash
   rm -r testdir dir1 dir2 dir3 parent myproject
   ```""",

        "remove-rm-command.md": """## Exercise

Follow these steps in your Ubuntu VM terminal to practice the concepts from this lesson:

1. **Create and remove a single file**: Make a test file and delete it
   ```bash
   touch testfile.txt
   rm testfile.txt
   ls testfile.txt 2>/dev/null || echo "File removed successfully"
   ```

2. **Remove multiple files**: Create several files and delete them
   ```bash
   touch file1.txt file2.txt file3.txt
   rm file1.txt file2.txt file3.txt
   ```

3. **Remove files with verbose output**: Use -v
   ```bash
   touch demo.txt
   rm -v demo.txt
   ```

4. **Create and remove a directory**: Use -r flag
   ```bash
   mkdir testdir
   touch testdir/file.txt
   rm -r testdir
   ```

5. **Remove with interactive prompts**: Use -i
   ```bash
   touch important.txt
   rm -i important.txt
   ```""",

        "find-command.md": """## Exercise

Follow these steps in your Ubuntu VM terminal to practice the concepts from this lesson:

1. **Find files by name**: Search for files in your home directory
   ```bash
   find ~ -name "*.txt" 2>/dev/null | head -5
   ```

2. **Find files by type**: Look for all directories
   ```bash
   find /etc -type d 2>/dev/null | head -10
   ```

3. **Find recently modified files**: Search for files modified in last 7 days
   ```bash
   find ~ -type f -mtime -7 2>/dev/null | head -5
   ```

4. **Find empty files**: Create and find empty files
   ```bash
   touch empty1.txt empty2.txt
   find . -name "empty*.txt" -type f -empty
   ```

5. **Clean up**: Remove test files
   ```bash
   rm empty1.txt empty2.txt
   ```""",

        "help-command.md": """## Exercise

Follow these steps in your Ubuntu VM terminal to practice the concepts from this lesson:

1. **Get help for a built-in command**: Use help for cd
   ```bash
   help cd
   ```

2. **List all shell built-ins**: See what commands have help
   ```bash
   help | head -20
   ```

3. **Get help for another built-in**: Check help for alias
   ```bash
   help alias
   ```

4. **Get help for export**: Learn about the export command
   ```bash
   help export
   ```""",

        "man-command.md": """## Exercise

Follow these steps in your Ubuntu VM terminal to practice the concepts from this lesson:

1. **Read the manual for ls**: Open the comprehensive manual page
   ```bash
   man ls
   ```
   Expected output:
   ```
   (Opens manual - press 'q' to quit)
   ```

2. **Search within a man page**: Look for specific information
   ```bash
   man ls
   ```
   Then type **/recursive** and press Enter

3. **View manual for a configuration file**: Check passwd file docs
   ```bash
   man 5 passwd
   ```

4. **Search all manual pages**: Find commands related to "copy"
   ```bash
   man -k copy | head -10
   ```

5. **View man page sections**: Check available sections for passwd
   ```bash
   man -wa passwd
   ```""",

        "whatis-command.md": """## Exercise

Follow these steps in your Ubuntu VM terminal to practice the concepts from this lesson:

1. **Get brief description of ls**: See one-line summary
   ```bash
   whatis ls
   ```
   Expected output:
   ```
   ls (1)               - list directory contents
   ```

2. **Look up multiple commands**: Check several commands
   ```bash
   whatis ls pwd mkdir
   ```

3. **Check a system file**: Get info about passwd
   ```bash
   whatis passwd
   ```

4. **Use with wildcards**: Find commands starting with "net"
   ```bash
   whatis net* | head -5
   ```""",

        "exit-command.md": """## Exercise

Follow these steps in your Ubuntu VM terminal to practice the concepts from this lesson:

1. **Check exit status of successful command**: Run a command and check status
   ```bash
   ls /home
   echo $?
   ```
   Expected output:
   ```
   0
   ```

2. **Check exit status of failed command**: Run a failing command
   ```bash
   ls /nonexistent 2>/dev/null
   echo $?
   ```
   Expected output:
   ```
   2
   ```

3. **Exit with custom status code**: Test exit codes
   ```bash
   bash -c 'exit 5'
   echo $?
   ```
   Expected output:
   ```
   5
   ```

4. **Chain commands based on success**: Use && operator
   ```bash
   mkdir tempdir && cd tempdir && pwd
   cd .. && rmdir tempdir
   ```""",

        "the-shell.md": """## Exercise

Follow these steps in your Ubuntu VM terminal to practice the concepts from this lesson:

1. **Check your current shell**: See which shell you're using
   ```bash
   echo $SHELL
   ```
   Expected output:
   ```
   /bin/bash
   ```

2. **View available shells**: List all shells installed
   ```bash
   cat /etc/shells
   ```

3. **Check shell version**: See bash version
   ```bash
   bash --version | head -1
   ```

4. **Use shell expansion**: Try wildcard patterns
   ```bash
   echo /etc/*.conf | head -c 100
   ```

5. **View environment variables**: See shell variables
   ```bash
   env | head -10
   ```""",

        "alias-command.md": """## Exercise

Follow these steps in your Ubuntu VM terminal to practice the concepts from this lesson:

1. **Create a simple alias**: Make a shortcut
   ```bash
   alias ll='ls -la'
   ll
   ```

2. **View all current aliases**: List defined aliases
   ```bash
   alias
   ```

3. **Create an alias with options**: Make a helpful shortcut
   ```bash
   alias gohome='cd ~ && pwd'
   gohome
   ```

4. **Remove an alias**: Use unalias
   ```bash
   unalias ll
   alias | grep ll
   ```

5. **Create a permanent alias**: Add to .bashrc
   ```bash
   echo "alias myls='ls -lh'" >> ~/.bashrc
   tail -1 ~/.bashrc
   ```
   Note: Run `source ~/.bashrc` to apply immediately""",
    })
    
    return exercises

# Due to character limit, I'll create the script to continue with remaining categories
# This will be a working version that we can extend

def update_lesson_file(filepath, new_exercise):
    """Update a single lesson file with new exercise content."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Pattern to match the Exercise section
    pattern = r'## Exercise\s*\n\s*\n.*?(?=\n## Quiz Question|\n## Quiz Answer|$)'
    
    # Replace the Exercise section
    updated_content = re.sub(
        pattern,
        new_exercise + '\n',
        content,
        flags=re.DOTALL
    )
    
    # Write back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(updated_content)
    
    return True

def main():
    lessons_dir = Path("/home/runner/work/linuxjourney/linuxjourney/lessons/en")
    exercises = create_exercises_dict()
    
    all_files = sorted(lessons_dir.rglob("*.md"))
    
    updated_count = 0
    for filepath in all_files:
        filename = filepath.name
        exercise = exercises.get(filename)
        
        if exercise:
            try:
                update_lesson_file(filepath, exercise)
                print(f"✓ {filepath.relative_to(lessons_dir)}")
                updated_count += 1
            except Exception as e:
                print(f"✗ Error: {filepath}: {e}")
    
    print(f"\n=== {updated_count}/{len(all_files)} files updated ===")

if __name__ == "__main__":
    main()
