# 線性迴歸理論與實作對照
**從數學公式到 R 程式碼**

---
📚 **導航**：[回到目錄](./README.md) | 上一章：[快速上手指南](./R快速上手指南.md) | 下一章：[模型診斷實戰](./R模型診斷實戰指南.md)
---

> **適用對象**：已完成「10 分鐘快速上手」的學生，想深入理解 `lm()` 背後原理

> 📖 **閱讀方式**：
> - **GitHub 線上**：你現在就在正確的地方！繼續往下看 ✓
> - **RStudio**：在 Preview 視窗中閱讀，可直接複製程式碼執行
> - **本地閱讀器**：Typora、VS Code 等 Markdown 工具

> 📌 **學習目標**：
> - 理解 OLS（最小平方法）的數學原理
> - 掌握迴歸係數的計算公式
> - 能手動驗證 R 的計算結果
> - 理解 summary() 輸出的每個數字

---

## 第一部分：簡單線性迴歸的數學基礎

### 模型設定

**母體迴歸模型**：
```
Y = β₀ + β₁X + ε
```

**名詞解釋**：
- `Y`：應變數（dependent variable）
- `X`：自變數（independent variable）
- `β₀`：截距（intercept）
- `β₁`：斜率（slope）
- `ε`：誤差項（error term）

**樣本估計式**：
```
Ŷ = b₀ + b₁X
```

其中 `b₀` 和 `b₁` 是從樣本資料估計出來的係數。

---

## 第二部分：OLS 估計公式 ⭐

### 斜率 β₁ 的估計公式

**數學公式**：
```
       Σ(xᵢ - x̄)(yᵢ - ȳ)
b₁ = ───────────────────
       Σ(xᵢ - x̄)²
```

**白話文**：
- 分子：X 和 Y 的共變異數（covariance）
- 分母：X 的變異數（variance）
- **意義**：X 每變動 1 單位，Y 平均變動多少

---

### 截距 β₀ 的估計公式

**數學公式**：
```
b₀ = ȳ - b₁x̄
```

**白話文**：
- 迴歸線必定通過點 (x̄, ȳ)
- 截距 = Y 的平均值 - 斜率 × X 的平均值

---

## 第三部分：手算 vs R 計算（驗證）

### 案例：mtcars 資料（mpg ~ wt）

讓我們用兩種方法計算迴歸係數，驗證結果一致。

#### 方法 1：R 的 lm() 函數

```r
# 使用 lm() 快速計算
model <- lm(mpg ~ wt, data = mtcars)
coef(model)

# 輸出：
# (Intercept)          wt
#   37.285126   -5.344472
```

---

#### 方法 2：手動計算（用 R 實作公式）

```r
# 取出資料
x <- mtcars$wt
y <- mtcars$mpg

# 計算平均值
x_bar <- mean(x)
y_bar <- mean(y)

# 計算斜率 b₁
numerator <- sum((x - x_bar) * (y - y_bar))    # 分子
denominator <- sum((x - x_bar)^2)              # 分母
b1 <- numerator / denominator

# 計算截距 b₀
b0 <- y_bar - b1 * x_bar

# 顯示結果
cat("手算結果：\n")
cat("截距 b₀ =", b0, "\n")
cat("斜率 b₁ =", b1, "\n")

# 輸出：
# 手算結果：
# 截距 b₀ = 37.28513
# 斜率 b₁ = -5.344472
```

---

#### 驗證：兩種方法結果一致 ✓

```r
# 比較兩種方法的結果
comparison <- data.frame(
  Method = c("lm()", "手算"),
  Intercept = c(coef(model)[1], b0),
  Slope = c(coef(model)[2], b1)
)
print(comparison)

# 輸出：
#   Method Intercept     Slope
# 1  lm()  37.28513 -5.344472
# 2  手算  37.28513 -5.344472
```

**結論**：`lm()` 函數就是用這個公式計算的！✓

---

## 第四部分：決定係數 R² 的計算

### R² 的三種理解方式

#### 1. 變異數分解（ANOVA）

