# Decrypting a simple file

## Step 1:
Run the following command in the terminal on the right to get an encrypted secret file.
```bash
wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-CD0267EN-SkillsNetwork/labs/module1/encrypted_secretfile
```

## Step 2:
View the file content from the explorer menu on the left.

You will see that the content is not readable, and is all encrypted. This has been encoded using aes-256-cbc cipher. Each cipher has its own algorithm. aes-256-cbc is one of the older and simpler ciphers, and there are now much better algorithms to encrypt the data.


Steo 3:
Run the following command to decrypt the file.
```bash
openssl aes-256-cbc -d -a -pbkdf2 -in encrypted_secretfile -out secrets.txt
```
|Command option|Meaning|
|-|-|
|aes-256-cbc|The cipher algorithm|
|-d|Decrypt|
|-a|Base64 decode|
|-pbkdf2|Use password-based key derivation function 2|
|-in encrypted_secretfile|Input file|
|-out secrets.txt|Output file|

## Step 4:
It will prompt you for a password. When the file was encrypted, it was done so with the aes-256-cbc cipher using a password. You need to type the password into the prompt to decrypt the file. The file has been encrypted with the password adios. The same needs to be given to decrypt it.

Type the password and press enter. Note that the password will not appear on the terminal.

## Step 5:
The decrypted file will be viewable through the explorer with decrypted contents.