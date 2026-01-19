---
title: "Linux History"
layout: default
parent: Getting Started
grand_parent: Fundamentals
nav_order: 1
---

## Lesson Content

Welcome to your **Linux Journey**! If you're ready to dive into the powerful world of Linux, you've come to the right place. My name is Penguin Pete, and I'll be your guide. To get started, let's explore a brief **history of Linux**.

### The Predecessors of Linux

To understand how Linux was created, we must go back to 1969 when Ken Thompson and Dennis Ritchie of Bell Laboratories developed the UNIX operating system. It was later rewritten in the C programming language, which made it portable and led to its widespread adoption.

![Timeline of Unix](https://file.labex.io/images/ed9c245d-e8be-4287-bf34-67750b042542.jpg)

Over a decade later, Richard Stallman initiated the GNU (a recursive acronym for "GNU's Not UNIX") project. The goal was to create a completely free and open-source UNIX-like operating system. While the GNU project produced many essential components, including the GNU General Public License (GPL), its own kernel, named Hurd, was not completed in time.

### The Role of the Kernel

The kernel is the core component of an operating system. It acts as a bridge, allowing the hardware to communicate with the software. The kernel manages system resources, such as the CPU, memory, and peripheral devices. Essentially, the kernel controls everything that happens on your system. While other UNIX-like systems such as BSD and MINIX were being developed, they all lacked a freely available and unified kernel.

### The Birth of the Linux Kernel

This brings us to 1991, when a Finnish student named Linus Torvalds began developing a new kernel as a personal project. This kernel, which we now know as the Linux kernel, filled the missing piece of the GNU operating system. The combination of the GNU tools and the Linux kernel created the complete, open-source operating system that is widely used today. This milestone was a pivotal moment in the **history of Linux**.

![Linus Torvalds in 2018](https://file.labex.io/images/3e1311fd-b8ca-45e7-8d02-9aac6377bb36.jpg)

_Linus Torvalds in 2018 (Source: [Wikipedia](https://en.wikipedia.org/wiki/Linus_Torvalds))_

## Exercise

Follow these steps in your Ubuntu VM terminal to practice the concepts from this lesson:

1. **Check your distribution**: Try this command
   ```bash
   cat /etc/os-release
   ```
   Expected output:
   ```
   (Output will vary based on your system)
   ```

2. **View system information**: Try this command
   ```bash
   uname -a
   ```
   Expected output:
   ```
   (Output will vary based on your system)
   ```

3. **Check package manager**: Try this command
   ```bash
   which apt yum dnf pacman
   ```
   Expected output:
   ```
   (Output will vary based on your system)
   ```

4. **View installed packages: Use appropriate list command for your system**
   ```bash
   # Follow the instructions from the lesson
   ```

## Quiz Question

Who developed the Linux kernel? Please answer in English and be mindful of capitalization.

