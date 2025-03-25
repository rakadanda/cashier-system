#!/bin/bash

# Backend setup
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
flask db upgrade
python seed.py &

# Frontend setup
cd ../frontend
npm install
npm run dev &

# Wait for servers to start
sleep 5
echo "🚀 System ready! Access the app at http://localhost:5173"
