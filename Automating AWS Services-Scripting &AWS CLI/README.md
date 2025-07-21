
# Automating AWS Services with Scripting and the AWS CLI

This lab demonstrates how to automate AWS service operations using the AWS Console, CLI, and SDK. You’ll gain hands-on experience in infrastructure automation, secure access, scripting, and cost optimization using Python, EC2, S3, CloudWatch, and more.

---

## 🧠 Skills Demonstrated

- Secure EC2 access with Systems Manager Session Manager
- AWS CLI scripting for EC2, S3, and EBS
- Python automation using Boto3 SDK
- Snapshot rotation and lifecycle management
- Custom CloudWatch metric generation
- EC2 automation with tagging logic (`Stopinator`)
- Security credentials and metadata service



## 🧪 Tasks Completed

### ✅ 1: Connect to EC2 via Session Manager

- Connected to EC2 using Systems Manager Session Manager

📷 `screenshots/session-manager-connection.png`

---

### ✅ 2: Create EC2 Key Pairs via 3 Methods

#### • Console
- Created key pair `console` using Console UI  
📷 `screenshots/console-keypair.png`

#### • AWS CLI
```bash
aws ec2 create-key-pair --key-name CLI
````

📷 `screenshots/cli-keypair.png`

#### • Python SDK

```bash
cat create-keypair.py
./create-keypair.py
```

📷 `screenshots/sdk-keypair.png`

---

### ✅ 3: Manage S3 via CLI

```bash
aws s3 mb s3://data-123
aws s3 cp create-keypair.py s3://data-123
aws s3 sync . s3://data-123
```

📷 `screenshots/s3-bucket-listing.png`

---

### ✅ 4: Automate EBS Snapshots

* Manual snapshot via Console
* Snapshot via CLI:

```bash
aws ec2 create-snapshot --volume-id <VOLUME_ID> --description CLI
```

* Rotating snapshots:

```bash
cat snapshotter.py
./snapshotter.py
```

📷 `screenshots/snapshot-list.png`

---

### ✅ 5: EC2 Automation with The Stopinator

* Tagged EC2 instance and used `stopinator.py` to stop or terminate based on tag:

```bash
cat stopinator.py
./stopinator.py
```

📷 `screenshots/stopinator-action.png`

---

### ✅ 6: Custom CloudWatch Metrics

* Metric creation:

```bash
aws cloudwatch put-metric-data --namespace Lab --metric-name ALLIE --value 42
```

* Game-based metric generator:

```bash
./highlow.py
```

📷 `screenshots/cloudwatch-metrics.png`

---

### ✅ 7: View Security Credentials

* Accessed temporary credentials via instance metadata:

```bash
./show-credentials
```

📷 `screenshots/security-credentials.png`

---

### ✅ 8: CLI Help and Documentation

```bash
aws help
aws ec2 help
aws ec2 describe-instances help
```

📷 `screenshots/aws-help.png`




