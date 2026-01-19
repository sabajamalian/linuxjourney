---
title: "Path of a Packet"
layout: default
parent: Routing
grand_parent: Networking
nav_order: 3
---

## Lesson Content

Understanding how data travels across a network is fundamental to networking. This journey, often called the **packet path**, involves a coordinated effort between different protocols and hardware. Let's trace the **packet path** in two common scenarios: communication within a local network and communication with an external network.

### Packet Path Within a Local Network

When a device sends a packet to another device on the same local network, the process is relatively straightforward.

1. First, the sending host checks if the destination IP address is on the same subnet by comparing it against its own IP address and subnet mask.
2. To send a packet, the host needs four key pieces of information: a source IP, a destination IP, a source MAC address, and a destination MAC address. Initially, the host does not know the destination host's MAC address.
3. The host uses the Address Resolution Protocol (ARP) to find the missing information. It broadcasts an ARP request on the local network, asking which device has the target IP address. The corresponding device replies with its MAC address.
4. With the destination MAC address now known, the packet is fully addressed and can be sent directly to the destination host on the local network.

### Packet Path to an External Network

When a packet is destined for a device outside the local network, the process involves routers to forward the packet.

1. The sending host determines that the destination IP address is not on its local network. Because ARP broadcasts are limited to the local network, the host cannot directly discover the final destination's MAC address.
2. The host consults its routing table. Since there is no specific route for the external IP, it uses the default route, which points to the default gateway (a router). The packet is prepared with the original source and destination IP addresses. The destination MAC address, however, is set to the MAC address of the default gateway. If the gateway's MAC is unknown, the host uses ARP to find it.
3. Once the packet reaches the router, the router examines the destination IP address and consults its own routing table to determine the next hop on the **packet path**. The router then rewrites the packet's MAC addresses: the source MAC becomes the router's MAC, and the destination MAC becomes the MAC of the next hop. This process is repeated at every router along the path.
4. When the packet finally arrives at the router connected to the destination's local network, that router uses ARP to find the final host's MAC address and delivers the packet.
5. Throughout this entire journey, the source and destination IP addresses in the packet header remain unchanged. Only the MAC addresses are updated at each hop.

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

Which protocol is used to find the MAC address of a host on the local network, given its IP address? Please answer with the three-letter acronym in all uppercase.

