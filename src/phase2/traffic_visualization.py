"""
traffic_visualization.py

This script generates visualizations of the analyzed network traffic using Matplotlib. The visualizations include:
- Packet Size Distribution: Histogram showing the distribution of packet sizes.
- Communication Frequency: Bar chart showing the frequency of communication between bots and the C2 server.
- Traffic Volume Over Time: Line graph showing the total packet size transferred over time.

The generated graphs will be saved in the /results/ directory for further analysis and documentation.
"""

import pandas as pd
import matplotlib.pyplot as plt
import os

# Ensure the /results directory exists
os.makedirs('../results', exist_ok=True)

# Load the CSV files generated from Step 2 using raw strings for the file paths
packet_sizes = pd.read_csv(r'C:\Users\hailey\botnet-detection-ml-techniques\src\processed_data\extracted_packet_sizes.csv')
communication_freq = pd.read_csv(r'C:\Users\hailey\botnet-detection-ml-techniques\src\processed_data\extracted_communication_frequency.csv')
traffic_volume = pd.read_csv(r'C:\Users\hailey\botnet-detection-ml-techniques\src\processed_data\extracted_traffic_volume.csv')

# Step 1: Generate Packet Size Distribution Histogram
def plot_packet_size_distribution(df):
    """
    Plot a histogram showing the distribution of packet sizes.
    
    Args:
    df (DataFrame): DataFrame containing packet size data
    """
    plt.figure(figsize=(8, 6))
    plt.hist(df['packet_size'], bins=10, color='skyblue', edgecolor='black')
    plt.title('Packet Size Distribution')
    plt.xlabel('Packet Size (Bytes)')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.savefig('../results/packet_size_distribution.png')
    plt.close()

# Step 2: Generate Communication Frequency Bar Chart
def plot_communication_frequency(df):
    """
    Plot a bar chart showing the communication frequency between bots and the C2 server.
    
    Args:
    df (DataFrame): DataFrame containing communication frequency data
    """
    plt.figure(figsize=(8, 6))
    plt.bar(df['src_ip'], df['communication_count'], color='salmon')
    plt.title('Communication Frequency Between Bots and C2 Server')
    plt.xlabel('Bot IP Address')
    plt.ylabel('Number of Communications')
    plt.grid(True)
    plt.savefig('../results/cnc_request_frequency.png')
    plt.close()

# Step 3: Generate Traffic Volume Over Time Line Graph
def plot_traffic_volume_over_time(df):
    """
    Plot a line graph showing the traffic volume (packet count) over time.
    
    Args:
    df (DataFrame): DataFrame containing traffic volume data
    """
    plt.figure(figsize=(10, 6))
    plt.plot(df['timestamp'], df['packet_count'], marker='o', linestyle='-', color='purple')
    plt.title('Traffic Volume Over Time')
    plt.xlabel('Time')
    plt.ylabel('Packet Count')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('../results/traffic_volume_over_time.png')
    plt.close()

if __name__ == "__main__":
    # Generate the visualizations
    print("Generating packet size distribution...")
    plot_packet_size_distribution(packet_sizes)
    
    print("Generating communication frequency chart...")
    plot_communication_frequency(communication_freq)
    
    print("Generating traffic volume over time graph...")
    plot_traffic_volume_over_time(traffic_volume)
    
    print("All visualizations have been generated and saved in the /results/ directory.")
