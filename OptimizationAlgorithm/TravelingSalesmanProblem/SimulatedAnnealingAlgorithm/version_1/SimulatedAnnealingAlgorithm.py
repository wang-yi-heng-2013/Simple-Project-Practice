import math
import random


# 针对旅行商问题设计的模拟退火算法
class simulatedannealingalgorithm:


    def __init__(self,city,temperature=100,rate=0.9,num_solution_same_temperature=10):
        # 初始化各参数
        self.city=city  # 保存各个城市的坐标
        self.num_city=len(self.city)    # 获得城市数量
        self.city_grapf=[ [0]*self.num_city for _ in range(self.num_city) ] # 保存城市间距离的无向图

        self.temperature=temperature    # 初始温度
        self.rate=rate  # 退火步长
        self.num_solution_same_temperature=num_solution_same_temperature    # 每次等温过程中获取的解的数量

        self.distance_current = 10000  # 当前解的路径（单个值）
        self.distance_best_same_temperature = 10000  # 当前温度下最优解的最短路径（单个值）
        self.distance_best_different_temperature = [10000,]  # 不同温度下最优解的最短路径（列表：所有解）
        self.solution_current = [ i for i in range(self.num_city) ]  # 当前解（单个值）
        self.solution_best_same_temperature = [ i for i in range(self.num_city) ]   # 当下温度获得的最优解（单个值）
        self.solution_best_different_temperature = [ list(range(self.num_city)) ]  # 不同温度下比较出来的最优解（列表：所有解）


    # 算法开始入口
    def start(self):
        # 获得城市间距离的无向图
        self.distance_city(self.city, self.num_city)
        # 开始模拟退火算法
        self.simulated_annealing_algorithm(self.temperature,self.rate,self.num_solution_same_temperature)


    # 计算各个城市间的距离
    def distance_city(self, city, num_city):
        for i in range(num_city):
            for j in range(num_city):
                if i!=j:
                    dis=math.sqrt( math.pow(city[i][0]-city[j][0],2)+math.pow(city[i][1]-city[j][1],2) )
                    self.city_grapf[i][j]=dis
                    self.city_grapf[j][i]=dis

    # 使用模拟退火算法计算最短路径
    def simulated_annealing_algorithm(self,temperature,rate,num_solution_same_temperature):
        # 随机生成一个初始解（打乱当前解排序即可）
        self.creat_initial_solution()


        while temperature>0.1:
            for i in range(num_solution_same_temperature):
                # 探索新的解
                solution_temp = self.reach_new_solution(self.solution_current)
                distance_temp = self.distance_calculate(solution_temp,self.city_grapf)
                # 比较新解与当前解（暂时用这种直接比较）
                if distance_temp < self.distance_current :
                    self.solution_best_same_temperature=solution_temp
                    self.distance_best_same_temperature=distance_temp

                    self.solution_current=solution_temp
                    self.distance_current=distance_temp


            # 将该温度下的最优解存进列表中
            self.solution_best_different_temperature.append(self.solution_current)
            self.distance_best_different_temperature.append(self.distance_current)

            # 将同一温度下的最优解更新为当前解
            self.solution_best_same_temperature = self.solution_current
            self.distance_best_same_temperature = self.distance_current

            # 温度下降（迭代）
            temperature= rate * temperature



    # 随机生成一个初始解
    def creat_initial_solution(self):
        for i in range(self.num_city):
            target=random.randint(0,self.num_city-1)
            temp=self.solution_current[i]
            self.solution_current[i]=self.solution_current[target]
            self.solution_current[target]=temp
        self.distance_current=self.distance_calculate(self.solution_current,self.city_grapf)

        # 让所有需要的解都等于这个初始解
        self.distance_best_same_temperature = self.distance_current
        self.distance_best_different_temperature[0] = self.distance_current
        self.solution_best_same_temperature = self.solution_current
        self.solution_best_different_temperature[0] = self.solution_current


    # 通过城市列表计算路径
    def distance_calculate(self,solution,city_graph):
        distance=0
        for i in range(len(solution)-1):
            distance+=city_graph[solution[i]][solution[i+1]]
        distance+=city_graph[solution[-1]][solution[0]]
        return distance


    # 获得新解的方法
    def reach_new_solution(self,now_solution):
        new_solution=now_solution

        # 随机选择对当前路线的修改操作
        # （暂时默认1）
        # choose=random.randint(1,3)
        choose=1
        if choose==1:
            # 导致一部分城市顺序
            city_a=random.randint(0,self.num_city-5)
            new_solution[city_a:city_a+4]=new_solution[city_a:city_a+4][::-1]


        return new_solution


    # 获取最优解
    def solution_best(self):
        best_distance = min(self.distance_best_different_temperature)
        location= self.distance_best_different_temperature.index(best_distance)
        best_solution = self.solution_best_different_temperature[location]

        return best_solution,best_distance
