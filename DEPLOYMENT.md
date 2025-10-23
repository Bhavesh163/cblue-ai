# Cblue AI - Deployment Guide

## Architecture Overview

```
┌─────────────┐     WebSocket      ┌──────────────┐
│   Frontend  │◄──────────────────►│   FastAPI    │
│   (Flask)   │                    │   Backend    │
└─────────────┘                    └──────┬───────┘
                                          │
                                          ▼
                                   ┌──────────────┐
                                   │    Redis     │
                                   │    Queue     │
                                   └──────┬───────┘
                                          │
                                          ▼
                                   ┌──────────────┐
                                   │    Worker    │
                                   │  (Retrieval) │
                                   └──────┬───────┘
                                          │ UNIX Socket
                                          ▼
                                   ┌──────────────┐
                                   │ Model Service│
                                   │ OpenThaiGPT  │
                                   │ 14B FP32 GPU │
                                   └──────────────┘
```

## Prerequisites

- Ubuntu 24.04 (WSL2 or native)
- NVIDIA RTX 3090 with CUDA 12.1+
- Python 3.11+
- Docker & Docker Compose
- 32GB+ RAM
- Model at: `/home/ballhog/Litigation_ai/models/14b`

## Installation

### 1. Install System Dependencies

```bash
# CUDA & GPU drivers
sudo apt update
sudo apt install nvidia-driver-535 nvidia-cuda-toolkit

# Python & tools
sudo apt install python3.11 python3.11-venv python3-pip redis-server postgresql

# Docker
curl -fsSL https://get.docker.com | sh
sudo usermod -aG docker $USER
```

### 2. Setup Python Environments

```bash
cd cblue-ai

# Model service (GPU)
cd services/model_service
python3.11 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
deactivate
cd ../..

# Worker
cd services/worker
python3.11 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
deactivate
cd ../..

# Frontend
cd frontend
python3.11 -m venv venv
source venv/bin/activate
pip install Flask flask-cors requests
deactivate
cd ..
```

### 3. Configure Environment

```bash
# Create .env file
cat > .env << EOF
MODEL_PATH=/home/ballhog/Litigation_ai/models/14b
MODEL_SOCKET=/var/run/openthaigpt.sock
REDIS_URL=redis://localhost:6379/0
DATABASE_URL=postgresql://cblue:changeme@localhost:5432/cblue_ai
MAX_QUEUE_LENGTH=50
MAX_TOKENS=512
EOF
```

## Running the System

### Option 1: Automated Startup

```bash
./start.sh
```

### Option 2: Manual Startup

```bash
# 1. Infrastructure
docker-compose up -d redis postgres nginx prometheus grafana

# 2. Model Service (GPU - run in separate terminal)
cd services/model_service
source venv/bin/activate
python run.py --model-path /home/ballhog/Litigation_ai/models/14b --socket /var/run/openthaigpt.sock

# 3. Worker (run in separate terminal)
cd services/worker
source venv/bin/activate
python worker.py

# 4. API (run in separate terminal)
cd services/api
uvicorn main:app --host 0.0.0.0 --port 8000

# 5. Frontend (run in separate terminal)
cd frontend
source venv/bin/activate
python app.py
```

## Access Points

- **Frontend**: http://localhost:8080
- **API**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs
- **Grafana**: http://localhost:3000 (admin/admin)
- **Prometheus**: http://localhost:9090

## Monitoring

### Check System Health

```bash
# API health
curl http://localhost:8000/health

# Queue length
redis-cli LLEN job_queue

# GPU usage
nvidia-smi

# Model service status
ls -la /var/run/openthaigpt.sock
```

### Logs

```bash
# Docker services
docker-compose logs -f

# Model service
tail -f services/model_service/model.log

# Worker
tail -f services/worker/worker.log
```

## Production Checklist

- [ ] Change default passwords in docker-compose.yml
- [ ] Setup SSL certificates in infra/ssl/
- [ ] Configure firewall (ufw allow 80,443)
- [ ] Setup log rotation
- [ ] Configure backup cron jobs
- [ ] Setup Sentry for error tracking
- [ ] Enable Prometheus alerts
- [ ] Test OOM recovery
- [ ] Load test with 50+ concurrent users
- [ ] Document escalation procedures

## Troubleshooting

### Model Service Won't Start

```bash
# Check GPU
nvidia-smi

# Check CUDA
python -c "import torch; print(torch.cuda.is_available())"

# Clear GPU memory
sudo fuser -v /dev/nvidia*
sudo kill -9 <PID>
```

### Queue Backing Up

```bash
# Check worker status
ps aux | grep worker.py

# Clear queue (emergency)
redis-cli DEL job_queue

# Scale workers (if needed)
# Start additional worker instance
```

### OOM Errors

```bash
# Reduce max_tokens in .env
# Restart model service with memory limit
ulimit -v 20000000  # 20GB
python run.py ...
```

## Backup & Recovery

### Daily Backup

```bash
# Database
docker exec postgres pg_dump -U cblue cblue_ai > backup_$(date +%Y%m%d).sql

# FAISS index
tar -czf faiss_backup_$(date +%Y%m%d).tar.gz common/retrieval/index/

# Config
cp .env .env.backup
```

### Restore

```bash
# Database
docker exec -i postgres psql -U cblue cblue_ai < backup_20251022.sql

# FAISS
tar -xzf faiss_backup_20251022.tar.gz -C common/retrieval/
```

## Performance Tuning

### GPU Optimization

```python
# In model_service/run.py
torch.cuda.set_per_process_memory_fraction(0.95)  # Use 95% of GPU
torch.backends.cudnn.benchmark = True  # Faster inference
```

### Redis Tuning

```bash
# In docker-compose.yml, add to redis command:
--maxmemory 2gb --maxmemory-policy allkeys-lru
```

## Security Notes

- Model socket at `/var/run/openthaigpt.sock` has 666 permissions (local only)
- API uses CORS - restrict origins in production
- PII redaction active for phone, email, Thai ID
- Legal disclaimer shown for legal queries
- Rate limit: 10 req/s per IP (Nginx)
- Queue limit: 50 jobs max

## Support

- Email: cblue.thailand@gmail.com
- Phone: +66 (0)81 854 4291
