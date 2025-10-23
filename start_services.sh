#!/bin/bash

echo "========================================="
echo "Cblue AI Customer Support - Startup"
echo "========================================="
echo ""

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Check Redis
echo -n "Checking Redis... "
if redis-cli ping > /dev/null 2>&1; then
    echo -e "${GREEN}✓ Running${NC}"
else
    echo -e "${YELLOW}⚠ Not running${NC}"
    echo "  Starting Redis with Docker..."
    docker run -d --name cblue-redis -p 6379:6379 redis:alpine > /dev/null 2>&1
    sleep 2
    if redis-cli ping > /dev/null 2>&1; then
        echo -e "  ${GREEN}✓ Redis started${NC}"
    else
        echo -e "  ${RED}✗ Failed to start Redis${NC}"
        echo "  Please install Redis: sudo apt-get install redis-server"
    fi
fi
echo ""

# Start Frontend
echo -n "Starting Frontend (port 3000)... "
cd frontend
source venv/bin/activate
pkill -f "python.*app.py" > /dev/null 2>&1
python app.py > ../logs/frontend.log 2>&1 &
FRONTEND_PID=$!
sleep 2
if curl -s http://localhost:3000 > /dev/null; then
    echo -e "${GREEN}✓ Running (PID: $FRONTEND_PID)${NC}"
else
    echo -e "${RED}✗ Failed${NC}"
fi
cd ..
echo ""

# Start API
echo -n "Starting API (port 8010)... "
cd services/api
source venv/bin/activate
pkill -f "python.*main.py" > /dev/null 2>&1
python main.py > ../../logs/api.log 2>&1 &
API_PID=$!
sleep 2
if curl -s http://localhost:8010/health > /dev/null 2>&1; then
    echo -e "${GREEN}✓ Running (PID: $API_PID)${NC}"
else
    echo -e "${YELLOW}⚠ Check logs/api.log${NC}"
fi
cd ../..
echo ""

# Start Worker
echo -n "Starting Worker... "
cd services/worker
source venv/bin/activate
pkill -f "python.*worker.py" > /dev/null 2>&1
python worker.py > ../../logs/worker.log 2>&1 &
WORKER_PID=$!
sleep 1
if ps -p $WORKER_PID > /dev/null; then
    echo -e "${GREEN}✓ Running (PID: $WORKER_PID)${NC}"
else
    echo -e "${YELLOW}⚠ Check logs/worker.log${NC}"
fi
cd ../..
echo ""

echo "========================================="
echo "Services Status"
echo "========================================="
echo ""
echo "🌐 Frontend:  http://localhost:3000"
echo "🔌 API:       http://localhost:8010"
echo "📊 Health:    http://localhost:8010/health"
echo ""
echo "📧 Contact: cblue.thailand@gmail.com"
echo "📱 Phone: +66 (0)81 854 4291"
echo ""
echo "Logs:"
echo "  - Frontend: logs/frontend.log"
echo "  - API:      logs/api.log"
echo "  - Worker:   logs/worker.log"
echo ""
echo "To stop services: ./stop_services.sh"
echo "========================================="
