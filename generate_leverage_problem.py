#!/usr/bin/env python3
# 生成有高影響點的 Leverage 圖

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
n = 30

# 創建有高影響點的數據
x = np.random.uniform(1, 5, n-1)
y = 2 + 0.8 * x + np.random.normal(0, 0.5, n-1)

# 添加一個高影響點（高 leverage + 高 residual）
x_outlier = 8.0  # 遠離其他 x 值
y_outlier = 1.0  # 偏離趨勢線
x = np.append(x, x_outlier)
y = np.append(y, y_outlier)

# 建立模型
X = x.reshape(-1, 1)
model = LinearRegression()
model.fit(X, y)
y_pred = model.predict(X)

# 計算標準化殘差
residuals = y - y_pred
standardized_residuals = (residuals - np.mean(residuals)) / np.std(residuals)

# 計算槓桿值（簡化版）
leverage = 1/n + (x - np.mean(x))**2 / np.sum((x - np.mean(x))**2)

plt.figure(figsize=(8, 6))

# 繪製一般點
normal_points = np.arange(n-1)
plt.scatter(leverage[normal_points], standardized_residuals[normal_points],
           alpha=0.7, color='steelblue', s=50, label='一般觀測值')

# 繪製高影響點（紅色，較大）
outlier_idx = n-1
plt.scatter(leverage[outlier_idx], standardized_residuals[outlier_idx],
           color='red', s=100, label='高影響點', zorder=5)

# 標註點編號
plt.annotate(f'{outlier_idx+1}', (leverage[outlier_idx], standardized_residuals[outlier_idx]),
            xytext=(5, 5), textcoords='offset points', fontsize=10, fontweight='bold')

# 添加水平線
plt.axhline(y=0, color='gray', linestyle='-', alpha=0.5)
plt.axhline(y=2, color='red', linestyle=':', alpha=0.7, label='Cook\'s D = 0.5')
plt.axhline(y=-2, color='red', linestyle=':', alpha=0.7)
plt.axhline(y=3, color='darkred', linestyle='--', alpha=0.7, label='Cook\'s D = 1.0')
plt.axhline(y=-3, color='darkred', linestyle='--', alpha=0.7)

plt.xlabel('槓桿值 (Leverage)', fontsize=12)
plt.ylabel('標準化殘差 (Standardized Residuals)', fontsize=12)
plt.title('殘差 vs 槓桿值：有高影響點', fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3)
plt.legend()

# 添加說明文字
plt.text(0.02, 0.98, f'❌ 第 {outlier_idx+1} 號觀測值\n超出 Cook\'s D = 1.0\n影響過大',
         transform=plt.gca().transAxes, fontsize=10, verticalalignment='top',
         bbox=dict(boxstyle='round', facecolor='mistyrose', alpha=0.8))

plt.tight_layout()
plt.savefig('img/leverage_problem.png', dpi=150, bbox_inches='tight')
plt.close()

print("Leverage 問題圖已生成：img/leverage_problem.png")