---
title: "System V Overview"
layout: default
parent: Init
grand_parent: Administration
nav_order: 1
---

## Lesson Content

The primary role of an init system is to start and stop essential processes. Linux has seen three major init implementations: System V, Upstart, and systemd. This lesson focuses on the most traditional version, **System V init**, often referred to as **SysV** or simply **systemv** (pronounced 'System Five').

To determine if your system uses the **systemv** implementation, check for an `/etc/inittab` file. If this file exists, you are most likely running a SysV-based distribution.

### How System V Manages Processes

The **systemv init** process starts and stops services sequentially. For instance, if a service named `foo-b` depends on `foo-a`, `foo-b` cannot start until `foo-a` is fully running. The **initv** system achieves this using shell scripts. These scripts, located in specific directories, handle the starting and stopping of services. While you can write custom scripts, most systems rely on the pre-packaged ones that manage essential OS services.

### Advantages and Disadvantages

The main advantage of this sequential approach is its simplicity and predictability. Troubleshooting dependencies is straightforward because you know `foo-a` always starts before `foo-b`. However, the major drawback of the **init v** model is performance, as services are typically started one at a time, leading to slower boot times compared to modern parallel systems.

### Understanding Runlevels in System V

In a **systemv** environment, the machine's state is defined by **runlevels**, numbered from 0 to 6. These modes can vary slightly between Linux distributions, but they generally follow this standard convention:

- 0: Shutdown
- 1: Single User Mode
- 2: Multiuser mode without networking
- 3: Multiuser mode with networking
- 4: Unused
- 5: Multiuser mode with networking and GUI
- 6: Reboot

### Init Scripts and Directories

When your system boots, it checks its configured runlevel and executes the corresponding scripts. These scripts are typically found in directories like **/etc/rc.d/rc[runlevel].d/** or within a central **/etc/init.d** directory. Scripts beginning with `S` (Start) are executed during startup, while those beginning with `K` (Kill) are run during shutdown. The numbers following `S` or `K` dictate the execution order.

For example:

```bash
pete@icebox:/etc/rc.d/rc0.d$ ls
K10updates  K80openvpn
```

In this example, switching to runlevel 0 (shutdown) will first run the script to kill the updates service, followed by the script for OpenVPN. You can find the default runlevel for your machine in the `/etc/inittab` file, where you can also change it.

It is important to note that **System V** has been largely superseded by `systemd` in most modern Linux distributions. However, you may still encounter the concept of runlevels in newer init systems, as they often provide a compatibility layer to support legacy services that rely on **systemv init** scripts.

## Exercise

Follow these steps in your Ubuntu VM terminal to practice the concepts from this lesson:

1. **Check init system**: Try this command
   ```bash
   ps -p 1
   ```
   Expected output:
   ```
   (Output will vary based on your system)
   ```

2. **List services**: Try this command
   ```bash
   systemctl list-units --type=service | head -15
   ```
   Expected output:
   ```
   (Output will vary based on your system)
   ```

3. **Check service status**: Try this command
   ```bash
   systemctl status ssh` (if available)
   ```
   Expected output:
   ```
   (Output will vary based on your system)
   ```

4. **View runlevel**: Try this command
   ```bash
   runlevel` or `who -r
   ```
   Expected output:
   ```
   (Output will vary based on your system)
   ```

## Quiz Question

What runlevel is usually used for shutdown?

