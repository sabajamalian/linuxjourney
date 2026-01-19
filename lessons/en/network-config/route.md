---
index: 2
lang: "en"
title: "route"
meta_title: "route - Network Config"
meta_description: "Learn to manage your Linux routing table. This guide covers adding and deleting network routes using the modern 'ip route command in linux' and the legacy 'route' command."
meta_keywords: "ip route command in linux, linux ip route command, add route, delete route, routing table, network routing, linux networking, ip route"
---

## Lesson Content

In Linux, the routing table directs network traffic to its correct destination. While we've previously discussed viewing this table, you can also manually add or remove routes to control how data packets are forwarded. This is essential for configuring complex network setups or troubleshooting connectivity issues.

### Using the Legacy route Command

The `route` command is a traditional tool for managing the routing table. While still functional, it is considered legacy, and the `ip` command is now preferred.

To add a new network route, you specify the network address, subnet mask, and the gateway (`gw`):

```bash
sudo route add -net 192.168.2.1/23 gw 10.11.12.3
```

To delete a route, use the `del` flag with the network address:

```bash
sudo route del -net 192.168.2.1/23
```

### Modern Route Management with ip route

The `ip route` command is the modern and more powerful tool for network configuration in Linux. It offers a more consistent and extensive set of options for managing network interfaces and routes. Using the **linux ip route command** is the recommended practice for current systems.

To add a route with the **ip route command in linux**, you use the `add` action, specifying the destination network and the next hop via the gateway:

```bash
ip route add 192.168.2.1/23 via 10.11.12.3
```

To delete a route, you can use the `delete` action. You can specify the route in full or just the destination network if it's unique:

```bash
# Delete by specifying the full route
ip route delete 192.168.2.1/23 via 10.11.12.3

# Or, delete by specifying only the destination
ip route delete 192.168.2.1/23
```

Mastering the `ip route` command is a key skill for any Linux administrator responsible for network management.

## Exercise

Follow these steps in your Ubuntu VM terminal to practice the concepts from this lesson:

1. **View IP configuration**: Try this command
   ```bash
   ip addr show
   ```
   Expected output:
   ```
   (Output will vary based on your system)
   ```

2. **Check network interfaces**: Try this command
   ```bash
   ls /sys/class/net/
   ```
   Expected output:
   ```
   (Output will vary based on your system)
   ```

3. **View ARP table**: Try this command
   ```bash
   ip neigh` or `arp -a
   ```
   Expected output:
   ```
   (Output will vary based on your system)
   ```

4. **Check network statistics**: Try this command
   ```bash
   netstat -i` or `ip -s link
   ```
   Expected output:
   ```
   (Output will vary based on your system)
   ```

## Quiz Question

When using the legacy `route` command, what is the flag used to delete a route? Please answer in English, paying attention to case.

