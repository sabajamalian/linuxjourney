---
title: "Continuous Monitoring"
layout: default
parent: Process Utilization
grand_parent: Administration
nav_order: 7
---

## Lesson Content

These monitoring tools are good to look at when your machine is having issues, but what about machines that are having issues when you aren't looking? For those, you'll need to use a continuous monitoring tool, something that will collect, report, and save your system activity information. In this lesson, we will go over a great tool to use: **sar**.

### Installing sar

Sar is a tool that is used to do historical analysis on your system. First, make sure you have it installed by installing the `sysstat` package: `sudo apt install sysstat`.

### Setting up data collection

Usually, once you install `sysstat`, your system will automatically start collecting data. If it doesn't, you can enable it by modifying the `ENABLED` field in `/etc/default/sysstat`.

### Using sar

```bash
sudo sar -q
```

This command will list the details from the start of the day.

```bash
sudo sar -r
```

This will list the details of memory usage from the start of the day.

```bash
sudo sar -P
```

This will list the details of CPU usage.

To see a view of a different day, you can go into `/var/log/sysstat/saXX` where `XX` is the day you want to view.

```bash
sar -q /var/log/sysstat/sa02
```

## Exercise

Follow these steps in your Ubuntu VM terminal to practice the concepts from this lesson:

1. **View top processes**: Try this command
   ```bash
   top -b -n 1 | head -20
   ```
   Expected output:
   ```
   (Output will vary based on your system)
   ```

2. **Check memory usage**: Try this command
   ```bash
   free -h
   ```
   Expected output:
   ```
   (Output will vary based on your system)
   ```

3. **View CPU info**: Try this command
   ```bash
   cat /proc/cpuinfo | grep 'model name' | head -1
   ```
   Expected output:
   ```
   (Output will vary based on your system)
   ```

4. **Check load average**: Try this command
   ```bash
   uptime
   ```
   Expected output:
   ```
   (Output will vary based on your system)
   ```

## Quiz Question

What is a good tool to use for monitoring system resources?

