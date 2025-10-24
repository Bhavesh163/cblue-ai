# Deployment Guide for cblue.co.th

## Prerequisites
- Ubuntu/Debian VPS with root access
- Domain cblue.co.th pointing to your server IP

## One-Command Deployment

```bash
./deploy.sh
```

This will:
1. Install nginx, Python, and SSL certificates
2. Deploy frontend to `/var/www/cblue-ai/frontend`
3. Start API server on port 8010
4. Configure nginx to serve both
5. Enable HTTPS with Let's Encrypt

## Manual Deployment Steps

### 1. Upload files to server
```bash
scp -r . user@your-server-ip:/tmp/cblue-ai
```

### 2. Run deployment script on server
```bash
ssh user@your-server-ip
cd /tmp/cblue-ai
sudo ./deploy.sh
```

## Post-Deployment

### Check Services
```bash
sudo systemctl status cblue-api
sudo systemctl status nginx
```

### View Logs
```bash
# API logs
sudo journalctl -u cblue-api -f

# Nginx logs
sudo tail -f /var/log/nginx/error.log
```

### Restart Services
```bash
sudo systemctl restart cblue-api
sudo systemctl restart nginx
```

## Update Deployment

```bash
cd /var/www/cblue-ai
sudo git pull  # or upload new files
sudo systemctl restart cblue-api
```

## Architecture

```
User Browser
    ↓
https://cblue.co.th (Nginx)
    ↓
    ├─→ /          → Frontend (HTML/CSS/JS)
    └─→ /api/*     → API Server (Port 8010)
                        ↓
                   Knowledge Base
```

## Important Notes

✅ **API server MUST be running** for chatbot to work
✅ Chatbot automatically detects localhost vs production
✅ SSL certificates auto-renew via certbot
✅ API runs as systemd service (auto-restart on failure)

## Troubleshooting

**Chatbot not working?**
```bash
# Check if API is running
curl http://localhost:8010/health

# Check API logs
sudo journalctl -u cblue-api -n 50
```

**502 Bad Gateway?**
- API server is down: `sudo systemctl start cblue-api`
- Check logs: `sudo journalctl -u cblue-api -f`
