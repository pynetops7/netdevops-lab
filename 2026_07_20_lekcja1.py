#dane
host = "grzegorz"
port = 42

#komendy na urządzeniu
commands = ["show version", "show vlan", "show interfaces"]

#urządzenie
device = {
    "model": "Catalyst 9000",
    "ports": 22
}

#wypisuje odpowiedź
print(host)
print(port)
print(commands)
print(device)