
#!/usr/bin/env python3
"""
Network Security TCP Port Scanner
For authorized security testing only.
"""

import argparse
import csv
import ipaddress
import socket
from datetime import datetime, timezone
from pathlib import Path


def parse_ports(value):
    """Parse ports such as 22,80,443 or 1-100."""
    ports = set()

    try:
        for item in value.split(","):
            item = item.strip()

            if "-" in item:
                start, end = map(int, item.split("-", 1))
                if start > end:
                    raise ValueError
                ports.update(range(start, end + 1))
            else:
                ports.add(int(item))

        if not ports or any(p < 1 or p > 65535 for p in ports):
            raise ValueError

        if len(ports) > 1024:
            raise ValueError("Maximum 1024 ports per scan")

        return sorted(ports)

    except ValueError as exc:
        raise argparse.ArgumentTypeError(
            "Use valid ports, e.g. 22,80,443 or 1-100 "
            "(maximum 1024 distinct ports)."
        ) from exc


def scan_port(host, port, timeout):
    """Return open, closed, or filtered/unknown."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(timeout)
            result = sock.connect_ex((host, port))

            if result == 0:
                return "open"
            if result in (111, 10061, 61):
                return "closed"
            return "filtered/unknown"

    except socket.timeout:
        return "filtered/unknown"
    except OSError:
        return "filtered/unknown"


def main():
    parser = argparse.ArgumentParser(
        description="Scan TCP ports on an authorized target."
    )
    parser.add_argument(
        "--target",
        required=True,
        help="IPv4 address of an authorized target"
    )
    parser.add_argument(
        "--ports",
        type=parse_ports,
        default=parse_ports("22,80,443,445,3389"),
        help="Ports/ranges, e.g. 22,80,443 or 1-100"
    )
    parser.add_argument(
        "--timeout",
        type=float,
        default=0.5,
        help="Connection timeout in seconds (0.1 to 3)"
    )
    parser.add_argument(
        "--output",
        default="reports/scan_report.csv",
        help="CSV report path"
    )
    args = parser.parse_args()

    if not 0.1 <= args.timeout <= 3:
        parser.error("--timeout must be between 0.1 and 3 seconds")

    try:
        target_ip = ipaddress.ip_address(args.target)
        if target_ip.version != 4:
            parser.error("This basic scanner supports IPv4 only")
        host = str(target_ip)
    except ValueError:
        parser.error("Provide a valid IPv4 address")

    # Restrict the example to loopback/private IPv4 addresses.
    if not (target_ip.is_loopback or target_ip.is_private):
        parser.error(
            "For this learning version, use a loopback or private "
            "IPv4 address you are authorized to test."
        )

    print(f"\nTarget: {host}")
    print(f"Ports to check: {len(args.ports)}")
    print("-" * 48)

    rows = []
    for port in args.ports:
        state = scan_port(host, port, args.timeout)
        print(f"TCP {port:5}  {state}")
        rows.append({
            "target": host,
            "port": port,
            "protocol": "TCP",
            "state": state,
            "scanned_at_utc": datetime.now(timezone.utc).isoformat()
        })

    report_path = Path(args.output)
    report_path.parent.mkdir(parents=True, exist_ok=True)

    with report_path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)

    print("-" * 48)
    print(f"Report saved to: {report_path}")


if __name__ == "__main__":
    main()
