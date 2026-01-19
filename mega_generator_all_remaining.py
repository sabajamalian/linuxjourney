#!/usr/bin/env python3
"""
Mega generator for all remaining 144 lessons.
This creates exercises for: permissions, processes, packages, devices,  
filesystem, boot-system, kernel, init, process-utilization, logging,
network-basics, network-config, network-sharing, routing, subnetting,
troubleshooting, dns, getting-started, and advanced-text-fu
"""
import re
from pathlib import Path

def get_remaining_exercises():
    """Get exercises for all remaining 144 lessons."""
    ex = {}
    
    # ========== PERMISSIONS LESSONS (8 files) ==========
    ex["file-permissions.md"] = """## Exercise

Follow these steps in your Ubuntu VM terminal to practice the concepts from this lesson:

1. **Create a test file and check permissions**: Make a file and view its permissions
   ```bash
   touch testfile.txt
   ls -l testfile.txt
   ```
   Expected output:
   ```
   -rw-rw-r-- 1 user user 0 Jan 19 10:30 testfile.txt
   ```

2. **Understand permission notation**: Break down the permission string
   - First character: file type (- for regular file, d for directory)
   - Next 9 characters: rwxrwxrwx (owner, group, others)
   - rw-rw-r-- means: owner can read/write, group can read/write, others can only read

3. **Check directory permissions**: View permissions of a directory
   ```bash
   ls -ld /home
   ```
   Expected output:
   ```
   drwxr-xr-x 3 root root 4096 Jan 15 10:30 /home
   ```

4. **View permissions in octal**: Use stat to see numeric permissions
   ```bash
   stat -c "%a %n" testfile.txt
   ```
   Expected output:
   ```
   664 testfile.txt
   ```

5. **Clean up**: Remove test file
   ```bash
   rm testfile.txt
   ```"""

    ex["modifying-permissions.md"] = """## Exercise

Follow these steps in your Ubuntu VM terminal to practice the concepts from this lesson:

1. **Create a test file**: Make a file to modify permissions
   ```bash
   touch myfile.txt
   ls -l myfile.txt
   ```
   Expected output:
   ```
   -rw-rw-r-- 1 user user 0 Jan 19 10:30 myfile.txt
   ```

2. **Add execute permission for owner**: Use chmod with symbolic notation
   ```bash
   chmod u+x myfile.txt
   ls -l myfile.txt
   ```
   Expected output:
   ```
   -rwxrw-r-- 1 user user 0 Jan 19 10:30 myfile.txt
   ```

3. **Remove write permission for group**: Use chmod to remove permissions
   ```bash
   chmod g-w myfile.txt
   ls -l myfile.txt
   ```
   Expected output:
   ```
   -rwxr--r-- 1 user user 0 Jan 19 10:30 myfile.txt
   ```

4. **Set permissions with octal notation**: Use numeric mode
   ```bash
   chmod 755 myfile.txt
   ls -l myfile.txt
   ```
   Expected output:
   ```
   -rwxr-xr-x 1 user user 0 Jan 19 10:30 myfile.txt
   ```

5. **Set restrictive permissions**: Make file owner-only accessible
   ```bash
   chmod 600 myfile.txt
   ls -l myfile.txt
   ```
   Expected output:
   ```
   -rw------- 1 user user 0 Jan 19 10:30 myfile.txt
   ```

6. **Clean up**: Remove test file
   ```bash
   rm myfile.txt
   ```"""

    ex["ownership-permissions.md"] = """## Exercise

Follow these steps in your Ubuntu VM terminal to practice the concepts from this lesson:

1. **Create a test file and check ownership**: Make a file and see who owns it
   ```bash
   touch testfile.txt
   ls -l testfile.txt
   ```
   Expected output:
   ```
   -rw-rw-r-- 1 your-username your-username 0 Jan 19 10:30 testfile.txt
   ```

2. **View file ownership details**: Use stat command
   ```bash
   stat testfile.txt
   ```
   Expected output:
   ```
   File: testfile.txt
   Size: 0           Blocks: 0          IO Block: 4096   regular empty file
   Device: 802h/2050d  Inode: 123456      Links: 1
   Access: (0664/-rw-rw-r--)  Uid: ( 1000/your-username)   Gid: ( 1000/your-username)
   ```

3. **Create a directory and check ownership**: Make a directory
   ```bash
   mkdir testdir
   ls -ld testdir
   ```
   Expected output:
   ```
   drwxrwxr-x 2 your-username your-username 4096 Jan 19 10:30 testdir
   ```

4. **View numeric user and group IDs**: Check IDs with stat
   ```bash
   stat -c "Owner UID: %u, Owner GID: %g" testfile.txt
   ```
   Expected output:
   ```
   Owner UID: 1000, Owner GID: 1000
   ```

5. **Clean up**: Remove test files
   ```bash
   rm testfile.txt
   rmdir testdir
   ```"""

    ex["process-permissions.md"] = """## Exercise

Follow these steps in your Ubuntu VM terminal to practice the concepts from this lesson:

1. **Check your current process permissions**: View your effective user ID
   ```bash
   id
   ```
   Expected output:
   ```
   uid=1000(user) gid=1000(user) groups=1000(user),4(adm),27(sudo)
   ```

2. **Create a script and check its execution**: Make an executable file
   ```bash
   echo '#!/bin/bash' > myscript.sh
   echo 'echo "Hello from $USER"' >> myscript.sh
   chmod +x myscript.sh
   ./myscript.sh
   ```
   Expected output:
   ```
   Hello from your-username
   ```

3. **View process ownership**: See which user owns running processes
   ```bash
   ps aux | grep bash | head -3
   ```
   Expected output:
   ```
   USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
   user      1234  0.0  0.1  21536  5124 pts/0    Ss   10:30   0:00 /bin/bash
   ```

4. **Check effective permissions**: Run a command and verify permissions
   ```bash
   touch permtest.txt
   ls -l permtest.txt
   ```
   Expected output:
   ```
   -rw-rw-r-- 1 user user 0 Jan 19 10:30 permtest.txt
   (File owned by the user who created it)
   ```

5. **Clean up**: Remove test files
   ```bash
   rm myscript.sh permtest.txt
   ```"""

    ex["setuid-set-user-id.md"] = """## Exercise

Follow these steps in your Ubuntu VM terminal to practice the concepts from this lesson:

1. **Find files with setuid bit set**: Look for SUID executables
   ```bash
   find /usr/bin -perm -4000 2>/dev/null | head -5
   ```
   Expected output:
   ```
   /usr/bin/sudo
   /usr/bin/passwd
   /usr/bin/chsh
   /usr/bin/newgrp
   /usr/bin/gpasswd
   ```

2. **Check passwd command permissions**: View the SUID bit on passwd
   ```bash
   ls -l /usr/bin/passwd
   ```
   Expected output:
   ```
   -rwsr-xr-x 1 root root 68208 Jan 15 2020 /usr/bin/passwd
   (Note the 's' in owner execute permission)
   ```

3. **Create a test script and set SUID**: Experiment with SUID (for learning)
   ```bash
   echo '#!/bin/bash' > testscript.sh
   echo 'echo "Running as: $(whoami)"' >> testscript.sh
   chmod +x testscript.sh
   chmod u+s testscript.sh
   ls -l testscript.sh
   ```
   Expected output:
   ```
   -rwsr-xr-x 1 user user 50 Jan 19 10:30 testscript.sh
   ```

4. **Test the script**: Run it to see current user
   ```bash
   ./testscript.sh
   ```
   Expected output:
   ```
   Running as: your-username
   (SUID doesn't work for scripts in modern systems for security)
   ```

5. **Check SUID in octal notation**: View numeric permissions
   ```bash
   stat -c "%a" testscript.sh
   ```
   Expected output:
   ```
   4755
   (4 prefix indicates SUID bit is set)
   ```

6. **Clean up**: Remove test script
   ```bash
   rm testscript.sh
   ```"""

    ex["setgid-set-group-id.md"] = """## Exercise

Follow these steps in your Ubuntu VM terminal to practice the concepts from this lesson:

1. **Find files with setgid bit**: Look for SGID files
   ```bash
   find /usr/bin -perm -2000 2>/dev/null | head -5
   ```
   Expected output:
   ```
   /usr/bin/ssh-agent
   /usr/bin/wall
   (SGID executables on system)
   ```

2. **Create a directory with SGID**: Make a directory for testing
   ```bash
   mkdir testdir
   chmod g+s testdir
   ls -ld testdir
   ```
   Expected output:
   ```
   drwxrwsr-x 2 user user 4096 Jan 19 10:30 testdir
   (Note the 's' in group execute permission)
   ```

3. **Create a file in SGID directory**: Test inheritance
   ```bash
   touch testdir/newfile.txt
   ls -l testdir/newfile.txt
   ```
   Expected output:
   ```
   -rw-rw-r-- 1 user user 0 Jan 19 10:30 testdir/newfile.txt
   (File inherits the group from parent directory)
   ```

4. **Check SGID in octal notation**: View numeric permissions
   ```bash
   stat -c "%a" testdir
   ```
   Expected output:
   ```
   2775
   (2 prefix indicates SGID bit is set)
   ```

5. **Clean up**: Remove test directory
   ```bash
   rm -r testdir
   ```"""

    ex["sticky-bit.md"] = """## Exercise

Follow these steps in your Ubuntu VM terminal to practice the concepts from this lesson:

1. **Check /tmp directory sticky bit**: View the sticky bit on /tmp
   ```bash
   ls -ld /tmp
   ```
   Expected output:
   ```
   drwxrwxrwt 15 root root 4096 Jan 19 10:30 /tmp
   (Note the 't' at the end - sticky bit)
   ```

2. **Create a directory and set sticky bit**: Make a test directory
   ```bash
   mkdir testshared
   chmod +t testshared
   ls -ld testshared
   ```
   Expected output:
   ```
   drwxrwxr-t 2 user user 4096 Jan 19 10:30 testshared
   ```

3. **Set sticky bit with octal notation**: Use numeric mode
   ```bash
   chmod 1777 testshared
   ls -ld testshared
   ```
   Expected output:
   ```
   drwxrwxrwt 2 user user 4096 Jan 19 10:30 testshared
   (1 prefix indicates sticky bit)
   ```

4. **Test sticky bit behavior**: Create a file in the directory
   ```bash
   touch testshared/myfile.txt
   ls -l testshared/
   ```
   Expected output:
   ```
   -rw-rw-r-- 1 user user 0 Jan 19 10:30 myfile.txt
   (Only owner can delete this file, even though dir is world-writable)
   ```

5. **Clean up**: Remove test directory
   ```bash
   rm -r testshared
   ```"""

    ex["umask.md"] = """## Exercise

Follow these steps in your Ubuntu VM terminal to practice the concepts from this lesson:

1. **Check current umask value**: View your default umask
   ```bash
   umask
   ```
   Expected output:
   ```
   0002
   (Common default umask value)
   ```

2. **Create a file and check default permissions**: See umask in action
   ```bash
   touch testfile1.txt
   ls -l testfile1.txt
   ```
   Expected output:
   ```
   -rw-rw-r-- 1 user user 0 Jan 19 10:30 testfile1.txt
   (666 - 002 = 664 permissions)
   ```

3. **Change umask temporarily**: Set a more restrictive umask
   ```bash
   umask 0077
   umask
   ```
   Expected output:
   ```
   0077
   ```

4. **Create a file with new umask**: See how permissions change
   ```bash
   touch testfile2.txt
   ls -l testfile2.txt
   ```
   Expected output:
   ```
   -rw------- 1 user user 0 Jan 19 10:30 testfile2.txt
   (666 - 077 = 600 permissions)
   ```

5. **Create a directory with current umask**: Check directory permissions
   ```bash
   mkdir testdir
   ls -ld testdir
   ```
   Expected output:
   ```
   drwx------ 2 user user 4096 Jan 19 10:30 testdir
   (777 - 077 = 700 permissions)
   ```

6. **Restore default umask and clean up**: Reset umask
   ```bash
   umask 0002
   rm testfile1.txt testfile2.txt
   rmdir testdir
   ```"""

    # Continue with more categories...
    # I'll add more in the next section
    
    return ex

def update_lesson_file(filepath, new_exercise):
    """Update a single lesson file with new exercise content."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    pattern = r'## Exercise\s*\n\s*\n.*?(?=\n## Quiz Question|\n## Quiz Answer|$)'
    
    updated_content = re.sub(
        pattern,
        new_exercise + '\n',
        content,
        flags=re.DOTALL
    )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(updated_content)
    
    return True

def main():
    lessons_dir = Path("/home/runner/work/linuxjourney/linuxjourney/lessons/en")
    exercises = get_remaining_exercises()
    
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
    
    print(f"\n=== {updated_count} files updated in this batch ===")

if __name__ == "__main__":
    main()
