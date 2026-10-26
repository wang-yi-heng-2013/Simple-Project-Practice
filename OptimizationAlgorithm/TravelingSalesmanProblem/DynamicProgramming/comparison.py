import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

x=[4,5,6,7,8,9,10,11,12,13]
y1=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.8, 7.8, 88.5, 1071.0]
y2=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.8, 0.0, 0.0, 0.0]

plt.plot(x,y1,label="暴力枚举")
plt.plot(x,y2,label="动态规划")
plt.legend()

plt.xticks(np.arange(4, 14, 1))

plt.title("两种方法在不同数据规模下的运行时间")
plt.xlabel("城市数量/个")
plt.ylabel("运行时间/秒")

plt.savefig("对比图.png")
plt.show()