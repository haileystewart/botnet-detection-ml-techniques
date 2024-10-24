"""
feature_extraction.py

This script extracts meaningful features from the pre-processed network traffic. The key features to extract include:
- Packet sizes
- Communication frequency between bots and the C2 server
- Traffic volume (number of packets and data transferred over time)

The extracted data will be used in the traffic pattern analysis and visualization stages.
"""

import pandas as pd

# Load the pre-processed data from the correct file path
traffic_data = pd.read_csv('../processed_data/processed_traffic_data.csv')

def extract_packet_sizes(df):
    """
    Extract packet size information from the network traffic data.
    
    Args:
    df (DataFrame): Pre-processed traffic data

    Returns:
    DataFrame: Packet size data for analysis
    """
    packet_sizes = df[['packet_size']]  # Assuming packet size is stored in a column named 'packet_size'
    return packet_sizes

def extract_communication_frequency(df):
    """
    Extract communication frequency between bots and the C2 server.
    
    Args:
    df (DataFrame): Pre-processed traffic data

    Returns:
    DataFrame: Communication frequency data
    """
    communication_freq = df.groupby(['src_ip', 'dst_ip']).size().reset_index(name='communication_count')
    return communication_freq

def extract_traffic_volume(df):
    """
    Extract traffic volume over time (number of packets and data transferred).
    
    Args:
    df (DataFrame): Pre-processed traffic data

    Returns:
    DataFrame: Traffic volume data with timestamps
    """
    # Group by timestamp and aggregate packet sizes and the number of packets
    traffic_volume = df.groupby('timestamp').agg({
        'packet_size': 'sum',   # Sum of packet sizes gives total data transferred at a given time
        'packet_size': 'count'  # Count the number of packets transferred at a given time
    }).rename(columns={'packet_size': 'packet_count'}).reset_index()  # Rename the count column to 'packet_count'
    
    return traffic_volume

if __name__ == "__main__":
    # Step 1: Extract packet size data
    packet_sizes = extract_packet_sizes(traffic_data)
    print("Packet Sizes:\n", packet_sizes.head())

    # Step 2: Extract communication frequency data
    communication_freq = extract_communication_frequency(traffic_data)
    print("\nCommunication Frequency:\n", communication_freq.head())

    # Step 3: Extract traffic volume data
    traffic_volume = extract_traffic_volume(traffic_data)
    print("\nTraffic Volume Over Time:\n", traffic_volume.head())

    # Optional: Save the extracted features to CSV for further analysis
    packet_sizes.to_csv('../processed_data/extracted_packet_sizes.csv', index=False)
    communication_freq.to_csv('../processed_data/extracted_communication_frequency.csv', index=False)
    traffic_volume.to_csv('../processed_data/extracted_traffic_volume.csv', index=False)
