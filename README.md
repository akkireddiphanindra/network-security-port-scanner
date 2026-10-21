
```text
╔══════════════════════════════════════════════════════════════════════════════╗
║  PHANINDRA@CYBERLAB  /  NETWORK SECURITY TOOLKIT                              ║
╠══════════════════════════════════════════════════════════════════════════════╣
║                                                                              ║
║   ██████╗  ██████╗ ██████╗ ████████╗                                        ║
║   ██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝                                        ║
║   ██████╔╝██║   ██║██████╔╝   ██║                                           ║
║   ██╔═══╝ ██║   ██║██╔══██╗   ██║                                           ║
║   ██║     ╚██████╔╝██║  ██║   ██║                                           ║
║   ╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝                                           ║
║                                                                              ║
║   >>> TCP PORT SCANNER                                                      ║
║   Scan authorized private IPv4 targets | Validate ports | Export CSV        ║
║                                                                              ║
╠══════════════════════════════════════════════════════════════════════════════╣
║  PROTOCOL : TCP          OUTPUT : CSV REPORT          STATUS : READY         ║
║  SECURITY : AUTHORIZED TESTING ONLY                                          ║
╚══════════════════════════════════════════════════════════════════════════════╝
```

<img width="1536" height="1024" alt="Neon TCP Port Scanner Terminal" src="https://github.com/user-attachments/assets/505dfb8d-b1df-471a-861e-2fb9d34239d4" />


# Network Security TCP Port Scanner

A Python-based network security project for assessing TCP port exposure on authorized IPv4 targets. It demonstrates socket programming, input validation, connection timeouts, and CSV reporting.

## Features

- Configurable TCP ports and port ranges
- Connection timeout handling
- Open, closed, and filtered/unknown result classification
- Input validation and error handling
- CSV scan report generation
- Automated unit tests for port parsing

## Technology Stack

- Python 3.9+
- TCP/IP and socket programming
- CSV reporting
- Python unittest

## Project Structure

```text
network-security-port-scanner/
├── port_scanner.py
├── tests/
│   └── test_port_scanner.py
├── reports/
├── README.md
├── requirements.txt
└── .gitignore
```

## Setup

Clone the repository:

```bash
git clone https://github.com/akkireddiphanindra/network-security-port-scanner.git
cd network-security-port-scanner
```

No third-party dependencies are required for the basic scanner.

## Usage

Scan selected ports on your own computer:

```bash
python port_scanner.py --target 127.0.0.1 --ports 22,80,443
```

Scan a small range on an authorized private network host:

```bash
python port_scanner.py --target 192.168.1.10 --ports 1-100
```

Set a timeout and custom report path:

```bash
python port_scanner.py --target 127.0.0.1 --ports 22,80,443 --timeout 1 --output reports/test.csv
```

Use a target you own or have explicit permission to assess.

## Run Tests

```bash
python -m unittest discover -s tests -v
```

The unit tests cover port-list parsing, range handling, duplicate removal, and invalid input.

## Understanding Results

- **Open:** The TCP connection succeeded.
- **Closed:** The connection was refused.
- **Filtered/unknown:** The result was inconclusive, timed out, or another network error occurred.

These results do not identify vulnerabilities by themselves.

## Limitations

This is a learning project for IPv4 TCP scanning. It does not perform UDP scanning, vulnerability exploitation, stealth scanning, or comprehensive service detection.

## Responsible Use

Only scan systems you own or are authorized to test. Follow applicable laws and organizational security policies.

## Future Enhancements

- Additional automated tests for network results
- JSON report export
- Service identification
- A web-based results viewer

## Author

Akkireddi Phanindra

GitHub: https://github.com/akkireddiphanindra
