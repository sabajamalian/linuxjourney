# Student Guide: Linux Journey

## Welcome to Linux Journey!

This course will teach you Linux fundamentals through hands-on practice in your own Ubuntu virtual machine. You have full root access to your VM, which means you can practice all commands and experiment freely.

## Getting Started

### Your Virtual Machine

You have been assigned a personal Ubuntu Linux VM for this course. Your instructor will provide:

- **VM Address**: The IP address of your VM (e.g., `20.10.30.40`)
- **Username**: Your login username (typically `student`)
- **SSH Key**: A private key file for authentication (or you'll use your own)

### Connecting to Your VM

#### From Linux or Mac

1. Open a terminal application
2. If using a private key file, ensure correct permissions:
   ```bash
   chmod 600 ~/path/to/your-key.pem
   ```
3. Connect to your VM:
   ```bash
   ssh student@YOUR_VM_ADDRESS
   ```
   Or with a key file:
   ```bash
   ssh -i ~/path/to/your-key.pem student@YOUR_VM_ADDRESS
   ```

#### From Windows

**Option 1: Windows Terminal or PowerShell**
```powershell
ssh student@YOUR_VM_ADDRESS
```

**Option 2: PuTTY**
1. Download and install [PuTTY](https://www.putty.org/)
2. Open PuTTY
3. Enter your VM address in "Host Name"
4. Click "Open"
5. Login with your username when prompted

**Option 3: WSL (Windows Subsystem for Linux)**
1. Install WSL if not already installed
2. Open WSL terminal
3. Follow the Linux instructions above

### First Login

When you first connect, you'll see a welcome message and command prompt:

```
student@linux-journey-student:~$
```

This means you're logged in and ready to start learning!

## Your Learning Environment

### What You Have

- **Ubuntu Linux**: Latest LTS (Long Term Support) version
- **Full root access**: You can use `sudo` for any administrative commands
- **Your own space**: Everything you do is isolated from other students
- **Safe environment**: You can experiment freely; mistakes won't affect others

### Understanding Root Access

Many Linux commands require administrative privileges. In your VM, you have full sudo access:

```bash
# Regular command
ls /home

# Command requiring root privileges
sudo apt update
```

When you use `sudo`, you're running the command as the root (administrator) user. The first time you use sudo in a session, you may be prompted for your password.

## Following the Lessons

### Course Structure

The course has three levels:

1. **Grasshopper**: Learn the basics (Start here!)
2. **Journeyman**: System internals
3. **Networking Nomad**: Network administration

### How to Learn

1. **Read**: Each lesson introduces a concept and commands
2. **Practice**: Try every command in your VM terminal
3. **Experiment**: Modify commands to see what happens
4. **Explore**: Use `man` pages to learn more about commands

### Example Learning Flow

1. Open the lesson file (e.g., `lessons/en/command-line/the-shell.md`)
2. Read the lesson content
3. Follow along in your VM terminal
4. Complete the exercises
5. Answer the quiz questions to test your understanding

## Tips for Success

### Practice Safely

- **Experiment freely**: Your VM is yours alone; you can't break anything that matters
- **Try to recover**: If something goes wrong, try to fix it (that's learning!)
- **Ask for help**: If you're stuck, ask your instructor
- **Take notes**: Document commands and concepts that work well

### Essential Commands to Remember

```bash
# Get help for any command
man command_name

# Clear your terminal
clear

# See command history
history

# Exit the terminal
exit
```

### Working with Root Access

Since you have full sudo access:

```bash
# Install new software
sudo apt install package_name

# Edit system files
sudo nano /etc/filename

# Restart services
sudo systemctl restart service_name

# Change system settings
sudo systemctl enable service_name
```

**Important**: With great power comes great responsibility! Some commands can delete important files or stop your system. Read carefully before executing sudo commands.

### Managing Your Files

Create organized directories for practice:

```bash
# Create a practice directory
mkdir ~/practice

# Create lesson-specific directories
mkdir ~/practice/command-line
mkdir ~/practice/permissions
mkdir ~/practice/networking

# Navigate to practice area
cd ~/practice
```

## Common Tasks

### Updating Your System

Keep your VM up to date:

```bash
sudo apt update          # Update package lists
sudo apt upgrade -y      # Install available updates
```

### Installing Additional Software

If a lesson requires specific software:

```bash
sudo apt install software-name
```

### Checking Disk Space

Monitor your VM's disk usage:

```bash
df -h                    # Show disk space
du -sh ~/               # Show home directory size
```

### Viewing System Information

Learn about your VM:

```bash
uname -a                 # System information
lsb_release -a          # Ubuntu version
hostname                # VM hostname
whoami                  # Current username
```

## Troubleshooting

### Can't Connect to VM

1. Check your internet connection
2. Verify the VM address is correct
3. Ensure the VM is running (ask your instructor)
4. Check SSH key file permissions (should be 600)

### Forgot a Command

```bash
# Search command history
history | grep keyword

# Get help for a command
man command_name
command_name --help
```

### Terminal Appears Frozen

- Press `Ctrl+C` to cancel current command
- Press `Ctrl+Z` to suspend current command
- Type `exit` to close terminal and reconnect

### Made a Mistake

Most mistakes are recoverable:

```bash
# Undo file deletion (if just deleted)
# Unfortunately, rm is permanent - be careful!

# Restore a file from backup (if you made one)
cp ~/backup/file.txt ~/file.txt

# Reinstall a broken package
sudo apt install --reinstall package_name
```

## Best Practices

1. **Read before executing**: Understand what a command does before running it
2. **Make backups**: Before editing important files: `cp file.txt file.txt.backup`
3. **Use tab completion**: Press Tab to autocomplete commands and filenames
4. **Check before sudo**: Double-check commands that require root access
5. **Practice regularly**: Consistent practice builds skills faster

## After the Course

### What Happens to Your VM?

Your VM will be deleted after the course ends. Make sure to:

- Save any important notes or scripts to your local computer
- Download any files you want to keep:
  ```bash
  # From your local computer
  scp student@YOUR_VM_ADDRESS:~/file.txt ~/Downloads/
  ```

### Continuing Your Learning

- Set up your own Linux VM or dual-boot system
- Explore additional Linux distributions
- Join Linux communities and forums
- Work on personal projects using Linux

## Getting Help

- **During class**: Ask your instructor
- **Course materials**: Review lesson files in the repository
- **Man pages**: `man command_name` for detailed documentation
- **Online**: Search for "Ubuntu [your question]"

## Ready to Start?

1. Connect to your VM
2. Open `lessons/en/command-line/the-shell.md`
3. Start learning!

Good luck on your Linux journey! 🐧
