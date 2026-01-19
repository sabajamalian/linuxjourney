---
title: "Upstart Overview"
layout: default
parent: Init
grand_parent: Administration
nav_order: 3
---

## Lesson Content

Upstart was developed by Canonical, so it was the init implementation on Ubuntu for a while; however, on modern Ubuntu installations, systemd is now used. Upstart was created to improve upon the issues with SysV, such as strict startup processes, blocking of tasks, etc. Upstart's event and job-driven model allow it to respond to events as they happen.

To find out if you are using Upstart, if you have a `/usr/share/upstart` directory, that's a pretty good indicator.

Jobs are the actions that Upstart performs, and events are messages that are received from other processes to trigger jobs. To see a list of jobs and their configuration:

```plaintext
pete@icebox:~$ ls /etc/init
acpid.conf                   mountnfs.sh.conf
alsa-restore.conf            mtab.sh.conf
alsa-state.conf              networking.conf
alsa-store.conf              network-interface.conf
anacron.conf                 network-interface-container.conf
```

Inside these job configurations, you'll find information on how and when to start jobs.

For example, in the `networking.conf` file, it could say something as simple as:

```plaintext
start on runlevel [235]
stop on runlevel [0]
```

This means that it will start setting up networking on runlevel 2, 3, or 5 and will stop networking on runlevel 0. There are many ways to write the configuration file, and you'll discover that when you look at the different job configurations available.

The way that Upstart works is that:

1. First, it loads the job configurations from `/etc/init`.
2. Once a startup event occurs, it will run jobs triggered by that event.
3. These jobs will make new events, and then those events will trigger more jobs.
4. Upstart continues to do this until it completes all the necessary jobs.

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

What is the init implementation that is used by Ubuntu?