**公式**：
```
R² = SSR / SST = 1 - (SSE / SST)
```

**名詞解釋**：
- **SST**（Total Sum of Squares）：總變異
  - `SST = Σ(yᵢ - ȳ)²`
- **SSR**（Regression Sum of Squares）：迴歸解釋的變異
  - `SSR = Σ(ŷᵢ - ȳ)²`
- **SSE**（Error Sum of Squares）：殘差變異
  - `SSE = Σ(yᵢ - ŷᵢ)²`

**關係式**：`SST = SSR + SSE`

---

#### 2. R 手動計算 R²

```r
# 方法 A：使用 SSR 和 SST
y_hat <- predict(model)                # 預測值
SST <- sum((y - mean(y))^2)           # 總變異
SSR <- sum((y_hat - mean(y))^2)       # 迴歸變異
SSE <- sum((y - y_hat)^2)             # 殘差變異

R_squared_method1 <- SSR / SST
R_squared_method2 <- 1 - (SSE / SST)

cat("R² (方法 1) =", R_squared_method1, "\n")
cat("R² (方法 2) =", R_squared_method2, "\n")

# 輸出：
# R² (方法 1) = 0.7528328
# R² (方法 2) = 0.7528328
```

---

#### 3. 與 R 內建結果比較

```r
# R 內建的 R²
summary(model)$r.squared

# 輸出：
# [1] 0.7528328

# 驗證：一致！
```

---

## 第五部分：summary() 輸出完整解讀 ⭐

### 重新檢視 summary() 輸出

```r
summary(model)
```

輸出：
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
Multiple R-squared:  0.7528,	Adjusted R-squared:  0.7446
F-statistic: 91.38 on 1 and 30 DF,  p-value: 1.294e-10
```

---

### 逐行解讀（現在你看懂 90% 了）

#### 區塊 1：Residuals（殘差摘要）

```
    Min      1Q  Median      3Q     Max
-4.5432 -2.3647 -0.1252  1.4096  6.8727
```

**意義**：
- 殘差 = 實際值 - 預測值 (`yᵢ - ŷᵢ`)
- 這是殘差的五數摘要
- **理想狀況**：中位數接近 0，分布對稱

**R 驗證**：
```r
residuals <- residuals(model)
summary(residuals)

#    Min. 1st Qu.  Median    Mean 3rd Qu.    Max.
# -4.5432 -2.3647 -0.1252  0.0000  1.4096  6.8727
```

---

#### 區塊 2：Coefficients（係數表）⭐

這是最重要的部分！

| 欄位        | Intercept | wt       | 說明                          |
|-------------|-----------|----------|-------------------------------|
| Estimate    | 37.2851   | -5.3445  | 估計的係數值（b₀, b₁）        |
| Std. Error  | 1.8776    | 0.5591   | 標準誤（估計的不確定性）      |
| t value     | 19.858    | -9.559   | t 統計量 = Estimate / Std.Error |
| Pr(>\|t\|)    | < 2e-16   | 1.29e-10 | p-value（顯著性檢定）         |

---

##### 2.1 Estimate（估計值）

```r
coef(model)
# (Intercept)          wt
#   37.285126   -5.344472
```

**意義**：迴歸方程式 `mpg = 37.29 - 5.34 × wt`

---

##### 2.2 Std. Error（標準誤）

**公式**（斜率的標準誤）：
```
         σ̂
SE(b₁) = ───────────
         √Σ(xᵢ - x̄)²
```

其中 `σ̂` 是殘差標準誤（Residual standard error）

**R 計算**：
```r
# 取得殘差標準誤
sigma_hat <- summary(model)$sigma  # 3.046

# 計算 SE(b₁)
SE_b1 <- sigma_hat / sqrt(sum((x - mean(x))^2))
SE_b1

# [1] 0.5591464  # 與 summary() 一致！
```

**意義**：
- 標準誤越小 → 估計越精確
- 如果重複抽樣，係數估計值的標準差

---

##### 2.3 t value（t 統計量）

**公式**：
```
       Estimate
