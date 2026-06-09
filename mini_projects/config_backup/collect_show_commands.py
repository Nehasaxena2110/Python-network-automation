# ==================================================
# Project     : Multi-Device Show Command Collector
# Purpose     : Connect to multiple devices and
#               collect command outputs.
#
# Skills      : Python, YAML, Netmiko
# ==================================================

import yaml

with open("devices.yaml") as file:
    data = yaml.safe_load(file)

for device in data["devices"]:
    print(f"Connecting to {device['hostname']}")
    print(f"Collecting output from {device['ip']}")
