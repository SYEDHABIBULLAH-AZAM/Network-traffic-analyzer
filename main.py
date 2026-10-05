import pandas as pd
import matplotlib.pyplot as plt
from scapy.all import rdpcap, IP

def analyze_network_traffic(pcap_file):
    print("[*] Reading PCAP file...")
    try:
        packets = rdpcap(pcap_file)
    except FileNotFoundError:
        print(f"[Error] File '{pcap_file}' nahi mili! Check karein ki file folder me hai ya nahi.")
        return

    print(f"[+] Total Packets Captured: {len(packets)}")
    
    packet_data = []
    THRESHOLD_SIZE = 50000  # Exfiltration alert limit (in bytes)
    
    print("\n--- Analyzing Packets & Checking Exfiltration ---")
    for pkt in packets:
        if IP in pkt:
            src_ip = pkt[IP].src
            dst_ip = pkt[IP].dst
            proto = pkt[IP].proto
            pkt_size = len(pkt)
            
            packet_data.append({"Source": src_ip, "Destination": dst_ip, "Protocol": proto, "Size": pkt_size})
            
            # Exfiltration Detection Logic (Unusually large packets)
            if pkt_size > THRESHOLD_SIZE:
                print(f"[ALERT] Potential Data Exfiltration! Size: {pkt_size} bytes from {src_ip} to {dst_ip}")

    # Convert to Pandas DataFrame for analysis
    df = pd.DataFrame(packet_data)
    
    if not df.empty:
        print("\n--- Protocol Summary ---")
        proto_counts = df['Protocol'].value_counts()
        print(proto_counts)
        
        # Traffic Visualization using Matplotlib
        print("\n[*] Generating Traffic Pattern Visualization Graph...")
        plt.figure(figsize=(8, 5))
        proto_counts.plot(kind='bar', color='teal', edgecolor='black')
        plt.title('Network Traffic Protocol Distribution')
        plt.xlabel('Protocol ID')
        plt.ylabel('Packet Count')
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.show()
    else:
        print("[-] No IP packets found in the capture file.")

if __name__ == "__main__":
    analyze_network_traffic("network_traffic.pcapng")