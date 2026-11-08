import math
import time
from SimulatedAnnealingAlgorithm import simulatedannealingalgorithm
import ChartPainting


# 要求解最小值的函数
def function(x,y):
    return 5*math.cos(x*y)+x*y+pow(y,3)

# 获取函数定义域
border=[-5,5,-5,5]

# 调用模型
min_function = simulatedannealingalgorithm(function,border[0],border[1],border[2],border[3])
time_start=time.time()
min_function.start()
time_end=time.time()

# 获取所需参数
best_solution=min_function.solution_best()
time_cost=round(time_end-time_start,4)
loss=min_function.solution_best_same_temperature

# 输出结果
print("函数最小值所在坐标：(",best_solution[0],",",best_solution[1],")")
print("最小值：",best_solution[2])
print("模拟退火算法花费时间：",time_cost)
print("损失值总数统计：",len(loss))
print("\n")

# 绘制图表
ChartPainting.paint_extrance(loss)
