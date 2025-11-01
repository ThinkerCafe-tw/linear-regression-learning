# GitHub Pages 部署指南

## 🌐 為什麼使用 GitHub Pages？

- ✅ 不需要本地伺服器，直接在線上使用
- ✅ 可以分享連結給學生或同事
- ✅ 隨時隨地訪問，手機、平板都能用
- ✅ 完全免費
- ✅ 自動解決 CORS 問題

## 📋 部署步驟

### 方法 1：透過網頁介面（最簡單）

#### 步驟 1：建立 GitHub Repository

1. 前往 https://github.com
2. 登入您的帳號
3. 點擊右上角 `+` → `New repository`
4. 設定：
   - Repository name: `linear-regression-learning`
   - Description: `線性迴歸互動學習系統`
   - ✅ Public（必須是 Public 才能用 GitHub Pages）
   - ✅ Add a README file
5. 點擊 `Create repository`

#### 步驟 2：上傳檔案

1. 在 repository 頁面，點擊 `Add file` → `Upload files`
2. 上傳以下檔案：
   - `線性迴歸學習系統.html`
   - `linear_regression_knowledge.json`
3. 在 Commit message 輸入：`Initial commit: 上傳學習系統`
4. 點擊 `Commit changes`

#### 步驟 3：啟用 GitHub Pages

1. 點擊 repository 上方的 `Settings`
2. 在左側選單找到 `Pages`
3. 在 `Source` 區域：
   - Branch: 選擇 `main`
   - Folder: 選擇 `/ (root)`
4. 點擊 `Save`
5. 等待 1-2 分鐘，頁面會顯示網址

#### 步驟 4：訪問您的學習系統

您的網址會是：
```
https://[您的GitHub用戶名].github.io/linear-regression-learning/線性迴歸學習系統.html
```

例如：
```
https://andrew-tang.github.io/linear-regression-learning/線性迴歸學習系統.html
```

---

### 方法 2：使用 Git 指令（進階）

如果您熟悉 Git，可以用指令：

```bash
# 1. 在 GitHub 建立 repository 後，取得 repository URL

# 2. 進入線性迴歸資料夾
cd "/Users/thinkercafe/Library/Mobile Documents/com~apple~CloudDocs/MEGA下載/RECORD/授課與演講/線性迴歸"

# 3. 初始化 Git（如果還沒有）
git init

# 4. 只加入需要的檔案
git add 線性迴歸學習系統.html
git add linear_regression_knowledge.json
git add README.md

# 5. 建立 commit
git commit -m "Initial commit: 上傳線性迴歸學習系統"

# 6. 連接到 GitHub（替換成您的 repository URL）
git remote add origin https://github.com/[您的用戶名]/linear-regression-learning.git

# 7. 推送到 GitHub
git branch -M main
git push -u origin main

# 8. 啟用 GitHub Pages（需要在網頁介面設定）
```

---

## 🎯 建議的檔案結構

在 GitHub repository 中，建議這樣組織：

```
linear-regression-learning/
├── index.html                              ← 重新命名為 index.html（推薦）
├── linear_regression_knowledge.json
├── README.md
└── docs/                                   ← 可選：放原始教材
    ├── ch02_1.pdf
    ├── 線性回歸.pdf
    └── 沙龍線性回歸實作.pptx
```

### 為什麼要重新命名為 index.html？

如果主檔案命名為 `index.html`，您的網址會更簡潔：
```
https://[用戶名].github.io/linear-regression-learning/
```

而不是：
```
https://[用戶名].github.io/linear-regression-learning/線性迴歸學習系統.html
```

---

## 📝 重新命名檔案（可選）

如果想要簡潔的網址：

```bash
# 複製一份並重新命名
cp "線性迴歸學習系統.html" index.html

# 然後上傳 index.html 到 GitHub
```

---

## 🔧 更新內容

當您需要更新內容時：

### 透過網頁介面：
1. 前往 GitHub repository
2. 點擊要更新的檔案
3. 點擊右上角的鉛筆圖示（編輯）
4. 修改後點擊 `Commit changes`
5. 等待 1-2 分鐘自動重新部署

### 使用 Git 指令：
```bash
# 修改檔案後
git add .
git commit -m "更新學習內容"
git push
```

---

## 🌍 分享給他人

部署完成後，只需分享網址：
```
https://[您的用戶名].github.io/linear-regression-learning/
```

任何人都可以：
- 直接訪問，不需要下載
- 在手機、平板、電腦上使用
- 追蹤自己的學習進度（使用 localStorage）

---

## 💡 額外優化建議

### 1. 加入 README.md

在 GitHub repository 首頁顯示說明：

```markdown
# 線性迴歸互動學習系統

整合多元教材資源的互動式線性迴歸學習平台

## 🚀 立即使用

前往：https://[您的用戶名].github.io/linear-regression-learning/

## ✨ 特色

- 📊 11 個學習模組（基礎→進階）
- 🎯 3 種學習路徑
- ✨ 互動式介面
- 🌓 深色模式
- 📐 數學公式渲染

## 📚 內容來源

- 中國醫藥大學生物統計中心教材
- Wooldridge 計量經濟學
- R 語言實作範例
```

### 2. 加入自訂網域（可選）

如果您有自己的網域名稱，可以在 GitHub Pages 設定中綁定。

### 3. 加入 Google Analytics（可選）

追蹤使用情況。

---

## ❓ 常見問題

### Q1: GitHub Pages 免費嗎？
**A:** 是的，完全免費，沒有流量限制。

### Q2: 可以設定為私密嗎？
**A:** GitHub Pages 需要 Public repository。如果需要私密，可以考慮使用 Vercel、Netlify 等服務。

### Q3: 更新會立即生效嗎？
**A:** 通常 1-2 分鐘內就會更新，有時可能需要清除瀏覽器快取。

### Q4: 可以使用中文檔名嗎？
**A:** 可以，但網址會變成編碼後的形式。建議主要檔案用英文命名（如 index.html）。

### Q5: 手機可以正常使用嗎？
**A:** 可以！系統已經做了響應式設計，手機、平板都能完美顯示。

---

## 🎉 部署完成後

恭喜！您的線性迴歸學習系統已經上線了！

可以：
- 📤 分享連結給學生
- 📱 在任何裝置上使用
- 🔄 隨時更新內容
- 📊 追蹤使用情況（如果設定了 Analytics）

---

**需要協助？**

如果部署過程遇到問題，可以：
1. 查看 GitHub Pages 官方文件：https://pages.github.com/
2. 檢查 repository 的 Actions 頁面查看部署狀態
3. 確認檔案都正確上傳且可以訪問
