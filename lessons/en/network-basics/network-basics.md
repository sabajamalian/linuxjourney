---
index: 1
lang: "en"
title: "Network Basics"
meta_title: "Network Basics - Network Basics"
meta_description: "Discover the best way to learn Linux by starting with network basics. This guide covers the basics of network components like WAN, LAN, routers, and hosts for beginners."
meta_keywords: "basics network, basics linux, best way to learn linux, basics of linux, WAN, LAN, WLAN, network tutorial, networking guide"
---

## Lesson Content

Understanding the **basics of linux** networking is a fundamental skill. For many, grasping these concepts is the **best way to learn linux** more deeply, as networks are integral to how modern systems operate. Let's explore a typical home network to understand the core components.

### Core Network Components

Your home network is a small ecosystem of devices working together. Here are the key players:

- **ISP (Internet Service Provider):** This is the company you pay for your internet connection, linking your home to the global internet.
- **Router:** The router is the central hub of your network. It directs traffic, allowing each machine to connect to the internet and communicate with each other. Modern routers support both wired (Ethernet) and wireless connections.

### Understanding Network Types WAN LAN and WLAN

Networks are categorized by their scale. In a home setup, you'll encounter these three common types, which form the foundation of **basics network** knowledge:

- **WAN (Wide Area Network):** This term describes the vast network outside your home, connecting your router to the broader internet.
- **WLAN (Wireless Local Area Network):** This is your Wi-Fi network. It connects wireless devices, like laptops and smartphones, to your router without physical cables.
- **LAN (Local Area Network):** This refers to the wired part of your network, connecting devices like desktop PCs or game consoles to your router via an Ethernet cable.

### Hosts and Packets

On any network, every connected device—be it a computer, phone, or server—is known as a **host**.

All data transmitted across these networks, from web pages to emails, is broken down into small pieces called **packets**. Throughout the Networking Nomad section, you will learn in detail how these packets travel to and from different hosts, completing their journey across the internet.

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

What is the local area network known as? Please answer in English, paying attention to capitalization.

## Quiz Answer

LAN
