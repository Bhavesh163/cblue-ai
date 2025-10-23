#!/bin/bash
cd "/mnt/c/Cblue + customer support/cblue-ai"

echo "🚀 Starting Cblue AI System..."

# Start worker
echo "⚙️ Starting Worker..."
cd services/worker
source venv/bin/activate
python worker.py > ../../logs/worker.log 2>&1 &
WORKER_PID=$!
echo "Worker PID: $WORKER_PID"
cd ../..

# Start API
echo "🌐 Starting API..."
cd services/api
source venv/bin/activate
uvicorn main:app --host 0.0.0.0 --port 8010 > ../../logs/api.log 2>&1 &
API_PID=$!
echo "API PID: $API_PID"
cd ../..

# Wait for API to start
sleep 3

# Start Frontend
echo "🎨 Starting Frontend..."
cd frontend
source venv/bin/activate
python app.py > ../logs/frontend.log 2>&1 &
FRONTEND_PID=$!
echo "Frontend PID: $FRONTEND_PID"
cd ..

echo ""
echo "✅ All services started!"
echo "Frontend: http://localhost:3000"
echo "API: http://localhost:8010"
echo "API Health: http://localhost:8010/health"
echo ""
echo "PIDs: Worker=$WORKER_PID API=$API_PID Frontend=$FRONTEND_PID"
echo "Logs in: logs/"
echo ""
echo "Press Ctrl+C to stop all services"

# Save PIDs
echo "$WORKER_PID" > logs/worker.pid
echo "$API_PID" > logs/api.pid
echo "$FRONTEND_PID" > logs/frontend.pid

# Wait
trap "kill $WORKER_PID $API_PID $FRONTEND_PID 2>/dev/null" EXIT
wait
