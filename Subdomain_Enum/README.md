# Subdomain Scanner

## About

I created this project to learn more about web reconnaissance and how security professionals discover publicly accessible subdomains during security assessments.

The script uses a wordlist of common subdomains and attempts to connect to each one. When a valid response is received, the subdomain is considered active and can be recorded for further analysis.

## What I Learned

Building this project helped me understand:

* Subdomain enumeration techniques
* Web reconnaissance methodologies
* HTTP requests using Python
* Wordlist-based discovery
* Automation for security assessments
* Information gathering during penetration testing

## Features

* Wordlist-based subdomain discovery
* Automated HTTP/HTTPS requests
* Detection of active subdomains
* Stores discovered hosts for later analysis
* Simple and lightweight Python implementation

## Requirements

* Python 3
* Requests library
* A subdomain wordlist (e.g., SecLists)

Install the required package:

```bash id="f0a5zj"
pip install requests
```

## How It Works

1. Loads a list of common subdomain names from a wordlist.
2. Appends each entry to the target domain.
3. Sends an HTTP/HTTPS request to the generated hostname.
4. Identifies active subdomains based on successful responses.
5. Saves discovered hosts for future investigation.

## Why This Project Exists

Subdomain enumeration is a common reconnaissance technique used during security assessments and bug bounty engagements. Understanding how these tools work helps security professionals identify exposed assets, improve asset visibility, and strengthen an organization's security posture.

This project was developed as part of my cybersecurity learning journey and demonstrates basic automation, web reconnaissance, and Python scripting skills.

## Disclaimer

This project is intended for educational purposes, cybersecurity research, and authorized security testing only.

Only perform reconnaissance activities against domains and systems that you own or have explicit permission to assess. Unauthorized scanning or enumeration may violate applicable laws, regulations, or organizational policies.

The author is not responsible for any misuse of this software.
