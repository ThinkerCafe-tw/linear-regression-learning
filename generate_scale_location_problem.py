#!/usr/bin/env python3
# 生成有問題的 Scale-Location 圖（異質變異數）

import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

# 設定中文字體
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'SimHei', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

# 確保 img 目錄存在
import os
os.makedirs('img', exist_ok=True)

np.random.seed(42)
n = 50

# 創建有異質變異數的數據（變異數隨X增加）
x = np.linspace(1, 10, n)
# 變異數隨 x 增加：σ = 0.5 + 0.5*x
noise = np.random.normal(0, 0.5 + 0.5 * x/10)
y = 2 + 0.8 * x + noise

# 建立模型
X = x.reshape(-1, 1)
model = LinearRegression()
model.fit(X, y)
y_pred = model.predict(X)

# 計算標準化殘差
residuals = y - y_pred
standardized_residuals = (residuals - np.mean(residuals)) / np.std(residuals)

# Scale-Location 圖：√|標準化殘差|
sqrt_abs_residuals = np.sqrt(np.abs(standardized_residuals))

plt.figure(figsize=(8, 6))
plt.scatter(y_pred, sqrt_abs_residuals, alpha=0.7, color='steelblue', s=50)

# 添加上升趨勢線（LOESS 近似）
z = np.polyfit(y_pred, sqrt_abs_residuals, 2)  # 二次多項式擬合
p = np.poly1d(z)
x_smooth = np.linspace(min(y_pred), max(y_pred), 100)
plt.plot(x_smooth, p(x_smooth), "r-", linewidth=2, alpha=0.8, label='趨勢線')

plt.xlabel('配適值 (Fitted Values)', fontsize=12)
plt.ylabel('√|標準化殘差|', fontsize=12)
plt.title('Scale-Location 圖：紅線上升（異質變異數）', fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3)

# 添加說明文字
plt.text(0.02, 0.98, '❌ 紅線明顯上升\n表示變異數遞增',
         transform=plt.gca().transAxes, fontsize=10, verticalalignment='top',
         bbox=dict(boxstyle='round', facecolor='mistyrose', alpha=0.8))

plt.tight_layout()
plt.savefig('img/scale_location_problem.png', dpi=150, bbox_inches='tight')
plt.close()

print("Scale-Location 問題圖已生成：img/scale_location_problem.png")