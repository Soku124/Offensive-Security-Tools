# Network Scanner

## About

I built this project to learn how devices communicate on a local network and how security professionals discover active hosts during network assessments. This scanner uses Python and Scapy to perform ARP-based host discovery, allowing it to identify devices that are currently active on a network segment.

The script sends ARP requests across a specified IP address or IP range and collects responses from devices that are online. It then displays the IP and MAC addresses of the discovered hosts.

## What I Learned

Working on this project helped me better understand:

* Network discovery techniques
* ARP (Address Resolution Protocol)
* Ethernet and Layer 2 communication
* Packet crafting and analysis with Scapy
* Host enumeration during security assessments
* Basic network reconnaissance concepts

## Features

* Scan a single IP address or an entire subnet
* Discover active hosts on the local network
* Retrieve IP and MAC addresses of responding devices
* Fast and lightweight implementation using Scapy
* Command-line interface with target selection

## Requirements

* Python 3
* Scapy

Install Scapy:

```bash
pip install scapy
```

## Usage

Scan a single host:

```bash
python network_scanner.py -t 192.168.1.1
```

Scan an entire subnet:

```bash
python network_scanner.py -t 192.168.1.0/24
```

Example output:

```text
IP                              MAC Address
------------------------------------------------------------

192.168.1.1                     aa:bb:cc:dd:ee:ff
192.168.1.5                     11:22:33:44:55:66
192.168.1.10                    77:88:99:aa:bb:cc
```

## Why This Project Exists

Host discovery is one of the first steps in network administration and security testing. I created this project to gain practical experience with network reconnaissance and to better understand how security professionals identify devices connected to a network.

This project is part of my cybersecurity learning journey and demonstrates my understanding of networking fundamentals, packet manipulation, and Python-based security tool development.

## Disclaimer

This project was created for educational purposes, cybersecurity research, and authorized security testing only.

Only scan networks and systems that you own or have explicit permission to assess. Unauthorized network scanning may violate organizational policies or applicable laws.

The author is not responsible for any misuse of this software.
