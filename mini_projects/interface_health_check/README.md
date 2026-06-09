# Interface Health Check

## Overview

This project automates interface health monitoring for Cisco network devices.

The script connects to network devices, collects interface information using `show ip interface brief`, and generates a summary report showing interface status.

## Technologies Used

* Python
* Netmiko
* YAML
* Cisco IOS
* Network Automation

## Project Structure

```text
interface_health_check/
│
├── devices.yaml
├── interface_health_check.py
├── sample_output.txt
└── README.md
```

## Input File

### devices.yaml

```yaml
devices:
  - hostname: R1
    ip: 10.1.1.1
    device_type: cisco_ios

  - hostname: R2
    ip: 10.1.1.2
    device_type: cisco_ios
```

## Workflow

1. Read device inventory from YAML.
2. Connect to each device using SSH.
3. Execute `show ip interface brief`.
4. Collect interface status information.
5. Generate a health report.
6. Identify interfaces that are down.

## Sample Output

```text
==================================================
Device: R1
==================================================

Up Interfaces   : 3
Down Interfaces : 2

Interfaces Down:
- GigabitEthernet0/1
- GigabitEthernet0/3

==================================================
Device: R2
==================================================

Up Interfaces   : 5
Down Interfaces : 1

Interfaces Down:
- GigabitEthernet0/2
```

## Skills Demonstrated

* Network Automation
* Python Programming
* YAML Parsing
* SSH Automation
* Netmiko
* Data Analysis
* Report Generation

## Use Cases

* Daily health checks
* Interface monitoring
* Proactive troubleshooting
* Network operations reporting

## Future Enhancements

* Export report to CSV
* Export report to Excel
* Email notifications
* Dashboard integration
* Scheduled execution using cron
* Multi-vendor device support

```
```
