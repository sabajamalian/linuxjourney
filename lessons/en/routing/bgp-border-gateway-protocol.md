---
index: 7
lang: "en"
title: "Border Gateway Protocol"
meta_title: "Border Gateway Protocol - Routing"
meta_description: "Explore the fundamentals of Border Gateway Protocol (BGP), the core protocol that enables internet routing. Learn how BGP facilitates communication between autonomous systems and the principles of border gateway protocol routing."
meta_keywords: "BGP, Border Gateway Protocol, border gateway protocol routing, internet routing, autonomous systems, Linux networking, BGP tutorial, network protocols"
---

## Lesson Content

### The Backbone of the Internet

The final major protocol we will cover is the Border Gateway Protocol (BGP). BGP is the fundamental protocol that allows the internet to function by managing how data packets are routed across its vast collection of networks. It is specifically designed to exchange routing and reachability information among different Autonomous Systems (AS).

### What is an Autonomous System?

An Autonomous System (AS) is a large network or a group of networks managed by a single administrative entity. Examples include internet service providers (ISPs), large corporations, universities, and government agencies. Without BGP, these systems would be isolated and unable to communicate with one another. While other protocols handle routing _within_ an AS, BGP is responsible for routing _between_ them.

### The Process of Border Gateway Protocol Routing

The primary function of BGP is **border gateway protocol routing**. Let's consider an example. Imagine you are on your home network and a friend is using the Wi-Fi at a coffee shop. When your friend sends you a message, the data packet first travels through the coffee shop's local network. It follows internal routing tables until it reaches a "border" router at the edge of that network.

This border router uses BGP to determine the best path for the packet to leave its own AS and travel across other autonomous systems to eventually reach your home network's AS. BGP doesn't just find a path; it makes policy decisions to find the _best_ path based on rules configured by network administrators, ensuring efficient and reliable data exchange across the global internet.

## Exercise

Follow these steps in your Ubuntu VM terminal to practice the concepts from this lesson:

1. **View routing table**: Try this command
   ```bash
   ip route show
   ```
   Expected output:
   ```
   (Output will vary based on your system)
   ```

2. **Check default gateway**: Try this command
   ```bash
   ip route | grep default
   ```
   Expected output:
   ```
   (Output will vary based on your system)
   ```

3. **Trace route to server**: Try this command
   ```bash
   traceroute 8.8.8.8` (if available) or use `tracepath
   ```
   Expected output:
   ```
   (Output will vary based on your system)
   ```

4. **View network interfaces**: Try this command
   ```bash
   ip link show
   ```
   Expected output:
   ```
   (Output will vary based on your system)
   ```

## Quiz Question

What protocol basically makes the internet work? Please answer using the uppercase English acronym.

