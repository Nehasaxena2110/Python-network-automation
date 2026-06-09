from netmiko import ConnectHandler

# Device details
device = {
    "device_type": "cisco_ios",
    "host": "10.1.1.1",
    "username": "YOUR_USERNAME",
    "password": "YOUR_PASSWORD"
}

# List of commands to execute
commands = [
    "show version",
    "show ip interface brief",
    "show cdp neighbors"
]

# Connect to the device
conn = ConnectHandler(**device)

# Execute commands one by one
for command in commands:
    print(f"\n===== {command} =====")
    output = conn.send_command(command)
    print(output)

# Disconnect from the device
conn.disconnect()
