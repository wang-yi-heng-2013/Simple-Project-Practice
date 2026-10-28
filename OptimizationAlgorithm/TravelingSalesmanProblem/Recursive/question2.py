# 解决20个城市的旅行商问题
import random
import time
from BruteForce import brute_force

# 先生成一个20*20的列表，初始化值为-1，表示所有城市之间路不通
D=[[-1 for _ in range(20)] for _ in range(20)]

# 给城市与城市之间的距离随机赋初值
for i in range(len(D)):
    for j in range(len(D[0])):
        # 去掉自回路的存在
        if i==j:
            continue
        num = random.randint(1,100)
        # 所做图为无向图，故为对称矩阵
        D[i][j] = num
        D[j][i] = num

# print(D)

S = brute_force(D,0)

# 记录暴力枚举求解所花费的时间
start_time = time.time()
# 调用方法求解最短路径
path_min=S.tsp()
end_time = time.time()
print("花费时间：",end_time-start_time,"秒")
print("最短路径：",path_min)

# 开始回溯
M = S.array
lists = list(range(len(S.X)))
start = S.start_node
path = ""+str(start+1)

# 通过回溯矩阵找出城市遍历顺序
while len(lists) > 0:
    # 去掉当前已经经历过的节点
    lists.pop(lists.index(start))
    # 计算剩余未经历节点在回溯表中对应的列数
    m = S.transfer(lists)
    # 获得下一个节点
    next_node = S.array[start][m]
    path+="--->"+str(next_node+1)
    start = next_node

print("城市遍历顺序：",path)