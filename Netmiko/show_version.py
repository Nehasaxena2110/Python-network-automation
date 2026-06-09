from netmiko import ConnectHandler

device = {
    "device_type": "cisco_ios",
    "host": "10.1.1.1",
    "username": "YOUR_USERNAME",
    "password": "YOUR_PASSWORD"
}

connection = ConnectHandler(**device)

output = connection.send_command("show version")

print(output)

connection.disconnect()
