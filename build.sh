#!/bin/bash
echo "Derleme başlıyor..."
g++ src/engine/scanner.cpp -o scanner
pip install -r requirements.txt
echo "Sistem hazır. 'python3 src/interface/dashboard.py' ile başlat."
