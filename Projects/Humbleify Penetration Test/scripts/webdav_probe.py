#!/usr/bin/env python3
"""Non-destructive WebDAV capability probe (authorized targets only).

This script performs *read-only* checks:
- OPTIONS to see if WebDAV methods are advertised
- HEAD to validate reachability

It does NOT upload files, create resources, or attempt authentication bypass.

Usage:
  python3 scripts/webdav_probe.py https://example.local/uploads/
"""

import sys
import requests

def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: webdav_probe.py <url>", file=sys.stderr)
        return 2

    url = sys.argv[1].rstrip("/") + "/"

    try:
        head = requests.head(url, timeout=10, allow_redirects=True, verify=False)
        print(f"[HEAD] {head.status_code} {head.url}")
    except Exception as e:
        print(f"[!] HEAD failed: {e}", file=sys.stderr)
        return 1

    try:
        opt = requests.options(url, timeout=10, allow_redirects=True, verify=False)
        allow = opt.headers.get("Allow") or opt.headers.get("allow") or ""
        dav = opt.headers.get("DAV") or opt.headers.get("dav") or ""
        print(f"[OPTIONS] {opt.status_code}")
        if allow:
            print(f"  Allow: {allow}")
        if dav:
            print(f"  DAV: {dav}")
    except Exception as e:
        print(f"[!] OPTIONS failed: {e}", file=sys.stderr)
        return 1

    return 0

if __name__ == "__main__":
    raise SystemExit(main())
