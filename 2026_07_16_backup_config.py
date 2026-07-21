#zadanie 2: wynik trzech komend wysłanych do sandboxa przy użyciu pętli for zapisuje do pliku *.txt
#import funkcji ConnectHandel z biblioteki netmiko
from netmiko import ConnectHandler

#urządzenie - do zmiany dane logowania
device = {
    "device_type": "cisco_xe",   # typ systemu operacyjnego urządzenia
    "host": "devnetsandboxiosxec9k.cisco.com",      # hostname lub IP z panelu Cisco
    "username": "pynet.ops7",  # login z panelu
    "password": "CD-N-Bs50w13nbw", # hasło z panelu
    "port": 22,
}

# nawiązuje połączenie SSH
conn = ConnectHandler(**device)

# wysyła komendę zgodnie z możliwościami urządzenia i wymaganiami zadania
output = conn.send_command("show version", "show ip interface brief", "show vlan brief")

# wypisuje odpowiedź urządzenia - całkowicie do zmiany
print(output)

# zamyka sesję SSH
conn.disconnect()