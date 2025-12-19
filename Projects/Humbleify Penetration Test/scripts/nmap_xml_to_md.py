#!/usr/bin/env python3
"""Convert Nmap XML output to a Markdown port/service table.

This is intended for *authorized* reporting workflows.
It does not perform scanning; it only parses an existing Nmap XML file.

Usage:
  python3 scripts/nmap_xml_to_md.py artifacts/nmap/scan.xml
"""

import sys
import xml.etree.ElementTree as ET

def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: nmap_xml_to_md.py <scan.xml>", file=sys.stderr)
        return 2

    xml_path = sys.argv[1]
    tree = ET.parse(xml_path)
    root = tree.getroot()

    rows = []
    for host in root.findall("host"):
        status = host.find("status")
        if status is not None and status.get("state") != "up":
            continue

        ports = host.find("ports")
        if ports is None:
            continue

        for port in ports.findall("port"):
            proto = port.get("protocol", "")
            portid = port.get("portid", "")
            state_el = port.find("state")
            state = state_el.get("state", "") if state_el is not None else ""
            if state != "open":
                continue

            service_el = port.find("service")
            name = service_el.get("name", "") if service_el is not None else ""
            product = service_el.get("product", "") if service_el is not None else ""
            version = service_el.get("version", "") if service_el is not None else ""
            extrainfo = service_el.get("extrainfo", "") if service_el is not None else ""

            banner = " ".join([x for x in [product, version] if x]).strip()
            rows.append((int(portid), proto, name, banner, extrainfo))

    rows.sort(key=lambda r: r[0])

    print("| Port | Proto | Service | Product/Version | Extra |")
    print("|---:|---|---|---|---|")
    for portid, proto, name, banner, extra in rows:
        banner = banner.replace("|", "\|")
        extra = extra.replace("|", "\|")
        print(f"| {portid} | {proto} | {name} | {banner} | {extra} |")

    return 0

if __name__ == "__main__":
    raise SystemExit(main())
