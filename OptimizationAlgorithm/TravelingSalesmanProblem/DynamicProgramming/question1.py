from TSP_DynamicProgramming import tsp_dynamic_programming

# 用无向图保存城市之间的距离
dist = [
    [0, 12, 1, 8],
    [12, 0, 2, 3],
    [1, 2, 0, 10],
    [8, 3, 10, 0]
]

# 调用动态规划方法获取最短路径和路线
distance, path = tsp_dynamic_programming(dist)

# 输出结果
print(f"最短路径长度: {distance}")
print(f"最优路径: {' -> '.join(map(str, path))}")