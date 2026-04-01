# Alexandra (Allie) Evan
Security Engineer • Cloud Security • Threat Detection & AI Integration

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?logo=linkedin)](https://www.linkedin.com/in/allie-evan/)

Virginia Tech alum (B.S. Business Information Technology – Cybersecurity) • WiCyS Member  
PwC – Digital Assurance & Transparency Associate • Arlington, VA

---

## Featured Projects

| Project | Description |
| --- | --- |
| [GitLab CI/CD → EC2 (Dockerized Python App)](https://github.com/alevan22/alevan22/tree/main/Projects/GitLab-CI-CD-Pipeline-Python-App) | Pipeline with test → build → deploy: dockerizes the app, pushes to Docker Hub, then deploys to Ubuntu EC2 using masked CI variables and branch rules. |
| **Elastic SIEM + Tines: Automated Alert Triage & Email Summaries** *(WIP link)* | Deployed Elastic Agent on a Windows host in AWS, authored detections, and integrated Elastic → Tines to enrich alerts and email AI-generated incident summaries. |
| [Secure Inter-VPC Networking & Zero-Trust APIs (VPC Peering + Cognito + API Gateway + WAF)](https://github.com/alevan22/alevan22/tree/main/Projects/Secure%20Inter%E2%80%91VPC%20Networking%20%26%20Zero%E2%80%91Trust%20APIs%20(VPC%20Peering%20%2B%20Cognito%20%2B%20API%20Gateway%20%2B%20WAF)) | Designed inter-VPC connectivity (peering, route tables, SG/NACL) and a token-enforced API plane using Cognito JWT authorizer on API Gateway (optional WAF). Includes hosted-UI login, token tests, and SSM-only admin access (no inbound SSH). |
| [AWS CloudFormation Drift Detection & Auto-Remediation](https://github.com/alevan22/alevan22/tree/main/Projects/AWS%20CloudFormation%20Drift%20Detection%20%26%20Auto-Remediation) | Scheduled EventBridge → Lambda workflow that runs `DetectStackDrift`, identifies drifted resources, and restores them to the template state. Versioned templates in S3, least-privilege IAM, and auditable logs. |
| [High-Availability OPNsense Firewall (CARP + pfSync) + Suricata IDS](https://github.com/alevan22/alevan22/tree/main/Projects/High%20Availability%20Firewall%20Lab%20with%20OPNsense) | Built a redundant OPNsense pair with virtual IP failover; tuned 50+ Suricata rules for port scans and malware while maintaining application availability. |
| [Penetration Test: Humbleify Web App](https://github.com/alevan22/alevan22/blob/main/Projects/Humbleify%20Penetration%20Test/README.md) | Identified XSS and access-control issues; validated with Burp, Nessus, and Metasploit; risk-rated findings and proposed fixes. |

---

## Skills & Focus Areas

| Area | Tools / Experience |
| --- | --- |
| Cloud Security | AWS IAM, KMS, S3, CloudTrail, CloudFormation, Lambda, EventBridge, Cognito, API Gateway, WAF |
| Network Security | VPC design, VPC Peering, SG/NACL hardening, Route 53 (DNS fundamentals), SSM Session Manager (keyless access) |
| Security Engineering | OPNsense, Suricata, Nessus, Elastic Security (SIEM), detection tuning, log pipelines |
| Automation & DevSecOps | GitLab CI/CD, Docker, Python, Bash, Power Automate |
| Threat Detection & IR | MITRE ATT&CK, alert enrichment, triage workflows (Elastic ↔ Tines), basic playbook automation |
| Risk & Compliance | NIST 800-53/171, COBIT, SOX (ITGC/ICFR), audit analytics & reporting |
| Analytics & Reporting | Power BI (DAX), SQL, VBA |

---

## Experience

### PwC – Digital Assurance & Transparency Associate
*Jul 2024 – Present • Washington, DC*

- Helped secure a multimillion-dollar client contract by translating technical remediation plans into executive-aligned proposals.  
- Automated compliance tracking for 250+ controls across 12 apps in 14 regions using Power BI, DAX, and Power Automate, reducing reporting time by ~50%.  
- Supported a $2M+ SOX SDLC remediation program: developed pitch materials, identified security/compliance gaps in DevOps processes, and defined scalable controls.  
- Assessed/validated 25+ IAM, SSO, and network controls across a hybrid cloud migration for 10,000+ users, reducing misconfiguration risk.  
- Collaborated across DevOps, engineering, and compliance teams to implement practical cloud guardrails and close audit findings.

### KPMG – Technology Risk Consulting Intern
*Summer 2023 • Baltimore, MD*

- Performed infrastructure vulnerability assessments across public-cloud deployments using NIST and COBIT; highlighted IAM and network segmentation risks.  
- Partnered with technical and audit teams to communicate control findings and remediation strategies across large financial-services stakeholders.  
- Built VBA automations to streamline project-plan tracking during a major enterprise separation, saving ~20+ hours of manual updates.

---

## Certifications
- CompTIA Security+  
- AWS Certified Cloud Practitioner

---

## Currently Exploring
- CI/CD hardening and secure deployments on AWS (GitLab → EC2)  
- SIEM + SOAR-lite automations (Elastic detections, Tines enrichment, auto-summaries)  
- Infrastructure-as-Code security patterns (CloudFormation/Terraform), API auth patterns, and WAF managed rules

---

Thanks for visiting—feel free to connect or explore the hands-on projects above.



