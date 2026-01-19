---
title: "Subnet Math"
layout: default
parent: Subnetting
grand_parent: Networking
nav_order: 3
---

## Lesson Content

To determine the number of hosts a subnet can support, you need to understand some basic **subnet math**. The subnet mask is the key to this calculation.

### The Role of the Subnet Mask

Let's use an IP address of **192.168.1.0** with a subnet mask of **255.255.255.0**. The primary function of the subnet mask is to distinguish the network portion of the address from the host portion.

To see how this works, we can convert these values to their binary form.

```
192.168.1.165  = 11000000.10101000.00000001.10100101
255.255.255.0  = 11111111.11111111.11111111.00000000
```

### Performing Subnet Mask Math

In the binary representation above, the `1`s in the subnet mask correspond to the network portion of the IP address. This part is "masked" or fixed. The `0`s in the subnet mask correspond to the host portion, which represents the range of addresses you can assign to devices.

In our example, the host portion is `00000000`. This is an 8-bit field, and with 8 bits, you can create 2^8, or 256, unique combinations (from 0 to 255).

### Calculating Available Hosts

While there are 256 possible combinations, not all of them can be assigned to hosts. In any subnet, two addresses are reserved:

1. **Network Address:** The first address, where all host bits are `0` (e.g., 192.168.1.0).
2. **Broadcast Address:** The last address, where all host bits are `1` (e.g., 192.168.1.255).

Therefore, the actual number of usable hosts is 256 - 2 = 254. This means for the `192.168.1.0` network with a `255.255.255.0` mask, you can assign IP addresses from `192.168.1.1` to `192.168.1.254`. This core calculation is a fundamental part of **subnet math**.

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

What is the binary equivalent of 255?

