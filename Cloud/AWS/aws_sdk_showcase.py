#!/usr/bin/env python3
"""
AWS SDK (boto3) Showcase - Common AWS Operations
==============================================

This file demonstrates various AWS SDK operations using boto3.
Install required packages: pip install boto3 python-dotenv

Setup:
1. Configure AWS credentials:
   - AWS CLI: `aws configure`
   - Environment variables: AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY
   - IAM roles (recommended for EC2)

2. Set your AWS region in environment variables or boto3 config
"""

import boto3
import json
import os
from datetime import datetime
from botocore.exceptions import ClientError, NoCredentialsError

# Initialize AWS clients
def get_aws_clients():
    """Initialize and return AWS service clients"""
    try:
        session = boto3.Session()
        
        clients = {
            'ec2': session.client('ec2'),
            's3': session.client('s3'),
            'rds': session.client('rds'),
            'lambda': session.client('lambda'),
            'sns': session.client('sns'),
            'sqs': session.client('sqs'),
            'cloudwatch': session.client('cloudwatch'),
            'iam': session.client('iam'),
        }
        
        print("✅ AWS clients initialized successfully")
        return clients
    except NoCredentialsError:
        print("❌ AWS credentials not found. Please configure your credentials.")
        return None

# EC2 Operations
def ec2_operations(ec2_client):
    """Demonstrate EC2 operations"""
    print("\n🖥️  EC2 OPERATIONS")
    print("=" * 50)
    
    try:
        # List EC2 instances
        response = ec2_client.describe_instances()
        instance_count = 0
        
        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                instance_count += 1
                instance_id = instance['InstanceId']
                state = instance['State']['Name']
                instance_type = instance['InstanceType']
                
                print(f"Instance: {instance_id}")
                print(f"  State: {state}")
                print(f"  Type: {instance_type}")
                
                # Get instance tags
                tags = instance.get('Tags', [])
                for tag in tags:
                    if tag['Key'] == 'Name':
                        print(f"  Name: {tag['Value']}")
                print()
        
        print(f"Total instances found: {instance_count}")
        
        # List available AMIs (limit to 5 for demo)
        print("\n📀 Available AMIs (Latest 5):")
        amis = ec2_client.describe_images(
            Owners=['amazon'],
            Filters=[
                {'Name': 'name', 'Values': ['amzn2-ami-hvm-*']},
                {'Name': 'state', 'Values': ['available']}
            ],
            MaxResults=5
        )
        
        for ami in amis['Images']:
            print(f"  {ami['ImageId']}: {ami['Name']}")
            
    except ClientError as e:
        print(f"❌ EC2 Error: {e}")

# S3 Operations
def s3_operations(s3_client):
    """Demonstrate S3 operations"""
    print("\n🪣 S3 OPERATIONS")
    print("=" * 50)
    
    try:
        # List S3 buckets
        response = s3_client.list_buckets()
        
        print("S3 Buckets:")
        for bucket in response['Buckets']:
            bucket_name = bucket['Name']
            creation_date = bucket['CreationDate'].strftime('%Y-%m-%d %H:%M:%S')
            print(f"  📦 {bucket_name} (created: {creation_date})")
            
            # Get bucket region
            try:
                location = s3_client.get_bucket_location(Bucket=bucket_name)
                region = location['LocationConstraint'] or 'us-east-1'
                print(f"     Region: {region}")
                
                # List objects in bucket (limit to 5)
                objects = s3_client.list_objects_v2(Bucket=bucket_name, MaxKeys=5)
                if 'Contents' in objects:
                    print("     Objects:")
                    for obj in objects['Contents']:
                        size = obj['Size']
                        modified = obj['LastModified'].strftime('%Y-%m-%d %H:%M:%S')
                        print(f"       📄 {obj['Key']} ({size} bytes, modified: {modified})")
                else:
                    print("     📭 Bucket is empty")
                    
            except ClientError as e:
                if e.response['Error']['Code'] == 'AccessDenied':
                    print("     ⚠️  Access denied for this bucket")
                else:
                    print(f"     ❌ Error accessing bucket: {e}")
            print()
            
    except ClientError as e:
        print(f"❌ S3 Error: {e}")

# RDS Operations
def rds_operations(rds_client):
    """Demonstrate RDS operations"""
    print("\n🗄️  RDS OPERATIONS")
    print("=" * 50)
    
    try:
        # List RDS instances
        response = rds_client.describe_db_instances()
        
        if response['DBInstances']:
            for db in response['DBInstances']:
                db_id = db['DBInstanceIdentifier']
                engine = db['Engine']
                status = db['DBInstanceStatus']
                instance_class = db['DBInstanceClass']
                
                print(f"Database: {db_id}")
                print(f"  Engine: {engine}")
                print(f"  Status: {status}")
                print(f"  Class: {instance_class}")
                
                if 'Endpoint' in db:
                    print(f"  Endpoint: {db['Endpoint']['Address']}")
                print()
        else:
            print("No RDS instances found")
            
    except ClientError as e:
        print(f"❌ RDS Error: {e}")

# Lambda Operations
def lambda_operations(lambda_client):
    """Demonstrate Lambda operations"""
    print("\n⚡ LAMBDA OPERATIONS")
    print("=" * 50)
    
    try:
        # List Lambda functions
        response = lambda_client.list_functions()
        
        if response['Functions']:
            for func in response['Functions']:
                func_name = func['FunctionName']
                runtime = func['Runtime']
                last_modified = func['LastModified']
                
                print(f"Function: {func_name}")
                print(f"  Runtime: {runtime}")
                print(f"  Last Modified: {last_modified}")
                print(f"  Memory: {func['MemorySize']} MB")
                print(f"  Timeout: {func['Timeout']} seconds")
                print()
        else:
            print("No Lambda functions found")
            
    except ClientError as e:
        print(f"❌ Lambda Error: {e}")

