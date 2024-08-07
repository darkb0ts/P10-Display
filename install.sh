#!/bin/bash

# Update package lists
echo "Updating package lists..."
sudo apt-get update

# Install Apache
echo "Installing Apache..."
sudo apt-get install -y apache2

sudo apt-get install cpython -y

sudo apt-get install nmap -y

# Start Apache service and enable it to start on boot
echo "Starting Apache service..."
sudo systemctl start apache2
echo "Enabling Apache to start on boot..."
sudo systemctl enable apache2

# Install MySQL (MariaDB)
echo "Installing MySQL (MariaDB)..."
sudo apt-get install -y mariadb-server

# Start MySQL service and enable it to start on boot
echo "Starting MySQL service..."
sudo systemctl start mariadb
echo "Enabling MySQL to start on boot..."
sudo systemctl enable mariadb

# Set MySQL root password to 'root'
echo "Setting MySQL root password..."
sudo mysql -e "UPDATE mysql.user SET Password=PASSWORD('root') WHERE User='root';"
sudo mysql -e "FLUSH PRIVILEGES;"

# Install PHP
echo "Installing PHP and necessary modules..."
sudo apt-get install -y php libapache2-mod-php php-mysql

# Restart Apache to load PHP module
echo "Restarting Apache to load PHP module..."
sudo systemctl restart apache2

# Create a PHP info file for testing
echo "Creating PHP info file..."
echo "<?php phpinfo(); ?>" | sudo tee /var/www/html/info.php

# Set correct permissions for web root
echo "Setting permissions for /var/www/html..."
sudo chown -R www-data:www-data /var/www/html
sudo chmod -R 755 /var/www/html

echo "LAMP installation completed. You can test PHP by visiting http://your_raspberry_pi_ip/info.php"

# Display the IP address of the Raspberry Pi
echo "Your Raspberry Pi IP address is: $(hostname -I | awk '{print $1}')"
