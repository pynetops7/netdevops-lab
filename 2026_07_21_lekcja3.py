def opisz_vlan(vlan_id):
    if vlan_id == 20:
        return "VLAN domyślny"
    else:
        return "VLAN niestandardowy"

vlan = [10, 20, 30]

for i in vlan:
    print(opisz_vlan(i))