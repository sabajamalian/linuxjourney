---
title: "Link State Protocols"
layout: default
parent: Routing
grand_parent: Networking
nav_order: 6
---

## Lesson Content

Link state protocols are great for large-scale networks. They are more complex than distance vector protocols; however, a large upside is their ability to converge quickly. This is because instead of periodically sending out the whole routing table, they only send updates to neighboring routes. They use a different algorithm to calculate the shortest path first and construct their network topology in the form of a graph to show which routers are connected to other routers.

One of the common link state protocols is OSPF (Open Shortest Path First). It only updates the routing tables if there is a network change. It does not have a hop limit.

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

What is one of the most common link state protocols?

