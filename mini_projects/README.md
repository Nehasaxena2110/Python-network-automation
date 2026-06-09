# Configuration Backup System

## Overview

This project automates the backup of Cisco IOS device configurations using Python and Netmiko.

The script connects to devices listed in a YAML inventory file, retrieves the running configuration, and saves the output to local backup files.

## Technologies Used

* Python
* Netmiko
* YAML
* SSH
* Cisco IOS

## Project Structure

```text
config_backup/
│
├── devices.yaml
├── backup_configs.py
├── backups/
│   ├── R1_backup.txt
│   └── R2_backup.txt
└── README.md
```

## Input File

### devices.yaml

```yaml
devices:
  - hostname: R1
    ip: 10.1.1.1

  - hostname: R2
    ip: 10.1.1.2
```

## Workflow

1. Read device inventory from YAML.
2. Connect to each device using SSH.
3. Execute `show running-config`.
4. Save configuration to a backup file.
5. Disconnect from the device.

## Sample Output

```text
Connecting to R1...
Configuration saved to backups/R1_backup.txt

Connecting to R2...
Configuration saved to backups/R2_backup.txt

Backup process completed successfully.
```

## Skills Demonstrated

* Network Automation
* Python Programming
* YAML Parsing
* Netmiko
* File Handling
* Configuration Management

## Future Enhancements

* Timestamped backups
* Multi-vendor support
* Backup verification
* Email notifications
* Scheduled backups

```
```
