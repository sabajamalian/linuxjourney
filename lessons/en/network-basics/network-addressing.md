---
index: 4
lang: "en"
title: "Network Addressing"
meta_title: "Network Addressing - Network Basics"
meta_description: "Discover the fundamentals of network addressing. This guide explains MAC addresses, IP addresses, and hostnames, key concepts for understanding how devices communicate in Linux networking."
meta_keywords: "network addressing, MAC address, IP address, hostname, network identifiers, Linux networking, network basics, beginner, tutorial, guide"
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

Practice the commands in your Ubuntu VM terminal. Experiment with different options and variations to deepen your understanding.

## Quiz Question

How many bytes are in an IPv4 address?

## Quiz Answer

4
