---
index: 3
lang: "en"
title: "traceroute"
meta_title: "traceroute - Troubleshooting"
meta_description: "Master the traceroute linux command to trace network routes and troubleshoot connectivity issues. This tutorial explains how traceroute uses TTL to map the path packets take to their destination."
meta_keywords: "traceroute, traceroute linux, Linux networking, network troubleshooting, TTL, packet routing, Linux commands, beginner, tutorial"
---

## Lesson Content

The `traceroute` command is a fundamental network diagnostic tool used to trace the path that packets take from your computer to a destination host. By revealing each "hop" or router along the way, it helps you identify network bottlenecks and troubleshoot connectivity problems. The `traceroute linux` utility is essential for any system administrator or network engineer.

### How Traceroute Works

The mechanism behind `traceroute` lies in its clever manipulation of the Time To Live (TTL) field in an IP packet's header. The process works as follows:

1. `traceroute` sends out a probe packet with a TTL value of 1.
2. The first router on the path receives the packet, decrements the TTL to 0, and discards it. The router then sends an ICMP "Time Exceeded" message back to your computer.
3. `traceroute` records the router's IP address and the round-trip time.
4. It then sends another packet, this time with a TTL of 2. This packet successfully passes the first router but is dropped by the second router, which again sends back a "Time Exceeded" message.
5. This process repeats, with the TTL incrementing by one for each subsequent set of packets. By building a list of the routers that return "Time Exceeded" messages, `traceroute` maps the entire route.
6. The process concludes when the packets finally reach the destination, which responds with an ICMP "Echo Reply" message.

### Understanding Traceroute Output

Let's examine a sample output from running `traceroute` in a Linux terminal:

```bash
$ traceroute google.com
traceroute to google.com (216.58.216.174), 30 hops max, 60 byte packets
 1  192.168.4.254 (192.168.4.254)  0.028 ms  0.009 ms  0.008 ms
 2  100.64.1.113 (100.64.1.113)  1.227 ms  1.226 ms 0.920 ms
 3  100.64.0.20 (100.64.0.20)  1.501 ms 1.556 ms  0.855 ms
```

Each numbered line represents a hop along the network path. Here's how to interpret the information:

- **Hop Number:** The first column (e.g., `1`, `2`, `3`) indicates the sequence of the router in the path.
- **Router Name and IP Address:** The next part shows the hostname (if it can be resolved) and the IP address of the router at that hop.
- **Round-Trip Times (RTT):** The last three columns show the round-trip time for each of the three probe packets sent to that specific hop. These times, measured in milliseconds (ms), help you gauge the latency at each step of the journey.

Using the `traceroute linux` command effectively provides invaluable insight into your network's performance and structure.

## Exercise

Follow these steps in your Ubuntu VM terminal to practice the concepts from this lesson:

1. **Test connectivity**: Try this command
   ```bash
   ping -c 4 8.8.8.8
   ```
   Expected output:
   ```
   (Output will vary based on your system)
   ```

2. **Check network status**: Try this command
   ```bash
   ip link show
   ```
   Expected output:
   ```
   (Output will vary based on your system)
   ```

3. **View open connections**: Try this command
   ```bash
   ss -tuln | head -15
   ```
   Expected output:
   ```
   (Output will vary based on your system)
   ```

4. **Test DNS resolution**: Try this command
   ```bash
   nslookup google.com` or `host google.com
   ```
   Expected output:
   ```
   (Output will vary based on your system)
   ```

## Quiz Question

What gets decremented by one when making hops across the network? (Please answer in English, paying attention to capitalization.)

