# 100% Free Deployment Guide

## Option A: AWS Free Tier (Recommended - Full Control)

### Setup (5 minutes):
1. Go to https://aws.amazon.com/free
2. Create account (requires credit card, but won't charge)
3. Launch EC2 instance:
   - Choose Ubuntu 22.04
   - Select t2.micro (free tier)
   - Download key pair
4. Connect and deploy:
```bash
ssh -i your-key.pem ubuntu@your-ec2-ip
git clone <your-repo>
cd cblue-ai
sudo ./deploy.sh
```
5. Point cblue.co.th to EC2 IP in your domain settings

**Free for:** 12 months, then ~$8/month

---

## Option B: Split Deployment (100% Free Forever)

### Step 1: Deploy API to Render.com (Free)

1. Go to https://render.com
2. Sign up with GitHub
3. Click "New +" → "Web Service"
4. Connect your GitHub repo
5. Settings:
   - Name: cblue-api
   - Region: Singapore
   - Branch: main
   - Build Command: `pip install -r services/api/requirements.txt`
   - Start Command: `uvicorn services.api.main:app --host 0.0.0.0 --port $PORT`
6. Click "Create Web Service"
7. Copy your URL (e.g., `cblue-api.onrender.com`)

### Step 2: Update Chatbot

Edit `frontend/chatbot-integration.js`:
```javascript
const API_URL = 'https://cblue-api.onrender.com';
```

### Step 3: Deploy Frontend to Vercel (Free)

1. Go to https://vercel.com
2. Sign up with GitHub
3. Click "Add New" → "Project"
4. Import your repo
5. Settings:
   - Framework: Other
   - Root Directory: `frontend`
   - Build Command: (leave empty)
6. Click "Deploy"
7. Add custom domain: cblue.co.th

**Done!** 100% free forever.

**Trade-off:** API sleeps after 15 min inactivity (30 sec wake-up time on first request)

---

## Option C: Oracle Cloud (Free Forever)

1. Sign up at https://oracle.com/cloud/free
2. Create "Always Free" compute instance
3. Choose Ubuntu (ARM)
4. Deploy same as AWS

**Free forever** - No time limit!

---

## Comparison

| Option | Cost | Speed | Complexity |
|--------|------|-------|------------|
| AWS Free Tier | Free 12mo | Fast | Easy |
| Render + Vercel | Free forever | 30s delay | Easiest |
| Oracle Cloud | Free forever | Fast | Medium |

---

## My Recommendation

**For cblue.co.th:**

Use **Render + Vercel** (Option B):
- ✅ 100% free forever
- ✅ No server management
- ✅ Auto HTTPS
- ✅ Takes 10 minutes to setup
- ⚠️ 30 second delay on first chatbot use (acceptable for most sites)

**If you need instant response:**
- Use AWS Free Tier for 12 months
- Then switch to Oracle Cloud (free forever)
