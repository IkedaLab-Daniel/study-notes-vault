#!/bin/bash

# AWS EC2 Laravel Deployment Fix for Avatar Upload
# Run this on your EC2 instance after deployment

echo "Fixing Laravel storage symlink and permissions for avatar uploads..."

cd .

# Create storage symlink
php artisan storage:link

# Detect the web server user
WEB_USER=""
if id "apache" &>/dev/null; then
    WEB_USER="apache"
elif id "nginx" &>/dev/null; then
    WEB_USER="nginx"  
elif id "www-data" &>/dev/null; then
    WEB_USER="www-data"
elif id "ec2-user" &>/dev/null; then
    WEB_USER="ec2-user"
else
    WEB_USER=$(whoami)
fi

echo "Using web user: $WEB_USER"

# Set proper permissions for storage directories
sudo chown -R $WEB_USER:$WEB_USER storage/
sudo chown -R $WEB_USER:$WEB_USER bootstrap/cache/
sudo chmod -R 775 storage/
sudo chmod -R 775 bootstrap/cache/

# Set permissions for public/storage symlink (if it exists)
if [ -L "public/storage" ] || [ -d "public/storage" ]; then
    sudo chown -R $WEB_USER:$WEB_USER public/storage
    sudo chmod -R 755 public/storage
fi

# Also set permissions for the main public directory
sudo chown -R $WEB_USER:$WEB_USER public/
sudo chmod -R 755 public/

echo "Storage setup completed!"
echo "Web user: $WEB_USER"
echo "Test avatar upload functionality now."