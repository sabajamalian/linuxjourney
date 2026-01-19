---
index: 9
lang: "en"
title: "DHCP Overview"
meta_title: "DHCP Overview - Network Basics"
meta_description: "Learn the fundamentals of DHCP (Dynamic Host Configuration Protocol). This guide covers how DHCP assigns IP addresses, its four-step process (DORA), and its role in the network's DHCP layer. Perfect for Linux networking beginners."
meta_keywords: "DHCP, Dynamic Host Configuration Protocol, dhcp layer, IP address, Linux networking, DHCP process, DORA, network configuration"
---

## Lesson Content

The Dynamic Host Configuration Protocol (DHCP) is a fundamental networking protocol used to automatically assign IP addresses and other network configuration parameters to devices on a network.

### What is DHCP?

Think of DHCP as a phone company for your devices. When you get a new phone, you need a number to start communicating. You contact your carrier, and they assign you one. Similarly, when a device connects to a network, it needs an IP address to communicate with other devices. DHCP is the service that provides this IP address.

This IP address is typically "leased" for a specific period. Before the lease expires, the device can renew it, ensuring continuous connectivity. This automated process is essential for managing devices on any network.

### The Role of a DHCP Server

A DHCP server is responsible for managing a pool of IP addresses and leasing them to client devices. In a typical home network, your router often acts as the DHCP server. In larger networks, a dedicated server handles this task.

Using DHCP offers significant advantages:

- **Automation:** Network administrators don't need to manually configure every device, saving time and effort.
- **Accuracy:** It prevents common errors like assigning duplicate IP addresses, which can cause network conflicts.

Every physical network should have its own DHCP server to streamline the process of hosts requesting and receiving IP addresses. This protocol operates at the Application Layer, forming a crucial part of the network's configuration services, sometimes conceptually referred to as the `dhcp layer`.

### The Four-Step DHCP Process

The process of a device obtaining an IP address via DHCP involves a four-step exchange, often remembered by the acronym DORA:

1. **DHCP Discover:** The client device broadcasts a `DISCOVER` message across the network to find an available DHCP server.
2. **DHCP Offer:** Any DHCP server that receives the discover message can respond with an `OFFER` message. This message contains a proposed IP address, subnet mask, gateway address, and lease duration.
3. **DHCP Request:** The client receives one or more offers and chooses one. It then broadcasts a `REQUEST` message to inform all DHCP servers which offer it has accepted.
4. **DHCP Acknowledgment (ACK):** The server that made the accepted offer sends a final `ACK` message to the client, confirming the lease and finalizing the configuration.

While the full protocol is more complex, these four steps represent the core of how DHCP dynamically configures hosts on a network.

## Exercise

Practice the commands in your Ubuntu VM terminal. Experiment with different options and variations to deepen your understanding.

## Quiz Question

What are the four steps in the DHCP process, in order? Please answer in English, using uppercase words separated by a comma and a space.

## Quiz Answer

DISCOVER, OFFER, REQUEST, ACK
