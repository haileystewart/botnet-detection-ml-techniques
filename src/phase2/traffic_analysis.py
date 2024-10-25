"""
traffic_analysis.py

This script is responsible for pre-processing the Wireshark-captured network traffic. It will:
- Parse the captured traffic to extract key features, such as:
    - Packet size
    - Protocol type
    - Time intervals between packets
    - Frequency of C&C requests
- These features will help quantify the traffic and identify patterns that could indicate botnet activity.
"""

import pandas as pd
from scapy.all import *
import os
from datetime import datetime

# Ensure the /processed_data directory exists
os.makedirs('../processed_data', exist_ok=True)

# Path to the PCAP file captured by Wireshark
pcap_file = 'botnet_traffic.pcap'

def parse_pcap(file):
    """
    Parse the PCAP file and extract key features for analysis.

    Args:
    file (str): Path to the PCAP file

    Returns:
    DataFrame: Parsed network traffic data containing key features
    """
    packets = rdpcap(file)
    
    data = []
    
    for packet in packets:
        # Extract relevant fields only if the packet has an IP layer and TCP/UDP
        if IP in packet and (TCP in packet or UDP in packet):
            # Extract packet details
            timestamp = packet.time
            src_ip = packet[IP].src
            dst_ip = packet[IP].dst
            protocol = packet.sprintf("%IP.proto%")  # Either 'TCP' or 'UDP'
            packet_size = len(packet)
            
            # Extract time in readable format
            readable_time = datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
            
            # Create a dictionary for each packet
            data.append({
                'timestamp': readable_time,
                'src_ip': src_ip,
                'dst_ip': dst_ip,
                'protocol': protocol,
                'packet_size': packet_size
            })
    
    # Create a DataFrame to store the parsed data
    traffic_df = pd.DataFrame(data)
    
    return traffic_df

def calculate_time_intervals(df):
    """
    Calculate the time intervals between packets.

    Args:
    df (DataFrame): Parsed traffic data

    Returns:
    DataFrame: Traffic data with time intervals added
    """
    df['timestamp'] = pd.to_datetime(df['timestamp'])  # Ensure timestamps are in datetime format
    df['time_interval'] = df['timestamp'].diff().dt.total_seconds().fillna(0)  # Calculate intervals in seconds
    return df

def filter_cnc_traffic(df, c2_server_ip):
    """
    Filter traffic related to the Command & Control (C&C) server.

    Args:
    df (DataFrame): Parsed traffic data
    c2_server_ip (str): IP address of the C&C server

    Returns:
    DataFrame: Filtered traffic containing only C&C-related packets
    """
    return df[(df['src_ip'] == c2_server_ip) | (df['dst_ip'] == c2_server_ip)]

if __name__ == "__main__":
    # Step 1: Parse the pcap file and extract traffic details
    parsed_traffic = parse_pcap(pcap_file)
    
    # Step 2: Calculate time intervals between packets
    parsed_traffic_with_intervals = calculate_time_intervals(parsed_traffic)
    
    # Step 3: Filter for C&C server traffic (replace with actual C2 server IP)
    c2_server_ip = "192.168.1.100"
    cnc_traffic = filter_cnc_traffic(parsed_traffic_with_intervals, c2_server_ip)
    
    # Print some example rows for review
    print(cnc_traffic.head())
    
    # Step 4: Save the pre-processed data to CSV for further analysis
    cnc_traffic.to_csv('../processed_data/processed_traffic_data.csv', index=False)

