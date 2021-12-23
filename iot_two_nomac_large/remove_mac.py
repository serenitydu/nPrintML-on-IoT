from scapy.all import *
import os

dir = 'pcaps'
for pcap in os.listdir(dir):
    pcap_path = os.path.join(dir, pcap)
    # print(pcap_path)
    pcap_file = rdpcap(pcap_path)
    for packet in pcap_file:
        packet[Ether].src = '00:00:00:00:00:00'
        packet[Ether].dst = '00:00:00:00:00:00'
        # print(packet[Ether].src)
    wrpcap(pcap_path, pcap_file)