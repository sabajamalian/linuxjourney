---
index: 3
lang: "en"
title: "DNS Process"
meta_title: "DNS Process - DNS"
meta_description: "Explore the step-by-step DNS resolution process, from root servers to the authoritative DNS server. Understand how a Linux server finds a domain, a crucial concept for production environments and domain hosting."
meta_keywords: "DNS process, DNS lookup, domain resolution, linux dns, production server, domain hosting, dns server, TLD, root servers, authoritative dns"
---

## Lesson Content

Let's explore how a computer, such as a `Linux server`, finds a `domain` like `catzontheinterwebz.com` using DNS. The process works like a funnel, narrowing down the search until we reach the specific `DNS server` that holds the answer.

### The Initial Query

First, your host asks its configured recursive DNS server, "Where is `catzontheinterwebz.com`?" This recursive server, often provided by your ISP, likely doesn't know the answer directly. So, it begins the resolution process by contacting the highest authority: the Root Servers. This initial step is the same whether you're browsing from home or a `production server` is communicating with an API.

### Root Servers

The internet's DNS hierarchy starts with 13 logical Root Servers, which are mirrored across hundreds of physical locations worldwide. These servers don't know the IP address for every `domain`, but they know who manages the Top-Level Domains (TLDs) like `.com`, `.org`, and `.net`. When asked about `catzontheinterwebz.com`, a Root Server will respond, "I don't know, but you should ask the `.com` TLD server," and provide its IP address.

### Top-Level Domain Servers

Next, the recursive server sends a new query to the `.com` TLD server, again asking for the location of `catzontheinterwebz.com`. The TLD server's job is to point to the correct authoritative name servers for that specific `domain`. It doesn't have the final IP address, but it knows which `DNS server` is responsible for the `domain`, a detail often configured through your `domain hosting` provider. The TLD server replies with the IP address of that authoritative name server.

### Authoritative DNS Server

Finally, the recursive server sends one last request to the authoritative `DNS server`. This is the server that holds the actual DNS records for the `catzontheinterwebz.com` `domain`. This server checks its records, finds the 'A' record for the host, and returns the final IP address. This is a critical step for anyone `making` a website or application live, as this server provides the definitive link between the `domain` name and the `production server`'s IP address. With the IP address in hand, your computer can now connect and retrieve the content.

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

What is the abbreviation for the nameservers where .com, .net, .org, etc., addresses are found? Please answer using only uppercase English letters.

## Quiz Answer

TLD
