#!/bin/bash

RED='\033[0;31m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m' 

title() {
    clear
    echo -e """${CYAN}
         ▄▄▄▄▄▄▄▄
        ▄████████████
      ▄██   ████▀▀████
  ▐▄ ▐███▄ ▄███▌   ███▌▄██
   █▌████████████▄███████▌
   █████████ ▐██████████▀
     ██████████████████
      ████████████████
       ▀██████████████
         ▀█████████████▄
            ▀▀▀██████████ 
${NC}
${BLUE}Setup - GhostSniffer${NC}

[${CYAN}01${NC}] Install Python modules
[${CYAN}02${NC}] Check and install Python3
[${CYAN}03${NC}] Update system dependencies
[${CYAN}99${NC}] Help
[${CYAN}00${NC}] Exit
    """
}

setup_modules() {
    echo -e "${NC}[${BLUE}*${NC}] Installing Python modules...${NC}"
    pip3 install --upgrade scapy colorama scapy
    echo -e "${NC}[${CYAN}✓${NC}] Modules installed successfully.${NC}"
}

setup_python() {
    if command -v python3 &>/dev/null; then
        echo -e "${NC}[${CYAN}✓${NC}] Python3 is already installed.${NC}"
    else
        echo -e "${NC}[${RED}!${NC}] Python3 is not installed. Installing...${NC}"
        sudo apt update && sudo apt install python3 python3-pip -y
        echo -e "${NC}[${CYAN}✓${NC}] Python3 installed successfully.${NC}"
    fi
}

update_dependencies() {
    echo -e "${NC}[${BLUE}*${NC}] Updating system packages...${NC}"
    sudo apt update && sudo apt upgrade -y
    echo -e "${NC}[${CYAN}✓${NC}] System updated successfully.${NC}"
}

help() {
    echo -e """
${CYAN} █  █  █▀▀▀  █     █▀▀█ 
${NC} █▀▀█  █▀▀▀  █     █▄▄█ 
${CYAN} █  █  █▄▄▄  █▄▄█  █
    """
    echo -e "${NC}[${CYAN}✓${NC}] Command: ${CYAN}'python3 main.py -i <INTERFACE>'"
}

main() {
    while true; do
        title
        read -p "Setup> " choice

        case $choice in
            1) setup_modules ;;
            2) setup_python ;;
            3) update_dependencies ;;
            99) help ;;
            0) echo -e "${NC}[${CYAN}+${NC}] Bye bye...${NC}"; exit 0 ;;
            *) echo -e "${NC}[${RED}X${NC}] Invalid option, try again.${NC}" ;;
        esac

        echo -e "\n${NC}[${CYAN}-${NC}] Press Enter to return to the menu...${NC}"
        read
    done
}

main