t = ───────────────
     Std. Error
```

**R 計算**：
```r
t_value <- coef(model)[2] / SE_b1
t_value

# [1] -9.559044  # 與 summary() 一致！
```

**意義**：
- 檢定 H₀: β₁ = 0（斜率是否為 0）
- |t| 越大 → 越有證據拒絕 H₀
- 這裡 |t| = 9.56，非常顯著

---

##### 2.4 Pr(>|t|)（p-value）

**定義**：
- 在 H₀: β₁ = 0 為真的情況下，觀察到 |t| ≥ 9.56 的機率
- p-value = 1.29e-10（非常非常小）

**判斷準則**：
- p < 0.001：***（極顯著）
- p < 0.01：**（非常顯著）
- p < 0.05：*（顯著）
- p ≥ 0.05：不顯著

**R 計算**：
```r
# 自由度 = n - 2 = 32 - 2 = 30
df <- nrow(mtcars) - 2

# 雙尾檢定的 p-value
p_value <- 2 * pt(-abs(t_value), df = df)
p_value

# [1] 1.293959e-10  # 與 summary() 一致！
```

**結論**：車重對油耗有極顯著影響（p < 0.001）✓

---

#### 區塊 3：模型整體診斷

```
Residual standard error: 3.046 on 30 degrees of freedom
Multiple R-squared:  0.7528,	Adjusted R-squared:  0.7446
F-statistic: 91.38 on 1 and 30 DF,  p-value: 1.294e-10
```

---

##### 3.1 Residual standard error（殘差標準誤）

**公式**：
```
      √ SSE
σ̂ = ─────────
     √(n - k)
```

其中：
- `SSE`：殘差平方和
- `n`：樣本數
- `k`：參數個數（含截距，此例為 2）

**R 計算**：
```r
SSE <- sum(residuals(model)^2)
n <- nrow(mtcars)
k <- 2  # β₀ 和 β₁

sigma_hat <- sqrt(SSE / (n - k))
sigma_hat

# [1] 3.045882  # 與 summary() 一致！
```

**意義**：
- 預測的平均誤差約 3.05 英里/加侖
- 越小越好（但不可能為 0）

---

##### 3.2 Adjusted R-squared（調整後 R²）

**公式**：
```
              (n - 1)
R̄² = 1 - (1 - R²) × ───────
              (n - k)
```

**為什麼需要調整？**
- 加入更多變數，R² 一定會增加（即使變數無意義）
- Adjusted R² 會「懲罰」無用變數
- 用於比較不同變數個數的模型

**R 計算**：
```r
R2 <- summary(model)$r.squared
n <- nrow(mtcars)
k <- 2

R2_adj <- 1 - (1 - R2) * ((n - 1) / (n - k))
R2_adj

# [1] 0.7445939  # 與 summary() 一致！
```

---

##### 3.3 F-statistic（F 檢定）

**檢定假設**：
- H₀: 所有斜率係數 = 0（模型無解釋力）
- H₁: 至少有一個斜率 ≠ 0（模型有解釋力）

**公式**：
```
     SSR / (k - 1)
F = ───────────────
     SSE / (n - k)
```

**R 計算**：
```r
SSR <- sum((y_hat - mean(y))^2)
SSE <- sum((y - y_hat)^2)
k <- 2
n <- nrow(mtcars)

F_stat <- (SSR / (k - 1)) / (SSE / (n - k))
F_stat

# [1] 91.37533  # 與 summary() 一致！
```

**p-value**：
```r
p_value_F <- pf(F_stat, df1 = k - 1, df2 = n - k, lower.tail = FALSE)
p_value_F

# [1] 1.293959e-10  # 與 summary() 一致！
```

**結論**：模型整體極顯著（p < 0.001），有顯著解釋力 ✓

---

## 第六部分：多元線性迴歸擴展

### 從簡單到多元

**簡單線性迴歸**：
```r
model1 <- lm(mpg ~ wt, data = mtcars)
```

**多元線性迴歸**：
```r
model2 <- lm(mpg ~ wt + hp, data = mtcars)
summary(model2)
```

---

### 多元迴歸的係數解釋

輸出：
```
Coefficients:
            Estimate Std. Error t value Pr(>|t|)
