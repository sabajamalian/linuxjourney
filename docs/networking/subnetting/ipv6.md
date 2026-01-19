---
title: "IPv6"
layout: default
parent: Subnetting
grand_parent: Networking
nav_order: 7
---

## Lesson Content

Every device that connects to the internet, from your server to your smartphone, requires a unique IP address to communicate. The most widely used version, IPv4, provides a finite number of addresses, a limit we are rapidly approaching in our increasingly connected world. This issue is known as IPv4 address exhaustion.

### What is IPv6?

To solve this problem, the Internet Engineering Task Force (IETF) developed a new version of the Internet Protocol: IPv6. The primary purpose of IPv6 is to dramatically expand the available pool of IP addresses, ensuring the internet can continue to grow and accommodate billions of new devices. It also includes other improvements to the network protocol.

### IPv4 vs IPv6

While IPv6 was created to address the limitations of IPv4, its adoption has been gradual. It is not intended to immediately replace IPv4. Instead, the two network protocols are designed to coexist and complement each other. Many networks today run in a "dual-stack" mode, supporting both IPv4 and IPv6 simultaneously. If you are familiar with IPv4, the core concepts of IPv6 will be easy to grasp.

### Understanding IPv6 Addresses

The most significant difference you will notice is the address format. An IPv4 address is a 32-bit number typically written as four decimal numbers separated by periods (e.g., `192.168.1.1`). In contrast, an IPv6 address is a 128-bit number written in hexadecimal and separated by colons.

Here is what a typical IPv6 address looks like:

```plaintext
2dde:1235:1256:3:200:f8ed:fe23:59cf
```

This longer format allows for a vastly larger number of unique IP addresses, securing the future of internet connectivity.

## Exercise

Follow these steps in your Ubuntu VM terminal to practice the concepts from this lesson:

1. **View IP address**: Try this command
   ```bash
   ip addr show | grep inet
   ```
   Expected output:
   ```
   (Output will vary based on your system)
   ```

2. **Calculate subnet: Use `ipcalc 192.168.1.0/24` (if available)**
   ```bash
   # Follow the instructions from the lesson
   ```

3. **Check network mask**: Try this command
   ```bash
   ifconfig | grep netmask` or `ip addr
   ```
   Expected output:
   ```
   (Output will vary based on your system)
   ```

4. **View CIDR notation**: Try this command
   ```bash
   ip addr show | grep inet
   ```
   Expected output:
   ```
   (Output will vary based on your system)
   ```

## Quiz Question

What is the name of the IP protocol designed to increase the number of available addresses for hosts on the Internet? Please answer in English using the protocol's common name, paying attention to capitalization.

