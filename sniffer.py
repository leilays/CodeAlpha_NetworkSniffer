from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP

def packet_callback(packet):
    if packet.haslayer(IP):
        ip_layer = packet[IP]
        src_ip = ip_layer.src
        dst_ip = ip_layer.dst
        proto = ip_layer.proto

        print(f"[+] Packet: {src_ip} ---> {dst_ip} | Protocol: {proto}")

        if packet.haslayer(TCP) or packet.haslayer(UDP):
            try:
                payload = bytes(packet.payload)
                if payload:
                    print(f"    Payload: {payload[:50]}...")
            except Exception:
                pass

print("[*] Starting network sniffer... Press Ctrl+C to stop.")
sniff(prn=packet_callback, store=False)
