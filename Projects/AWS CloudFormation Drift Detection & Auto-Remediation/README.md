# 🔄 AWS CloudFormation Drift Detection & Auto-Remediation

## 📘 Overview
This project automatically detects and remediates drift in CloudFormation stacks using AWS-native services. It’s designed to maintain compliance and integrity of cloud infrastructure.

## ☁️ Tech Stack
- AWS CloudFormation
- AWS Lambda (Python)
- Amazon EventBridge
- AWS Config (Optional Extension)
- CloudWatch

## 🧰 Features
- Detects stack drifts via scheduled EventBridge rule
- Lambda analyzes drift result and triggers remediation
- Sends alerts/logs via CloudWatch
- Configurable for tagging and IAM enforcement

## 🧠 Security Concepts Applied
- IAM least privilege for Lambda execution role
- IaC integrity monitoring
- Event-driven detection & response

## 📸 Demo
![CloudWatch Alert Screenshot](./screenshots/alert-demo.png)

## 🗺️ Architecture
See [`architecture/diagram.png`](architecture/diagram.png) and [`explanation.md`](architecture/explanation.md) for system flow.

## 📦 How to Deploy
1. Deploy `drift-remediation.yml` in CloudFormation
2. Set up EventBridge rule using `eventbridge/rule.json`
3. Ensure your Lambda role has appropriate permissions


