#!/bin/bash

# AWS EC2 Laravel Deployment Fix for Avatar Upload
# Run this on your EC2 instance after deployment

echo "Fixing Laravel storage symlink and permissions for avatar uploads..."

# Navigate to your Laravel project directory
cd /path/to/your/laravel/project

# Create storage symlink
php artisan storage:link

# Set proper permissions for storage directories
sudo chown -R www-data:www-data storage/
sudo chown -R www-data:www-data bootstrap/cache/
sudo chmod -R 775 storage/
sudo chmod -R 775 bootstrap/cache/

# Set permissions for public/storage symlink
sudo chown -R www-data:www-data public/storage
sudo chmod -R 755 public/storage

echo "Storage setup completed!"
echo "Test avatar upload functionality now."