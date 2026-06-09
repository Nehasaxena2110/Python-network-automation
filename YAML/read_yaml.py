# ==================================================
# Script Name : read_yaml.py
# Author      : Neha Saxena
# Purpose     : Read network device inventory from
#               a YAML file and display details.
#
# Skills      : Python, YAML Parsing, Automation
# ==================================================

import yaml

# Open YAML file
with open("devices.yaml", "r") as file:
    data = yaml.safe_load(file)

# Display device information
for device in data["devices"]:
    print("-" * 40)
    print(f"Hostname : {device['hostname']}")
    print(f"IP       : {device['ip']}")
    print(f"Role     : {device['role']}")

print("-" * 40)
