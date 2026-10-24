# 使用动态规划求解旅行商问题
def tsp_dynamic_programming(dist):
    # 获取城市数量
    n = len(dist)

    # 如果城市数量不超过1，则没有计算的必要，直接返回
    if n <= 1:
        return 0, [0]

    # 获取正无穷大值
    INF = float('inf')
    # 列表dp[mask][i]用于记录每一种状态的最短距离
    # 其中，mask用二进制表示，第i位为1表示已访问城市i;为0表示未访问
    # 默认从第一个城市出发，经过mask中的城市，最后到达城市i的最短距离
    dp = [[INF] * n for _ in range(1 << n)]
    # 列表parent记录路径，用于回溯
    parent = [[-1] * n for _ in range(1 << n)]

    # 默认从城市0(即第一个城市)出发
    dp[1][0] = 0

    # 遍历所有"已访问城市集合"状态
    # 每个城市只有已访问/未访问(1/0)两种状态
    # 需要遍历2^n次，即"已访问城市集合"有2^n种可能
    for mask in range(1 << n):
        # 虽然每种状态都要遍历，但出发城市必须已访问，即为1
        # 检查mask的第一位是否为1，即第一个城市是否已访问
        if not (mask & 1):
            continue

        # 遍历已访问城市，将遍历到的城市当做当前所在城市
        # 即访问过mask中的城市后，到达城市i的状态
        for i in range(n):
            # i必须在mask中，且dp[mask][i]可达
            if not (mask & (1 << i)) or dp[mask][i] == INF:
                continue

            # 遍历未访问城市，将遍历到的城市作为下一个要访问的城市
            # 即在mask条件下，将"城市i到城市j"作为一种遍历到的可能状态
            for j in range(n):
                # 判断城市j是否已访问，若已访问则跳过
                if mask & (1 << j):
                    continue

                # 将城市j作为下一个要访问城市
                # 用临时变量暂存更新后的路径长度和访问过的城市集合
                new_mask = mask | (1 << j)
                new_cost = dp[mask][i] + dist[i][j]
                # 判断该状态下所走过的路径是否比已保存的路径短
                # 若更短，则更新路径表和路线表
                if new_cost < dp[new_mask][j]:
                    dp[new_mask][j] = new_cost
                    parent[new_mask][j] = i

    # 所有城市都已访问，找回到起点的最小总距离
    # 所求的最短路径应该在所有城市都以访问过的状态下，即mask中的每一位都为1
    full_mask = (1 << n) - 1
    min_cost = INF
    last_city = -1
    for i in range(1, n):
        if dp[full_mask][i] == INF:
            continue
        # 计算该状态下每一列代表的最短路径并更新
        # 第i列表示城市i作为最后一个访问的城市
        total = dp[full_mask][i] + dist[i][0]
        if total < min_cost:
            min_cost = total
            last_city = i

    # 回溯得到最优路径
    path = []
    mask = full_mask
    cur = last_city
    while cur != -1:
        path.append(cur+1)
        prev = parent[mask][cur]
        mask ^= (1 << cur)
        cur = prev

    # 由于路线是通过回溯得到的，因此最终结果要倒置
    path.reverse()
    path.append(path[0])

    # 返回最短路径和路线
    return min_cost, path
