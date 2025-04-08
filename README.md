# AWS Demo Project

This repository contains AWS CloudFormation templates and Lambda code for a simple AWS demo project.

## Contents

- `s3-bucket.yaml`: CloudFormation template for creating an S3 bucket
- `lambda/list_s3_objects.py`: Python Lambda function to list objects in an S3 bucket
- `complete-stack.yaml`: Comprehensive CloudFormation template that deploys both the S3 bucket and Lambda function with proper IAM permissions

## Deployment Instructions

### Option 1: Deploy using AWS Management Console

1. Log in to the AWS Management Console
2. Navigate to CloudFormation
3. Click "Create stack" > "With new resources"
4. Select "Upload a template file" and upload `complete-stack.yaml`
5. Follow the prompts to complete the stack creation

### Option 2: Deploy using AWS CLI

```bash
aws cloudformation create-stack \
  --stack-name my-aws-demo \
  --template-body file://complete-stack.yaml \
  --capabilities CAPABILITY_IAM
```

## Testing the Lambda Function

After deployment, you can test the Lambda function using the AWS Management Console or AWS CLI:

### Using AWS Management Console

1. Navigate to the Lambda service
2. Find and select the deployed function
3. Click the "Test" tab
4. Create a new test event with the following JSON:
   ```json
   {}
   ```
5. Click "Test" to execute the function

### Using AWS CLI

```bash
aws lambda invoke \
  --function-name my-aws-demo-list-s3-objects \
  --payload '{}' \
  response.json

cat response.json
```

## Clean Up

To delete all resources created by this stack:

```bash
aws cloudformation delete-stack --stack-name my-aws-demo
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.
