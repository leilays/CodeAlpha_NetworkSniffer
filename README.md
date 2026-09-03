# CodeAlpha_NetworkSniffer

##  Project Overview
This project is developed as a part of the **CodeAlpha Cybersecurity Internship Program**. The goal of this task is to build a basic network packet sniffer using Python to capture, filter, and analyze live network traffic.

---

##  Features
- **Live Packet Capture:** Captures network packets in real-time using the `Scapy` library[cite: 1].
- **Protocol & Port Filtering:** Differentiates between TCP and UDP protocols, extracting source/destination IPs and port numbers.
- **Privacy-Safe Monitoring:** Focuses only on network headers (IPs and ports) without exposing sensitive or private payload data.

---

## Prerequisites & Installation
Make sure you have Python 3 and Scapy installed in your environment (recommended: Kali Linux / Ubuntu).

1. Clone the repository:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/CodeAlpha_NetworkSniffer.git](https://github.com/YOUR_USERNAME/CodeAlpha_NetworkSniffer.git)
   cd CodeAlpha_NetworkSniffer
