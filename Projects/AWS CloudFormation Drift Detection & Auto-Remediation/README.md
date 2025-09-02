
# ☁️ CloudFormation Drift Detection Lab

This project implements an automated CloudFormation drift detection solution using **AWS Lambda**, **SNS**, and **EventBridge**, with alerting for drifted resources.

![Structure diagram](./Screenshots/AWS-CloudForm-Structure.png)

---

## 🧱 `drift-detection-template.yaml`

```yaml
AWSTemplateFormatVersion: '2010-09-09'
Description: Sample template to demonstrate drift detection

Resources:
  SampleBucket:
    Type: AWS::S3::Bucket
    Properties:
      BucketName: drift-detection-demo-bucket
```

---

## 🔐 `lambda-execution-role.json`

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "cloudformation:DetectStackDrift",
        "cloudformation:DescribeStackDriftDetectionStatus",
        "cloudformation:DescribeStackResources",
        "sns:Publish"
      ],
      "Resource": "*"
    },
    {
      "Effect": "Allow",
      "Action": "logs:*",
      "Resource": "*"
    }
  ]
}
```

---

## 🐍 `lambda_function.py`

```python
import boto3
import time
import os

cf = boto3.client('cloudformation')
sns = boto3.client('sns')

STACK_NAME = os.environ['STACK_NAME']
SNS_TOPIC_ARN = os.environ['SNS_TOPIC_ARN']

def lambda_handler(event, context):
    print(f"Starting drift detection for stack: {STACK_NAME}")
    drift_detection = cf.detect_stack_drift(StackName=STACK_NAME)
    detection_id = drift_detection['StackDriftDetectionId']

    while True:
        status_response = cf.describe_stack_drift_detection_status(StackDriftDetectionId=detection_id)
        status = status_response['DetectionStatus']
        if status == 'DETECTION_COMPLETE':
            break
        time.sleep(5)

    drift_status = status_response['StackDriftStatus']
    print(f"Drift Status: {drift_status}")

    if drift_status == 'DRIFTED':
        resources = cf.describe_stack_resources(StackName=STACK_NAME)
        drifted_resources = [res for res in resources['StackResources'] if res['ResourceStatus'] != 'CREATE_COMPLETE']

        message = f"[ALERT] Stack {STACK_NAME} is DRIFTED.\n"
        for r in drifted_resources:
            message += f"- {r['LogicalResourceId']} ({r['ResourceType']}): {r['ResourceStatus']}\n"

        sns.publish(
            TopicArn=SNS_TOPIC_ARN,
            Subject=f"Drift Alert: {STACK_NAME}",
            Message=message
        )
```

---

## 📬 `sns_setup.sh`

```bash
#!/bin/bash

TOPIC_NAME=DriftDetectionAlertTopic
EMAIL=your_email@example.com

# Create topic
aws sns create-topic --name $TOPIC_NAME

# Subscribe email
aws sns subscribe \
  --topic-arn arn:aws:sns:us-east-1:YOUR_ACCOUNT_ID:$TOPIC_NAME \
  --protocol email \
  --notification-endpoint $EMAIL
```

> ⚠️ Replace `YOUR_ACCOUNT_ID` and `your_email@example.com` with your actual values.

---



---

## ✅ Summary

This setup automatically:

* Detects stack drift
* Waits for detection to complete
* Notifies via email if drifted resources are found


