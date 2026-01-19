---
title: "Root Access Guide"
layout: default
parent: Guides
nav_order: 3
---

# Common Commands Requiring Root Access

This guide lists commands you'll encounter in Linux Journey that require administrative (root) privileges. In your Ubuntu VM, you have full sudo access to practice all these commands safely.

## Package Management

Commands for installing, updating, and managing software:

```bash
# Update package lists
sudo apt update

# Upgrade installed packages
sudo apt upgrade

# Install new software
sudo apt install package_name

# Remove software
sudo apt remove package_name

# Clean up unused packages
sudo apt autoremove
```

## System Services

Managing system services with systemd:

```bash
# Start a service
sudo systemctl start service_name

# Stop a service
sudo systemctl stop service_name

# Restart a service
sudo systemctl restart service_name

# Enable service at boot
sudo systemctl enable service_name

# Disable service at boot
sudo systemctl disable service_name

# Check service status (no sudo needed)
systemctl status service_name
```

## User Management

Creating and managing user accounts:

```bash
# Create a new user
sudo useradd username

# Create a new user with home directory
sudo useradd -m username

# Delete a user
sudo userdel username

# Change user password
sudo passwd username

# Add user to a group
sudo usermod -aG groupname username
```

## File Permissions and Ownership

Changing file permissions and ownership:

```bash
# Change file permissions
sudo chmod 755 filename

# Change file ownership
sudo chown user:group filename

# Change ownership recursively
sudo chown -R user:group directory/
```

## Network Configuration

Configuring network interfaces:

```bash
# Configure IP address
sudo ip addr add 192.168.1.100/24 dev eth0

# Bring interface up/down
sudo ip link set eth0 up
sudo ip link set eth0 down

# Restart networking
sudo systemctl restart networking

# Request DHCP lease
sudo dhclient
```

## Filesystem Operations

Mounting filesystems and disk management:

```bash
# Mount a filesystem
sudo mount /dev/sdb1 /mnt/external

# Unmount a filesystem
sudo umount /mnt/external

# Create a filesystem
sudo mkfs.ext4 /dev/sdb1

# Check filesystem
sudo fsck /dev/sdb1

# Edit /etc/fstab
sudo nano /etc/fstab
```

## System Configuration

Editing system configuration files:

```bash
# Edit hosts file
sudo nano /etc/hosts

# Edit hostname
sudo hostnamectl set-hostname newname

# Edit system configuration files
sudo nano /etc/config-file

# View system logs (some require sudo)
sudo less /var/log/syslog
sudo journalctl
```

## Process Management

Managing processes with elevated privileges:

```bash
# Kill a process
sudo kill -9 PID

# Run a command as root
sudo command

# Open a root shell (use carefully!)
sudo -i

# Run previous command with sudo
sudo !!
```

## Power Management

Shutting down or restarting the system:

```bash
# Shutdown immediately
sudo shutdown -h now

# Shutdown in 10 minutes
sudo shutdown -h +10

# Restart system
sudo reboot

# Halt the system
sudo halt
```

## Kernel Module Management

Loading and unloading kernel modules:

```bash
# List loaded modules (no sudo needed)
lsmod

# Load a module
sudo modprobe module_name

# Remove a module
sudo modprobe -r module_name

# View module information (no sudo needed)
modinfo module_name
```

## Firewall Configuration

Managing firewall rules (if using ufw):

```bash
# Enable firewall
sudo ufw enable

# Disable firewall
sudo ufw disable

# Allow a port
sudo ufw allow 22/tcp

# Check firewall status
sudo ufw status
```

## Important Notes

### About sudo

- `sudo` stands for "superuser do"
- It temporarily elevates your privileges to run a single command
- You'll be prompted for YOUR password (not root's password)
- In your VM, you have full sudo access for learning purposes

### Best Practices

1. **Read before executing**: Always understand what a sudo command does
2. **Use sudo only when needed**: Don't run every command with sudo
3. **Check twice for destructive operations**: Commands like `rm -rf` with sudo can delete important system files
4. **Practice recovery**: If you break something, try to fix it - that's how you learn!

### Safe Experimentation

In your dedicated VM, you can:

- Install and remove packages freely
- Modify system configurations
- Restart services
- Practice recovery from mistakes
- Experiment with system settings

Your VM is isolated, so feel free to experiment. If something breaks, you can ask your instructor for help or start fresh with a new VM.

## Commands That Don't Require Root

For comparison, here are common commands that do NOT require sudo:

```bash
# File operations in your home directory
ls, cd, cat, less, touch, mkdir, rm (your own files)

# Viewing system information
uname, hostname, whoami, df, free, top, ps

# Network information
ping, traceroute, netstat (most uses), ip addr show

# File searching
find, grep, locate

# Package information
apt search, apt show

# System logs (some)
journalctl --user, less /var/log/syslog (if permissions allow)
```

## Getting Help

If you're unsure whether a command needs sudo:

1. Try it without sudo first
2. If you get "Permission denied", try with sudo
3. Read the man page: `man command_name`
4. Ask your instructor

Remember: Having full root access in your VM means you can practice all Linux administration tasks realistically. Take advantage of this learning environment!
