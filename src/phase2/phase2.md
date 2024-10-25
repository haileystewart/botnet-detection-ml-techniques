# Phase 2: Network Traffic Analysis

## Overview
In Phase 2, the goal is to analyze the simulated botnet traffic from Phase 1 and extract key patterns that can be used to improve botnet detection methods.

### Key Tasks:
1. **Pre-process the Captured Traffic (traffic_analysis.py)**:
   - Use the Wireshark-captured network traffic from Phase 1 as the input.
   - Extract key features such as:
     - Packet size
     - Protocol type
     - Time intervals between packets
     - Frequency of C&C requests

2. **Feature Extraction (feature_extraction.py)**:
   - Process the data to identify key traffic features like:
     - Packet size distribution
     - Communication frequency between the bots and C2 server
     - Traffic volume (data transferred over time)
   - These features will help in analyzing the botnet's activity patterns.

3. **Traffic Pattern Identification and Visualization (traffic_visualization.py)**:
   - Use the extracted features to identify botnet traffic patterns.
   - Visualize these patterns with **Matplotlib** and save the graphs in the `/results/` directory.
   - Graphs will show:
     - Frequency of C&C requests
     - Packet sizes and overall traffic volume over time

### Expected Deliverables:
- **traffic_analysis.py**: Script for parsing and pre-processing the traffic data.
- **feature_extraction.py**: Script for extracting meaningful traffic features.
- **traffic_visualization.py**: Script for visualizing the traffic patterns.
- **Traffic graphs**: Stored in `/results/` as `.png` files.

### How to Run the Scripts:
1. **Step 1**: Run `traffic_analysis.py` to process the raw Wireshark data and extract relevant features.
2. **Step 2**: Run `feature_extraction.py` to analyze the traffic data for packet size, protocol types, and frequency of communication.
3. **Step 3**: Run `traffic_visualization.py` to generate visual representations of the data (graphs) and save them in `/results/`.

---
