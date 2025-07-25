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
                   [ Internet (NAT Network) ]
                            |
                   VirtualBox DHCP NAT (10.0.2.0/24)
                            |
          +----------------+----------------+
          |                                 |
 [OPNsense Master]                [OPNsense Backup]
     .251                                 .252
      |                                     |
 [pfSync: 10.0.0.1]               [pfSync: 10.0.0.2]
     | <--- state sync link ---> |
      |                                     |
      +---------------+---------------------+
                      |
                  [LAN Switch]
                      |
                [Windows 10 VM]

---

## ⚙️ Configuration Summary

### 1. 🔁 VM Cloning

- Clone the original OPNsense VM to create a **backup** instance.
- Generate **new MAC addresses** to avoid conflicts.

### 2. 🔧 VirtualBox Network Setup

- Create 3 networks:
  - **WAN (NAT Network)**: 10.0.2.0/24
  - **LAN (Internal)**: 10.200.200.0/24
  - **pfSync (Internal)**: 10.0.0.0/24

Enable **promiscuous mode** on LAN and WAN adapters.

### 3. 🎛️ Interface IP Assignments

| Interface | Master IP         | Backup IP        |
|-----------|-------------------|------------------|
| LAN       | 10.200.200.251    | 10.200.200.252   |
| pfSync    | 10.0.0.1          | 10.0.0.2         |

---

## 🌐 Virtual IPs (CARP)

| Virtual IP (VIP)       | Network | VHID | Used For         | Skew |
|------------------------|---------|------|------------------|------|
| 10.200.200.254         | LAN     | 1    | Default Gateway   | 0 / 100 |
| 10.0.2.254             | WAN     | 2    | Outbound NAT      | 0 / 100 |

> The **lower skew (0)** on the master ensures it takes priority.

---

## 🔄 pfSync & XML-RPC

### 🔌 pfSync (State Replication)
- Dedicated interface between firewalls.
- Allows session state transfer during failover.

### 📦 XML-RPC Sync (Master → Backup)
- Master syncs:
  - Firewall rules
  - NAT settings
  - DHCP leases
  - Users/groups
- Uses admin credentials over pfSync link.

---

## 🔁 Outbound NAT Configuration

Set **Hybrid Outbound NAT** and add a rule:

- Interface: WAN  
- Source: LAN network (10.200.200.0/24)  
- Translation address: `10.0.2.254` (VIP WAN)  

Applied to both master and backup to ensure seamless egress.

---

## 🧪 Testing: Simulated Failover

1. Start pinging:
   - `10.200.200.254` (VIP gateway)
   - `10.200.200.251` (Master)
   - `10.200.200.252` (Backup)

2. Simulate outage by **disconnecting WAN/LAN adapters** on the master.

3. Backup promotes itself as **new master**:
   - VIP `10.200.200.254` responds uninterrupted
   - `CARP` status widget confirms role change

4. Reconnect Master → it resumes **master role** seamlessly.

---

## 🧠 Skills Demonstrated

✅ High Availability Networking  
✅ OPNsense Configuration  
✅ Firewall Rule Management  
✅ Network Redundancy Planning  
✅ pfSync + XML-RPC Integration  
✅ VirtualBox Network Architecture  
✅ NAT & Gateway Failover  
✅ State Table Synchronization

---

## 🔗 Lab Source & Reference

- 📹 **YouTube Tutorial**: [Suricata IDS/IPS & HA Cluster Setup in OPNsense](https://www.youtube.com/watch?v=-fR3ULmaM-c&t=409s)  
- 📘 Inspired by: *Morgan Maxwell Real Estate* virtual lab series  

---



