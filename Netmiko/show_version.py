from netmiko import ConnectHandler

# Device details
device = {
    "device_type": "cisco_ios",
    "host": "10.1.1.1",
    "username": "YOUR_USERNAME",
    "password": "YOUR_PASSWORD"
}

# Connect to device
connection = ConnectHandler(**device)

# Run command
output = connection.send_command("show version")

# Display output
print(output)

# Close connection
connection.disconnect()
