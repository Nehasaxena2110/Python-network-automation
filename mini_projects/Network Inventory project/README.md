
# Network Inventory Generator

## Overview

The Network Inventory Generator automates the collection and organization of network device information.

The project reads devices from a YAML inventory file and generates a structured inventory report in JSON format.

This helps network engineers maintain an accurate inventory of routers, switches, and other network devices.

---

## Technologies Used

- Python
- YAML
- JSON
- Netmiko
- Network Automation

---

## Project Structure

```text
network_inventory/
│
├── README.md
├── devices.yaml
├── network_inventory.py
├── inventory_report.json
└── sample_output.txt
```

---

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

---

## Workflow

1. Read device information from YAML inventory.
2. Process each device.
3. Collect device details.
4. Generate inventory report.
5. Export data to JSON format.

---

## Generated Report

### inventory_report.json

```json
[
    {
        "hostname": "R1",
        "ip": "10.1.1.1",
        "device_type": "cisco_ios"
    },
    {
        "hostname": "R2",
        "ip": "10.1.1.2",
        "device_type": "cisco_ios"
    }
]
```

---

## Sample Output

```text
Inventory report generated successfully.

Devices Found: 2

Hostname : R1
IP       : 10.1.1.1
Type     : cisco_ios

Hostname : R2
IP       : 10.1.1.2
Type     : cisco_ios
```

---

## Skills Demonstrated

- Python Programming
- Network Automation
- YAML Parsing
- JSON Generation
- Data Collection
- Inventory Management
- File Handling

---

## Real-World Use Cases

- Network Asset Management
- Device Inventory Tracking
- Hardware Audits
- Upgrade Planning
- Compliance Reporting

---

## Future Enhancements

- Collect IOS Version
- Collect Device Model
- Collect Serial Number
- Export Reports to CSV
- Multi-Vendor Support
- Automated Scheduled Inventory Collection

---

## Author

Neha Saxena
