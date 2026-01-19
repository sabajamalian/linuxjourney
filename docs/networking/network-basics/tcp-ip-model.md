---
title: "TCP/IP Model"
layout: default
parent: Network Basics
grand_parent: Networking
nav_order: 3
---

## Lesson Content

The theoretical OSI model gave birth to what eventually became the TCP/IP model, which is the practical foundation the internet is built on. It represents the actual implementation of networking. The TCP/IP model utilizes the TCP/IP protocol suite, which we commonly refer to as TCP/IP. Effective **networking with TCP/IP** depends on these protocols, which work together to specify how data should be gathered, addressed, transmitted, and routed. By examining the **layers in the TCP/IP model**, we can understand how a data packet travels through the network.

### The Four Layers of the TCP/IP Model

The model is divided into four distinct layers, each with a specific function. Understanding these layers is crucial for any **real world protocol project** or network troubleshooting task.

### Application Layer

This is the top layer of the TCP/IP model, where user-facing applications and network services reside. It determines how programs, like your web browser or email client, interface with the transport layer services to send and receive data.

This layer uses protocols such as:

- HTTP (Hypertext Transfer Protocol): The foundation of data communication for the World Wide Web.
- SMTP (Simple Mail Transfer Protocol): Used for sending electronic mail (email).

### Transport Layer

The transport layer is responsible for end-to-end communication and data integrity. It establishes how data will be transmitted, manages port numbers, and ensures that packets are delivered reliably. The **layers of TCP protocol** suite are most prominent here.

This layer primarily uses:

- TCP (Transmission Control Protocol): Provides reliable, ordered, and error-checked delivery of a stream of data. It is connection-oriented.
- UDP (User Datagram Protocol): Offers a faster, connectionless data delivery method that is considered unreliable because it does not guarantee delivery or order.

### Network Layer

This layer, also known as the Internet Layer, specifies how to move packets between hosts and across different networks. Its main job is addressing and routing. The IP address assigned at this layer is fundamental to a device's identity on a network, which relates to the concept of **ip affiliation meaning** it is part of a specific network.

This layer uses protocols like:

- IP (Internet Protocol): Routes packets from a source machine to a destination machine.
- ICMP (Internet Control Message Protocol): Used for sending error messages and operational information, such as with the `ping` command.

### Link Layer

Also known as the Network Interface Layer, this layer specifies how to send data across a physical piece of hardware. It handles the transmission of data packets on the local network segment, such as over Ethernet, Wi-Fi, or fiber optic cables.

The protocol lists above are not exhaustive, and you'll encounter many others. In the following lessons, we will dive deeper into each of these layers to see how a packet traverses the network from the perspective of the TCP/IP model.

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

What is the top layer of the TCP/IP model? (Please answer in English. Note that the answer is case-sensitive.)

