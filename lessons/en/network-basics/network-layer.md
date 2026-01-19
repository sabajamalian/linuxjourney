---
index: 7
lang: "en"
title: "Network Layer"
meta_title: "Network Layer - Network Basics"
meta_description: "Explore the Network layer in Linux networking. This guide explains how IP addresses and subnets enable packet routing for data transmission across networks."
meta_keywords: "Network layer, IP addresses, subnets, Linux networking, packet routing, data transmission, OSI model, IP packet"
---

## Lesson Content

The Network layer is responsible for the logical addressing and routing of data packets from a source host to a destination host. While a packet might sometimes travel within a single local network, the internet is a vast collection of interconnected networks.

### The Role of Packet Routing

The primary function of the Network layer is to determine the optimal path for data to travel. This process, known as **packet routing**, ensures that information reaches its intended destination efficiently, even if it needs to cross multiple network boundaries. In **Linux networking**, this layer is fundamental for all internet communication.

### Understanding Subnets and IP Addresses

The smaller networks that constitute the internet are called **subnets**. All subnets are connected, which allows a device on one network to communicate with a device on another, such as accessing a website like `google.com`. The rules for traveling between these different subnets are defined by **IP addresses**. An IP address provides a unique identifier for a device on a network, much like a street address for a house.

### Encapsulation at the Network Layer

At the Network layer, the data segment received from the Transport layer is encapsulated into a new unit called an IP packet. During this process, a header is added to the packet, which includes the source IP address (where the packet came from) and the destination IP address (where it is going). With this crucial addressing information attached, the packet now has everything it needs for its journey and is passed down to the Data Link layer to be prepared for physical transmission.

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

What are the smaller networks that make up the Internet called? Please answer using a single, lowercase English word.

