---
title: "Routing Protocols"
layout: default
parent: Routing
grand_parent: Networking
nav_order: 4
---

## Lesson Content

Manually configuring routes on a routing table for every device on a large network would be an incredibly tedious task. To automate this process, we use dynamic **routing protocols**. These protocols allow routers to adapt to network changes automatically by learning different routes, building them into the routing table, and forwarding packets accordingly. There are two primary types of routing protocols: distance vector and link state.

### Distance Vector Protocols

Distance vector protocols operate on the principle of "routing by rumor." Each router shares its entire routing table with its directly connected neighbors at regular intervals. When a router receives a routing table from a neighbor, it updates its own table with any new or better routes. The "distance" is typically measured by a metric like hop count. This method is simple but can be slow to converge and is susceptible to routing loops. An example of a distance vector protocol is the Routing Information Protocol (RIP).

### Link State Protocols

In contrast, **link state protocols** provide each router with a complete map of the network topology. Instead of sharing their entire routing table, routers send out information about the state of their own links (e.g., connected neighbors and the cost of the connection) to all other routers on the network. Using this information, every router can independently build an identical map of the network and calculate the best path to every destination. This approach leads to faster **network convergence** and is more scalable than distance vector protocols. An example is the Open Shortest Path First (OSPF) protocol.

### Network Convergence

Before we discuss protocols further, it's important to understand a key concept in routing known as **network convergence**. When using routing protocols, routers communicate to collect and exchange information. Convergence is the state where all routers have a consistent and accurate view of the network topology. When every routing table correctly maps the entire network, the network is considered "converged." If a change occurs, such as a link going down, convergence is temporarily broken until all routers learn about the change and update their routing tables.

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

What is the term for the state where all routing tables on a network agree on the network topology? (Please answer in English, paying attention to capitalization.)

