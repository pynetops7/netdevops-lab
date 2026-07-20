commands = ["show version", "show vlan", "show interfaces"]

for cmd in commands:
    print(cmd)

status = "up"

if status == "up":
    print("Interfejs działa")
else:
    print("Interfejs nie działa")   