# CloudWatch Operations
def cloudwatch_operations(cw_client):
    """Demonstrate CloudWatch operations"""
    print("\n📊 CLOUDWATCH OPERATIONS")
    print("=" * 50)
    
    try:
        # List CloudWatch alarms
        response = cw_client.describe_alarms()
        
        if response['MetricAlarms']:
            for alarm in response['MetricAlarms']:
                alarm_name = alarm['AlarmName']
                state = alarm['StateValue']
                metric = alarm['MetricName']
                
                print(f"Alarm: {alarm_name}")
                print(f"  State: {state}")
                print(f"  Metric: {metric}")
                print(f"  Threshold: {alarm['Threshold']}")
                print()
        else:
            print("No CloudWatch alarms found")
            
        # Create a custom metric (example)
        print("📈 Sending custom metric...")
        cw_client.put_metric_data(
            Namespace='MyApp/Demo',
            MetricData=[
                {
                    'MetricName': 'DemoMetric',
                    'Value': 42.0,
                    'Unit': 'Count',
                    'Timestamp': datetime.now()
                }
            ]
        )
        print("✅ Custom metric sent successfully")
        
    except ClientError as e:
        print(f"❌ CloudWatch Error: {e}")

# IAM Operations (Basic)
def iam_operations(iam_client):
    """Demonstrate IAM operations"""
    print("\n👤 IAM OPERATIONS")
    print("=" * 50)
    
    try:
        # Get current user info
        try:
            user = iam_client.get_user()
            print(f"Current User: {user['User']['UserName']}")
            print(f"  ARN: {user['User']['Arn']}")
            print(f"  Created: {user['User']['CreateDate']}")
        except ClientError:
            print("Current user information not available (might be using role-based access)")
        
        # List IAM roles (first 5)
        roles = iam_client.list_roles(MaxItems=5)
        print("\nIAM Roles (first 5):")
        for role in roles['Roles']:
            print(f"  🎭 {role['RoleName']}")
            print(f"     Created: {role['CreateDate']}")
            
    except ClientError as e:
        print(f"❌ IAM Error: {e}")

# Utility Functions
def create_sample_s3_operations(s3_client):
    """Sample S3 file operations (commented for safety)"""
    print("\n🔧 S3 SAMPLE OPERATIONS (Demo Code)")
    print("=" * 50)
    
    sample_code = '''
    # Create a bucket
    bucket_name = 'my-demo-bucket-' + str(int(datetime.now().timestamp()))
    s3_client.create_bucket(Bucket=bucket_name)
    
    # Upload a file
    s3_client.upload_file('local-file.txt', bucket_name, 'uploaded-file.txt')
    
    # Download a file
    s3_client.download_file(bucket_name, 'uploaded-file.txt', 'downloaded-file.txt')
    
    # Delete an object
    s3_client.delete_object(Bucket=bucket_name, Key='uploaded-file.txt')
    
    # Delete the bucket
    s3_client.delete_bucket(Bucket=bucket_name)
    '''
    
    print("Sample S3 operations code:")
    print(sample_code)

def get_aws_account_info():
    """Get AWS account information"""
    try:
        sts_client = boto3.client('sts')
        identity = sts_client.get_caller_identity()
        
        print("🔍 AWS ACCOUNT INFO")
        print("=" * 50)
        print(f"Account ID: {identity['Account']}")
        print(f"User ARN: {identity['Arn']}")
        print(f"User ID: {identity['UserId']}")
        
    except ClientError as e:
        print(f"❌ Error getting account info: {e}")

def main():
    """Main function to demonstrate AWS SDK operations"""
    print("🚀 AWS SDK (boto3) SHOWCASE")
    print("=" * 50)
    
    # Get AWS account info
    get_aws_account_info()
    
    # Initialize AWS clients
    clients = get_aws_clients()
    
    if not clients:
        print("\n❌ Cannot proceed without AWS credentials")
        print("\n📝 Setup Instructions:")
        print("1. Install: pip install boto3")
        print("2. Configure credentials:")
        print("   - Run: aws configure")
        print("   - Or set environment variables:")
        print("     export AWS_ACCESS_KEY_ID='your-key'")
        print("     export AWS_SECRET_ACCESS_KEY='your-secret'")
        print("     export AWS_DEFAULT_REGION='us-east-1'")
        return
    
    print(f"\n🌍 Region: {boto3.Session().region_name}")
    
    # Demonstrate different AWS services
    ec2_operations(clients['ec2'])
    s3_operations(clients['s3'])
    rds_operations(clients['rds'])
    lambda_operations(clients['lambda'])
    cloudwatch_operations(clients['cloudwatch'])
    iam_operations(clients['iam'])
    
    # Show sample operations
    create_sample_s3_operations(clients['s3'])
    
    print("\n✨ AWS SDK Showcase completed!")
    print("\n📚 Additional Resources:")
    print("- Boto3 Documentation: https://boto3.amazonaws.com/v1/documentation/api/latest/")
    print("- AWS CLI Documentation: https://docs.aws.amazon.com/cli/")
    print("- AWS SDK Examples: https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python")

if __name__ == "__main__":
    main()