
# Netmiko Examples

This folder contains Python automation scripts using the Netmiko library.

## Topics Covered

- Device connectivity
- Show command execution
- Configuration backup
- Interface status collection

## Scripts

### show_version.py
Connects to a Cisco device and runs:

```bash
show version
```

### backup_config.py
Collects and saves the running configuration.

### show_ip_int_brief.py
Retrieves interface status information.Similar code as for giving any show command.

###Give-Mulitiple-Show-commands.py
Gives multiple show commands at once.

## Requirements

```bash
pip install netmiko
```

## Skills Demonstrated

- Python
- Netmiko
- Network Automation
- Cisco IOS Device Management
