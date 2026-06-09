# ==================================================
# Project     : Configuration Backup System
# Author      : Neha Saxena
# Purpose     : Back up running configurations from
#               network devices listed in a YAML file.
#
# Skills      : Python, Netmiko, YAML, File Handling
# ==================================================

import yaml
from netmiko import ConnectHandler

USERNAME = "YOUR_USERNAME"
PASSWORD = "YOUR_PASSWORD"

# Read inventory
with open("devices.yaml", "r") as file:
    inventory = yaml.safe_load(file)

# Process devices
for device in inventory["devices"]:

    print(f"\nConnecting to {device['hostname']}...")

    connection = ConnectHandler(
        device_type=device["device_type"],
        host=device["ip"],
        username=USERNAME,
        password=PASSWORD
    )

    config = connection.send_command(
        "show running-config"
    )

    filename = f"{device['hostname']}_backup.txt"

    with open(filename, "w") as backup_file:
        backup_file.write(config)

    print(f"Backup saved to {filename}")

    connection.disconnect()

print("\nBackup process completed.")
