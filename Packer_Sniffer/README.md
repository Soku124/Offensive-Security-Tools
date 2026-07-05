# HTTP Packet Sniffer

## About

I created this project while learning about network traffic analysis and packet inspection. The goal was to understand how data travels across a network and why transmitting sensitive information over unencrypted protocols can be dangerous.

This tool uses Python and Scapy to capture HTTP traffic on a network interface and display the requested URLs. It also looks for common login-related keywords in HTTP requests to demonstrate how credentials and other sensitive information may be exposed when communication is not encrypted.

## What I Learned

Building this project helped me gain practical experience with:

* Network packet sniffing
* HTTP protocol fundamentals
* Packet analysis using Scapy
* Traffic monitoring techniques
* How unencrypted communications can expose sensitive data
* Basic network security and defensive concepts

## Features

* Captures network traffic from a specified interface
* Detects and displays HTTP requests
* Extracts requested URLs
* Identifies common login-related keywords in HTTP traffic
* Demonstrates the risks of transmitting data without encryption

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
sudo python packet_sniffer.py
```

Make sure the correct network interface is specified in the code before execution.

Example output:

```text
[+] HTTP Request >> example.com/login

[+] Possible username/password > username=admin&password=test123
```

## Why This Project Exists

The purpose of this project is to better understand how packet sniffing works and why secure communication protocols such as HTTPS are important. By observing HTTP traffic in a controlled environment, it becomes easier to understand how attackers may gather information and how security professionals can identify and mitigate such risks.

This project is part of my cybersecurity learning journey and helped me develop a deeper understanding of network traffic analysis and protocol security.

## Disclaimer

This project was created for educational purposes, cybersecurity research, and authorized security testing only.

It should only be used in lab environments or on networks where you have explicit permission to monitor traffic. Capturing or inspecting network traffic without authorization may be illegal and unethical.

The author does not support or encourage unauthorized monitoring, interception, or collection of data and is not responsible for any misuse of this software.
