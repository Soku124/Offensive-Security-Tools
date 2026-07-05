# ARP Spoofer

## About

I created this project while learning about network security and Man-in-the-Middle (MITM) attacks. The purpose of this tool is to understand how ARP spoofing works, how attackers can manipulate network traffic, and most importantly, how defenders can detect and prevent such attacks.

The script uses Python and Scapy to perform ARP poisoning between two devices on a local network by sending forged ARP responses. This causes the target devices to associate the attacker's MAC address with another device's IP address, allowing traffic to be redirected through the attacker's machine.

## What I Learned

Through this project, I gained hands-on experience with:

* The ARP (Address Resolution Protocol)
* MAC and IP address resolution
* Packet crafting using Scapy
* Network traffic redirection concepts
* Man-in-the-Middle attack techniques
* Network security weaknesses and defenses

## Features

* Automatically discovers target MAC addresses
* Crafts and sends spoofed ARP packets
* Performs continuous ARP poisoning
* Displays the number of packets sent in real time
* Lightweight and built entirely in Python

## Requirements

* Python 3
* Scapy

Install Scapy:

```bash
pip install scapy
```

## Running the Script

Run the script with administrator/root privileges:

```bash
sudo python arp_spoofer.py
```

Stop execution at any time using:

```bash
CTRL + C
```

## Why This Project Exists

The goal of this project is not to attack networks but to understand how these attacks work in practice. Studying offensive techniques helps security professionals build stronger defenses, recognize suspicious network activity, and better protect systems from real-world threats.

This repository is part of my cybersecurity learning journey and serves as a practical demonstration of networking and security concepts.

## Disclaimer

This project was created for educational purposes, cybersecurity research, and authorized security testing only.

Please use it responsibly and only in lab environments or on systems where you have explicit permission to perform security testing. Unauthorized use of this software may be illegal and unethical.

I am not responsible for any misuse of this project.
