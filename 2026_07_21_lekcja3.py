#definicja funkcji, intrukcja warunkowa, podejmowanie decyzji
def opisz_vlan(vlan_id):
    if vlan_id == 20:
        return "VLAN domyślny"
    else:
        return "VLAN niestandardowy"

#zmienne, porty
vlan = [10, 20, 30]

#pętla for
for i in vlan:
    print(opisz_vlan(i))