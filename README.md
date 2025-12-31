# air-wifi

A Python tool for performing Wi-Fi deauthentication attacks by simply entering the BSSID and CH.  
`air-wifi` automatically finds the target's BSSID and channel using `airodump-ng`, sets the correct channel, and launches an infinite deauth attack using `aireplay-ng`.

> ⚠️ For **educational and authorized testing** only.

---

## Features

- Lists available wireless interfaces
- Enables monitor mode via `airmon-ng`
- Scans for nearby Wi-Fi networks using `airodump-ng`
- Automatically finds the BSSID and channel based on SSID
- Retries if SSID not found
- Sets channel on monitor interface
- Launches an infinite deauth attack using `aireplay-ng`

---

## Requirements

- Python 3.x
- Linux (tested on Ubuntu)
- `aircrack-ng` suite:
  - `airodump-ng`
  - `airmon-ng`
  - `aireplay-ng`

---

## Installation

Install dependencies:

```bash
sudo apt update
sudo apt install aircrack-ng
```
#Author 
SIMON