"""
traffic_visualization.py

This script generates visualizations of the analyzed network traffic using Matplotlib. The visualizations include:
- The frequency of C&C requests over time
- The size of packets exchanged between bots and the C2 server
- The overall traffic volume over time

The generated graphs will be saved in the /results/ directory for further analysis and documentation.
"""

import pandas as pd
import matplotlib.pyplot as plt
import os

# Ensure the /results directory exists
os.makedirs('../results', exist_ok=True)

# Load the extracted data from CSV files
packet_sizes = pd.read_csv('extracted_packet_sizes.csv')
communication_freq = pd.read_csv('extracted_communication_frequency.csv')
traffic_volume = pd.read_csv('extracted_traffic_volume.csv')

def plot_packet_sizes(df):
    """
    Plot the distribution of packet sizes.
    
    Args:
    df (DataFrame): Data containing packet sizes
    """
    plt.figure(figsize=(10, 6))
    plt.hist(df['packet_size'], bins=20, color='blue', edgecolor='black')
    plt.title('Packet Size Distribution')
    plt.xlabel('Packet Size (bytes)')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.savefig('../results/packet_size_distribution.png')
    plt.show()

def plot_communication_frequency(df):
    """
    Plot the communication frequency between bots and the C2 server.
    
    Args:
    df (DataFrame): Data containing communication frequency
    """
    plt.figure(figsize=(10, 6))
    plt.bar(df['bot_ip'], df['communication_count'], color='green')
    plt.title('Communication Frequency Between Bots and C2 Server')
    plt.xlabel('Bot IP')
    plt.ylabel('Number of Communications')
    plt.grid(True)
    plt.savefig('../results/cnc_request_frequency.png')
    plt.show()

def plot_traffic_volume(df):
    """
    Plot the total traffic volume over time.
    
    Args:
    df (DataFrame): Data containing traffic volume over time
    """
    plt.figure(figsize=(10, 6))
    plt.plot(df['timestamp'], df['packet_size'], marker='o', color='red')
    plt.title('Traffic Volume Over Time')
    plt.xlabel('Timestamp')
    plt.ylabel('Total Packet Size (bytes)')
    plt.grid(True)
    plt.savefig('../results/traffic_volume_over_time.png')
    plt.show()

if __name__ == "__main__":
    # Plot 1: Packet Size Distribution
    plot_packet_sizes(packet_sizes)

    # Plot 2: Communication Frequency Between Bots and C2 Server
    plot_communication_frequency(communication_freq)

    # Plot 3: Traffic Volume Over Time
    plot_traffic_volume(traffic_volume)

