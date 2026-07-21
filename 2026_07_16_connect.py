#import funkcji ConnectHandler z biblioteki netmiko
from netmiko import ConnectHandler

#urządzenie
device = {
    "device_type": "cisco_xe",   # typ systemu operacyjnego urządzenia
    "host": "devnetsandboxiosxec9k.cisco.com",      # hostname lub IP z panelu Cisco
    "username": "pynet.ops7",  # login z panelu
    "password": "9zrob_KL6-WJ3", # hasło z panelu
    "port": 22,
}

# nawiązuje połączenie nową sesję SSH z urządzeniem
conn = ConnectHandler(**device)

# wysyła komendę zgodnie z możliwościami urządzenia
output = conn.send_command("show ip interface brief")

# wypisuje odpowiedź urządzenia
print(output)

# zamyka sesję SSH
conn.disconnect()