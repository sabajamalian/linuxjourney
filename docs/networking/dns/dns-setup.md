---
title: "DNS Setup"
layout: default
parent: DNS
grand_parent: Networking
nav_order: 5
---

## Lesson Content

We won't go through setting up a DNS server, as that would be quite a lengthy tutorial. Instead, here is a quick comparison list of popular DNS servers to use with Linux.

### BIND

The most popular DNS server on the Internet, it's the standard that is used with Linux distributions. It was originally developed at the University of California at Berkeley, hence the name BIND (Berkeley Internet Name Domain). If you need full-featured power and flexibility, you can't go wrong with BIND.

### DNSmasq

Lightweight and much easier to configure than BIND. If you want simplicity and don't need all the bells and whistles of BIND, use DNSmasq. It comes with all the tools you need to set up DHCP and DNS, recommended for a smaller network.

### PowerDNS

Full-featured and similar to BIND, it offers you a little bit more flexibility with options. It reads information from multiple databases such as MySQL, PostgreSQL, etc., for easier administration. Just because BIND has been the way we do things, it doesn't mean it has to stay that way.

This isn't a complete list, but it should give you an idea of where to look if you are setting up your own DNS server.

## Exercise

Follow these steps in your Ubuntu VM terminal to practice the concepts from this lesson:

1. **View DNS configuration**: Try this command
   ```bash
   cat /etc/resolv.conf
   ```
   Expected output:
   ```
   (Output will vary based on your system)
   ```

2. **Test DNS lookup**: Try this command
   ```bash
   nslookup google.com` or `host google.com
   ```
   Expected output:
   ```
   (Output will vary based on your system)
   ```

3. **Check hosts file**: Try this command
   ```bash
   cat /etc/hosts
   ```
   Expected output:
   ```
   (Output will vary based on your system)
   ```

4. **Query DNS**: Try this command
   ```bash
   dig google.com` (if available) or use nslookup
   ```
   Expected output:
   ```
   (Output will vary based on your system)
   ```

## Quiz Question

What is the de facto DNS server for Linux?

