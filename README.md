# 🛡️ Network Traffic Analyzer with Python & Wireshark

A robust cybersecurity and network traffic analysis tool built from scratch using Python. This application parses network packet captures (`.pcap`), analyzes protocol distributions, and automatically flags potential data exfiltration attempts based on customizable packet size thresholds.

---

## 🚀 Key Features & Capabilities
- **Packet Parsing & Capture:** Integrates seamlessly with Wireshark for raw traffic capture and uses Scapy for deep packet inspection.
- **Exfiltration Detection:** Automatically scans packet payloads and flags unusually large data transfers that exceed defined byte thresholds.
- **Data Structuring:** Leverages Pandas DataFrames to organize, clean, and summarize complex network protocols.
- **Data Visualization:** Generates clean, graphical representations of protocol distributions using Matplotlib to help visualize network behavior instantly.

---

## 🛠️ Tech Stack & Libraries Used
- **Language:** Python 3.14
- **Traffic Capture Tool:** Wireshark
- **Core Python Libraries:**
  - `scapy` (For packet manipulation, reading `.pcap` files, and inspecting network layers)
  - `pandas` (For handling tabular network data and statistical summaries)
  - `matplotlib` (For plotting real-time graphical charts of protocol distribution)

---

## ⚙️ Step-by-Step Installation & Usage

Follow these steps to set up and run the project locally on your machine:

1. **Clone the Repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/Network-traffic-analyzer.git](https://github.com/YOUR_USERNAME/Network-traffic-analyzer.git)
   cd Network-traffic-analyzer