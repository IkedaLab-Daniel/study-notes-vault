# Laravel AWS Deployment Guide (EC2 + RDS)

This guide provides step-by-step instructions for deploying a standard Laravel application to the AWS cloud using services from the Free Tier.

**Core Stack:**
*   **Web Server:** AWS EC2 (`t2.micro`)
*   **Database:** AWS RDS (`db.t2.micro`) running MySQL.

**Disclaimer:** This is a foundational guide for a practice deployment. Real-world production environments involve more advanced security (like IAM roles), automation (CI/CD pipelines), and configuration.

---

## Phase 1: Set Up AWS RDS (Your Database)

1.  **Navigate to RDS:** Log in to your AWS Management Console and go to the RDS service.
2.  **Create Database:** Click "Create database".
    *   Choose a database creation method: **Standard Create**
    *   Engine type: **MySQL**
    *   Templates: **Free tier**
3.  **Settings:**
    *   **DB instance identifier:** Give it a unique name, e.g., `laravel-database`.
    *   **Master username:** Choose a username, e.g., `admin`.
    *   **Master password:** Create a strong password and **save it securely in a password manager.** Do not lose this.
4.  **Connectivity:**
    *   **Compute resource:** Don't connect to an EC2 compute resource yet. We'll do this manually.
    *   **Public access:** Set this to **No**. This is critical. It ensures your database is not exposed to the public internet.
5.  **Create Database:** Keep the rest of the defaults and click "Create database". It will take 5-10 minutes for the database to be created.
6.  **Get Your Endpoint:** Once the database status is "Available", click on it to view its details. Go to the **Connectivity & security** tab and copy the **Endpoint** name. It will look something like `laravel-database.xxxxxxxxxxxx.us-east-1.rds.amazonaws.com`. Save this for later.

---

## Phase 2: Set Up AWS EC2 (Your Web Server)

1.  **Navigate to EC2:** Go to the EC2 service in your AWS Console.
2.  **Launch Instance:**
    *   **Name:** `laravel-web-server`
    *   **Application and OS Images (AMI):** Choose **Amazon Linux 2023 AMI**. It's free-tier eligible and the latest version.
    *   **Instance type:** Choose **t2.micro** (also free-tier eligible).
3.  **Key Pair (for login):**
    *   This is how you will access your server. Click "Create new key pair".
    *   **Key pair name:** `laravel-key`
    *   **Key pair type:** RSA, `.pem`
    *   Click "Create key pair". Your browser will download `laravel-key.pem`. **Save this file somewhere safe. If you lose it, you lose access to your server.**
4.  **Network Settings:**
    *   Click **Edit**.
    *   **Create security group:** Select this option.
    *   **Security group name:** `laravel-sg`
    *   **Inbound security groups rules:**
        *   **SSH Rule:** The default SSH rule is good. For the "Source type", you can set it to **Anywhere (0.0.0.0/0)** if you have a changing (dynamic) IP address. **WARNING:** This is less secure as it allows anyone on the internet to attempt to connect to your server. A more secure option is **My IP**, but you would have to update the rule whenever your IP address changes.
        *   **HTTP/S Rules:** Click **Add security group rule** and add a rule for `HTTP` (Port 80, Source: Anywhere). Add another for `HTTPS` (Port 443, Source: Anywhere). This allows web traffic.
5.  **Launch Instance:** Keep the default storage and click "Launch instance".

---

## Phase 3: Connect EC2 and RDS

This is the crucial firewall configuration step that allows your server and database to communicate.

1.  Go back to your **RDS instance** details.
2.  In the **Connectivity & security** tab, click on the VPC security group link.
3.  Select the **Inbound rules** tab for that security group and click **Edit inbound rules**.
4.  **Add a new rule:**
    *   **Type:** `MYSQL/Aurora` (it will auto-fill port 3306).
    *   **Source:** Click in the search box and select the security group you created for your EC2 instance (e.g., `laravel-sg`).
5.  Click **Save rules**.

---

## Phase 4: Configuring the EC2 Server (Amazon Linux 2023)

