---
title: "rpm and dpkg"
layout: default
parent: Packages
grand_parent: Fundamentals
nav_order: 5
---

## Lesson Content

Although most of this course is about package management systems (the Batmans of package management), we mustn't forget about the Robins. Although very useful and reliable, they don't come with that sweet Batmobile and utility belt.

Just like `.exe` is a single executable file, so is `.deb` and `.rpm`. You normally wouldn't see these if you use package repositories, but if you directly download packages, you will most likely get them in these popular formats. Obviously, they are exclusive to their distributions: `.deb` for Debian-based and `.rpm` for Red Hat-based.

To install these direct packages, you can use the package management commands: `rpm` and `dpkg`. These tools are used to install package files; however, they will not install the package dependencies. So, if your package had 10 dependencies, you would have to install those packages separately and then their dependencies, and so on and so forth. As you can see, that was one of the reasons that brought forth the full-blown management systems that we will discuss later.

Keep in mind that there will be countless times when you need to install, query, or verify a package with one of these tools, so remember these commands.

### Install a package

```bash
Debian: $ dpkg -i some_deb_package.deb
RPM: $ rpm -i some_rpm_package.rpm
```

The `i` stands for install. You can also use the longer format of `--install`.

### Remove a package

```bash
Debian: $ dpkg -r some_deb_package.deb
RPM: $ rpm -e some_rpm_package.rpm
```

Debian: `r` for remove
RPM: `e` for erase

### List installed packages

```bash
Debian: $ dpkg -l
RPM: $ rpm -qa
```

Debian: `l` for list
RPM: `q` for query and `a` for all

## Exercise

Follow these steps in your Ubuntu VM terminal to practice the concepts from this lesson:

1. **List installed packages**: View all installed packages
   ```bash
   dpkg -l | head -20
   ```
   Expected output:
   ```
   Desired=Unknown/Install/Remove/Purge/Hold
   | Status=Not/Inst/Conf-files/Unpacked/halF-conf/Half-inst/trig-aWait/Trig-pend
   |/ Err?=(none)/Reinst-required (Status,Err: uppercase=bad)
   ||/ Name                Version        Architecture Description
   +++-==================-==============-============-================================
   ii  adduser            3.118ubuntu2   all          add and remove users and groups
   ```

2. **Check if a package is installed**: Query specific package
   ```bash
   dpkg -l | grep wget
   ```
   Expected output:
   ```
   ii  wget               1.20.3-1ubuntu1 amd64        retrieves files from the web
   ```

3. **View package details**: Get information about a package
   ```bash
   dpkg -s wget
   ```
   Expected output:
   ```
   Package: wget
   Status: install ok installed
   Priority: important
   Section: web
   Installed-Size: 975
   ```

4. **List files from a package**: See what files a package installed
   ```bash
   dpkg -L wget | head -10
   ```
   Expected output:
   ```
   /.
   /usr
   /usr/bin
   /usr/bin/wget
   /usr/share
   ```

5. **Search for available packages**: Find packages (if apt is available)
   ```bash
   apt search curl 2>/dev/null | head -10
   ```
   Expected output:
   ```
   Sorting... Done
   Full Text Search... Done
   curl/focal-updates 7.68.0-1ubuntu2.20 amd64
     command line tool for transferring data with URL syntax
   ```

## Quiz Question

What is the package management tool for `.deb` files?

