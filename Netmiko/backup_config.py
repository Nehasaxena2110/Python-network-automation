from netmiko import ConnectHandler

# Device details
device = {
    "device_type": "cisco_ios",
    "host": "10.1.1.1",
    "username": "YOUR_USERNAME",
    "password": "YOUR_PASSWORD"
}

# Connect to the device
conn = ConnectHandler(**device)

# Retrieve running configuration
config = conn.send_command("show running-config")

# Save configuration to a file
with open("backup.txt", "w") as file:
    file.write(config)

print("Configuration backup completed successfully.")

# Disconnect from device
conn.disconnect()
