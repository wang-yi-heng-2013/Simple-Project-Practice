import random
import matplotlib.pyplot as plt
from SimulatedAnnealingAlgorithm import simulatedannealingalgorithm
import ChartPainting

# 让输出的图表能显示中文
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 随机生成30个城市的坐标
city = []
for _ in range(30):
    x = round(random.random()*100,2)
    y = round(random.random()*100,2)
    city.append([x,y])

# 绘制这30个城市分布的散点图
x = [ a[0] for a in city ]
y = [ a[1] for a in city ]
plt.scatter(x,y,color='red',s=60,zorder=5)

plt.xlabel("X")
plt.ylabel("Y")
plt.title("城市分布散点图")
plt.savefig("version_2_city.png")
plt.show()

# 调用模拟退火算法的模型来求解最短路径
city_order = simulatedannealingalgorithm(city)
city_order.start()
# 获取最短路线和对应距离
best_solution,best_distance = city_order.solution_best()

# 获取损失函数
loss=city_order.distance_best_different_temperature
print(loss)
print(loss[0],loss[-1])
print(best_solution)
print(best_distance)

# 绘制损失函数折线图
ChartPainting.loss_changes(loss)
# 绘制各个城市的连线图
ChartPainting.path_vision_plot(x,y,best_solution)