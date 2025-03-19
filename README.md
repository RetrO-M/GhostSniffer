<p align='center'>
  <b>GhostSniffer</b><br>  
  <a href="https://github.com/RetrO-M">Github</a> |
  <a href="https://github.com/RetrO-M/GhostSniffer/issues">Report Bug</a> |
  <a href="https://x.com/DeAn0nim0us">Twitter</a>
</p>

This script uses Scapy to capture network packets from a specified interface and extract HTTP request information, as well as potential credentials (such as usernames and passwords) sent in clear text over the network.

The script operates interactively and displays requested URLs along with any possible login credentials, including source and destination IP addresses.

## Donate
**Monero** : `455RrwkuryVRioADddHWfGXrWHSLk4n1DHX36E4tKkBHScps4CeFwMWVemyqgWkL5eYf5L2zRVkgQB4Y9dwaechDKqQzC7p`

## Setup

### Setup GhostSniffer

1. **Download** : `git clone https://github.com/RetrO-M/GhostSniffer` & `cd GhostSniffer`
2. **Setup** : `bash setup.sh`

### Install modules

```sh
pip install scapy
pip install colorama
```

## Features
- **HTTP Packet Capture**: `The script captures HTTP packets and extracts the requested URLs.`
- **Credential Identification**: `If any sensitive information (such as usernames and passwords) is sent in clear text, it will be displayed.`
- **Source and Destination IPs**: `The tool displays the source and destination IP addresses of captured requests.`
- **HTTPS Packet Display**: `Indicates encrypted HTTPS connections (without decrypted content).`
- **Interactive Display**: `Formats results using Colorama for better readability.`

## Usage

### Running the Script
To use the script, specify the network interface to monitor. For example, to monitor the Wi-Fi interface, run the following command: `python main.py -i Wi-Fi`

### Arguments
`-i`, `--interface`: The name of the network interface to use (e.g., `Wi-Fi`, `eth0`, etc.)

### Sample output

```cs
HTTPS  192.168.1.1 → 127.0.0.1
HTTP  testphp.vulnweb.com/userinfo.php  192.168.1.1 → 127.0.0.1
testphp.vulnweb.com/userinfo.php  username=test&password=test → login=test%2Ftest
```

```cs
'username', 'uname', 'user', 'login', 'password', 'pass', 'signin',
'signup', 'name', 'email', 'phone', 'uid', 'passw', 'passContainer'
```

## Legal Disclaimer
- This tool is provided for educational purposes only. Using this tool to intercept network packets without authorization is illegal. You must obtain explicit permission from network owners before running this script.

- If you are a minor, please consult an adult before using this tool.

## Disclaimer
- **Warning**: 
  - This tool is intended for educational use and testing in a controlled environment. Using this tool to capture or eavesdrop on information without explicit consent is illegal. You must obtain permission before using this tool on any network that is not your own.
  The author is not responsible for any misuse of this tool. If you are a minor, you should consult an adult before using this tool. It is your responsibility to comply with all relevant laws and regulations regarding cybersecurity in your country.

- **IMPORTANT**: 
  - If this tool is used for illegal activities, I reserve the right to remove the repository at any time without notice.
