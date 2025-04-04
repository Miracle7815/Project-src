import pandas as pd
import matplotlib.pyplot as plt

# 读取Excel文件
df = pd.read_excel('data.xlsx')

# 提取数据
module_name = df.iloc[0, 0]  # 获取模块名称
data_values = df.iloc[0, 1:].values  # 获取T1-T300的数据
time_points = range(1, len(data_values)+1)  # 创建时间点序列(1-300)

# 创建图表
plt.figure(figsize=(15, 6))

# 绘制曲线
plt.plot(time_points, data_values,
         label=f'Coverage: {module_name}',
         color='royalblue',
         linewidth=2)

# 标记数据突变点（从0.84跳到0.9的位置）
change_point = None
for i in range(1, len(data_values)):
    if data_values[i] != data_values[i-1]:
        change_point = i+1  # +1因为时间点从1开始
        plt.axvline(x=change_point, color='red', linestyle='--', alpha=0.5)
        plt.text(change_point, 0.85, f'T{change_point}',
                 rotation=90, va='bottom', ha='right', color='red')
        break

# 添加图表元素
plt.title(f'Coverage Timeline for {module_name}', fontsize=14, pad=20)
plt.xlabel('Time Points (T1-T300)', fontsize=12)
plt.ylabel('Coverage Rate', fontsize=12)
plt.ylim(0, 1.00)  # 设置Y轴范围以更好显示数据变化
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(loc='upper left')

# 调整X轴刻度
plt.xticks([1, 50, 100, 150, 200, 250, 300])

# 显示图表
plt.tight_layout()
plt.show()