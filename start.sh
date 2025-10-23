#!/bin/bash
set -e

echo "🚀 Starting Cblue AI System"

# 1. Start infrastructure
echo "📦 Starting Redis, Postgres, Nginx..."
docker-compose up -d redis postgres nginx

# 2. Start model service (GPU)
echo "🤖 Starting Model Service on GPU..."
cd services/model_service
python run.py --socket /var/run/openthaigpt.sock &
MODEL_PID=$!
cd ../..

# 3. Start worker
echo "⚙️ Starting Worker..."
cd services/worker
python worker.py &
WORKER_PID=$!
cd ../..

# 4. Start API
echo "🌐 Starting API..."
cd services/api
uvicorn main:app --host 0.0.0.0 --port 8000 &
API_PID=$!
cd ../..

# 5. Start frontend
echo "🎨 Starting Frontend..."
cd frontend
python app.py &
FRONTEND_PID=$!
cd ..

echo "✅ All services started!"
echo "Frontend: http://localhost:8080"
echo "API: http://localhost:8000"
echo "Grafana: http://localhost:3000"

# Cleanup on exit
trap "kill $MODEL_PID $WORKER_PID $API_PID $FRONTEND_PID; docker-compose down" EXIT

wait
