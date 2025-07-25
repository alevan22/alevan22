# 🛡️ High Availability Firewall Cluster with OPNsense

## 📖 Overview

This lab demonstrates how to build a **redundant firewall cluster using OPNsense**, simulating a **production-grade high availability (HA)** setup. The goal is to ensure uninterrupted network connectivity using automatic failover between a **master** and **backup** firewall instance, powered by:

- CARP (Common Address Redundancy Protocol)
- pfSync (state replication)
- XML-RPC (configuration sync)

> 🔁 *Failover occurs seamlessly with zero impact to LAN clients.*

---

## 🧰 Tools & Technologies

- **OPNsense Firewall (x2)**
- **VirtualBox** (VM host + network simulation)
- **Kali Linux & Windows 10 VMs** (testing)
- Protocols:
  - CARP (shared virtual IPs)
  - pfSync (state table sync)
  - XML-RPC (config sync)
- DHCP / NAT Simulation
- Interfaces: WAN, LAN, pfSync

---

## 🧪 Network Architecture


