
# Humbleify Penetration Test

## Overview
This repository documents a team-based penetration test conducted on a duplicate Humbleify server in April 2024. The objective was to simulate an internal attacker scenario on an outdated production-like Ubuntu 14.04 host to uncover high-impact vulnerabilities.

---

## Objectives
✅ Enumerate active services and identify exposed attack surface.  
✅ Exploit misconfigurations and weak authentication controls.  
✅ Escalate privileges to root and demonstrate data breach potential.  
✅ Recommend prioritized remediation steps.

---

## Methodology

### 1️⃣ Reconnaissance & Enumeration
- `nmap -sS -sV -T4 <target>` identified:
  - SSH (22), ProFTPD (21), UnrealIRCD (6667), Apache/WebDAV (80), MySQL (3306).
- `enum4linux` & banner grabbing revealed OS & service versions.
- MySQL with no encryption or access control.

### 2️⃣ Initial Access
- Brute-force employee accounts:
  ```bash
  hydra -L users.txt -P passwords.txt ssh://<target>
  ```
  Validated 7 accounts with weak passwords.

### 3️⃣ Exploitation
- Metasploit modules for ProFTPD and UnrealIRCD to gain shell access.
- `davtest` used on misconfigured WebDAV to upload a PHP webshell.

### 4️⃣ Data Exfiltration
- `mysqldump` retrieved PII of ~430,000 customers in plaintext:
  ```bash
  mysqldump -u root -p customerdb > dump.sql
  ```

### 5️⃣ Privilege Escalation
- Identified insecure `sudo` permissions:
  ```bash
  sudo -l
  ```
  Escalated to root via misconfigured cron job.

---

## Key Findings
🚨 Weak employee passwords (common/guessable; MD5 hashing).  
🚨 Legacy backdoor on UnrealIRCD still active.  
🚨 Sensitive PII unencrypted in MySQL database.  
🚨 Insecure `sudo` rules enabling root privilege escalation.

---

## Tools & Techniques
- Recon: Nmap, Enum4linux
- Brute-forcing: Hydra, Hashcat
- Exploitation: Metasploit, davtest
- Privilege escalation: GTFOBins techniques, cron job abuse
- Data exfiltration: mysqldump
- Validation: Wireshark

---

## Full Report
![Humbleify Report Screenshot](https://github.com/alevan22/alevan22/blob/main/Projects/Humbleify%20Penetration%20Test/Humblify%20Penetration%20Test.pdf)

