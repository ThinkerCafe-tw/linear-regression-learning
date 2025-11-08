# 生成線性迴歸診斷圖
# 用於教材：R模型診斷實戰指南

# 載入必要套件
library(ggplot2)

# 使用 mtcars 資料建立模型
model <- lm(mpg ~ wt, data = mtcars)

# 設定中文字型（如果需要）
# par(family = "Arial Unicode MS")  # macOS
# par(family = "Microsoft YaHei")   # Windows

# 設定輸出參數
png_width <- 800
png_height <- 600
png_res <- 120

# 1. Residuals vs Fitted（殘差 vs 配適值）
png("img/diagnostic_plot_1.png", width = png_width, height = png_height, res = png_res)
plot(model, which = 1, main = "殘差 vs 配適值",
     xlab = "配適值", ylab = "殘差",
     cex.main = 1.2, cex.lab = 1.1)
dev.off()

# 2. Normal Q-Q（常態 Q-Q 圖）
png("img/diagnostic_plot_2.png", width = png_width, height = png_height, res = png_res)
plot(model, which = 2, main = "常態 Q-Q 圖",
     xlab = "理論分位數", ylab = "標準化殘差",
     cex.main = 1.2, cex.lab = 1.1)
dev.off()

# 3. Scale-Location（標準化殘差的平方根）
png("img/diagnostic_plot_3.png", width = png_width, height = png_height, res = png_res)
plot(model, which = 3, main = "尺度-位置圖",
     xlab = "配適值", ylab = "標準化殘差的平方根",
     cex.main = 1.2, cex.lab = 1.1)
dev.off()

# 4. Residuals vs Leverage（殘差 vs 槓桿值）
png("img/diagnostic_plot_4.png", width = png_width, height = png_height, res = png_res)
plot(model, which = 5, main = "殘差 vs 槓桿值",
     xlab = "槓桿值", ylab = "標準化殘差",
     cex.main = 1.2, cex.lab = 1.1)
dev.off()

# 生成組合圖
png("img/diagnostic_plots_all.png", width = 1200, height = 900, res = 120)
par(mfrow = c(2, 2))
plot(model, which = 1:4,
     main = c("殘差 vs 配適值", "常態 Q-Q 圖", "尺度-位置圖", "殘差 vs 槓桿值"),
     cex.main = 1.1)
dev.off()

print("診斷圖已生成完成！")
print("檔案位置：")
print("- img/diagnostic_plot_1.png")
print("- img/diagnostic_plot_2.png")
print("- img/diagnostic_plot_3.png")
print("- img/diagnostic_plot_4.png")
print("- img/diagnostic_plots_all.png")