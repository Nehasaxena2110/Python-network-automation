# ==================================================
# Script Name : parse_device_info.py
# Purpose     : Read and display device information
#               from a JSON file.
# Skills      : Python, JSON Parsing
# ==================================================

import json

with open("sample_device.json", "r") as file:
    data = json.load(file)

print("Hostname :", data["hostname"])
print("IP Address :", data["ip_address"])
print("Role :", data["role"])
print("Vendor :", data["vendor"])