(Intercept) 37.22727    1.59879  23.285  < 2e-16 ***
wt          -3.87783    0.63273  -6.129 1.12e-06 ***
hp          -0.03177    0.00903  -3.519  0.00145 **
```

**迴歸方程式**：
```
mpg = 37.23 - 3.88×wt - 0.032×hp
```

**係數解釋**：
- `wt` 的係數 = -3.88：**控制馬力不變**，車重每增加 1000 磅，油耗減少 3.88 mpg
- `hp` 的係數 = -0.032：**控制車重不變**，馬力每增加 1 hp，油耗減少 0.032 mpg

**關鍵差異**：
- 簡單迴歸：`wt` 係數 = -5.34
- 多元迴歸：`wt` 係數 = -3.88（變小了！）
- **原因**：車重和馬力有相關性，多元迴歸排除了馬力的影響

---

### 模型比較

```r
# 比較 R²
summary(model1)$r.squared  # 0.7528（只用 wt）
summary(model2)$r.squared  # 0.8268（加入 hp）

# 加入 hp 後，R² 從 75% 提升到 83% ✓
```

---

## 第七部分：完整驗證程式碼

```r
# ===== 完整驗證：從零開始複製 lm() 的所有結果 =====

# 1. 資料準備
x <- mtcars$wt
y <- mtcars$mpg
n <- length(y)

# 2. 計算係數
x_bar <- mean(x)
y_bar <- mean(y)
b1 <- sum((x - x_bar) * (y - y_bar)) / sum((x - x_bar)^2)
b0 <- y_bar - b1 * x_bar

cat("係數：b₀ =", b0, ", b₁ =", b1, "\n\n")

# 3. 計算預測值和殘差
y_hat <- b0 + b1 * x
residuals <- y - y_hat

# 4. 計算 SSE, SSR, SST
SSE <- sum(residuals^2)
SST <- sum((y - y_bar)^2)
SSR <- SST - SSE

# 5. 計算 R²
R2 <- SSR / SST
R2_adj <- 1 - (1 - R2) * ((n - 1) / (n - 2))

cat("R² =", R2, "\n")
cat("Adjusted R² =", R2_adj, "\n\n")

# 6. 計算殘差標準誤
sigma_hat <- sqrt(SSE / (n - 2))
cat("Residual standard error =", sigma_hat, "\n\n")

# 7. 計算標準誤（係數）
SE_b1 <- sigma_hat / sqrt(sum((x - x_bar)^2))
SE_b0 <- sigma_hat * sqrt(1/n + x_bar^2 / sum((x - x_bar)^2))

# 8. 計算 t 統計量
t_b0 <- b0 / SE_b0
t_b1 <- b1 / SE_b1

# 9. 計算 p-value
p_b0 <- 2 * pt(-abs(t_b0), df = n - 2)
p_b1 <- 2 * pt(-abs(t_b1), df = n - 2)

cat("係數檢定：\n")
cat("  b₀: t =", t_b0, ", p =", p_b0, "\n")
cat("  b₁: t =", t_b1, ", p =", p_b1, "\n\n")

# 10. 計算 F 統計量
F_stat <- (SSR / 1) / (SSE / (n - 2))
p_F <- pf(F_stat, df1 = 1, df2 = n - 2, lower.tail = FALSE)

cat("F-statistic =", F_stat, ", p-value =", p_F, "\n\n")

