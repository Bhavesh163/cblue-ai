#!/bin/bash

echo "Stopping Cblue AI Services..."
echo ""

pkill -f "python.*app.py" && echo "✓ Frontend stopped"
pkill -f "python.*main.py" && echo "✓ API stopped"
pkill -f "python.*worker.py" && echo "✓ Worker stopped"

echo ""
echo "All services stopped."
