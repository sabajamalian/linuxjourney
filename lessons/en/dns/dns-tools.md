---
index: 6
lang: "en"
title: "DNS Tools"
meta_title: "DNS Tools - DNS"
meta_description: "Explore essential Linux DNS tools like nslookup and the powerful dig command. This beginner-friendly Linux tutorial covers DNS queries and DNS troubleshooting techniques."
meta_keywords: "nslookup, dig command, DNS tools, Linux DNS, DNS troubleshooting, name server lookup, Linux tutorial, beginner Linux"
---

## Lesson Content

In Linux, several command-line utilities are available for network diagnostics. When it comes to Domain Name System (DNS) issues, two primary **DNS tools** stand out: `nslookup` and `dig`. Understanding how to use them is crucial for any **DNS troubleshooting** on a **Linux DNS** server or client.

### Using nslookup for Basic DNS Queries

The `nslookup` (name server lookup) tool is a classic utility for querying DNS servers to obtain domain name or IP address mapping information. While it is sometimes considered deprecated in favor of `dig`, it remains a quick and easy tool for simple lookups.

To find the IP address for a domain like `www.google.com`, you can run:

```bash
pete@icebox:~$ nslookup www.google.com
Server:         127.0.1.1
Address:        127.0.1.1#53

Non-authoritative answer:
Name:   www.google.com
Address: 216.58.192.4
```

In this output, `Server` and `Address` show the DNS server that answered the query. The `Non-authoritative answer` means the server provided a cached result rather than querying the authoritative source directly. `Name` and `Address` show the resolved IP address for the domain.

### Advanced DNS Troubleshooting with dig

The `dig` (domain information groper) command is a powerful and flexible tool for interrogating DNS name servers. It provides more detailed information than `nslookup`, making it the preferred choice for serious **DNS troubleshooting**.

Here is an example of using the **dig command**:

```bash
pete@icebox:~$ dig www.google.com

; <<>> DiG 9.9.5-3-Ubuntu <<>> www.google.com
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 42376
;; flags: qr rd ra; QUERY: 1, ANSWER: 5, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; MBZ: 0005 , udp: 512
;; QUESTION SECTION:
;www.google.com.                        IN      A

;; ANSWER SECTION:
www.google.com.         5       IN      A       74.125.239.147
www.google.com.         5       IN      A       74.125.239.144
www.google.com.         5       IN      A       74.125.239.146
www.google.com.         5       IN      A       74.125.239.145
www.google.com.         5       IN      A       74.125.239.148

;; Query time: 27 msec
;; SERVER: 127.0.1.1#53(127.0.1.1)
;; WHEN: Sun Feb 07 10:14:00 PST 2016
;; MSG SIZE  rcvd: 123
```

The output from `dig` is organized into sections:

- **QUESTION SECTION**: Shows the query that was sent. Here, we asked for an `A` (address) record for `www.google.com`.
- **ANSWER SECTION**: Displays the answer received from the DNS server. In this case, Google has multiple IP addresses associated with its domain.
- **Statistics**: The final section provides metadata about the query, such as the query time and the server that responded.

Because of its detailed output and flexibility, `dig` is an indispensable utility for anyone managing or troubleshooting network services on Linux.

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

What tool is used to get detailed information about DNS name servers? Please answer using only lowercase English characters.

## Quiz Answer

dig
