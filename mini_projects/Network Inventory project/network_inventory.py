# ==================================================
# Project     : Network Inventory Generator
# Author      : Neha Saxena
# Purpose     : Collect device information and
#               generate an inventory report.
#
# Skills      : Python, Netmiko, YAML, JSON
# ==================================================

import yaml
import json

# Read device inventory
with open("devices.yaml", "r") as file:
    inventory = yaml.safe_load(file)

report = []

for device in inventory["devices"]:

    device_info = {
        "hostname": device["hostname"],
        "ip": device["ip"],
        "device_type": device["device_type"]
    }

    report.append(device_info)

# Save report
with open("inventory_report.json", "w") as file:
    json.dump(report, file, indent=4)

print("Inventory report generated.")
