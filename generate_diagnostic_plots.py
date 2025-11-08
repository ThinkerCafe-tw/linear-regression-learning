#!/usr/bin/env python3
# 生成線性迴歸診斷圖的模擬圖
# 用於教材：R模型診斷實戰指南

import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
from sklearn.linear_model import LinearRegression
import pandas as pd

# 設定中文字體
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'SimHei', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

# 創建 mtcars 類似的數據
np.random.seed(42)
n = 32
wt = np.random.uniform(1.5, 5.5, n)  # 車重
mpg = 37.3 - 5.3 * wt + np.random.normal(0, 3, n)  # 油耗 + 噪音

# 建立線性回歸模型
X = wt.reshape(-1, 1)
y = mpg
model = LinearRegression()
model.fit(X, y)

# 計算預測值和殘差
y_pred = model.predict(X)
residuals = y - y_pred
standardized_residuals = (residuals - np.mean(residuals)) / np.std(residuals)

# 計算槓桿值（簡化版）
leverage = 1/n + (wt - np.mean(wt))**2 / np.sum((wt - np.mean(wt))**2)

# 確保 img 目錄存在
import os
os.makedirs('img', exist_ok=True)

# 1. 殘差 vs 配適值圖
plt.figure(figsize=(8, 6))
plt.scatter(y_pred, residuals, alpha=0.7, color='steelblue')
plt.axhline(y=0, color='red', linestyle='--', alpha=0.7)
plt.xlabel('配適值 (Fitted Values)', fontsize=12)
plt.ylabel('殘差 (Residuals)', fontsize=12)
plt.title('殘差 vs 配適值', fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('img/diagnostic_plot_1.png', dpi=150, bbox_inches='tight')
plt.close()

# 2. 常態 Q-Q 圖
plt.figure(figsize=(8, 6))
# 手動創建 Q-Q 圖，確保參考線是虛線
theoretical_quantiles = stats.norm.ppf(np.linspace(0.01, 0.99, len(standardized_residuals)))
sample_quantiles = np.sort(standardized_residuals)

plt.scatter(theoretical_quantiles, sample_quantiles, alpha=0.7, color='steelblue', s=50)

# 添加虛線參考線
min_val = min(min(theoretical_quantiles), min(sample_quantiles))
max_val = max(max(theoretical_quantiles), max(sample_quantiles))
plt.plot([min_val, max_val], [min_val, max_val], 'r--', linewidth=2, alpha=0.8, label='理論常態線')

plt.xlabel('理論分位數 (Theoretical Quantiles)', fontsize=12)
plt.ylabel('標準化殘差 (Standardized Residuals)', fontsize=12)
plt.title('常態 Q-Q 圖', fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('img/diagnostic_plot_2.png', dpi=150, bbox_inches='tight')
plt.close()

# 3. 尺度-位置圖
sqrt_abs_residuals = np.sqrt(np.abs(standardized_residuals))
plt.figure(figsize=(8, 6))
plt.scatter(y_pred, sqrt_abs_residuals, alpha=0.7, color='steelblue')
# 添加平滑線（簡化版）
z = np.polyfit(y_pred, sqrt_abs_residuals, 1)
p = np.poly1d(z)
plt.plot(sorted(y_pred), p(sorted(y_pred)), "r--", alpha=0.8)
plt.xlabel('配適值 (Fitted Values)', fontsize=12)
plt.ylabel('|標準化殘差|^0.5', fontsize=12)
plt.title('尺度-位置圖', fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('img/diagnostic_plot_3.png', dpi=150, bbox_inches='tight')
plt.close()

# 4. 殘差 vs 槓桿值圖
plt.figure(figsize=(8, 6))
plt.scatter(leverage, standardized_residuals, alpha=0.7, color='steelblue')
plt.axhline(y=0, color='red', linestyle='--', alpha=0.7)
plt.axhline(y=2, color='red', linestyle=':', alpha=0.5)
plt.axhline(y=-2, color='red', linestyle=':', alpha=0.5)
plt.xlabel('槓桿值 (Leverage)', fontsize=12)
plt.ylabel('標準化殘差 (Standardized Residuals)', fontsize=12)
plt.title('殘差 vs 槓桿值', fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('img/diagnostic_plot_4.png', dpi=150, bbox_inches='tight')
plt.close()

# 5. 組合圖
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# 重新載入數據並計算
axes[0,0].scatter(y_pred, residuals, alpha=0.7, color='steelblue')
axes[0,0].axhline(y=0, color='red', linestyle='--', alpha=0.7)
axes[0,0].set_xlabel('配適值')
axes[0,0].set_ylabel('殘差')
axes[0,0].set_title('殘差 vs 配適值')
axes[0,0].grid(True, alpha=0.3)

axes[0,1].scatter(theoretical_quantiles, sample_quantiles, alpha=0.7, color='steelblue', s=30)
axes[0,1].plot([min_val, max_val], [min_val, max_val], 'r--', linewidth=2, alpha=0.8)
axes[0,1].set_xlabel('理論分位數')
axes[0,1].set_ylabel('標準化殘差')
axes[0,1].set_title('常態 Q-Q 圖')
axes[0,1].grid(True, alpha=0.3)

axes[1,0].scatter(y_pred, sqrt_abs_residuals, alpha=0.7, color='steelblue')
axes[1,0].plot(sorted(y_pred), p(sorted(y_pred)), "r--", alpha=0.8)
axes[1,0].set_xlabel('配適值')
axes[1,0].set_ylabel('|標準化殘差|^0.5')
axes[1,0].set_title('尺度-位置圖')
axes[1,0].grid(True, alpha=0.3)

axes[1,1].scatter(leverage, standardized_residuals, alpha=0.7, color='steelblue')
axes[1,1].axhline(y=0, color='red', linestyle='--', alpha=0.7)
axes[1,1].axhline(y=2, color='red', linestyle=':', alpha=0.5)
axes[1,1].axhline(y=-2, color='red', linestyle=':', alpha=0.5)
axes[1,1].set_xlabel('槓桿值')
axes[1,1].set_ylabel('標準化殘差')
axes[1,1].set_title('殘差 vs 槓桿值')
axes[1,1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('img/diagnostic_plots_all.png', dpi=150, bbox_inches='tight')
plt.close()

print("診斷圖已生成完成！")
print("檔案位置：")
print("- img/diagnostic_plot_1.png")
print("- img/diagnostic_plot_2.png")
print("- img/diagnostic_plot_3.png")
print("- img/diagnostic_plot_4.png")
print("- img/diagnostic_plots_all.png")