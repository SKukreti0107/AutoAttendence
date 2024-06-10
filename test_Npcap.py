from scapy.all import ARP, Ether, srp

def get_mac_addresses(ip_range):
    arp = ARP(pdst=ip_range)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether / arp
    result = srp(packet, timeout=3, verbose=False)[0]
    
    devices = []
    for sent, received in result:
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})
    
    return devices


ip_range = "192.168.21.0/24"  
devices = get_mac_addresses(ip_range)
for device in devices:
    print("IP Address:", device['ip'], "MAC Address:", device['mac'])
