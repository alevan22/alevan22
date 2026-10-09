# Alexandra (Allie) Evan

**Security Engineer | AI & LLM Security | Cloud Security | Threat Detection & Automation**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?logo=linkedin)](https://www.linkedin.com/in/allie-evan/)

- **M.S. Cybersecurity Engineering**, University of San Diego (in progress)
- **B.S. Business Information Technology, Cybersecurity**, Virginia Tech
- **Communities:** WiCyS | Rewriting the Code | Society of Women Engineers

---

## Featured Projects

### AI Security & Red Teaming

| Project | Description |
| --- | --- |
| **llmsec: Agentic Red-Teaming for LLM Apps** *(in progress)* | Building an automated **red-teaming framework** against a deliberately vulnerable local **LLM application** with **RAG**, **tool calling**, and a hidden canary secret. Seeded attacks run against the target, an independent **LLM judge** scores each result, and a reporter maps findings to the **OWASP Top 10 for LLM Applications**. The judge **fails closed** on errors, code-based evidence overrides it, and **cost caps** limit spend. First live run: 3 of 12 **secret-extraction** attacks succeeded for about $0.03. Next: a **promptfoo** static-attack baseline, then a multi-turn **adaptive attacker**. |
| **[Hack the Agent CTF: 5 of 5 Challenges](https://medium.com/@allie.evan2/hack-the-agent-llm-security-ctf-walkthrough-allie-evan-2a06c306d22c)** | Completed Ethiack's public **AI red-team** challenge against an LLM ticketing assistant. Exploited **unverifiable-claim bypass**, **information leakage**, **system-prompt disclosure**, and **indirect prompt injection** chained with an **SSRF** redirect to reach an internal endpoint. Published a walkthrough with evidence for each level and the **engineering control** that would have prevented it. |
| **[AI-Powered S3 Security Scanner](https://github.com/alevan22/alevan22/tree/main/Projects/AI-AWS-S3-Security-Scanner)** | Serverless **AWS Lambda** function in **Python** that uses **boto3** to list S3 buckets and flag any missing **default encryption** (SSE-S3 / SSE-KMS). Findings are sent to **Gemini** for an AI-generated summary. Built with a **least-privilege IAM** role, **CloudWatch** logging, and an **EventBridge** schedule design for recurring scans. |

### Cloud & Application Security

| Project | Description |
| --- | --- |
| [Secure Inter-VPC Networking & Zero-Trust APIs](https://github.com/alevan22/alevan22/tree/main/Projects/Secure%20Inter%E2%80%91VPC%20Networking%20%26%20Zero%E2%80%91Trust%20APIs%20(VPC%20Peering%20%2B%20Cognito%20%2B%20API%20Gateway%20%2B%20WAF)) | Designed private connectivity between VPCs using **VPC peering**, route tables, and **SG/NACL** controls. Protected the API layer with a **Cognito JWT authorizer** on **API Gateway** (optional **WAF**), tested with hosted-UI login and token checks. Administered instances through **SSM Session Manager** with **no inbound SSH**. |
| [AWS CloudFormation Drift Detection & Auto-Remediation](https://github.com/alevan22/alevan22/tree/main/Projects/AWS%20CloudFormation%20Drift%20Detection%20%26%20Auto-Remediation) | Scheduled **EventBridge → Lambda** workflow that runs `DetectStackDrift`, identifies drifted resources, and **auto-remediates** them back to the approved template state. Uses versioned templates in **S3**, **least-privilege IAM**, and **auditable logs**. |
| [GitLab CI/CD → EC2 (Dockerized Python App)](https://github.com/alevan22/alevan22/tree/main/Projects/GitLab-CI-CD-Pipeline-Python-App) | Built a **pipeline-as-code** workflow (test → build → deploy) using **YAML**, **Docker** multi-stage builds, and **masked CI variables** for registry and SSH credentials. Automates **SSH-based deployment to Ubuntu EC2** on branch-triggered runs, removing manual deploy steps. |
| [Penetration Test: Humbleify Web App](https://github.com/alevan22/alevan22/blob/main/Projects/Humbleify%20Penetration%20Test/README.md) | Assessed a web application and identified **XSS** and **access-control** vulnerabilities. Validated findings with **Burp Suite**, **Nessus**, and **Metasploit**, then **risk-rated** each issue and recommended remediation. |

---

## Skills & Focus Areas

| Area | Tools / Experience |
| --- | --- |
| **AI & LLM Security** | Prompt injection, indirect prompt injection, system-prompt leakage, excessive agency, RAG and tool-calling attack surface, OWASP Top 10 for LLM Applications, promptfoo |
| **AI-Assisted Engineering & Automation** | Claude Code, Cursor, Microsoft Copilot Agents, Gemini, Python, Bash, SQL, Power Automate, Power Apps |
| **Cloud & Infrastructure** | AWS (IAM, KMS, S3, Lambda, EventBridge, CloudFormation, CloudTrail, Cognito, API Gateway, WAF), VPC design, Docker, GitLab CI/CD |
| **Threat Detection & Offensive Security** | SIEM, SOAR, detection engineering, alert triage, MITRE ATT&CK, Suricata, Nessus, Metasploit, Burp Suite, Nmap, Kali Linux |
| **Governance, Risk & Compliance** | NIST 800-53 / 800-171, SOX (ITGC/ICFR), COBIT, Zero Trust, RBAC, audit analytics (Power BI, DAX) |

---

## Experience

### PwC | Digital Assurance & Transparency Associate
*July 2024 – August 2026*

- Selected to join PwC's internal AI Champions group; identified use cases for AI adoption and delivered demonstrations of the firm-approved AI tool.
- Engineered an internal Power Apps and Power Automate tool that applied OCR and tailored Microsoft Copilot prompts to extract key data from client evidence into a standardized testing format, reducing review time by 26%.
- Automated compliance tracking for 250+ controls across 12 apps in 14 regions using Power BI, DAX, and Power Automate, reducing reporting time by ~50%.
- Assessed and validated 25+ IAM, SSO, and network controls across a hybrid cloud migration for 10,000+ users, reducing misconfiguration risk.
- Supported a $2M+ SOX SDLC remediation program: developed pitch materials, identified security and compliance gaps in DevOps processes, and defined scalable controls.
- Helped secure a multimillion-dollar client contract by translating technical remediation plans into executive-aligned proposals.

### KPMG | Technology Risk Consulting Intern
*Summer 2023*

- Performed infrastructure vulnerability assessments across public-cloud deployments using NIST and COBIT; highlighted IAM and network segmentation risks.
- Partnered with technical and audit teams to communicate control findings and remediation strategies to large financial-services stakeholders.
- Built VBA automations to streamline project-plan tracking during a major enterprise separation, saving ~20+ hours of manual updates.

---

## Certifications
- CompTIA Security+
- AWS Certified Cloud Practitioner

---

## Currently Exploring
- Adaptive, agentic red-teaming of LLM applications and measuring the gap against static attack lists
- Prompt-injection defenses that live in code outside the model (allow-lists, authenticated tool use, output validation)
- Securing AI agents on AWS: least-privilege tool access, logging, and detection for agent activity

---

Thanks for visiting. Feel free to connect or explore the projects above.
