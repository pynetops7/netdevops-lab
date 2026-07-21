#komendy
commands = ["Gig1/0/1", "Gig1/0/2", "Gig1/0/3"]

#pętla for
for cmd in commands:
    print(f"Sprawdzam interfejs: {cmd}")

#zmienna, port
vlan_id = 10

#instrukcja warunkowa, podejmowanie decyzji
if vlan_id == 10:
    print("VLAN domyślny")
else:
    print("VLAN niestandardowy")   