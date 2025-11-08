#!/usr/bin/env python3
# 生成有問題的 Q-Q 圖範例
# 用於展示常見的非常態分布模式

import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

# 設定中文字體
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'SimHei', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

# 確保 img 目錄存在
import os
os.makedirs('img', exist_ok=True)

np.random.seed(42)
n = 50

def create_qq_plot(data, title, filename, description):
    """創建 Q-Q 圖"""
    plt.figure(figsize=(8, 6))

    # 計算分位數
    theoretical_quantiles = stats.norm.ppf(np.linspace(0.01, 0.99, len(data)))
    sample_quantiles = np.sort(data)

    # 繪製散點
    plt.scatter(theoretical_quantiles, sample_quantiles, alpha=0.7, color='steelblue', s=50)

    # 添加虛線參考線
    min_val = min(min(theoretical_quantiles), min(sample_quantiles))
    max_val = max(max(theoretical_quantiles), max(sample_quantiles))
    plt.plot([min_val, max_val], [min_val, max_val], 'r--', linewidth=2, alpha=0.8)

    plt.xlabel('理論分位數 (Theoretical Quantiles)', fontsize=12)
    plt.ylabel('標準化殘差 (Standardized Residuals)', fontsize=12)
    plt.title(title, fontsize=14, fontweight='bold')
    plt.grid(True, alpha=0.3)

    # 添加說明文字
    plt.text(0.02, 0.98, description, transform=plt.gca().transAxes,
             fontsize=10, verticalalignment='top',
             bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))

    plt.tight_layout()
    plt.savefig(filename, dpi=150, bbox_inches='tight')
    plt.close()

# 1. 右偏分配（右尾上翹）
right_skewed = np.random.exponential(2, n) - 2  # 指數分布
right_skewed = (right_skewed - np.mean(right_skewed)) / np.std(right_skewed)
create_qq_plot(right_skewed, '右偏分配：右尾上翹', 'img/qq_right_skewed.png',
               '❌ 右尾偏離虛線向上\n表示有極端大值')

# 2. 左偏分配（左尾下彎）
left_skewed = -np.random.exponential(2, n) + 2  # 負指數分布
left_skewed = (left_skewed - np.mean(left_skewed)) / np.std(left_skewed)
create_qq_plot(left_skewed, '左偏分配：左尾下彎', 'img/qq_left_skewed.png',
               '❌ 左尾偏離虛線向下\n表示有極端小值')

# 3. 厚尾分配（兩端偏離）
heavy_tail = np.random.laplace(0, 1, n)  # 拉普拉斯分布（厚尾）
heavy_tail = (heavy_tail - np.mean(heavy_tail)) / np.std(heavy_tail)
create_qq_plot(heavy_tail, '厚尾分配：兩端偏離', 'img/qq_heavy_tail.png',
               '❌ 兩端都偏離虛線\n表示有較多極端值')

# 4. 薄尾分配（S型彎曲）
thin_tail = np.random.uniform(-2, 2, n)  # 均勻分布（薄尾）
thin_tail = (thin_tail - np.mean(thin_tail)) / np.std(thin_tail)
create_qq_plot(thin_tail, '薄尾分配：S型彎曲', 'img/qq_thin_tail.png',
               '❌ S型彎曲模式\n表示缺乏極端值')

# 5. 理想常態分配（對照組）
normal_data = np.random.normal(0, 1, n)
create_qq_plot(normal_data, '理想常態分配', 'img/qq_normal_ideal.png',
               '✅ 點接近虛線\n符合常態分布')

# 6. 創建組合圖
fig, axes = plt.subplots(2, 3, figsize=(15, 10))
fig.suptitle('Q-Q 圖：不同分配類型的比較', fontsize=16, fontweight='bold')

# 數據和標題
datasets = [
    (normal_data, '✅ 理想常態', '✅ 點沿虛線分布'),
    (right_skewed, '❌ 右偏：右尾上翹', '右端點向上偏離'),
    (left_skewed, '❌ 左偏：左尾下彎', '左端點向下偏離'),
    (heavy_tail, '❌ 厚尾：兩端偏離', '兩端都有偏離'),
    (thin_tail, '❌ 薄尾：S型彎曲', 'S型彎曲模式'),
    (np.random.normal(0, 1, n), '✅ 另一個常態例子', '再次驗證常態')
]

for i, (data, title, desc) in enumerate(datasets):
    row, col = i // 3, i % 3
    ax = axes[row, col]

    # 計算分位數
    theoretical = stats.norm.ppf(np.linspace(0.01, 0.99, len(data)))
    sample = np.sort(data)

    # 繪製
    ax.scatter(theoretical, sample, alpha=0.7, color='steelblue', s=30)

    # 參考線
    min_val = min(min(theoretical), min(sample))
    max_val = max(max(theoretical), max(sample))
    ax.plot([min_val, max_val], [min_val, max_val], 'r--', linewidth=1.5, alpha=0.8)

    ax.set_title(title, fontsize=11, fontweight='bold')
    ax.set_xlabel('理論分位數', fontsize=9)
    ax.set_ylabel('樣本分位數', fontsize=9)
    ax.grid(True, alpha=0.3)
    ax.tick_params(labelsize=8)

    # 添加簡短說明
    ax.text(0.02, 0.98, desc, transform=ax.transAxes, fontsize=8,
            verticalalignment='top', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.7))

plt.tight_layout()
plt.savefig('img/qq_comparison_all.png', dpi=150, bbox_inches='tight')
plt.close()

print("Q-Q 圖問題範例已生成完成！")
print("檔案位置：")
print("- img/qq_normal_ideal.png - 理想常態分配")
print("- img/qq_right_skewed.png - 右偏分配（右尾上翹）")
print("- img/qq_left_skewed.png - 左偏分配（左尾下彎）")
print("- img/qq_heavy_tail.png - 厚尾分配（兩端偏離）")
print("- img/qq_thin_tail.png - 薄尾分配（S型彎曲）")
print("- img/qq_comparison_all.png - 所有類型比較圖")