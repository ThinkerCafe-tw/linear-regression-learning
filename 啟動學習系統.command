#!/bin/bash
cd "$(dirname "$0")"
echo "🚀 正在啟動線性迴歸學習系統..."
echo "📚 伺服器位址：http://localhost:8000"
echo "📖 請在瀏覽器開啟：http://localhost:8000/線性迴歸學習系統.html"
echo ""
echo "⏹  按 Ctrl+C 停止伺服器"
echo "----------------------------------------"
python3 -m http.server 8000