# 11. 與 lm() 比較
model <- lm(mpg ~ wt, data = mtcars)
cat("===== 驗證結果 =====\n")
cat("手算 vs lm() 的係數差異：\n")
cat("  b₀:", b0, "vs", coef(model)[1], "\n")
cat("  b₁:", b1, "vs", coef(model)[2], "\n")
cat("\nR²:", R2, "vs", summary(model)$r.squared, "\n")
cat("完全一致！✓\n")
```

---

## 第八部分：關鍵公式速查表

| 統計量            | 公式                                    | R 函數                        |
|-------------------|-----------------------------------------|-------------------------------|
| 斜率 b₁           | `Σ(xᵢ-x̄)(yᵢ-ȳ) / Σ(xᵢ-x̄)²`              | `coef(model)[2]`              |
| 截距 b₀           | `ȳ - b₁x̄`                               | `coef(model)[1]`              |
| R²                | `SSR / SST` 或 `1 - SSE/SST`            | `summary(model)$r.squared`    |
| Adjusted R²       | `1 - (1-R²)×(n-1)/(n-k)`                | `summary(model)$adj.r.squared`|
| 殘差標準誤 σ̂      | `√(SSE/(n-k))`                          | `summary(model)$sigma`        |
| 標準誤 SE(b₁)     | `σ̂ / √Σ(xᵢ-x̄)²`                         | `summary(model)$coef[2,2]`    |
| t 統計量          | `Estimate / Std.Error`                  | `summary(model)$coef[,3]`     |
| p-value           | `2×P(T > |t|)`                          | `summary(model)$coef[,4]`     |
| F 統計量          | `(SSR/(k-1)) / (SSE/(n-k))`             | `summary(model)$fstatistic`   |

---

## 🎯 測試你的理解

### 練習 1：手算驗證

使用內建資料 `women`（身高 vs 體重），手動計算迴歸係數並驗證：

```r
# 資料：15 位女性的身高和體重
head(women)
#   height weight
# 1     58    115
# 2     59    117
# ...

# 任務：
# 1. 用公式手算 b₀ 和 b₁
# 2. 用 lm() 計算
# 3. 比較結果是否一致

# 提示：
x <- women$height
y <- women$weight
# ... 你的程式碼
```

<details>
<summary>點擊查看解答</summary>

```r
x <- women$height
y <- women$weight

# 手算
x_bar <- mean(x)
y_bar <- mean(y)
b1 <- sum((x - x_bar) * (y - y_bar)) / sum((x - x_bar)^2)
b0 <- y_bar - b1 * x_bar

cat("手算：b₀ =", b0, ", b₁ =", b1, "\n")

# lm()
model <- lm(weight ~ height, data = women)
cat("lm()：", coef(model), "\n")

# 結果：
# 手算：b₀ = -87.51667 , b₁ = 3.45
# lm()： -87.51667 3.45
# 完全一致！✓
```

</details>

---

### 練習 2：解讀 summary()

```r
model <- lm(weight ~ height, data = women)
summary(model)
```

**問題**：
1. R² = 0.991，代表什麼意義？
2. `height` 的 p-value < 2e-16，結論是什麼？
3. 如果身高增加 1 英寸，體重預期增加多少磅？

<details>
<summary>點擊查看解答</summary>

1. **R² = 0.991**
   - 身高可以解釋 99.1% 的體重變異
   - 這是非常高的配適度！（接近完美線性關係）

2. **p-value < 2e-16**
   - 身高對體重有極顯著影響（p < 0.001）
   - 拒絕 H₀: β₁ = 0

3. **體重增加量**
   - 斜率 b₁ = 3.45
   - 身高每增加 1 英寸，體重預期增加 3.45 磅

</details>

---

## 📚 延伸學習

完成本章後，你已經理解：
- ✅ OLS 估計的數學原理
- ✅ 每個統計量的計算公式
- ✅ summary() 輸出的完整意義
- ✅ 如何手動驗證 R 的計算

**下一步**：
1. **模型診斷**：如何判斷模型可不可靠？（殘差分析）
2. **假設檢定**：如何檢定假設是否滿足？
3. **實務案例**：完整分析流程（從資料探索到報告撰寫）

---

**文件版本**：v1.0
**最後更新**：2025-11-07
**預計學習時間**：45-60 分鐘
**難度**：⭐⭐⭐☆☆（中級）
**前置需求**：完成「10 分鐘 R 快速上手」
