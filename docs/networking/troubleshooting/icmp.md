---
title: "ICMP"
layout: default
parent: Troubleshooting
grand_parent: Networking
nav_order: 1
---

## Lesson Content

The Internet Control Message Protocol (ICMP) is a fundamental part of the TCP/IP protocol suite. It is not used for exchanging data between systems but rather for reporting errors and sending operational information. For anyone looking to `learn linux` network administration, understanding ICMP is crucial for debugging network issues, such as failed packet delivery.

### ICMP Message Structure

Every ICMP message has a standardized structure that includes a type, a code, and a checksum.

- **Type**: This field indicates the general category of the ICMP message. For example, it specifies whether the message is an error report or an informational query.
- **Code**: This field provides more specific information about the message type. For instance, if the type is "Destination Unreachable," the code will specify why it was unreachable.
- **Checksum**: This is used to verify the integrity of the message, ensuring it was not corrupted during transmission.

This structure makes ICMP a powerful diagnostic tool, and this `linux tutorial` will help you understand its practical applications.

### Common ICMP Types

While there are many ICMP types, a few are particularly common in day-to-day network troubleshooting.

- **Type 8 - Echo Request**: This message is sent by the `ping` command to a target host to check for connectivity.
- **Type 0 - Echo Reply**: If the target host is reachable, it responds to an Echo Request with an Echo Reply, confirming that a connection can be established.
- **Type 3 - Destination Unreachable**: A router or host sends this message when a packet cannot be delivered to its final destination. There are 16 different code values that provide specific reasons, such as:
  - Code 0: Network Unreachable
  - Code 1: Host Unreachable
- **Type 11 - Time Exceeded**: This message is generated when a packet's Time-To-Live (TTL) value reaches zero before it arrives at its destination. This often happens in routing loops and is used by the `traceroute` command to map network paths.

These messages will become more familiar as we explore common network troubleshooting tools available in your Ubuntu Linux terminal.

## Exercise

Follow these steps in your Ubuntu VM terminal to practice the concepts from this lesson:

1. **Test connectivity**: Try this command
   ```bash
   ping -c 4 8.8.8.8
   ```
   Expected output:
   ```
   (Output will vary based on your system)
   ```

2. **Check network status**: Try this command
   ```bash
   ip link show
   ```
   Expected output:
   ```
   (Output will vary based on your system)
   ```

3. **View open connections**: Try this command
   ```bash
   ss -tuln | head -15
   ```
   Expected output:
   ```
   (Output will vary based on your system)
   ```

4. **Test DNS resolution**: Try this command
   ```bash
   nslookup google.com` or `host google.com
   ```
   Expected output:
   ```
   (Output will vary based on your system)
   ```

## Quiz Question

What is the ICMP type for an echo request? Please answer with the numerical value only.

