import time
from BruteForce import brute_force

# 用无向图保存路径数据
D=[
[-1, 12, 1, 8],
[ 12,-1, 2, 3],
[ 1, 2,-1, 10],
[ 8, 3, 10,-1]
]

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
path = ""+str(start)

# 通过回溯矩阵找出城市遍历顺序
while len(lists) > 0:
    # 去掉当前已经经历过的节点
    lists.pop(lists.index(start))
    # 计算剩余未经历节点在回溯表中对应的列数
    m = S.transfer(lists)
    # 获得下一个节点
    next_node = S.array[start][m]
    path+="--->"+str(next_node)
    start = next_node

print("城市遍历顺序：",path)