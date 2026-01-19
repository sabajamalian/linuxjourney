#!/usr/bin/env python3
import re
from pathlib import Path

def get_all_exercises():
    """Generate exercises for all lessons - extended version."""
    ex = {}
    
    # TEXT-FU LESSONS (16 files)
    ex["grep-command.md"] = """## Exercise

Follow these steps in your Ubuntu VM terminal to practice the concepts from this lesson:

1. **Create a sample file for testing**: Make a file with multiple lines
   ```bash
   cat > sample.txt << EOF
   The quick brown fox jumps over the lazy dog
   Fox hunting is a traditional activity
   The red fox is very clever
   Dogs and foxes are different animals
   EOF
   ```

2. **Basic grep search**: Find all lines containing "fox"
   ```bash
   grep fox sample.txt
   ```
   Expected output:
   ```
   The quick brown fox jumps over the lazy dog
   The red fox is very clever
   ```

3. **Case-insensitive search**: Use -i flag to find "fox" regardless of case
   ```bash
   grep -i fox sample.txt
   ```
   Expected output:
   ```
   The quick brown fox jumps over the lazy dog
   Fox hunting is a traditional activity
   The red fox is very clever
   ```

4. **Count matching lines**: Use grep -c to count occurrences
   ```bash
   grep -c fox sample.txt
   ```
   Expected output:
   ```
   2
   ```

5. **Show only the match**: Use grep -o to see just the matching text
   ```bash
   grep -o fox sample.txt
   ```
   Expected output:
   ```
   fox
   fox
   ```

6. **Clean up**: Remove the test file
   ```bash
   rm sample.txt
   ```"""

    ex["head-command.md"] = """## Exercise

Follow these steps in your Ubuntu VM terminal to practice the concepts from this lesson:

1. **View first 10 lines of a system file**: Use default head behavior
   ```bash
   head /etc/passwd
   ```
   Expected output:
   ```
   (First 10 lines of the passwd file)
   ```

2. **View first 5 lines**: Use the -n flag to specify line count
   ```bash
   head -n 5 /etc/passwd
   ```
   Expected output:
   ```
   (First 5 lines of the passwd file)
   ```

3. **Create a test file and view it**: Make a file with numbered lines
   ```bash
   seq 1 100 > numbers.txt
   head numbers.txt
   ```
   Expected output:
   ```
   1
   2
   3
   4
   5
   6
   7
   8
   9
   10
   ```

4. **View first 15 lines**: Use head -n with a larger number
   ```bash
   head -n 15 numbers.txt
   ```
   Expected output:
   ```
   (Numbers 1 through 15)
   ```

5. **Clean up**: Remove the test file
   ```bash
   rm numbers.txt
   ```"""

    ex["tail-command.md"] = """## Exercise

Follow these steps in your Ubuntu VM terminal to practice the concepts from this lesson:

1. **View last 10 lines of a file**: Use default tail behavior
   ```bash
   tail /etc/passwd
   ```
   Expected output:
   ```
   (Last 10 lines of the passwd file)
   ```

2. **View last 5 lines**: Use the -n flag
   ```bash
   tail -n 5 /etc/passwd
   ```
   Expected output:
   ```
   (Last 5 lines of the passwd file)
   ```

3. **Create a test file**: Make a file with numbered lines
   ```bash
   seq 1 100 > numbers.txt
   tail numbers.txt
   ```
   Expected output:
   ```
   91
   92
   93
   94
   95
   96
   97
   98
   99
   100
   ```

4. **Follow a file in real-time**: Monitor a log file (press Ctrl+C to stop)
   ```bash
   tail -f /var/log/syslog
   ```
   Expected output:
   ```
   (Real-time log output - press Ctrl+C to exit)
   ```

5. **Clean up**: Remove the test file
   ```bash
   rm numbers.txt
   ```"""

    ex["sort-command.md"] = """## Exercise

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
   echo -e "10\n2\n30\n1\n20" > numbers.txt
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
   ```"""

    ex["cut-command.md"] = """## Exercise

Follow these steps in your Ubuntu VM terminal to practice the concepts from this lesson:

1. **Create a test file with delimited data**: Make a CSV-style file
   ```bash
   cat > data.txt << EOF
   John,Doe,30,Engineer
   Jane,Smith,25,Designer
   Bob,Johnson,35,Manager
   EOF
   ```

2. **Extract first column**: Use cut with delimiter
   ```bash
   cut -d',' -f1 data.txt
   ```
   Expected output:
   ```
   John
   Jane
   Bob
   ```

3. **Extract multiple columns**: Get first and last columns
   ```bash
   cut -d',' -f1,4 data.txt
   ```
   Expected output:
   ```
   John,Engineer
   Jane,Designer
   Bob,Manager
   ```

4. **Extract by character position**: Get first 5 characters of each line
   ```bash
   cut -c1-5 data.txt
   ```
   Expected output:
   ```
   John,
   Jane,
   Bob,J
   ```

5. **Clean up**: Remove test file
   ```bash
   rm data.txt
   ```"""

    ex["uniq-unique-command.md"] = """## Exercise

Follow these steps in your Ubuntu VM terminal to practice the concepts from this lesson:

1. **Create a file with duplicate lines**: Make a test file
   ```bash
   cat > duplicates.txt << EOF
   apple
   apple
   banana
   banana
   banana
   cherry
   cherry
   EOF
   ```

2. **Remove adjacent duplicate lines**: Use basic uniq
   ```bash
   uniq duplicates.txt
   ```
   Expected output:
   ```
   apple
   banana
   cherry
   ```

3. **Count occurrences**: Use -c flag to count duplicates
   ```bash
   uniq -c duplicates.txt
   ```
   Expected output:
   ```
   2 apple
   3 banana
   2 cherry
   ```

4. **Show only duplicated lines**: Use -d flag
   ```bash
   uniq -d duplicates.txt
   ```
   Expected output:
   ```
   apple
   banana
   cherry
   ```

5. **Sort and remove duplicates**: Combine with sort for non-adjacent duplicates
   ```bash
   echo -e "apple\nbanana\napple\ncherry\nbanana" | sort | uniq
   ```
   Expected output:
   ```
   apple
   banana
   cherry
   ```

6. **Clean up**: Remove test file
   ```bash
   rm duplicates.txt
   ```"""

    ex["tr-translate-command.md"] = """## Exercise

Follow these steps in your Ubuntu VM terminal to practice the concepts from this lesson:

1. **Convert lowercase to uppercase**: Use tr to change case
   ```bash
   echo "hello world" | tr 'a-z' 'A-Z'
   ```
   Expected output:
   ```
   HELLO WORLD
   ```

2. **Delete specific characters**: Remove vowels from a string
   ```bash
   echo "hello world" | tr -d 'aeiou'
   ```
   Expected output:
   ```
   hll wrld
   ```

3. **Replace characters**: Change spaces to underscores
   ```bash
   echo "hello world from linux" | tr ' ' '_'
   ```
   Expected output:
   ```
   hello_world_from_linux
   ```

4. **Delete all digits**: Remove numbers from text
   ```bash
   echo "abc123def456" | tr -d '0-9'
   ```
   Expected output:
   ```
   abcdef
   ```

5. **Squeeze repeated characters**: Reduce multiple spaces to single space
   ```bash
   echo "hello    world" | tr -s ' '
   ```
   Expected output:
   ```
   hello world
   ```"""

    ex["wc-command.md"] = """## Exercise

Follow these steps in your Ubuntu VM terminal to practice the concepts from this lesson:

1. **Count lines, words, and characters**: Create a test file and count
   ```bash
   cat > testfile.txt << EOF
   This is line one
   This is line two
   This is line three
   EOF
   wc testfile.txt
   ```
   Expected output:
   ```
   3 12 51 testfile.txt
   ```

2. **Count only lines**: Use -l flag
   ```bash
   wc -l testfile.txt
   ```
   Expected output:
   ```
   3 testfile.txt
   ```

3. **Count only words**: Use -w flag
   ```bash
   wc -w testfile.txt
   ```
   Expected output:
   ```
   12 testfile.txt
   ```

4. **Count characters**: Use -c flag
   ```bash
   wc -c testfile.txt
   ```
   Expected output:
   ```
   51 testfile.txt
   ```

5. **Count lines in multiple files**: Use wc with multiple files
   ```bash
   wc -l /etc/hostname /etc/hosts
   ```
   Expected output:
   ```
   (Line counts for each file plus total)
   ```

6. **Clean up**: Remove test file
   ```bash
   rm testfile.txt
   ```"""

    ex["nl-wc-command.md"] = """## Exercise

Follow these steps in your Ubuntu VM terminal to practice the concepts from this lesson:

1. **Number lines in a file**: Create a test file and add line numbers
   ```bash
   cat > lines.txt << EOF
   First line
   Second line
   Third line
   EOF
   nl lines.txt
   ```
   Expected output:
   ```
        1  First line
        2  Second line
        3  Third line
   ```

2. **Count lines, words, and bytes**: Use wc on the file
   ```bash
   wc lines.txt
   ```
   Expected output:
   ```
   3 6 33 lines.txt
   ```

3. **Count only lines**: Use wc -l
   ```bash
   wc -l lines.txt
   ```
   Expected output:
   ```
   3 lines.txt
   ```

4. **Number non-empty lines only**: Use nl with -b flag
   ```bash
   echo -e "line1\n\nline3\n\nline5" | nl -b a
   ```
   Expected output:
   ```
        1  line1
        2  
        3  line3
        4  
        5  line5
   ```

5. **Clean up**: Remove test file
   ```bash
   rm lines.txt
   ```"""

    ex["paste-command.md"] = """## Exercise

Follow these steps in your Ubuntu VM terminal to practice the concepts from this lesson:

1. **Create two test files**: Make files to paste together
   ```bash
   echo -e "A\nB\nC" > file1.txt
   echo -e "1\n2\n3" > file2.txt
   ```

2. **Paste files side by side**: Merge files horizontally
   ```bash
   paste file1.txt file2.txt
   ```
   Expected output:
   ```
   A       1
   B       2
   C       3
   ```

3. **Use custom delimiter**: Paste with comma delimiter
   ```bash
   paste -d',' file1.txt file2.txt
   ```
   Expected output:
   ```
   A,1
   B,2
   C,3
   ```

4. **Paste serially**: Use -s to paste one file per line
   ```bash
   paste -s file1.txt
   ```
   Expected output:
   ```
   A       B       C
   ```

5. **Clean up**: Remove test files
   ```bash
   rm file1.txt file2.txt
   ```"""

    ex["join-split-command.md"] = """## Exercise

Follow these steps in your Ubuntu VM terminal to practice the concepts from this lesson:

1. **Create files with common fields**: Make two files to join
   ```bash
   echo -e "1 John\n2 Jane\n3 Bob" > names.txt
   echo -e "1 Engineer\n2 Designer\n3 Manager" > jobs.txt
   ```

2. **Join files on common field**: Merge based on first column
   ```bash
   join names.txt jobs.txt
   ```
   Expected output:
   ```
   1 John Engineer
   2 Jane Designer
   3 Bob Manager
   ```

3. **Create a large file to split**: Make a file with multiple lines
   ```bash
   seq 1 100 > bigfile.txt
   ```

4. **Split file into smaller files**: Use split command
   ```bash
   split -l 25 bigfile.txt part_
   ls part_*
   ```
   Expected output:
   ```
   part_aa  part_ab  part_ac  part_ad
   ```

5. **View one of the split files**: Check the content
   ```bash
   head part_aa
   ```
   Expected output:
   ```
   1
   2
   3
   4
   5
   6
   7
   8
   9
   10
   ```

6. **Clean up**: Remove all test files
   ```bash
   rm names.txt jobs.txt bigfile.txt part_*
   ```"""

    ex["expand-unexpand-command.md"] = """## Exercise

Follow these steps in your Ubuntu VM terminal to practice the concepts from this lesson:

1. **Create a file with tabs**: Make a test file with tab characters
   ```bash
   echo -e "Col1\tCol2\tCol3" > tabbed.txt
   cat tabbed.txt
   ```

2. **Convert tabs to spaces**: Use expand command
   ```bash
   expand tabbed.txt
   ```
   Expected output:
   ```
   Col1    Col2    Col3
   (Tabs converted to spaces)
   ```

3. **Specify tab width**: Use -t flag to set tab width
   ```bash
   expand -t 4 tabbed.txt
   ```
   Expected output:
   ```
   Col1 Col2 Col3
   (Tabs converted to 4 spaces)
   ```

4. **Convert spaces back to tabs**: Use unexpand command
   ```bash
   expand tabbed.txt | unexpand
   ```
   Expected output:
   ```
   (Spaces converted back to tabs)
   ```

5. **Clean up**: Remove test file
   ```bash
   rm tabbed.txt
   ```"""

    ex["pipe-tee-redirect.md"] = """## Exercise

Follow these steps in your Ubuntu VM terminal to practice the concepts from this lesson:

1. **Use pipe to chain commands**: List files and count them
   ```bash
   ls /etc | wc -l
   ```
   Expected output:
   ```
   (Number of files in /etc directory)
   ```

2. **Use tee to view and save output**: See output and save to file
   ```bash
   ls /etc | tee filelist.txt | head -10
   ```
   Expected output:
   ```
   (First 10 files displayed and all saved to filelist.txt)
   ```

3. **Chain multiple pipes**: Filter and sort results
   ```bash
   ls -l /etc | grep ".conf" | wc -l
   ```
   Expected output:
   ```
   (Number of .conf files in /etc)
   ```

4. **Use tee to append**: Append to file instead of overwriting
   ```bash
   echo "New entry" | tee -a filelist.txt
   cat filelist.txt | tail -5
   ```

5. **Complex pipe chain**: Combine multiple text processing tools
   ```bash
   cat /etc/passwd | cut -d: -f1 | sort | head -10
   ```
   Expected output:
   ```
   (First 10 usernames sorted alphabetically)
   ```

6. **Clean up**: Remove test file
   ```bash
   rm filelist.txt
   ```"""

    ex["stdout-standard-out-redirect.md"] = """## Exercise

Follow these steps in your Ubuntu VM terminal to practice the concepts from this lesson:

1. **Redirect output to a file**: Save command output to a file
   ```bash
   echo "Hello World" > output.txt
   cat output.txt
   ```
   Expected output:
   ```
   Hello World
   ```

2. **Append to a file**: Add more content without overwriting
   ```bash
   echo "Second line" >> output.txt
   cat output.txt
   ```
   Expected output:
   ```
   Hello World
   Second line
   ```

3. **Redirect ls output**: Save directory listing to a file
   ```bash
   ls -la ~ > homelist.txt
   head -5 homelist.txt
   ```
   Expected output:
   ```
   (First 5 lines of your home directory listing)
   ```

4. **Overwrite existing file**: Use > to replace file contents
   ```bash
   echo "New content" > output.txt
   cat output.txt
   ```
   Expected output:
   ```
   New content
   ```

5. **Clean up**: Remove test files
   ```bash
   rm output.txt homelist.txt
   ```"""

    ex["stdin-standard-in-redirect.md"] = """## Exercise

Follow these steps in your Ubuntu VM terminal to practice the concepts from this lesson:

1. **Create a test file**: Make a file to use as input
   ```bash
   cat > input.txt << EOF
   Line 1
   Line 2
   Line 3
   EOF
   ```

2. **Redirect file as input**: Use < to provide input to a command
   ```bash
   cat < input.txt
   ```
   Expected output:
   ```
   Line 1
   Line 2
   Line 3
   ```

3. **Use stdin with sort**: Sort contents of a file via stdin
   ```bash
   sort < input.txt
   ```
   Expected output:
   ```
   Line 1
   Line 2
   Line 3
   ```

4. **Combine input and output redirection**: Read from one file, write to another
   ```bash
   tr 'a-z' 'A-Z' < input.txt > output.txt
   cat output.txt
   ```
   Expected output:
   ```
   LINE 1
   LINE 2
   LINE 3
   ```

5. **Clean up**: Remove test files
   ```bash
   rm input.txt output.txt
   ```"""

    ex["stderr-standard-error-redirect.md"] = """## Exercise

Follow these steps in your Ubuntu VM terminal to practice the concepts from this lesson:

1. **Generate an error**: Try to access a non-existent file
   ```bash
   cat /nonexistent 2> error.log
   cat error.log
   ```
   Expected output:
   ```
   cat: /nonexistent: No such file or directory
   ```

2. **Redirect both stdout and stderr**: Send both to different files
   ```bash
   ls /etc /nonexistent > output.log 2> error.log
   cat output.log | head -5
   cat error.log
   ```

3. **Redirect stderr to stdout**: Combine error and output streams
   ```bash
   ls /etc /nonexistent 2>&1 | head -10
   ```
   Expected output:
   ```
   (Combined output and error messages)
   ```

4. **Discard errors**: Send stderr to /dev/null
   ```bash
   ls /etc /nonexistent 2>/dev/null | head -5
   ```
   Expected output:
   ```
   (Only shows successful output, errors discarded)
   ```

5. **Clean up**: Remove test files
   ```bash
   rm error.log output.log
   ```"""

    ex["env-environment.md"] = """## Exercise

Follow these steps in your Ubuntu VM terminal to practice the concepts from this lesson:

1. **View all environment variables**: Display current environment
   ```bash
   env | head -20
   ```
   Expected output:
   ```
   (Lists environment variables like PATH, HOME, USER, etc.)
   ```

2. **Check specific variable**: View the PATH variable
   ```bash
   echo $PATH
   ```
   Expected output:
   ```
   /usr/local/bin:/usr/bin:/bin:/usr/games
   ```

3. **Set a new variable**: Create a temporary environment variable
   ```bash
   export MYVAR="Hello Linux"
   echo $MYVAR
   ```
   Expected output:
   ```
   Hello Linux
   ```

4. **View user-related variables**: Check HOME and USER
   ```bash
   echo "User: $USER, Home: $HOME"
   ```
   Expected output:
   ```
   User: your-username, Home: /home/your-username
   ```

5. **Filter environment variables**: Find variables containing "PATH"
   ```bash
   env | grep PATH
   ```
   Expected output:
   ```
   PATH=/usr/local/bin:/usr/bin:/bin
   ```"""

    return ex

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
    exercises = get_all_exercises()
    
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
    
    print(f"\n=== {updated_count} additional files updated ===")

if __name__ == "__main__":
    main()
