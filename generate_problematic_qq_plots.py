#!/usr/bin/env python3
# 生成更典型、更清楚的 Q-Q 圖範例
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

np.random.seed(123)  # 更換隨機種子以獲得更好的範例
n = 100  # 增加樣本數讓分配特性更明顯

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

# 1. 右偏分配（右尾上翹）- 使用對數常態分配
np.random.seed(100)
log_normal_data = np.random.lognormal(mean=0.5, sigma=0.8, size=n)
# 輕度標準化，保持偏度特性
right_skewed = (log_normal_data - np.mean(log_normal_data)) / np.std(log_normal_data) * 0.8
create_qq_plot(right_skewed, '右偏分配：右尾上翹', 'img/qq_right_skewed.png',
               '❌ 右尾偏離虛線向上\n表示有極端大值')

# 2. 左偏分配（左尾下彎）- 使用 Beta 分配
np.random.seed(150)
beta_data = np.random.beta(a=8, b=2, size=n)  # 左偏的 beta 分配
left_skewed = (beta_data - np.mean(beta_data)) / np.std(beta_data) * 0.8
create_qq_plot(left_skewed, '左偏分配：左尾下彎', 'img/qq_left_skewed.png',
               '❌ 左尾偏離虛線向下\n表示有極端小值')

# 3. 厚尾分配（兩端偏離）- 使用 t 分配 + 人工極端值
np.random.seed(200)
t_data = np.random.standard_t(df=2, size=n-4)  # 自由度小的 t 分配
# 人工添加極端值確保厚尾效果明顯
extreme_values = [-3.5, -3.0, 3.0, 3.5]
heavy_tail = np.concatenate([t_data, extreme_values])
heavy_tail = (heavy_tail - np.mean(heavy_tail)) / np.std(heavy_tail)
create_qq_plot(heavy_tail, '厚尾分配：兩端偏離', 'img/qq_heavy_tail.png',
               '❌ 兩端都偏離虛線\n表示有較多極端值')

# 4. 薄尾分配（S型彎曲）- 使用截斷常態分配
np.random.seed(250)
# 生成截斷在 [-1.5, 1.5] 的常態分配
from scipy.stats import truncnorm
a, b = -1.5, 1.5
thin_tail_dist = truncnorm(a, b, loc=0, scale=0.8)
thin_tail = thin_tail_dist.rvs(size=n)
create_qq_plot(thin_tail, '薄尾分配：S型彎曲', 'img/qq_thin_tail.png',
               '❌ S型彎曲模式\n表示缺乏極端值')

# 5. 理想常態分配（對照組）
np.random.seed(300)
normal_data = np.random.normal(0, 1, n)
create_qq_plot(normal_data, '理想常態分配', 'img/qq_normal_ideal.png',
               '✅ 點接近虛線\n符合常態分布')

# 6. 雙峰分配（非常態的另一種類型）
np.random.seed(350)
# 混合兩個常態分配
mixture1 = np.random.normal(-1.5, 0.5, n//2)
mixture2 = np.random.normal(1.5, 0.5, n//2)
bimodal = np.concatenate([mixture1, mixture2])
np.random.shuffle(bimodal)  # 打亂順序
bimodal = (bimodal - np.mean(bimodal)) / np.std(bimodal)
create_qq_plot(bimodal, '雙峰分配：波浪狀', 'img/qq_bimodal.png',
               '❌ 波浪狀或階梯狀\n表示資料有分群現象')

# 7. 創建改進的組合圖
fig, axes = plt.subplots(2, 3, figsize=(16, 11))
fig.suptitle('Q-Q 圖診斷指南：常見分配模式識別', fontsize=18, fontweight='bold', y=0.98)

# 數據和標題（使用新的更典型的範例）
datasets = [
    (normal_data, '✅ 理想常態分配', '點沿虛線分布'),
    (right_skewed, '❌ 右偏：右尾上翹', '右端向上偏離'),
    (left_skewed, '❌ 左偏：左尾下彎', '左端向下偏離'),
    (heavy_tail, '❌ 厚尾：兩端偏離', '兩端都偏離虛線'),
    (thin_tail, '❌ 薄尾：S型彎曲', '缺乏極端值'),
    (bimodal, '❌ 雙峰：波浪狀', '階梯或波浪狀')
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

print("✅ 重新生成的 Q-Q 圖診斷範例已完成！")
print("\n📊 改進重點：")
print("- 增加樣本數至 100，讓分配特性更明顯")
print("- 使用不同隨機種子，確保典型模式")
print("- 避免過度標準化掩蓋分配特性")
print("- 人工添加極端值確保厚尾效果")
print("\n📁 檔案位置：")
print("- img/qq_normal_ideal.png - 理想常態分配（對照組）")
print("- img/qq_right_skewed.png - 右偏分配（對數常態，右尾上翹）")
print("- img/qq_left_skewed.png - 左偏分配（Beta 分配，左尾下彎）")
print("- img/qq_heavy_tail.png - 厚尾分配（t 分配 + 極端值，兩端偏離）")
print("- img/qq_thin_tail.png - 薄尾分配（截斷常態，S型彎曲）")
print("- img/qq_bimodal.png - 雙峰分配（混合分配，波浪狀）")
print("- img/qq_comparison_all.png - 六種類型完整比較圖")
print("\n🎯 現在每張圖都準確展示其聲稱的問題模式！")