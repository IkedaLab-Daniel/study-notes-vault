#!/usr/bin/env python3
"""
Quick test to verify AWS permissions
"""

import boto3
from botocore.exceptions import ClientError
from dotenv import load_dotenv

load_dotenv()

def test_permissions():
    """Test various AWS service permissions"""
    print("🔍 Testing AWS Permissions\n")
    
    tests = [
        ('STS', 'sts', 'get_caller_identity', {}),
        ('EC2', 'ec2', 'describe_instances', {'MaxResults': 5}),
        ('S3', 's3', 'list_buckets', {}),
        ('RDS', 'rds', 'describe_db_instances', {'MaxRecords': 5}),
        ('Lambda', 'lambda', 'list_functions', {'MaxItems': 5}),
        ('CloudWatch', 'cloudwatch', 'describe_alarms', {'MaxRecords': 5}),
        ('IAM', 'iam', 'get_user', {}),
    ]
    
    results = []
    
    for service_name, service, method, params in tests:
        try:
            client = boto3.client(service)
            getattr(client, method)(**params)
            results.append((service_name, '✅', 'Success'))
            print(f"✅ {service_name:15} - Permission granted")
        except ClientError as e:
            error_code = e.response['Error']['Code']
            if error_code in ['UnauthorizedOperation', 'AccessDenied', 'AccessDeniedException']:
                results.append((service_name, '❌', 'Access Denied'))
                print(f"❌ {service_name:15} - Access denied")
            else:
                results.append((service_name, '⚠️', error_code))
                print(f"⚠️  {service_name:15} - {error_code}")
        except Exception as e:
            results.append((service_name, '❌', str(e)[:30]))
            print(f"❌ {service_name:15} - Error: {str(e)[:50]}")
    
    print("\n" + "="*50)
    print("SUMMARY")
    print("="*50)
    
    success = sum(1 for _, status, _ in results if status == '✅')
    total = len(results)
    
    print(f"Passed: {success}/{total}")
    
    if success == total:
        print("\n🎉 All permissions working! You're ready to run the showcase.")
    elif success > 0:
        print("\n⚠️  Some permissions missing. Attach more policies for full functionality.")
    else:
        print("\n❌ No permissions found. Please attach ReadOnlyAccess policy.")

if __name__ == "__main__":
    test_permissions()
