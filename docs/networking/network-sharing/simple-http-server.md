---
title: "Simple HTTP Server"
layout: default
parent: Network Sharing
grand_parent: Networking
nav_order: 3
---

## Lesson Content

Python includes a built-in module that allows you to instantly create a web server, which is incredibly useful for sharing files over a network. Setting up a **linux simple http server** is a straightforward process that requires just a single command.

### Starting a Simple HTTP Server in Linux

To get started, navigate to the directory you wish to share using your terminal. Once you are in the desired directory, you can start a **simple http server linux** environment with the following command if you are using Python 3:

```bash
python -m http.server
```

This command launches a basic web server, making the contents of your current directory accessible over HTTP.

### Legacy Method for Python 2

For older systems that still use Python 2, the command is slightly different. The module was previously named `SimpleHTTPServer`. If you've ever wondered **what is python simplehttpserver**, it is simply the Python 2 equivalent of the `http.server` module. You can run it with:

```bash
python -m SimpleHTTPServer
```

### Accessing Your Simple Linux Web Server

After running the command, your **simple linux web server** will be active. You can access the shared files from another machine on the same network by opening a web browser and navigating to `http://IP_ADDRESS:8000`, replacing `IP_ADDRESS` with the local IP of the machine running the server.

To view the files on the same machine, you can use the localhost address: `http://localhost:8000`.

## Exercise

Follow these steps in your Ubuntu VM terminal to practice the concepts from this lesson:

1. **Check SSH availability**: Try this command
   ```bash
   which ssh
   ```
   Expected output:
   ```
   (Output will vary based on your system)
   ```

2. **Test local connection**: Try this command
   ```bash
   ss -tuln | grep :22
   ```
   Expected output:
   ```
   (Output will vary based on your system)
   ```

3. **View network shares**: Try this command
   ```bash
   mount | grep nfs` or similar
   ```
   Expected output:
   ```
   (Output will vary based on your system)
   ```

4. **Check rsync**: Try this command
   ```bash
   which rsync` and `rsync --version
   ```
   Expected output:
   ```
   (Output will vary based on your system)
   ```

## Quiz Question

For Python 3, what is the name of the module used to create a simple HTTP server? (Please answer in English, paying attention to case sensitivity).

