# ==================================================
# Project     : Interface Health Check
# Author      : Neha Saxena
# Purpose     : Connect to network devices and
#               identify interfaces that are up
#               or down.
#
# Skills      : Python, Netmiko, YAML,
#               Network Automation
# ==================================================

import yaml
from netmiko import ConnectHandler

USERNAME = "YOUR_USERNAME"
PASSWORD = "YOUR_PASSWORD"

# Read device inventory
with open("devices.yaml", "r") as file:
    inventory = yaml.safe_load(file)

for device in inventory["devices"]:

    print("\n" + "=" * 50)
    print(f"Device: {device['hostname']}")
    print("=" * 50)

    connection = ConnectHandler(
        device_type=device["device_type"],
        host=device["ip"],
        username=USERNAME,
        password=PASSWORD
    )

    output = connection.send_command(
        "show ip interface brief"
    )

    print(output)

    connection.disconnect()
