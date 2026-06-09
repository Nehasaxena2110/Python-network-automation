# ==================================================
# Script Name : parse_api_response.py
# Purpose     : Extract selected information from
#               API response data.
# ==================================================

import requests

response = requests.get(
    "https://jsonplaceholder.typicode.com/users"
)

data = response.json()

for user in data:
    print("-" * 40)
    print("Name :", user["name"])
    print("Email:", user["email"])
    print("City :", user["address"]["city"])
