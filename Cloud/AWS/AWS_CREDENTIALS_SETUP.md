# AWS Credentials Setup Guide

## Quick Start (3 Methods)

### Method 1: IAM User (Recommended for Development) ⭐

1. **Navigate to IAM in AWS Console**
   ```
   AWS Console → Services → IAM → Users → Add users
   ```

2. **Create User**
   - Username: `my-boto3-dev`
   - Access type: ☑️ Access key - Programmatic access
   - Click "Next: Permissions"

3. **Set Permissions**
   - Choose: "Attach existing policies directly"
   - Select policies:
     - For learning: `ReadOnlyAccess` (safest)
     - For development: `PowerUserAccess`
     - For specific services: `AmazonEC2FullAccess`, `AmazonS3FullAccess`, etc.
   - Click "Next" → "Create user"

4. **Save Credentials** ⚠️
   ```
   Access Key ID:     AKIAIOSFODNN7EXAMPLE
   Secret Access Key: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
   ```
   📥 Download the CSV file or copy immediately!

5. **Add to .env file**
   ```bash
   AWS_ACCESS_KEY_ID=AKIAIOSFODNN7EXAMPLE
   AWS_SECRET_ACCESS_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
   AWS_DEFAULT_REGION=us-east-1
   ```

---

### Method 2: AWS CLI Configuration

```bash
# Install AWS CLI (macOS)
brew install awscli

# Configure credentials
aws configure

# Enter when prompted:
AWS Access Key ID: [your_access_key]
AWS Secret Access Key: [your_secret_key]
Default region name: us-east-1
Default output format: json

# Verify configuration
aws sts get-caller-identity
```

Credentials are stored at: `~/.aws/credentials`

---

### Method 3: AWS Academy Learner Lab

1. **Start your Learner Lab**
2. **Click "AWS Details"**
3. **Click "Show" next to AWS CLI**
4. **Copy credentials section**
   ```
   [default]
   aws_access_key_id=ASIA...
   aws_secret_access_key=...
   aws_session_token=...  # Note: This is temporary!
   ```
5. **Paste into `~/.aws/credentials`**

⏰ **Note:** Academy credentials expire after lab session ends!

---

## Finding Your Credentials

### IAM Console Method:
```
AWS Console
  └─ Services
      └─ IAM (Identity and Access Management)
          └─ Users
              └─ Your Username
                  └─ Security credentials tab
                      └─ Create access key
```

### Existing Access Keys:
- Go to: IAM → Users → [Your User] → Security credentials
- You can see existing Access Key IDs
- ⚠️ You CANNOT retrieve the Secret Key after creation
- If lost, delete old key and create new one

---

## Security Best Practices 🔒

### ✅ DO:
- ✅ Create IAM users with minimal required permissions
- ✅ Use `ReadOnlyAccess` for learning/testing
- ✅ Add `.env` to `.gitignore`
- ✅ Rotate credentials regularly
- ✅ Delete unused access keys
- ✅ Enable MFA on your AWS account

### ❌ DON'T:
- ❌ Use root account credentials
- ❌ Commit credentials to Git
- ❌ Share credentials publicly
- ❌ Use same credentials across multiple apps
- ❌ Give more permissions than needed

---

## Testing Your Credentials

### Quick Test:
```bash
# Using AWS CLI
aws sts get-caller-identity

# Using Python (boto3)
python3 -c "import boto3; print(boto3.client('sts').get_caller_identity())"
```

### Expected Output:
```json
{
    "UserId": "AIDAI...",
    "Account": "123456789012",
    "Arn": "arn:aws:iam::123456789012:user/my-boto3-dev"
}
```

---

## Troubleshooting

### Error: "Unable to locate credentials"
**Solution:** Set credentials using one of the methods above

### Error: "The security token included in the request is invalid"
**Solutions:**
- Check if credentials are correct
- For Academy: Restart lab and get new credentials
- Delete old access key and create new one

### Error: "Access Denied"
**Solution:** Your IAM user needs more permissions
- Go to IAM → Users → [User] → Add permissions

### Error: "Region not set"
**Solution:** Add to `.env`:
```bash
AWS_DEFAULT_REGION=us-east-1
```

---

## Environment Variables Reference

```bash
# Required
AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_key
AWS_DEFAULT_REGION=us-east-1

# Optional (for temporary credentials)
AWS_SESSION_TOKEN=your_session_token

# Optional (for named profiles)
AWS_PROFILE=default
```

---

## Running the Showcase App

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Configure credentials (choose one method above)

# 3. Run the app
python3 aws_sdk_showcase.py
```

---

## Additional Resources

- 📘 [AWS IAM User Guide](https://docs.aws.amazon.com/IAM/latest/UserGuide/)
- 📘 [Boto3 Configuration](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/configuration.html)
- 📘 [AWS CLI Configuration](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html)
- 📘 [Security Best Practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)
