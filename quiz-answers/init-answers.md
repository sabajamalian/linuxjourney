# Init Quiz Answers

## 1. System V Overview

**Question:** What runlevel is usually used for shutdown?

**Answer:** 0

## 2. System V Service

**Question:** What is the full command to stop a service named `peanut` on a System V system? Please provide the exact command in English, paying attention to case.

**Answer:** sudo service peanut stop

## 3. Upstart Overview

**Question:** What is the init implementation that is used by Ubuntu?

**Answer:** systemd

## 4. Upstart Jobs

**Question:** How would you manually restart an Upstart job called `peanuts`? Please provide the full command. (Note: The answer is case-sensitive and must be in English.)

**Answer:** sudo initctl restart peanuts

## 5. Systemd Overview

**Question:** What unit is used to group together other units? Please answer in a single lowercase English word.

**Answer:** target

## 6. Systemd Goals

**Question:** What is the command to start a service named peanut.service? Please answer in English. The answer is case-sensitive.

**Answer:** sudo systemctl start peanut.service

## 7. Power States

**Question:** What is the full command, including `sudo`, to schedule a system power off in 4 minutes? Please provide the complete command in English, paying attention to spacing and case.

**Answer:** sudo shutdown -h +4

