---
title: "Network Addressing"
layout: default
parent: Network Basics
grand_parent: Networking
nav_order: 4
---

## Lesson Content

Before we explore how data packets travel across a network, it's essential to understand some core terminology. Just like a physical letter needs a destination and return address, network packets require similar information to reach their target. In computer networking, devices are identified using MAC (Media Access Control) addresses and IP addresses. To simplify things for humans, we also use hostnames.

### MAC Addresses

A MAC address is a unique, permanent hardware identifier assigned to a network interface card (NIC). This address is burned into the device during manufacturing and does not change. Every device that connects to a network, such as your computer or smartphone, has a NIC with a distinct MAC address. This hardware address is crucial for communication on a local network segment. An Ethernet MAC address typically looks like this: `00:C4:B5:45:B2:43`. The first three bytes of the address form the Organizationally Unique Identifier (OUI), which identifies the manufacturer. For instance, Dell uses the OUI `00-14-22`, so a Dell NIC might have a MAC address like `00-14-22-34-B2-C2`.

### IP Addresses

An IP address is a logical identifier for a device on a network, making it reachable across different networks, including the internet. Unlike a MAC address, an IP address is not tied to the hardware and can be assigned dynamically. We will focus on IPv4 for now, where an address looks like `10.24.12.4`. IP addresses are fundamental to the software side of networking, enabling routing and global communication. While public IP addresses are unique across the internet, they can change, and technologies like Network Address Translation (NAT) allow for private, non-unique addresses within a local network. It's important to remember that both MAC (hardware) and IP (software) addresses are necessary for successful network communication.

### Hostnames

While IP addresses are effective for computers, they are difficult for humans to remember. Hostnames solve this problem by mapping a user-friendly name to an IP address. For example, it's much easier to remember `myhost.com` than its corresponding IP address, such as `192.12.41.4`. This mapping is handled by the Domain Name System (DNS), which acts as the internet's phonebook, translating memorable hostnames into the numerical IP addresses required for network routing.

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

How many bytes are in an IPv4 address?

