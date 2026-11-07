import time
import matplotlib.pyplot as plt
from SimulatedAnnealingAlgorithm import simulatedannealingalgorithm
import ChartPainting

# 让输出的图表能显示中文
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 指定的30个城市的坐标
C =[[41, 94],[37, 84],[54, 67],[25, 62],[7, 64],[2, 99],[68, 58],[71, 44],
    [54, 62],[83, 69],[64, 60],[18, 54],[22, 60],[83, 46],[91, 38],[25, 38],
    [24, 42],[58, 69],[71, 71],[74, 78],[87, 76],[18, 40],[13, 40],[82, 7],
    [62, 32],[58, 35],[45, 21],[41, 26],[44, 35],[4, 50]]

'''
C =[[1304, 2312],[3639, 1315],[4177, 2244],[3712, 1399],[3488, 1535],[3326, 1556],
    [3238, 1229],[4196, 1004],[4312, 790],[4386, 570],[3007, 1970],[2562, 1756],
    [2788, 1491],[2381, 1676],[1332, 695],[3715, 1678],[3918, 2179],[4061, 2370],
    [3780, 2212],[3676, 2578],[4029, 2838],[4263, 2931],[3429, 1908],[3507, 2367],
    [3394, 2643],[3439, 3201],[2935, 3240],[3140, 3550],[2545, 2357],[2778, 2826],[2370, 2975]]
'''

# 绘制这30个城市分布的散点图
x = [ a[0] for a in C ]
y = [ a[1] for a in C ]
plt.scatter(x,y,color='red',s=60,zorder=5)

plt.xlabel("X")
plt.ylabel("Y")
plt.title("城市分布散点图")
#plt.savefig("version_4_city.png")
plt.show()

# 调用模拟退火算法的模型来求解最短路径
city_order = simulatedannealingalgorithm(C)
start=time.time()
city_order.start()
end=time.time()
# 获取最短路线和对应距离
best_solution,best_distance = city_order.solution_best()

# 获取损失函数
loss=city_order.distance_best_same_temperature
times_temperature_drop=len(loss)
print("损失函数：",loss)
print("损失函数的初始值：",loss[0],"结束值：",loss[-1])
print("损失值总数统计：",times_temperature_drop)
print("最短路径的路线：",best_solution)
print("最短路径：",best_distance)
print("计算",len(C),"个城市花费的时间：",round(end-start,4))

# 绘制损失函数折线图
ChartPainting.loss_changes(loss)
# 绘制各个城市的连线图
ChartPainting.path_vision_plot(x,y,best_solution)
