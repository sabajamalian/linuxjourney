#!/usr/bin/env python3
import os
import re
from pathlib import Path

# Define exercises for each lesson file
EXERCISES = {
    # command-line lessons
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
   .  ..  .bash_history  .bashrc  .profile  Desktop  Documents  Downloads
   ```

3. **Get detailed file information**: Use the long format to see permissions, sizes, and dates
   ```bash
   ls -l
   ```
   Expected output:
   ```
   total 24
   drwxr-xr-x 2 user user 4096 Jan 15 10:30 Desktop
   drwxr-xr-x 2 user user 4096 Jan 15 10:30 Documents
   ```

4. **Combine flags**: List all files in long format with reverse sorting
   ```bash
   ls -lar
   ```
   Expected output:
   ```
   (Shows all files in long format, sorted in reverse order)
   ```

5. **List a specific directory**: View contents of /etc directory
   ```bash
   ls /etc
   ```
   Expected output:
   ```
   (Shows system configuration files)
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
   ```
   Expected output:
   ```
   /home/your-username/Documents
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
   Expected output:
   ```
   -rw-rw-r-- 1 user user 0 Jan 19 10:31 file1.txt
   -rw-rw-r-- 1 user user 0 Jan 19 10:31 file2.txt
   -rw-rw-r-- 1 user user 0 Jan 19 10:31 file3.txt
   ```

3. **Update file timestamp**: Touch an existing file to update its modification time
   ```bash
   touch myfile.txt
   ls -l myfile.txt
   ```
   Expected output:
   ```
   -rw-rw-r-- 1 user user 0 Jan 19 10:32 myfile.txt
   (Note the updated timestamp)
   ```

4. **Clean up test files**: Remove the created files
   ```bash
   rm myfile.txt file1.txt file2.txt file3.txt
   ls -l *.txt
   ```
   Expected output:
   ```
   ls: cannot access '*.txt': No such file or directory
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
   /bin/ls: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked
   ```

3. **Check a directory**: Use file on a directory
   ```bash
   file /etc
   ```
   Expected output:
   ```
   /etc: directory
   ```

4. **Create and check different file types**: Make files with different extensions
   ```bash
   echo "Hello World" > test.txt
   file test.txt
   touch image.jpg
   file image.jpg
   ```
   Expected output:
   ```
   test.txt: ASCII text
   image.jpg: empty
   ```

5. **Clean up**: Remove test files
   ```bash
   rm test.txt image.jpg
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

2. **Create a file with cat**: Use cat to create and write content to a new file
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
   Expected output:
   ```
   This is line 1
   This is line 2
   ```

4. **Concatenate multiple files**: Create another file and combine them
   ```bash
   echo "File 2 content" > file2.txt
   cat mytext.txt file2.txt
   ```
   Expected output:
   ```
   This is line 1
   This is line 2
   File 2 content
   ```

5. **Clean up**: Remove test files
   ```bash
   rm mytext.txt file2.txt
   ```""",

    "less-command.md": """## Exercise

Follow these steps in your Ubuntu VM terminal to practice the concepts from this lesson:

1. **Open a file with less**: View a system file using less
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

3. **Search within less**: Open a file and search for a pattern
   ```bash
   less /etc/services
   ```
   Then type **/http** and press Enter to search for "http"

4. **View command output with less**: Pipe a long listing into less
   ```bash
   ls -lR /etc | less
   ```
   Expected output:
   ```
   (Displays output in pager format - press 'q' to quit)
   ```

5. **View multiple files**: Open several files in sequence
   ```bash
   less /etc/hostname /etc/hosts
   ```
   (Press **:n** for next file, **:p** for previous file)""",

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

2. **Repeat a specific command**: Run command number 2 from history
   ```bash
   !2
   ```
   Expected output:
   ```
   (Executes the command at position 2)
   ```

3. **Search history**: Use reverse search to find a previous command
   ```bash
   Press Ctrl+R, then type "ls"
   ```
   Expected output:
   ```
   (Shows most recent ls command - press Enter to execute)
   ```

4. **View last 10 commands**: Limit history output
   ```bash
   history 10
   ```
   Expected output:
   ```
   (Shows last 10 commands only)
   ```

5. **Clear history**: Remove all history entries
   ```bash
   history -c
   history
   ```
   Expected output:
   ```
   1  history
   ```""",

    "copy-cp-command.md": """## Exercise

Follow these steps in your Ubuntu VM terminal to practice the concepts from this lesson:

1. **Create a test file and copy it**: Make a file and create a copy
   ```bash
   echo "Original content" > original.txt
   cp original.txt copy.txt
   ls -l *.txt
   ```
   Expected output:
   ```
   -rw-rw-r-- 1 user user 17 Jan 19 10:30 copy.txt
   -rw-rw-r-- 1 user user 17 Jan 19 10:30 original.txt
   ```

2. **Copy with verbose output**: Use -v flag to see what's being copied
   ```bash
   cp -v original.txt another_copy.txt
   ```
   Expected output:
   ```
   'original.txt' -> 'another_copy.txt'
   ```

3. **Create a directory and copy files into it**: Make a test directory and copy files
   ```bash
   mkdir test_dir
   cp *.txt test_dir/
   ls test_dir/
   ```
   Expected output:
   ```
   another_copy.txt  copy.txt  original.txt
   ```

4. **Copy a directory recursively**: Copy entire directory with -r flag
   ```bash
   cp -r test_dir test_dir_backup
   ls test_dir_backup/
   ```
   Expected output:
   ```
   another_copy.txt  copy.txt  original.txt
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
   Expected output:
   ```
   -rw-rw-r-- 1 user user 13 Jan 19 10:30 newname.txt
   ```

2. **Move a file to a different directory**: Create a directory and move a file
   ```bash
   mkdir mydir
   mv newname.txt mydir/
   ls mydir/
   ```
   Expected output:
   ```
   newname.txt
   ```

3. **Move and rename simultaneously**: Move file to directory with new name
   ```bash
   mv mydir/newname.txt renamed_file.txt
   ls -l renamed_file.txt
   ```
   Expected output:
   ```
   -rw-rw-r-- 1 user user 13 Jan 19 10:30 renamed_file.txt
   ```

4. **Move multiple files**: Create several files and move them together
   ```bash
   touch file1.txt file2.txt file3.txt
   mv file1.txt file2.txt file3.txt mydir/
   ls mydir/
   ```
   Expected output:
   ```
   file1.txt  file2.txt  file3.txt
   ```

5. **Clean up**: Remove test files and directory
   ```bash
   rm -r mydir renamed_file.txt
   ```""",

    "make-directory-mkdir-command.md": """## Exercise

Follow these steps in your Ubuntu VM terminal to practice the concepts from this lesson:

1. **Create a single directory**: Make a new directory in your current location
   ```bash
   mkdir testdir
   ls -ld testdir
   ```
   Expected output:
   ```
   drwxrwxr-x 2 user user 4096 Jan 19 10:30 testdir
   ```

2. **Create multiple directories at once**: Make several directories with one command
   ```bash
   mkdir dir1 dir2 dir3
   ls -d dir*
   ```
   Expected output:
   ```
   dir1  dir2  dir3
   ```

3. **Create nested directories**: Use -p flag to create parent directories
   ```bash
   mkdir -p parent/child/grandchild
   ls -R parent/
   ```
   Expected output:
   ```
   parent/:
   child
   
   parent/child:
   grandchild
   
   parent/child/grandchild:
   ```

4. **Create directory with verbose output**: See confirmation as directory is created
   ```bash
   mkdir -v myproject
   ```
   Expected output:
   ```
   mkdir: created directory 'myproject'
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
   ls testfile.txt
   ```
   Expected output:
   ```
   ls: cannot access 'testfile.txt': No such file or directory
   ```

2. **Remove multiple files**: Create several files and delete them at once
   ```bash
   touch file1.txt file2.txt file3.txt
   rm file1.txt file2.txt file3.txt
   ls file*.txt
   ```
   Expected output:
   ```
   ls: cannot access 'file*.txt': No such file or directory
   ```

3. **Remove files with verbose output**: Use -v to see what's being deleted
   ```bash
   touch demo.txt
   rm -v demo.txt
   ```
   Expected output:
   ```
   removed 'demo.txt'
   ```

4. **Create and remove a directory**: Use -r flag for directories
   ```bash
   mkdir testdir
   touch testdir/file.txt
   rm -r testdir
   ls testdir
   ```
   Expected output:
   ```
   ls: cannot access 'testdir': No such file or directory
   ```

5. **Remove with interactive prompts**: Use -i to confirm each deletion
   ```bash
   touch important.txt
   rm -i important.txt
   ```
   Expected output:
   ```
   rm: remove regular empty file 'important.txt'? (type 'y' and press Enter)
   ```""",

    "find-command.md": """## Exercise

Follow these steps in your Ubuntu VM terminal to practice the concepts from this lesson:

1. **Find files by name**: Search for files in your home directory
   ```bash
   find ~ -name "*.txt" | head -5
   ```
   Expected output:
   ```
   (Lists up to 5 .txt files in your home directory)
   ```

2. **Find files by type**: Look for all directories in /etc
   ```bash
   find /etc -type d | head -10
   ```
   Expected output:
   ```
   /etc
   /etc/systemd
   /etc/ssh
   (and more directories)
   ```

3. **Find recently modified files**: Search for files modified in last 7 days
   ```bash
   find ~ -type f -mtime -7 | head -5
   ```
   Expected output:
   ```
   (Lists recently modified files)
   ```

4. **Find and execute command**: Find empty files and list them
   ```bash
   touch empty1.txt empty2.txt
   find . -name "empty*.txt" -type f -empty -exec ls -l {} \;
   ```
   Expected output:
   ```
   -rw-rw-r-- 1 user user 0 Jan 19 10:30 ./empty1.txt
   -rw-rw-r-- 1 user user 0 Jan 19 10:30 ./empty2.txt
   ```

5. **Clean up**: Remove test files
   ```bash
   rm empty1.txt empty2.txt
   ```""",

    "help-command.md": """## Exercise

Follow these steps in your Ubuntu VM terminal to practice the concepts from this lesson:

1. **Get help for a built-in command**: Use help for cd command
   ```bash
   help cd
   ```
   Expected output:
   ```
   cd: cd [-L|[-P [-e]] [-@]] [dir]
       Change the shell working directory.
   (displays usage information)
   ```

2. **List all shell built-ins**: See what commands have help available
   ```bash
   help | head -20
   ```
   Expected output:
   ```
   GNU bash, version 5.0.17(1)-release (x86_64-pc-linux-gnu)
   These shell commands are defined internally...
   ```

3. **Get help for another built-in**: Check help for the alias command
   ```bash
   help alias
   ```
   Expected output:
   ```
   alias: alias [-p] [name[=value] ... ]
       Define or display aliases.
   ```

4. **Compare with man pages**: See the difference between help and man
   ```bash
   help cd
   man cd
   ```
   Expected output:
   ```
   (help shows brief info, man might not have an entry for built-ins)
   ```""",

    "man-command.md": """## Exercise

Follow these steps in your Ubuntu VM terminal to practice the concepts from this lesson:

1. **Read the manual for ls**: Open the comprehensive manual page
   ```bash
   man ls
   ```
   Expected output:
   ```
   (Opens manual page - press 'q' to quit)
   ```

2. **Search within a man page**: Look for specific information
   ```bash
   man ls
   ```
   Then type **/recursive** and press Enter to find information about recursive listings

3. **View manual for a configuration file**: Check documentation for passwd file
   ```bash
   man 5 passwd
   ```
   Expected output:
   ```
   (Opens manual page for passwd file format)
   ```

4. **Search all manual pages**: Find commands related to "copy"
   ```bash
   man -k copy | head -10
   ```
   Expected output:
   ```
   cp (1)               - copy files and directories
   cpgr (8)             - copy with locking the given file
   (and more results)
   ```

5. **View man page sections**: Check what sections are available for passwd
   ```bash
   man -wa passwd
   ```
   Expected output:
   ```
   /usr/share/man/man1/passwd.1.gz
   /usr/share/man/man5/passwd.5.gz
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

2. **Look up multiple commands**: Check several commands at once
   ```bash
   whatis ls pwd cd mkdir
   ```
   Expected output:
   ```
   ls (1)               - list directory contents
   pwd (1)              - print name of current/working directory
   cd: nothing appropriate
   mkdir (1)            - make directories
   ```

3. **Check a system file**: Get info about passwd file
   ```bash
   whatis passwd
   ```
   Expected output:
   ```
   passwd (1)           - change user password
   passwd (5)           - the password file
   ```

4. **Use with wildcards**: Find all commands starting with "net"
   ```bash
   whatis net*
   ```
   Expected output:
   ```
   netcat (1)           - TCP/IP swiss army knife
   netstat (8)          - Print network connections
   (and more network-related commands)
   ```""",

    "exit-command.md": """## Exercise

Follow these steps in your Ubuntu VM terminal to practice the concepts from this lesson:

1. **Check exit status of successful command**: Run a command and check its status
   ```bash
   ls /home
   echo $?
   ```
   Expected output:
   ```
   (lists home directory)
   0
   ```

2. **Check exit status of failed command**: Run a failing command
   ```bash
   ls /nonexistent
   echo $?
   ```
   Expected output:
   ```
   ls: cannot access '/nonexistent': No such file or directory
   2
   ```

3. **Exit with custom status code**: Create a simple script to test exit codes
   ```bash
   bash -c 'exit 5'
   echo $?
   ```
   Expected output:
   ```
   5
   ```

4. **Chain commands based on success**: Use && to run command only if previous succeeds
   ```bash
   mkdir tempdir && cd tempdir && pwd
   ```
   Expected output:
   ```
   /home/user/tempdir
   ```

5. **Clean up**: Remove test directory and try exit
   ```bash
   cd ..
   rmdir tempdir
   ```
   Note: Type `exit` to close your terminal when ready""",

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

2. **View available shells**: List all shells installed on your system
   ```bash
   cat /etc/shells
   ```
   Expected output:
   ```
   /bin/sh
   /bin/bash
   /bin/dash
   /usr/bin/bash
   ```

3. **Check shell version**: See which version of bash you're running
   ```bash
   bash --version
   ```
   Expected output:
   ```
   GNU bash, version 5.0.17(1)-release (x86_64-pc-linux-gnu)
   ```

4. **Use shell expansion**: Try wildcard patterns
   ```bash
   echo /etc/*.conf | head -c 100
   ```
   Expected output:
   ```
   (Lists .conf files in /etc directory)
   ```

5. **View environment variables**: See what variables your shell maintains
   ```bash
   env | head -10
   ```
   Expected output:
   ```
   USER=your-username
   PATH=/usr/local/bin:/usr/bin:/bin
   HOME=/home/your-username
   (and more variables)
   ```""",

    "alias-command.md": """## Exercise

Follow these steps in your Ubuntu VM terminal to practice the concepts from this lesson:

1. **Create a simple alias**: Make a shortcut for a long command
   ```bash
   alias ll='ls -la'
   ll
   ```
   Expected output:
   ```
   (Shows detailed listing of all files)
   ```

2. **View all current aliases**: List defined aliases
   ```bash
   alias
   ```
   Expected output:
   ```
   alias ll='ls -la'
   (and any other default aliases)
   ```

3. **Create an alias with options**: Make a helpful shortcut
   ```bash
   alias gohome='cd ~ && pwd'
   gohome
   ```
   Expected output:
   ```
   /home/your-username
   ```

4. **Remove an alias**: Use unalias to delete an alias
   ```bash
   unalias ll
   alias
   ```
   Expected output:
   ```
   (ll alias is no longer listed)
   ```

5. **Create a permanent alias**: Add to .bashrc for persistence
   ```bash
   echo "alias myls='ls -lh'" >> ~/.bashrc
   cat ~/.bashrc | grep myls
   ```
   Expected output:
   ```
   alias myls='ls -lh'
   ```
   Note: Run `source ~/.bashrc` to apply changes immediately""",

}

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
    
    # Write back the updated content
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(updated_content)
    
    return True

def main():
    lessons_dir = Path("/home/runner/work/linuxjourney/linuxjourney/lessons/en")
    
    # Process files with pre-defined exercises
    for filename, exercise in EXERCISES.items():
        # Find the file in any subdirectory
        matches = list(lessons_dir.rglob(filename))
        if matches:
            filepath = matches[0]
            try:
                update_lesson_file(filepath, exercise)
                print(f"✓ Updated: {filepath}")
            except Exception as e:
                print(f"✗ Error updating {filepath}: {e}")
        else:
            print(f"✗ File not found: {filename}")

if __name__ == "__main__":
    main()
