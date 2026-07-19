from netmiko import ConnectHandler

device = {
    "device_type": "cisco_xe",   # typ systemu operacyjnego urządzenia
    "host": "devnetsandboxiosxec9k.cisco.com",      # hostname lub IP z panelu Cisco
    "username": "pynet.ops7",  # login z panelu
    "password": "9zrob_KL6-WJ3", # hasło z panelu
    "port": 22,
}

# nawiązuje połączenie SSH
conn = ConnectHandler(**device)

# wysyła komendę tak, jakbyś sam ją wpisał w terminalu na routerze
output = conn.send_command("show ip interface brief")

# wypisuje odpowiedź urządzenia
print(output)

# zamyka sesję SSH
conn.disconnect()