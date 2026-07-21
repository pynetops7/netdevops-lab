#import funkcji ConnectHandel z biblioteki netmiko
from netmiko import ConnectHandler

#urządzenie
device = {
    "device_type": "cisco_xe",   # typ systemu operacyjnego urządzenia
    "host": "devnetsandboxiosxec9k.cisco.com",      # hostname lub IP z panelu Cisco
    "username": "pynet.ops7",  # login z panelu
    "password": "CD-N-Bs50w13nbw", # hasło z panelu
    "port": 22,
}

# nawiązuje połączenie SSH
conn = ConnectHandler(**device)

# wysyła komendę zgodnie z możliwościami urządzenia
output = conn.send_command("show version", "show ip interface brief", "show vlan brief")

# wypisuje odpowiedź urządzenia
print(output)

# zamyka sesję SSH
conn.disconnect()