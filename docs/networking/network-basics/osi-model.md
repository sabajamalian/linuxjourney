---
title: "OSI Model"
layout: default
parent: Network Basics
grand_parent: Networking
nav_order: 2
---

## Lesson Content

Before diving into practical networking commands, it's essential to understand some foundational jargon. One of the most important concepts is the OSI model, which serves as a cornerstone for understanding network communications.

### What is the OSI Model?

The OSI (Open Systems Interconnection) model is a conceptual framework used to understand and standardize the functions of a telecommunication or computing system. It characterizes a networking system's functions into a set of seven distinct layers. For anyone working with **osi linux** networking, grasping this model provides a solid theoretical base.

### The Seven Layers of OSI

This model shows how a data packet traverses through a network across seven different layers:

1. Physical
2. Data Link
3. Network
4. Transport
5. Session
6. Presentation
7. Application

While we won't detail the specifics of each layer, knowing they exist is crucial for contextualizing network processes.

### Relevance in Modern Networking

Although the OSI model is primarily theoretical, its influence is significant. Most modern networking, including the internet, operates on the more practical TCP/IP model. However, the TCP/IP model was heavily influenced by the OSI framework. Many networking concepts and troubleshooting methods still refer to the OSI layers, making it a timeless and relevant piece of knowledge for network administrators.

## Exercise

Follow these steps in your Ubuntu VM terminal to practice the concepts from this lesson:

1. **View network interfaces**: Try this command
   ```bash
   ip addr show` or `ifconfig
   ```
   Expected output:
   ```
   (Output will vary based on your system)
   ```

2. **Check routing table**: Try this command
   ```bash
   ip route` or `route -n
   ```
   Expected output:
   ```
   (Output will vary based on your system)
   ```

3. **Test connectivity**: Try this command
   ```bash
   ping -c 3 8.8.8.8
   ```
   Expected output:
   ```
   (Output will vary based on your system)
   ```

4. **View DNS settings**: Try this command
   ```bash
   cat /etc/resolv.conf
   ```
   Expected output:
   ```
   (Output will vary based on your system)
   ```

## Quiz Question

What is used as the theoretical model of networking? (Please answer in English, using the acronym in uppercase.)

