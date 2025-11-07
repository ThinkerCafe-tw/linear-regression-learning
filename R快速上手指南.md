# 給初學者的 10 分鐘 R 快速上手指南
**線性迴歸實戰入門**

> **適用對象**：統計學、交通工程、資料分析課程的學生

> 📌 **教學目標**：
> - **學生端**：零基礎者可在 10 分鐘內完成第一個迴歸分析
> - **教師端**：可直接用於課堂演示或指定為預習作業
> - **學習成果**：學生能解讀 summary() 輸出並繪製迴歸線

---

## 第一步：安裝 R 和 RStudio（3 分鐘）

### ⚠️ 給教師的建議
- **課前作業**：請學生提前安裝 R + RStudio，並截圖回報成功畫面
- **Plan B**：準備 [Posit Cloud](https://posit.cloud/) 帳號（免安裝的線上版 RStudio）
- **課堂時間**：只用於「確認安裝」和「開始分析」，不用於除錯安裝問題

### 為什麼需要兩個軟體？
- **R**：統計運算引擎（就像汽車引擎）
- **RStudio**：操作介面（就像汽車儀表板）

### 安裝步驟

#### 1. 安裝 R（必須先裝）
1. 前往 https://cran.r-project.org/
2. 點選你的作業系統：
   - **Windows**：Download R for Windows → base → Download R 4.x.x
   - **macOS**：Download R for macOS → R-4.x.x-arm64.pkg（M1/M2 晶片）或 R-4.x.x.pkg（Intel 晶片）
   - **Linux**：依照發行版指示（Ubuntu: `sudo apt install r-base`）

3. 執行安裝檔，**全部使用預設設定**，一直按「下一步」即可

【📸 截圖 ①：R 官網下載頁面 + Windows 安裝程式】

#### 2. 安裝 RStudio（強烈建議）
1. 前往 https://posit.co/download/rstudio-desktop/
2. 下載 **RStudio Desktop（免費版）**
3. 執行安裝檔，同樣使用預設設定

> **💡 如果安裝失敗怎麼辦？**
> 使用 [Posit Cloud](https://posit.cloud/)（免費版），直接在瀏覽器中使用 RStudio，不需安裝任何軟體。註冊後即可立即開始。

---

## 第二步：認識 RStudio 介面（2 分鐘）

開啟 RStudio，你會看到四個區域：

```
┌─────────────────┬─────────────────┐
│                 │                 │
│   程式碼編輯區   │   環境/變數區    │
│   (左上)        │   (右上)        │
│                 │                 │
├─────────────────┼─────────────────┤
│                 │                 │
│   Console 區    │   圖表/檔案區    │
│   (左下)        │   (右下)        │
│                 │                 │
└─────────────────┴─────────────────┘
```

### 重要區域說明
- **Console（左下）**：輸入指令後按 Enter 立即執行
- **程式碼編輯區（左上）**：寫多行程式碼，按 `Ctrl+Enter`（Windows）或 `Cmd+Enter`（Mac）執行當前行
- **環境區（右上）**：顯示你建立的變數和資料
- **圖表區（右下）**：顯示繪圖結果

【📸 截圖 ②：RStudio 完整介面，標註四個區域】

---

## 第三步：第一個線性迴歸（5 分鐘）

### 情境說明
我們要分析：**汽車重量（wt）對油耗（mpg）的影響**
- 資料集：`mtcars`（R 內建資料，32 款汽車）
- 問題：車子越重，油耗越差嗎？

### ⚠️ 單位說明（避免混淆）
- **mpg = Miles Per Gallon**：一加侖汽油可跑多少英里
  - mpg = 20：很耗油（一加侖只能跑 20 英里）
  - mpg = 30：較省油（一加侖可跑 30 英里）
- 台灣常用的「公升/百公里」恰好相反！
- **迴歸結果**：係數為負 → 車重↑ → mpg↓ → **越耗油** ✓

### 步驟 1：載入並查看資料

在 **Console** 輸入以下指令（一次一行，按 Enter）：

```r
# 查看 mtcars 資料集的前 6 筆
head(mtcars)
```

**你會看到：**包含 mpg（油耗）、wt（車重）、hp（馬力）等 11 個變數的資料表

---

### 步驟 2：繪製散佈圖（視覺化）

```r
# 繪製油耗 vs 車重的散佈圖
plot(mtcars$wt, mtcars$mpg,
     xlab = "車重 (1000 lbs)",
     ylab = "油耗 (英里/加侖)",
     main = "車重與油耗的關係",
     pch = 19,           # 實心圓點
     col = "blue")       # 藍色
```

**觀察圖表**：你會發現車重越重，油耗數字越低（越耗油）

【📸 截圖 ③：散佈圖，標註「明顯的負相關」】

---

### 步驟 3：建立線性迴歸模型 ⭐

```r
# 建立模型：油耗 ~ 車重
model <- lm(mpg ~ wt, data = mtcars)

# 查看結果
summary(model)
```

**你會看到以下輸出**（這是最重要的部分！）：

```
Call:
lm(formula = mpg ~ wt, data = mtcars)

Residuals:
    Min      1Q  Median      3Q     Max
-4.5432 -2.3647 -0.1252  1.4096  6.8727

Coefficients:
            Estimate Std. Error t value Pr(>|t|)
(Intercept)  37.2851     1.8776  19.858  < 2e-16 ***
wt           -5.3445     0.5591  -9.559 1.29e-10 ***
---
Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1

Residual standard error: 3.046 on 30 degrees of freedom
Multiple R-squared:  0.7528,    Adjusted R-squared:  0.7446
F-statistic: 91.38 on 1 and 30 DF,  p-value: 1.294e-10
```

【📸 截圖 ④：summary(model) 完整輸出】

### 📌 第一次看結果：先忽略 90%

**現階段只看這三個數字：**
1. `wt` 那行的 `Estimate`：**-5.3445**（斜率）
2. `wt` 那行的 `Pr(>|t|)`：**1.29e-10**（p-value）
3. 最下面的 `R-squared`：**0.7528**

**其他的（Std. Error, t value, F-statistic）第二堂課再說** ✓

---

## 第四步：解讀結果（關鍵！）

### 迴歸方程式
```
mpg = 37.29 - 5.34 × wt
```

**白話文解釋**：
- **37.29**（截距）：車重為 0 時的理論油耗（實際無意義，因為車重不可能為 0）
- **-5.34**（斜率）：車重每增加 1000 磅，油耗減少 5.34 英里/加侖
  - 👉 **負號表示車越重油耗越差**

### 統計顯著性
看 `Pr(>|t|)` 這一欄：
- `wt` 的 p-value = `1.29e-10`（非常小！）
- **結論**：車重對油耗有顯著影響（p < 0.001）

### 模型配適度
- **R-squared: 0.7528**
  - 表示車重可以解釋 75.28% 的油耗變異
  - 👉 **這是一個配適度很好的模型**

---

## 第五步：繪製迴歸線

```r
# 在原本的散佈圖上加上迴歸線
plot(mtcars$wt, mtcars$mpg,
     xlab = "車重 (1000 lbs)",
     ylab = "油耗 (英里/加侖)",
     main = "線性迴歸：油耗 ~ 車重",
     pch = 19, col = "blue")

# 加上迴歸線（紅色）
abline(model, col = "red", lwd = 2)

# 加上圖例
legend("topright",
       legend = c("實際資料", "迴歸線"),
       col = c("blue", "red"),
       pch = c(19, NA),
       lty = c(NA, 1),
       lwd = c(NA, 2))
```

【📸 截圖 ⑤：帶有紅色迴歸線的散佈圖】

---

## 常見錯誤與解決方法

### 🚨 錯誤 1：中文輸入法的「全形符號」（最致命！）

```r
# 學生常常不小心用中文輸入法打程式碼
> model <- lm(mpg ~ wt,data = mtcars)  # 逗號是全形！
Error: unexpected input in "model <- lm(mpg ~ wt,"
```

**問題**：肉眼很難看出來（`,` 和 `,` 長很像），但 R 會報錯

**解決**：
1. **寫程式碼時務必切換到英文輸入法**
2. 如果一直報錯，複製程式碼到記事本檢查
3. 如果符號看起來「特別寬」就是全形

**常見全形符號陷阱**：
- 全形逗號 `,` → 半形逗號 `,`
- 全形括號 `（）` → 半形括號 `()`
- 全形空格（看不見但存在！）

---

### ❌ 錯誤 2：找不到資料集
```r
> model <- lm(mpg ~ wt, data = mtcar)  # 少打一個 s
Error in eval(predvars, data, env) : object 'wt' not found
```
**解決**：確認資料集名稱拼寫正確 `mtcars`

---

### ❌ 錯誤 3：變數名稱大小寫錯誤
```r
> model <- lm(MPG ~ WT, data = mtcars)  # 變數名全大寫
Error in eval(predvars, data, env) : object 'MPG' not found
```
**解決**：R 區分大小寫，必須是 `mpg` 和 `wt`（小寫）

---

### ❌ 錯誤 4：忘記指定 data 參數
```r
> model <- lm(mpg ~ wt)  # 沒寫 data = mtcars
Error in eval(predvars, data, env) : object 'mpg' not found
```
**解決**：加上 `data = mtcars`

---

### ❌ 錯誤 5：看不到圖
```r
> plot(mtcars$wt, mtcars$mpg)
# 圖表沒出現？
```
**解決**：
1. 檢查右下角「Plots」視窗是否被切換到其他頁籤
2. 點選右下角的「Plots」
3. 如果視窗太小，圖可能無法顯示，試著放大視窗

---

### ❌ 錯誤 6：路徑問題（如果載入外部資料）
```r
# Windows 學生常這樣寫
> data <- read.csv("C:\Users\學生\Desktop\data.csv")
Error: '\U' used without hex digits in character string
```
**解決**：反斜線要用兩個或改用正斜線
```r
# 方法 1：改用正斜線（推薦）
> data <- read.csv("C:/Users/學生/Desktop/data.csv")  # ✓

# 方法 2：使用兩個反斜線
> data <- read.csv("C:\\Users\\學生\\Desktop\\data.csv")  # ✓
```

---

## 🎉 恭喜！你已經完成第一個線性迴歸

### 你學到了什麼？
✅ 安裝 R 和 RStudio
✅ 使用 `lm()` 函數建立模型
✅ 用 `summary()` 查看結果
✅ 解讀迴歸係數和 p-value
✅ 繪製散佈圖和迴歸線

### 下一步學習
- **理論對照**：為什麼 `lm()` 可以算出這些數字？（最小平方法）
- **模型診斷**：如何判斷這個模型是否可靠？（殘差分析）
- **多元迴歸**：如何加入更多自變數？（`mpg ~ wt + hp`）

---

## 快速參考：重要指令整理

| 功能           | 基本指令                      | 常見變化                          | 說明                     |
|----------------|-------------------------------|-----------------------------------|--------------------------|
| 查看資料前幾筆 | `head(mtcars)`                | `head(mtcars, 10)`                | 顯示前 10 筆             |
| 查看資料結構   | `str(mtcars)`                 | `summary(mtcars)`                 | 變數型態、筆數、摘要     |
| 建立迴歸模型   | `lm(y ~ x, data = df)`        | `lm(y ~ x1 + x2, data = df)`      | 多元迴歸                 |
| 查看模型結果   | `summary(model)`              | `summary(model)$r.squared`        | 只取 R²                 |
| 取得係數       | `coef(model)`                 | `coef(model)[2]`                  | 只取斜率                 |
| 繪製散佈圖     | `plot(x, y)`                  | `plot(x, y, col = "red")`         | 加顏色                   |
| 加上迴歸線     | `abline(model)`               | `abline(model, col = "red", lwd = 2)` | 紅色粗線         |
| 診斷圖         | `plot(model)`                 | `par(mfrow = c(2,2)); plot(model)`| 四張圖並排               |

---

## 疑難排解：如何獲得幫助

### 方法 1：使用 R 內建說明
```r
?lm          # 查看 lm 函數的說明文件
?summary     # 查看 summary 函數的說明
help(plot)   # 另一種查詢方式
```

### 方法 2：查看範例
```r
example(lm)  # 執行 lm 的範例程式碼
```

### 方法 3：搜尋關鍵字
```r
help.search("regression")  # 搜尋包含 regression 的函數
```

### 方法 4：網路資源
- Stack Overflow：https://stackoverflow.com/questions/tagged/r
- R 官方手冊：https://cran.r-project.org/manuals.html
- Quick-R：https://www.statmethods.net/

---

## 附錄：完整程式碼（可複製）

```r
# ===== 第一個線性迴歸：完整流程 =====

# 1. 查看資料
head(mtcars)
str(mtcars)

# 2. 繪製散佈圖
plot(mtcars$wt, mtcars$mpg,
     xlab = "車重 (1000 lbs)",
     ylab = "油耗 (英里/加侖)",
     main = "車重與油耗的關係",
     pch = 19, col = "blue")

# 3. 建立線性迴歸模型
model <- lm(mpg ~ wt, data = mtcars)

# 4. 查看結果
summary(model)

# 5. 繪製迴歸線
plot(mtcars$wt, mtcars$mpg,
     xlab = "車重 (1000 lbs)",
     ylab = "油耗 (英里/加侖)",
     main = "線性迴歸：油耗 ~ 車重",
     pch = 19, col = "blue")
abline(model, col = "red", lwd = 2)
legend("topright",
       legend = c("實際資料", "迴歸線"),
       col = c("blue", "red"),
       pch = c(19, NA),
       lty = c(NA, 1),
       lwd = c(NA, 2))

# 6. 取得特定資訊
coef(model)            # 只看係數
confint(model)         # 信賴區間
predict(model)         # 預測值
residuals(model)       # 殘差

# 7. 模型診斷（進階）
par(mfrow = c(2, 2))   # 設定 2x2 圖表排列
plot(model)            # 自動產生 4 張診斷圖
```

---

## 🎯 測試你的理解

**任務**：分析「馬力（hp）對油耗（mpg）的影響」

```r
# 提示：只需要改一個變數名稱
model2 <- lm(mpg ~ hp, data = mtcars)
summary(model2)
```

**思考題**：
1. 馬力對油耗的影響是正還是負？
2. 哪個變數影響較大：車重還是馬力？（比較 R²）

---

**💡 解答與解析**

<details>
<summary>點擊查看解答（請先自己做完再看！）</summary>

### 問題 1：馬力的影響是負的 ✓

```r
Coefficients:
            Estimate Std. Error t value Pr(>|t|)
(Intercept) 30.09886    1.63392  18.421  < 2e-16 ***
hp          -0.06823    0.01012  -6.742 1.79e-07 ***
```

- 係數 = **-0.0682**（負號）
- 代表：馬力↑ → mpg↓ → **越耗油** ✓
- p-value = 1.79e-07（非常顯著）

---

### 問題 2：車重的影響較大 ✓

| 模型          | 自變數 | R²     | 解釋力   |
|---------------|--------|--------|----------|
| model (原本)  | 車重   | 0.7528 | 75.28%   |
| model2 (新)   | 馬力   | 0.6024 | 60.24%   |

**結論**：車重可解釋 75% 的變異，馬力只能解釋 60%

---

### 延伸思考

**Q：為什麼車重的影響比馬力大？**
- 車重直接影響移動所需能量（物理定律）
- 馬力大的車「可能」開很快才耗油，但不一定會開快

**Q：能不能同時考慮兩者？**
```r
model3 <- lm(mpg ~ wt + hp, data = mtcars)
summary(model3)
# R² = 0.8268（更高！）
```
→ 同時考慮車重和馬力，R² 提升到 82.68%！

</details>

---

**文件版本**：v1.1（根據資深講師反饋修訂）
**最後更新**：2025-11-07
**預計學習時間**：10 分鐘
**難度**：⭐☆☆☆☆（入門）

---

## 📸 截圖清單（共 5 張）

| 編號 | 內容                          | 用途                     |
|------|-------------------------------|--------------------------|
| ①    | R 官網下載頁 + 安裝程式       | 安裝指引                 |
| ②    | RStudio 完整介面              | 介面認識                 |
| ③    | 散佈圖（負相關）              | 視覺化示範               |
| ④    | summary(model) 輸出           | 結果解讀                 |
| ⑤    | 帶迴歸線的散佈圖              | 最終成果展示             |
