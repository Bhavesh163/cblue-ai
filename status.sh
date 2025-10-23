#!/bin/bash
echo "🔍 Cblue AI System Status"
echo "=========================="
echo ""

# Check Redis
echo "📦 Redis:"
docker ps | grep redis > /dev/null && echo "  ✅ Running" || echo "  ❌ Not running"

# Check Worker
echo "⚙️ Worker:"
ps aux | grep "services/worker/worker.py" | grep -v grep > /dev/null && echo "  ✅ Running (PID: $(cat logs/worker.pid 2>/dev/null || echo 'unknown'))" || echo "  ❌ Not running"

# Check API
echo "🌐 API:"
ps aux | grep "uvicorn.*8000" | grep -v grep > /dev/null && echo "  ✅ Running (PID: $(cat logs/api.pid 2>/dev/null || echo 'unknown'))" || echo "  ❌ Not running"
curl -s http://localhost:8000/health > /dev/null && echo "  ✅ Health check passed" || echo "  ❌ Health check failed"

# Check Frontend
echo "🎨 Frontend:"
ps aux | grep "frontend/app.py" | grep -v grep > /dev/null && echo "  ✅ Running (PID: $(cat logs/frontend.pid 2>/dev/null || echo 'unknown'))" || echo "  ❌ Not running"
curl -s http://localhost:8080 > /dev/null && echo "  ✅ Accessible" || echo "  ❌ Not accessible"

echo ""
echo "🌍 Access URLs:"
echo "  Frontend: http://localhost:8080"
echo "  API: http://localhost:8000"
echo "  API Docs: http://localhost:8000/docs"
echo ""
echo "📊 Queue Status:"
docker exec cblue-ai-redis-1 redis-cli LLEN job_queue 2>/dev/null | xargs echo "  Jobs in queue:"
