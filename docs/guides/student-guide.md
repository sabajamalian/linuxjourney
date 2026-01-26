---
title: "Student Guide"
layout: default
parent: Guides
nav_order: 1
---

# Student Guide: Linux Journey

## Welcome to Linux Journey!

This course will teach you Linux fundamentals through hands-on practice in your own Ubuntu virtual machine. You have full root access to your VM, which means you can practice all commands and experiment freely.

## Understanding Remote Servers and SSH

### What is a Remote Server?

A **remote server** is a computer that is physically located somewhere else (not in front of you) but can be accessed and controlled over a network, typically the internet. Think of it like this:

- **Your computer** (the one you're using right now) is called the **local machine** or **client**
- **The server** (the computer you want to connect to) is called the **remote machine** or **host**

Remote servers are powerful computers that run 24/7 in data centers around the world. They can be used for:
- Hosting websites and web applications
- Running databases
- Storing and processing data
- Providing cloud computing services
- Learning and practicing Linux (like in this course!)

When you connect to a remote server, you're essentially controlling that computer from your own machine. You type commands on your keyboard, they get sent over the internet to the server, the server executes them, and sends the results back to you.

### What is SSH?

**SSH** stands for **Secure Shell**. It is a network protocol (a set of rules for communication) that allows you to securely connect to and control a remote computer over an unsecured network like the internet.

#### Why is SSH Important?

1. **Security**: All communication between your computer and the remote server is encrypted, meaning no one can eavesdrop on your commands or data
2. **Remote Access**: You can control a Linux server from anywhere in the world as if you were sitting right in front of it
3. **No Graphical Interface Needed**: SSH gives you command-line access, which is the most common way to manage Linux servers
4. **Industry Standard**: SSH is used by system administrators, developers, and DevOps engineers worldwide

#### How SSH Works (Simplified)

1. You initiate a connection from your computer (client) to the server
2. The server and client establish an encrypted connection
3. You authenticate (prove who you are) using a username and password
4. Once authenticated, you get a command-line interface to the remote server
5. Every command you type is encrypted, sent to the server, executed, and the output is sent back to you

## Getting Started

### Your Virtual Machine

You have been assigned your own **personal Ubuntu Linux Virtual Machine (VM)** for this course.

#### What Does This Mean?

- **Virtual Machine (VM)**: A VM is a computer that runs as software inside another computer. It acts exactly like a real computer with its own operating system, storage, and resources, but it's created and managed by special software called a hypervisor. Your VM runs on powerful servers in a data center.

- **Ubuntu**: Ubuntu is one of the most popular Linux distributions (versions of Linux). It's known for being user-friendly, well-documented, and widely used in both personal and professional settings. Your VM runs the **latest version of Ubuntu**, giving you experience with current, real-world Linux.

- **Personal VM**: Each student gets their own individual VM. This means:
  - You have complete control over your environment
  - Your work and files are private and separate from other students
  - You can experiment freely without affecting anyone else
  - If you make a mistake, it only affects your own VM

Your instructor will provide you with:

- **VM Address**: The IP address of your VM (e.g., `20.10.30.40`) - this is like the "phone number" for your server
- **Username**: Your personal login username
- **Password**: Your personal password for authentication

### Connecting to Your VM

You will connect to your VM using SSH with your username and password.

---

#### Connecting from Windows

**Video Tutorial**: Watch this helpful video that explains how to enable SSH in Windows and connect to a remote server:
📺 [How to Enable and Use SSH on Windows](https://www.youtube.com/watch?v=TJCYJpITDk4)

**Step-by-Step Instructions:**

1. **Open PowerShell or Windows Terminal**
   - Press `Windows + X` and select "Windows Terminal" or "PowerShell"
   - Or search for "PowerShell" in the Start menu

2. **Check if SSH is available**
   ```powershell
   ssh
   ```
   If you see SSH usage information, it's already installed. If not, continue to step 3.

3. **Enable OpenSSH Client (if needed)**
   - Open Settings → Apps → Optional Features
   - Click "Add a feature"
   - Search for "OpenSSH Client"
   - Click "Install"

4. **Connect to your VM**
   ```powershell
   ssh your_username@YOUR_VM_ADDRESS
   ```
   Replace `your_username` with the username provided by your instructor, and `YOUR_VM_ADDRESS` with your VM's IP address.

5. **Accept the server's fingerprint**
   - The first time you connect, you'll see a message about the server's authenticity
   - Type `yes` and press Enter to continue

6. **Enter your password**
   - Type the password provided by your instructor
   - Note: You won't see any characters as you type (this is normal for security)
   - Press Enter

7. **You're connected!**
   - You should now see a Linux command prompt

---

#### Connecting from Mac

**Video Tutorial**: Watch this helpful video that explains how to use SSH on Mac to connect to a remote server:
📺 [How to Use SSH on Mac](https://youtu.be/SfTSBbaFN8Y)

**Step-by-Step Instructions:**

1. **Open Terminal**
   - Press `Cmd + Space` to open Spotlight
   - Type "Terminal" and press Enter
   - Or go to Applications → Utilities → Terminal

2. **Connect to your VM**
   ```bash
   ssh your_username@YOUR_VM_ADDRESS
   ```
   Replace `your_username` with the username provided by your instructor, and `YOUR_VM_ADDRESS` with your VM's IP address.

3. **Accept the server's fingerprint**
   - The first time you connect, you'll see a message like:
     ```
     The authenticity of host 'YOUR_VM_ADDRESS' can't be established.
     ED25519 key fingerprint is SHA256:...
     Are you sure you want to continue connecting (yes/no/[fingerprint])?
     ```
   - Type `yes` and press Enter

4. **Enter your password**
   - Type the password provided by your instructor
   - Note: You won't see any characters appear as you type (this is a security feature)
   - Press Enter

5. **You're connected!**
   - You should now see a Linux command prompt like:
     ```
     your_username@ubuntu:~$
     ```

---

### First Login

When you first connect successfully, you'll see a welcome message and command prompt:

```
your_username@ubuntu:~$
```

This means you're logged in and ready to start learning!

### Important: About Your VM Credentials

{: .warning }
> **Store Your Credentials Securely!** This lab environment will be required for multiple assignments and projects throughout the semester. Please save your username, password, and VM address in a secure location (such as a password manager) for future access.

#### Understanding Your VM's Isolation

Your VM credentials (username and password) are **completely independent** and **not connected to any school systems**. Here's what this means:

- **Isolated Environment**: Your VM is a standalone, sandboxed system. It has no connection to your school's authentication systems, student portal, email, or any other campus services.
- **Separate Credentials**: The password for your VM is unique to this machine only. It is not your school password, and changing one will not affect the other.
- **No Single Sign-On (SSO)**: Your VM does not use your school's single sign-on or directory services. You must use the specific credentials provided for this VM.
- **Your Responsibility**: Since this is an isolated system, you are responsible for remembering and securely storing your VM credentials. Your instructor cannot recover a password you set yourself.

#### Changing Your Password

For security best practices, you may want to change your password after your first login. Here's how:

1. **Connect to your VM** using the initial password provided by your instructor

2. **Run the password change command**:
   ```bash
   passwd
   ```

3. **Enter your current password** when prompted:
   ```
   Current password:
   ```
   (Type your current password and press Enter - characters won't be displayed)

4. **Enter your new password**:
   ```
   New password:
   ```
   (Type your new password and press Enter)

5. **Confirm your new password**:
   ```
   Retype new password:
   ```
   (Type the same new password again and press Enter)

6. **Success!** You'll see a confirmation message:
   ```
   passwd: password updated successfully
   ```

**Password Requirements:**
- Choose a strong password that you can remember
- Use a mix of uppercase, lowercase, numbers, and special characters
- Avoid using easily guessable information (birthdays, names, etc.)
- **Immediately record your new password in a secure location** (password manager recommended)

{: .note }
> If you change your password and forget it, contact your instructor. They may need to reset your VM, which could result in loss of your work.

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
2. Verify the VM address is correct (check for typos)
3. Make sure you're using the correct username
4. Ensure the VM is running (ask your instructor)
5. Double-check your password (remember, characters don't appear when typing)

### Password Not Working

- Make sure Caps Lock is not on
- Remember that passwords are case-sensitive
- You won't see any characters when typing your password (this is normal)
- If you've forgotten your password, contact your instructor

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
  # From your local computer (you'll be prompted for your password)
  scp your_username@YOUR_VM_ADDRESS:~/file.txt ~/Downloads/
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
