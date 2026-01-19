---
title: "Subnetting Cheats"
layout: default
parent: Subnetting
grand_parent: Networking
nav_order: 4
---

## Lesson Content

In modern networking, you will rarely perform subnet math by hand, as tools and calculators automate the process. However, understanding the manual conversion between decimal and binary is crucial for networking interviews, certification exams, and gaining a deeper understanding of how IP addressing works. This lesson provides some simple cheats to help you master it.

First, it's highly beneficial to memorize the base-2 calculations, as they form the foundation of binary math.

- 2^1 = 2
- 2^2 = 4
- 2^3 = 8
- 2^4 = 16
- 2^5 = 32
- 2^6 = 64
- 2^7 = 128
- 2^8 = 256

### The Binary Conversion Chart

To easily convert numbers, we use a chart that represents the value of each bit in an 8-bit octet of an IP address.

```plaintext
1   1  1  1  1 1 1 1
128 64 32 16 8 4 2 1
```

This chart is your primary tool. Each number corresponds to a bit's position. The full sum, `128+64+32+16+8+4+2+1`, equals 255, which is the highest possible value in an octet.

### Decimal to Binary Conversion

Let's convert the IP address `192.168.23.43` to binary. We'll walk through the first octet, `192`, to demonstrate the process. We use the values from our chart: `128 64 32 16 8 4 2 1`.

1. Start with the number `192`. Can you subtract 128 from it? Yes (192 - 128 = 64). So, the first bit is **1**.
2. Our new number is `64`. Can you subtract the next value, 64, from it? Yes (64 - 64 = 0). The second bit is **1**.
3. Our remainder is now `0`. We cannot subtract 32, 16, 8, 4, 2, or 1. Therefore, the remaining bits are all **0**.

The binary form of 192 is `11000000`. You can apply this same subtraction method to the other octets.

### Binary to Decimal Conversion

To convert from binary back to decimal, you simply add the values from the chart where a `1` appears in the binary number. Let's convert `11000000` back to decimal.

Looking at the chart `128 64 32 16 8 4 2 1`, the first two bits are `1`. This means we add the first two values:

`128 + 64 = 192`

Since all other bits are `0`, we don't add any other values. The formula `128 + 64 + 0 + 0 + 0 + 0 + 0 + 0` gives us 192. It's that simple!

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

What is the binary conversion of 123? Please provide the answer in English characters (numbers).

