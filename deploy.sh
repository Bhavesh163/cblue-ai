#!/bin/bash
set -e

echo "🚀 Deploying Cblue AI to cblue.co.th..."

# Update system
sudo apt update
sudo apt install -y python3-pip python3-venv nginx certbot python3-certbot-nginx

# Create deployment directory
sudo mkdir -p /var/www/cblue-ai
sudo cp -r . /var/www/cblue-ai/
sudo chown -R www-data:www-data /var/www/cblue-ai

# Setup Python virtual environment
cd /var/www/cblue-ai
sudo -u www-data python3 -m venv venv
sudo -u www-data venv/bin/pip install -r services/api/requirements.txt

# Setup SSL certificate
sudo certbot --nginx -d cblue.co.th -d www.cblue.co.th --non-interactive --agree-tos -m cblue.thailand@gmail.com

# Install nginx config
sudo cp infra/nginx-production.conf /etc/nginx/sites-available/cblue
sudo ln -sf /etc/nginx/sites-available/cblue /etc/nginx/sites-enabled/
sudo rm -f /etc/nginx/sites-enabled/default
sudo nginx -t
sudo systemctl restart nginx

# Install and start API service
sudo cp infra/cblue-api.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable cblue-api
sudo systemctl restart cblue-api

echo "✅ Deployment complete!"
echo "🌐 Your site is live at https://cblue.co.th"
echo ""
echo "📊 Check status:"
echo "  API: sudo systemctl status cblue-api"
echo "  Nginx: sudo systemctl status nginx"
echo ""
echo "📝 View logs:"
echo "  API: sudo journalctl -u cblue-api -f"
echo "  Nginx: sudo tail -f /var/log/nginx/error.log"
