# ==================================================
# Script Name : get_users.py
# Author      : Neha Saxena
# Purpose     : Retrieve data from a REST API.
#
# Skills      : Python, REST API, JSON Parsing
# ==================================================

import requests

response = requests.get(
    "https://jsonplaceholder.typicode.com/users"
)

print("Status Code:", response.status_code)

data = response.json()

for user in data:
    print(user["name"])
