# README: AWS Cloud Solution Deployment

## Overview

This project is a **serverless AWS Cloud Solution** that utilizes **AWS CDK**, **Lambda**, **API Gateway**, and **DynamoDB** to provide a scalable and cost-effective cloud architecture.

## Features

- **AWS Lambda**: Handles backend logic execution.
- **API Gateway**: Exposes secure REST endpoints.
- **DynamoDB**: NoSQL database for data storage.
- **CloudWatch**: Monitors application logs and performance.
- **AWS CDK**: Infrastructure as Code (IaC) for deploying AWS resources.
- **Cognito (Optional Enhancement)**: Provides authentication and user management.
- **EventBridge (Future Enhancement)**: Automates data processing and reporting.

## Architecture

The system is designed as follows:

1. **Client** sends requests via API Gateway.
2. **API Gateway** routes requests to AWS Lambda.
3. **Lambda Functions** process business logic and interact with DynamoDB.
4. **DynamoDB** stores and retrieves data securely.
5. **CloudWatch Logs** track API and Lambda execution.
6. **Cognito (if enabled)** manages user authentication.

## Prerequisites

Before deploying, ensure you have:

- **AWS CLI** installed and configured (`aws configure`)
- **Node.js & npm** installed
- **Python 3.x** installed
- **AWS CDK** installed globally (`npm install -g aws-cdk`)

## Installation & Setup

### 1️⃣ Clone the Repository

```sh
 git clone <repository-url>
 cd aws-cloud-solution
```

### 2️⃣ Set Up Virtual Environment

```sh
 python -m venv .env
 source .env/bin/activate  # Mac/Linux
 .env\Scripts\activate  # Windows
```

### 3️⃣ Install Dependencies

```sh
 pip install -r requirements.txt
```

### 4️⃣ Initialize AWS CDK

```sh
 cdk bootstrap
 cdk synth
```

### 5️⃣ Deploy the Solution

```sh
 cdk deploy
```

## Testing the Solution

### Using cURL:

```sh
 curl -X POST https://<api-id>.execute-api.<region>.amazonaws.com/prod/items \
 -H "Content-Type: application/json" \
 -d '{"id": "123", "data": "Test API call"}'
```

### Using Postman:

- Open Postman.
- Create a **POST** request to the API Gateway URL.
- Add **JSON payload**: `{ "id": "123", "data": "Test API call" }`
- Click **Send**.

## Monitoring & Debugging

- **Check CloudWatch Logs**:

```sh
 aws logs tail /aws/lambda/DataHandler --follow
```

- **Check DynamoDB Data**:
  - Go to AWS Console → DynamoDB → Tables → DataTable → Items.

## Cleanup (Destroying the Stack)

```sh
 cdk destroy
```

## Future Enhancements

- Implement **AWS Cognito** for user authentication.
- Automate reporting with **AWS EventBridge**.
- Optimize auto-scaling for cost efficiency.

