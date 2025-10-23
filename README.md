# Cblue AI - Customer Support & Litigation AI

Monorepo for Cblue's AI-powered customer support with OpenThaiGPT 1.5 14B on RTX 3090.

## Architecture

```
Frontend (React) ←WebSocket→ FastAPI ←Redis Queue→ Worker ←UNIX Socket→ Model Service (GPU)
                                         ↓
                                   Retrieval (FAISS+BM25)
```

## Structure

- `/common/` - Shared utilities (NLP, retrieval, prompting, schemas)
- `/services/api/` - FastAPI backend (WebSocket, auth, queue client)
- `/services/model_service/` - GPU model server (OpenThaiGPT 14B FP32)
- `/services/worker/` - Queue worker (retrieval + model inference)
- `/frontend/` - React widget (existing, unchanged)
- `/infra/` - Docker, Nginx, monitoring configs

## Quick Start

```bash
# 1. Start infrastructure
docker-compose up -d redis postgres nginx

# 2. Start model service (GPU, outside Docker)
cd services/model_service
python run.py --socket /var/run/openthaigpt.sock

# 3. Start worker
cd services/worker
python worker.py

# 4. Start API
cd services/api
uvicorn main:app --host 0.0.0.0 --port 8000

# 5. Frontend already embedded in Flask app.py
```

## Key Features

- Single GPU process, queued inference (1 active job)
- Hybrid retrieval (BM25 + FAISS)
- Streaming responses via WebSocket
- PII redaction, legal disclaimers
- Rate limiting, memory guards
- Fallback to small CPU model on OOM
