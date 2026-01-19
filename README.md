# Linux Journey

Learn Linux fundamentals through hands-on practice in your own Ubuntu environment.

A structured learning path from beginner to advanced Linux administration with three levels:

- **Grasshopper** - Learn the basics
- **Journeyman** - System internals
- **Networking Nomad** - Network administration

## Learning Environment

This course is designed for hands-on learning using **Ubuntu Linux VMs**. Each student receives their own dedicated virtual machine with full root access, allowing you to:

- Practice all commands without restrictions
- Experiment freely in a safe, isolated environment
- Learn system administration with full privileges
- Make mistakes and learn from them without affecting others

## Repository Structure

```plaintext
├── lessons/       # Course content by language
│   ├── en/        # English lessons
│   └── ...        # Other languages
├── docs/          # Setup and deployment guides
└── README.md
```

## Getting Started

### For Students

1. You will be provided with SSH access to your personal Ubuntu VM
2. Connect using: `ssh student@your-vm-address`
3. Follow the lessons in order, starting with Grasshopper level
4. Practice each command in your VM terminal

See [docs/student-guide.md](docs/student-guide.md) for detailed instructions.

**Note:** You have full root access in your VM! See [docs/root-access-guide.md](docs/root-access-guide.md) for a guide to commands requiring sudo/root privileges.

### For Instructors

See [docs/instructor-guide.md](docs/instructor-guide.md) for VM deployment and management instructions.

## Grasshopper

### Getting Started

What is Linux? Get started with choosing a distribution and installation.

Lessons are located in `lessons/en/getting-started/`

### Command Line

Learn the fundamentals of the command line, navigating files, directories, and more.

Lessons are located in `lessons/en/command-line/`

### Text-Fu

Learn basic text manipulation and navigation.

Lessons are located in `lessons/en/text-fu/`
### Advanced Text-Fu

Navigate text like a Linux spider monkey with Vim and Emacs.

Lessons are located in `lessons/en/advanced-text-fu/`
### User Management

Learn about user roles and management.

Lessons are located in `lessons/en/user-management/`
### Permissions

Learn about permission levels and modifying permissions.

Lessons are located in `lessons/en/permissions/`
### Processes

Learn about the running processes on the system.

Lessons are located in `lessons/en/processes/`
### Packages

Learn all about the dpkg, apt-get, rpm, and yum package management tools.

Lessons are located in `lessons/en/packages/`
## Journeyman

### Devices

Learn about Linux devices and how they interact with the kernel and user space.

Lessons are located in `lessons/en/devices/`
### The Filesystem

Learn about the Linux filesystem, the different types of filesystems, partitioning, and more.

Lessons are located in `lessons/en/filesystem/`
### Boot the System

Learn about the stages of the Linux boot process.

Lessons are located in `lessons/en/boot-system/`
### Kernel

The most important part of the Linux system; learn about how it works and how to configure it.

Lessons are located in `lessons/en/kernel/`
### Init

Learn about the different init systems: SysV, Upstart, and systemd.

Lessons are located in `lessons/en/init/`
### Process Utilization

Learn resource monitoring with top, load averages, iostat, and more!

Lessons are located in `lessons/en/process-utilization/`
### Logging

Learn about system logs and the /var/log directory.

Lessons are located in `lessons/en/logging/`
## Networking Nomad

### Network Sharing

Learn about network sharing with rsync, scp, nfs, and more.

Lessons are located in `lessons/en/network-sharing/`
### Network Basics

Learn about networking basics and the TCP/IP model.

Lessons are located in `lessons/en/network-basics/`
### Subnetting

Learn about subnets and how to do subnet arithmetic!

Lessons are located in `lessons/en/subnetting/`
### Routing

Learn how packets are routed across networks!

Lessons are located in `lessons/en/routing/`
### Network Config

Learn about network configuration using Linux tools!

Lessons are located in `lessons/en/network-config/`
### Troubleshooting

Learn about common networking tools to help you diagnose and troubleshoot issues!

Lessons are located in `lessons/en/troubleshooting/`
### DNS

Everything and more that you wanted to know about DNS.

Lessons are located in `lessons/en/dns/`
## License

Content is licensed under [CC BY-SA 4.0](http://creativecommons.org/licenses/by-sa/4.0/).
