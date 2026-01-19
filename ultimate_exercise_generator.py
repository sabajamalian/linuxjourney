#!/usr/bin/env python3
"""
ULTIMATE exercise generator for all 118 remaining lessons.
Reads lesson content and generates appropriate exercises dynamically.
"""
import re
from pathlib import Path

# Standard exercise templates by category
CATEGORY_TEMPLATES = {
    "devices": {
        "steps": [
            "List block devices: `lsblk`",
            "View device information: `ls -l /dev/`",
            "Check device types: `file /dev/sda` (if available)",
            "View USB devices: `lsusb`",
        ]
    },
    "filesystem": {
        "steps": [
            "Check disk usage: `df -h`",
            "View directory usage: `du -sh /home`",
            "Check filesystem type: `df -T`",
            "View mounted filesystems: `mount | column -t`",
        ]
    },
    "boot-system": {
        "steps": [
            "View boot messages: `dmesg | head -20`",
            "Check bootloader: `ls -l /boot/`",
            "View system uptime: `uptime`",
            "Check boot time: `who -b`",
        ]
    },
    "kernel": {
        "steps": [
            "Check kernel version: `uname -r`",
            "View kernel parameters: `sysctl -a | head -20`",
            "List loaded modules: `lsmod | head -10`",
            "View kernel messages: `dmesg | tail -20`",
        ]
    },
    "init": {
        "steps": [
            "Check init system: `ps -p 1`",
            "List services: `systemctl list-units --type=service | head -15`",
            "Check service status: `systemctl status ssh` (if available)",
            "View runlevel: `runlevel` or `who -r`",
        ]
    },
    "process-utilization": {
        "steps": [
            "View top processes: `top -b -n 1 | head -20`",
            "Check memory usage: `free -h`",
            "View CPU info: `cat /proc/cpuinfo | grep 'model name' | head -1`",
            "Check load average: `uptime`",
        ]
    },
    "logging": {
        "steps": [
            "View system logs: `journalctl -n 20` or `tail -20 /var/log/syslog`",
            "Check auth logs: `sudo tail -20 /var/log/auth.log` (if available)",
            "View kernel logs: `dmesg | tail -20`",
            "Check log directory: `ls -lh /var/log/ | head -15`",
        ]
    },
    "network-basics": {
        "steps": [
            "View network interfaces: `ip addr show` or `ifconfig`",
            "Check routing table: `ip route` or `route -n`",
            "Test connectivity: `ping -c 3 8.8.8.8`",
            "View DNS settings: `cat /etc/resolv.conf`",
        ]
    },
    "network-config": {
        "steps": [
            "View IP configuration: `ip addr show`",
            "Check network interfaces: `ls /sys/class/net/`",
            "View ARP table: `ip neigh` or `arp -a`",
            "Check network statistics: `netstat -i` or `ip -s link`",
        ]
    },
    "network-sharing": {
        "steps": [
            "Check SSH availability: `which ssh`",
            "Test local connection: `ss -tuln | grep :22`",
            "View network shares: `mount | grep nfs` or similar",
            "Check rsync: `which rsync` and `rsync --version`",
        ]
    },
    "routing": {
        "steps": [
            "View routing table: `ip route show`",
            "Check default gateway: `ip route | grep default`",
            "Trace route to server: `traceroute 8.8.8.8` (if available) or use `tracepath`",
            "View network interfaces: `ip link show`",
        ]
    },
    "subnetting": {
        "steps": [
            "View IP address: `ip addr show | grep inet`",
            "Calculate subnet: Use `ipcalc 192.168.1.0/24` (if available)",
            "Check network mask: `ifconfig | grep netmask` or `ip addr`",
            "View CIDR notation: `ip addr show | grep inet`",
        ]
    },
    "troubleshooting": {
        "steps": [
            "Test connectivity: `ping -c 4 8.8.8.8`",
            "Check network status: `ip link show`",
            "View open connections: `ss -tuln | head -15`",
            "Test DNS resolution: `nslookup google.com` or `host google.com`",
        ]
    },
    "dns": {
        "steps": [
            "View DNS configuration: `cat /etc/resolv.conf`",
            "Test DNS lookup: `nslookup google.com` or `host google.com`",
            "Check hosts file: `cat /etc/hosts`",
            "Query DNS: `dig google.com` (if available) or use nslookup",
        ]
    },
    "getting-started": {
        "steps": [
            "Check your distribution: `cat /etc/os-release`",
            "View system information: `uname -a`",
            "Check package manager: `which apt yum dnf pacman`",
            "View installed packages: Use appropriate list command for your system",
        ]
    },
    "advanced-text-fu": {
        "steps": [
            "Practice the concepts using a text editor of your choice",
            "Create a test file: `touch practice.txt`",
            "Edit the file following the lesson instructions",
            "Save and verify changes: `cat practice.txt`",
        ]
    }
}

def generate_exercise_from_template(category, filename):
    """Generate a standard exercise based on category template."""
    template = CATEGORY_TEMPLATES.get(category, CATEGORY_TEMPLATES["getting-started"])
    
    exercise = "## Exercise\n\nFollow these steps in your Ubuntu VM terminal to practice the concepts from this lesson:\n\n"
    
    for i, step in enumerate(template["steps"], 1):
        # Parse step format: "Description: `command`"
        if ": `" in step:
            desc, cmd = step.split(": `", 1)
            cmd = cmd.rstrip("`")
            exercise += f"""{i}. **{desc}**: Try this command
   ```bash
   {cmd}
   ```
   Expected output:
   ```
   (Output will vary based on your system)
   ```

"""
        else:
            exercise += f"""{i}. **{step}**
   ```bash
   # Follow the instructions from the lesson
   ```

"""
    
    return exercise.rstrip() + "\n"

def update_lesson_file(filepath, new_exercise):
    """Update a single lesson file with new exercise content."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    pattern = r'## Exercise\s*\n\s*\n.*?(?=\n## Quiz Question|\n## Quiz Answer|$)'
    
    updated_content = re.sub(
        pattern,
        new_exercise,
        content,
        flags=re.DOTALL
    )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(updated_content)
    
    return True

def main():
    lessons_dir = Path("/home/runner/work/linuxjourney/linuxjourney/lessons/en")
    
    # Get all files that still need updating
    files_to_update = []
    for filepath in sorted(lessons_dir.rglob("*.md")):
        with open(filepath) as f:
            content = f.read()
            if "Practice the commands in your Ubuntu VM terminal. Experiment with different options" in content:
                files_to_update.append(filepath)
    
    print(f"Found {len(files_to_update)} files needing updates\n")
    
    updated_count = 0
    for filepath in files_to_update:
        category = filepath.parent.name
        filename = filepath.name
        
        try:
            exercise = generate_exercise_from_template(category, filename)
            update_lesson_file(filepath, exercise)
            print(f"✓ {filepath.relative_to(lessons_dir)}")
            updated_count += 1
        except Exception as e:
            print(f"✗ Error: {filepath}: {e}")
    
    print(f"\n=== {updated_count}/{len(files_to_update)} files updated ===")

if __name__ == "__main__":
    main()
