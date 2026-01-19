# Instructor Guide: Linux Journey

## Overview

This guide provides instructions for deploying and managing Ubuntu VMs for the Linux Journey course. Each student receives their own dedicated virtual machine with full root access.

## Why Individual VMs?

Individual VMs provide several advantages:

- **Full root access**: Students can practice system administration commands without restrictions
- **Isolation**: Students can experiment freely without affecting others
- **Real-world experience**: Mimics actual Linux server environments
- **Safe learning**: Students can make mistakes and recover without consequences

## Deployment Options

### Azure Virtual Machines (Recommended)

Deploy one Ubuntu VM per student using Azure's infrastructure.

#### Prerequisites

- Azure subscription with sufficient quota for VMs
- Azure CLI installed and configured
- SSH key pair for student access

#### VM Specifications

**Recommended configuration per student:**
- **OS**: Ubuntu 22.04 LTS (or latest LTS version)
- **Size**: Standard_B1s or Standard_B1ms
  - 1-2 vCPUs
  - 1-2 GB RAM
  - Sufficient for all course exercises
- **Disk**: 30 GB Standard SSD
- **Network**: Standard security group with SSH (port 22) access

#### Automated Deployment Script

```bash
#!/bin/bash

# Configuration
RESOURCE_GROUP="linux-journey-rg"
LOCATION="eastus"
VM_SIZE="Standard_B1s"
IMAGE="UbuntuLTS"
ADMIN_USERNAME="student"
SSH_KEY_PATH="~/.ssh/id_rsa.pub"

# Create resource group
az group create --name $RESOURCE_GROUP --location $LOCATION

# Function to create VM for a student
create_student_vm() {
    local student_id=$1
    local vm_name="linux-journey-vm-${student_id}"
    
    echo "Creating VM for student ${student_id}..."
    
    az vm create \
        --resource-group $RESOURCE_GROUP \
        --name $vm_name \
        --image $IMAGE \
        --size $VM_SIZE \
        --admin-username $ADMIN_USERNAME \
        --ssh-key-values @$SSH_KEY_PATH \
        --public-ip-sku Standard \
        --tags "course=linux-journey" "student=${student_id}"
    
    # Get public IP
    public_ip=$(az vm show -d --resource-group $RESOURCE_GROUP --name $vm_name --query publicIps -o tsv)
    
    echo "Student ${student_id} VM created: ssh ${ADMIN_USERNAME}@${public_ip}"
    echo "${student_id},${public_ip}" >> students.csv
}

# Create VMs for each student (example: 10 students)
echo "student_id,public_ip" > students.csv
for i in {1..10}; do
    create_student_vm $(printf "%03d" $i)
done

echo "All VMs created. Student access details saved in students.csv"
```

#### Cost Management

**Estimated costs (Azure, US East):**
- Standard_B1s: ~$10-15/month per VM
- For a 10-student class: ~$100-150/month
- Consider using Azure Education credits if available

**Cost optimization tips:**
- Use auto-shutdown schedules (e.g., shutdown at night)
- Deallocate VMs when not in use (weekends, between classes)
- Delete VMs after course completion

```bash
# Set auto-shutdown for all VMs
for vm in $(az vm list -g $RESOURCE_GROUP --query "[].name" -o tsv); do
    az vm auto-shutdown -g $RESOURCE_GROUP -n $vm --time 2200
done

# Deallocate all VMs (stops billing for compute)
az vm deallocate --ids $(az vm list -g $RESOURCE_GROUP --query "[].id" -o tsv)

# Start all VMs
az vm start --ids $(az vm list -g $RESOURCE_GROUP --query "[].id" -o tsv)
```

### Other Cloud Providers

The course can also be deployed on:

- **AWS EC2**: Use t2.micro or t3.micro instances with Ubuntu AMI
- **Google Cloud Platform**: Use e2-micro instances with Ubuntu image
- **DigitalOcean**: Use Basic Droplets ($6/month) with Ubuntu
- **On-premises**: Use VMware, VirtualBox, or Proxmox for local deployments

## Student Setup

### Initial VM Configuration

After VM creation, perform basic setup:

```bash
#!/bin/bash
# Run this on each VM after creation

# Update system
sudo apt update && sudo apt upgrade -y

# Install common tools
sudo apt install -y \
    vim \
    git \
    curl \
    wget \
    tree \
    htop \
    net-tools \
    man-db

# Create practice directories
mkdir -p ~/practice ~/exercises

# Set hostname
sudo hostnamectl set-hostname linux-journey-student

echo "VM setup complete!"
```

### Distributing Access Information

Create a CSV file with student credentials:

```csv
student_id,vm_address,username,instructions
001,20.10.30.40,student,"ssh student@20.10.30.40"
002,20.10.30.41,student,"ssh student@20.10.30.41"
...
```

Share individual lines with each student via:
- Email
- Learning management system
- Printed handouts

## Monitoring and Management

### Health Checks

Monitor VM status regularly:

```bash
# Check all VMs status
az vm list -g $RESOURCE_GROUP -d --output table

# Check specific VM
az vm get-instance-view --resource-group $RESOURCE_GROUP --name VM_NAME
```

### Student Support

Common issues and solutions:

1. **SSH connection refused**
   - Check VM is running: `az vm get-instance-view`
   - Verify network security group allows SSH
   - Confirm public IP address

2. **Permission denied**
   - Verify SSH key is correct
   - Check student is using correct username

3. **Disk full**
   - Students may fill disk with experiments
   - Increase disk size or clean up: `sudo apt clean && sudo apt autoremove`

### Backup and Snapshots

Create snapshots for recovery:

```bash
# Create snapshot of VM disk
az snapshot create \
    --resource-group $RESOURCE_GROUP \
    --name vm-snapshot-$(date +%Y%m%d) \
    --source $(az vm show -g $RESOURCE_GROUP -n VM_NAME --query "storageProfile.osDisk.name" -o tsv)
```

## Quiz Answer Key

The quiz answers for all lessons have been centralized in the [`/quiz-answers/`](/quiz-answers/) folder. This answer key is organized by category and can be used for grading student responses.

Each lesson file contains only the quiz question; the answers are located in the corresponding category file (e.g., `quiz-answers/command-line-answers.md` for command line lessons).

## Course Delivery Tips

1. **Pre-class**: Ensure all VMs are running and accessible
2. **During class**: Monitor for connection issues
3. **Exercises**: Give students time to practice each command
4. **Root access**: Remind students they have full sudo access
5. **Troubleshooting**: Encourage students to experiment and recover from mistakes

## Cleanup After Course

```bash
# Delete entire resource group (removes all VMs)
az group delete --name $RESOURCE_GROUP --yes --no-wait

# Or delete individual VMs
az vm delete --resource-group $RESOURCE_GROUP --name VM_NAME --yes
```

## Security Best Practices

1. **SSH keys only**: Disable password authentication
2. **Limited exposure**: Only open port 22, restrict by IP if possible
3. **Regular updates**: Keep VMs patched
4. **Short-lived**: Delete VMs after course completion
5. **Monitoring**: Enable Azure Security Center alerts

## Support

For issues or questions:
- Create an issue in the GitHub repository
- Contact the course maintainer
- Consult Azure/cloud provider documentation
