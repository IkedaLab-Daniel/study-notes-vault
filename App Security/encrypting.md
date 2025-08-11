# Encrypt the file

Step 1:
Make changes, as you require, to the secret.txt file and encrypt it with a new password. It will prompt you to enter and renter the same password to verify. Make sure you remember the password.
```bash
openssl aes-256-cbc -a -pbkdf2 -in secrets.txt -out secrets.txt.enc
```

Step 2:
Now, if you see the file secrets.txt.enc, it will have encrypted contents.