1.  **Connect via SSH:**
    *   On your local machine, open a terminal and navigate to where you saved your `.pem` file.
    *   First, lock down permissions for your key file: `chmod 400 laravel-key.pem`
    *   Find the **Public IPv4 address** of your EC2 instance from the EC2 dashboard.
    *   Connect using the command:
        ```bash
        ssh -i "laravel-key.pem" ec2-user@YOUR_PUBLIC_IP
        ```

2.  **Install Web Server & PHP:** Run the following commands one by one on your EC2 instance. These are for **Amazon Linux 2023**.
    ```bash
    # Update all packages on the server
    sudo dnf update -y

    # Install Nginx web server
    sudo dnf install -y nginx

    # Install PHP 8.2 and required extensions for Laravel
    sudo dnf install -y php php-fpm php-gd php-mysqlnd php-xml php-mbstring php-json

    # Start Nginx and enable it to run on boot
    sudo systemctl start nginx
    sudo systemctl enable nginx

    # Start PHP-FPM and enable it to run on boot
    sudo systemctl start php-fpm
    sudo systemctl enable php-fpm
    ```

3.  **Install Composer (PHP Package Manager):**
    ```bash
    # Download and install Composer globally
    curl -sS https://getcomposer.org/installer | sudo php -- --install-dir=/usr/local/bin --filename=composer
    ```

---

## Phase 5: Deploying the Laravel App

1.  **Get Your Code:**
    *   Install Git: `sudo dnf install -y git`
    *   Navigate to the web root directory: `cd /usr/share/nginx/html`
    *   Clone your project into the current directory. *Note: You may need to make your repository public on GitHub/GitLab for this simple clone to work.*
        ```bash
        git clone https://github.com/your-username/your-repo.git .
        ```

2.  **Set Up Laravel:**
    *   Install dependencies: `composer install --no-dev --optimize-autoloader`
    *   Create your environment file: `cp .env.example .env`
    *   Generate an application key: `php artisan key:generate`
    *   **Edit the `.env` file:** `nano .env`
        *   Set `APP_ENV=production` and `APP_DEBUG=false`.
        *   Set `DB_CONNECTION=mysql`.
        *   Set `DB_HOST` to your **RDS Endpoint URL** from Phase 1.
        *   Set `DB_DATABASE`, `DB_USERNAME`, and `DB_PASSWORD` to the credentials you created for RDS.
    *   Set Laravel-specific permissions:
        ```bash
        sudo chown -R nginx:nginx /usr/share/nginx/html/storage /usr/share/nginx/html/bootstrap/cache
        ```

3.  **Configure Nginx for Laravel:**
    *   Create a new Nginx config file: `sudo nano /etc/nginx/conf.d/laravel.conf`
    *   Paste the following configuration. Replace `YOUR_PUBLIC_IP` with your EC2's actual Public IP address.
        ```nginx
        server {
            listen 80;
            server_name YOUR_PUBLIC_IP;
            root /usr/share/nginx/html/public;

            add_header X-Frame-Options "SAMEORIGIN";
            add_header X-Content-Type-Options "nosniff";

            index index.php;

            charset utf-8;

            location / {
                try_files $uri $uri/ /index.php?$query_string;
            }

            location = /favicon.ico { access_log off; log_not_found off; }
            location = /robots.txt  { access_log off; log_not_found off; }

            error_page 404 /index.php;

            location ~ \.php$ {
                fastcgi_pass unix:/run/php-fpm/www.sock;
                fastcgi_param SCRIPT_FILENAME $realpath_root$fastcgi_script_name;
                include fastcgi_params;
            }

            location ~ /\.(?!well-known).* {
                deny all;
            }
        }
        ```
    *   Restart Nginx to apply the changes: `sudo systemctl restart nginx`

4.  **Run Migrations:**
    *   Navigate to your project root: `cd /usr/share/nginx/html`
    *   Run the migrations. The `--force` flag is required in production.
        ```bash
        php artisan migrate --force
        ```

---

## Final Step: View Your App

Open your web browser and navigate to your EC2 instance's public IP address. You should see your Laravel application live!