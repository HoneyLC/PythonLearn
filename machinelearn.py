"""
机器学习
"""
# matplotlib 画图: 散点图,柱状图,折线图
import random

import matplotlib
from matplotlib import pyplot

font = {'family': 'MicroSoft YaHei', 'weight': 'bold'}
matplotlib.rc("font", **font)

# 画两小时内的气温
x = range(0, 120)
y = [random.randint(20, 35) for i in range(120)]
y_2 = [random.randint(20, 35) for i in range(120)]
pyplot.figure(figsize=(20, 8), dpi=80)
# 参数说明 : label : 图例, color : 颜色 , linestyle : 线段格式
pyplot.plot(x, y, label="北京", color='orange')
pyplot.plot(x, y_2, label="西安", color='cyan', linestyle='-.')
# 调整x轴的刻度
_xtick_lables = ["10点{}分".format(i) for i in range(60)]
_xtick_lables += ["11点{}分".format(i) for i in range(60)]
pyplot.xticks(x[::3], _xtick_lables[::3], rotation=45)

# 绘制网格
pyplot.grid(alpha=0.4)
# 添加描述信息
pyplot.xlabel("时间")
pyplot.ylabel("温度 单位(℃)")
pyplot.title("温度折线图")

# 添加图例
pyplot.legend()
# 图片保存
pyplot.savefig("./sig_size.png")
pyplot.show()

# 其他的图形参考:https://matplotlib.org/gallery/index.html
