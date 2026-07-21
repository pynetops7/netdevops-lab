commands = ["Gig1/0/1", "Gig1/0/2", "Gig1/0/3"]

for cmd in commands:
    print(f"Sprawdzam interfejs: {cmd}")

vlan_id = 10

if vlan_id == 10:
    print("VLAN domyślny")
else:
    print("VLAN niestandardowy")   