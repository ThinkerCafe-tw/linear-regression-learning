#!/bin/bash

echo "╔═══════════════════════════════════════════════════════════╗"
echo "║       線性迴歸學習系統 - GitHub Pages 快速部署           ║"
echo "╚═══════════════════════════════════════════════════════════╝"
echo ""

# 檢查是否已經初始化 git
if [ ! -d .git ]; then
    echo "📦 步驟 1：初始化 Git repository..."
    git init
    echo "✅ Git repository 已初始化"
    echo ""
else
    echo "✅ Git repository 已存在"
    echo ""
fi

# 檢查是否有 remote
if ! git remote | grep -q "origin"; then
    echo "⚠️  尚未設定 GitHub repository"
    echo ""
    echo "請先在 GitHub 建立一個新的 repository，然後輸入 repository URL："
    echo "例如：https://github.com/your-username/linear-regression-learning.git"
    echo ""
    read -p "Repository URL: " repo_url

    if [ -z "$repo_url" ]; then
        echo "❌ 未輸入 URL，部署取消"
        exit 1
    fi

    git remote add origin "$repo_url"
    echo "✅ Repository 已連接"
    echo ""
fi

echo "📝 步驟 2：加入檔案到 Git..."
git add index.html
git add linear_regression_knowledge.json
git add README.md
git add "GitHub-Pages-部署指南.md"
git add "使用說明.md"
echo "✅ 檔案已加入"
echo ""

echo "💾 步驟 3：建立 commit..."
read -p "Commit 訊息（按 Enter 使用預設）: " commit_msg
if [ -z "$commit_msg" ]; then
    commit_msg="更新線性迴歸學習系統"
fi
git commit -m "$commit_msg"
echo "✅ Commit 已建立"
echo ""

echo "🚀 步驟 4：推送到 GitHub..."
# 檢查是否是第一次推送
if git show-ref --verify --quiet refs/heads/main; then
    git push origin main
else
    git branch -M main
    git push -u origin main
fi

if [ $? -eq 0 ]; then
    echo ""
    echo "╔═══════════════════════════════════════════════════════════╗"
    echo "║                  🎉 部署成功！                            ║"
    echo "╚═══════════════════════════════════════════════════════════╝"
    echo ""
    echo "📋 後續步驟："
    echo ""
    echo "1. 前往您的 GitHub repository"
    echo "2. 點擊 Settings → Pages"
    echo "3. 在 Source 選擇 main branch"
    echo "4. 點擊 Save"
    echo "5. 等待 1-2 分鐘"
    echo ""
    echo "🌐 您的學習系統網址將會是："
    echo "   https://[您的用戶名].github.io/[repository名稱]/"
    echo ""
    echo "📖 詳細說明請查看：GitHub-Pages-部署指南.md"
    echo ""
else
    echo ""
    echo "❌ 推送失敗"
    echo "請檢查："
    echo "1. GitHub repository URL 是否正確"
    echo "2. 是否有權限推送到該 repository"
    echo "3. 網路連線是否正常"
    echo ""
fi
