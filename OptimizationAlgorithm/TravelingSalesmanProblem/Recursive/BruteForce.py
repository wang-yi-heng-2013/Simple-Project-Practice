# 针对旅行商问题专门设计的暴力枚举求解模型
class brute_force:
    def __init__(self,X,start_node):

        self.X = X  # 距离矩阵
        self.start_node = start_node    # 开始的节点
        # 用于记录每个状态下的最优选择
        self.array = [[0]*(2**(len(self.X)-1)) for i in range(len(self.X))] # 记录处于x节点，未经历M个节点时，矩阵储存x的下一步是M中哪个节点

    # 采用0,1表示一个城市是否有去过，只需存储一个正整数即可表示所有城市的状态，用该方法来进行转化
    # 将剩余未被访问的节点按顺序排列为二进制值，并转换为十进制，作为返回值
    def transfer(self, sets):
        su = 0
        for s in sets:
            su = su + 2**(s-1) # 二进制转换

        # 返回值表示当前经历节点下，剩余未经历节点组合所代表的列数
        return su

    # 暴力枚举起始入口
    def tsp(self):
        s = self.start_node
        num = len(self.X)
        cities = list(range(num))   # 创建节点的集合
        cities.pop(cities.index(s)) # 将起点排除，构建未经历节点的集合
        node  = s   # 初始节点
        return self.solve(node, cities) # 求解函数

    # 求解从node节点到所有未经过的节点的最短路径
    def solve(self, node, future_sets):
        # 迭代终止条件，表示没有了未遍历节点，直接连接当前节点和起点即可
        if len(future_sets) == 0:
            return self.X[node][self.start_node]

        # 用于保存所求最小路径
        d = 99999
        # node如果经过future_sets中节点，最后回到原点的距离
        distance = []

        # 遍历未经历的节点
        for i in range(len(future_sets)):
            s_i = future_sets[i]
            copy = future_sets[:]

            # 删除第i个节点，认为已经完成对其的访问
            copy.pop(i)
            # 利用递归递推方程
            # 计算选择当前节点后，剩下的节点做出选择后获得的最短路径
            distance.append(self.X[node][s_i] + self.solve(s_i,copy))
            # 根据公式，选择最小的路径作为剩余节点的最优策略
            d = min(distance)

            # 在选定最短路径后，确定node需要连接的下一个节点
            next_one = future_sets[distance.index(d)]
            # 未遍历节点集合，获得其所对应的列数
            c = self.transfer(future_sets)
            # 更新回溯矩阵，(当前节点，未遍历节点集合)——>下一个节点
            self.array[node][c] = next_one

        # 循环结束后，最终的d值是经历了所有节点的最短路径
        return d
