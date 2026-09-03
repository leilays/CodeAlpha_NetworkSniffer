from scapy.all import sniff, conf
from scapy.layers.inet import IP, TCP, UDP

print(f"[*] Active Interface: {conf.iface}")
print("[*] Sniffing network traffic (Press Ctrl+C to stop)...\n")

def packet_callback(packet):
    if packet.haslayer(IP):
        ip_layer = packet[IP]
        src_ip = ip_layer.src
        dst_ip = ip_layer.dst
        
        if packet.haslayer(TCP):
            proto = "TCP"
            sport = packet[TCP].sport
            dport = packet[TCP].dport
            print(f"[TCP] {src_ip}:{sport} ---> {dst_ip}:{dport}")
            
        elif packet.haslayer(UDP):
            proto = "UDP"
            sport = packet[UDP].sport
            dport = packet[UDP].dport
            print(f"[UDP] {src_ip}:{sport} ---> {dst_ip}:{dport}")
            
        else:
            print(f"[IP]  {src_ip} ---> {dst_ip} | Protocol: {ip_layer.proto}")

sniff(iface=conf.iface, prn=packet_callback, store=False)
