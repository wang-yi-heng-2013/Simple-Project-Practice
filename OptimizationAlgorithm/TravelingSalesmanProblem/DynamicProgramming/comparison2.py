import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

x=[15, 16, 17, 18, 19, 20, 21, 22, 23]
y=[0.31, 0.65, 1.58, 3.47, 7.12, 15.45, 32.99, 73.09, 177.80]

plt.plot(x,y,label="动态规划")
plt.legend()

plt.xticks(np.arange(14, 24, 1))

plt.title("动态规划在不同城市规模下的运算速度")
plt.xlabel("城市数量/个")
plt.ylabel("运行时间/秒")

plt.savefig("动态规划.png")
plt.show()