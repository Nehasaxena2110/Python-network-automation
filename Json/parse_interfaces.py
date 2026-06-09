# ==================================================
# Script Name : parse_interfaces.py
# Author      : Neha Saxena
# Purpose     : Parse interface information from a
#               JSON file and display interface
#               details.
#
# Skills      : Python, JSON Parsing, Dictionaries,
#               Lists, Loops
# ==================================================

import json

# Open JSON file
with open("interfaces.json", "r") as file:
    data = json.load(file)

# Loop through interfaces
for interface in data["interfaces"]:
    print("-" * 40)
    print(f"Interface : {interface['name']}")
    print(f"IP Address: {interface['ip']}")
    print(f"Status    : {interface['status']}")

print("-" * 40)
