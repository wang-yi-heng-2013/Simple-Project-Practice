# 解决20个城市的旅行商问题
import random
import time
from TSP_DynamicProgramming import tsp_dynamic_programming

# 先生成一个20*20的列表，初始化值为0，表示所有城市之间路不通
dist=[[0 for _ in range(20)] for _ in range(20)]

# 给城市与城市之间的距离随机赋初值
for i in range(len(dist)):
    for j in range(len(dist[0])):
        # 去掉自回路的存在
        if i==j:
            continue
        num = random.randint(1,100)
        # 所做图为无向图，故为对称矩阵
        dist[i][j] = num
        dist[j][i] = num

#for row in dist:
#    print(row)

# 记录动态规划求解所花费的时间
start_time = time.time()
# 调用动态规划方法获取最短路径和路线
cost, path = tsp_dynamic_programming(dist)
end_time = time.time()
# 为便于实验报告上展示清晰，故将路径字符串切断换行输出
path_str_1 = ' -> '.join(map(str, path[:10])) + ' -> '
path_str_2 = ' -> '.join(map(str, path[10:]))

# 输出结果
print(f"花费时间：{end_time - start_time}秒")
print(f"最短路径长度: {cost}")
print(f"最优路径: ")
print(path_str_1)
print(path_str_2)
