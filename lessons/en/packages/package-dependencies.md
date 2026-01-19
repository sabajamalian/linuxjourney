---
index: 4
lang: "en"
title: "Package Dependencies"
meta_title: "Package Dependencies - Packages"
meta_description: "Learn about Linux package dependencies and why they are crucial for software installation. This guide explains shared libraries and how package management handles dependencies to prevent broken software."
meta_keywords: "Linux package dependencies, shared libraries, Linux packages, package management, Linux software installation, Linux tutorial, beginner Linux, Linux guide"
---

## Lesson Content

In the world of Linux, software packages rarely stand alone. They often rely on other components, known as dependencies, to function correctly. This concept is fundamental to Linux package management.

### The Concept of Dependencies

To understand dependencies, think of a group of restaurants. Each restaurant creates unique dishes, but they all source their ingredients from the same central farm. The quality of their food is dependent on the farm's supplies. If the farm suddenly stopped providing ingredients, the restaurants couldn't operate. Similarly, Linux packages depend on other components to run.

### What are Shared Libraries

In Linux, these crucial dependencies are typically other packages or, more commonly, shared libraries. A shared library is a collection of pre-compiled code that multiple programs can use simultaneously. This is a core principle of efficient software installation.

Returning to our analogy, imagine the extra work if every restaurant had to grow its own food. By sharing a common resource—the farm—they save immense effort. Shared libraries work the same way, preventing developers from having to rewrite common functions for every new application. We will explore shared libraries in more detail later, but for now, it's important to know they are a common type of dependency.

### The Risk of Broken Packages

Effective package management is all about ensuring these dependencies are met. If a required package or shared library is missing during a software installation, the process will likely fail. The package will be considered "broken" because it lacks the necessary components to run. Your system's package manager is designed to handle these Linux package dependencies automatically, fetching and installing them to prevent such issues before they occur.

## Exercise

Follow these steps in your Ubuntu VM terminal to practice the concepts from this lesson:

1. **Check package dependencies**: View dependencies of a package
   ```bash
   apt show wget 2>/dev/null | grep -A10 "^Depends"
   ```
   Expected output:
   ```
   Depends: libc6 (>= 2.28), libgnutls30 (>= 3.6.12), libidn2-0 (>= 2.0), etc.
   ```

2. **View reverse dependencies**: See what depends on a package
   ```bash
   apt rdepends bash | head -15
   ```
   Expected output:
   ```
   bash
   Reverse Depends:
     bash-completion
     byobu
     command-not-found
   ```

3. **Check if dependencies are satisfied**: Verify package status
   ```bash
   dpkg -s wget | grep "^Status"
   ```
   Expected output:
   ```
   Status: install ok installed
   ```

4. **View dependency tree**: Show package relationships
   ```bash
   apt-cache depends wget | head -15
   ```
   Expected output:
   ```
   wget
     Depends: libc6
     Depends: libgnutls30
     Depends: libidn2-0
   ```

## Quiz Question

What is a collection of pre-compiled code that multiple programs can use? (Please answer in English, paying attention to uppercase and lowercase letters).

