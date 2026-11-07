import math
import random

# 针对旅行商问题设计的模拟退火算法
class simulatedannealingalgorithm:

    def __init__(self,city,temperature=600,rate=0.97,num_solution_same_temperature=400,early_stopping_times=20):
        # 初始化各参数
        self.city=city  # 保存各个城市的坐标
        self.num_city=len(self.city)    # 获得城市数量
        self.city_grapf=[ [0]*self.num_city for _ in range(self.num_city) ] # 保存城市间距离的无向图

        self.temperature=temperature    # 初始温度
        self.rate=rate  # 退火步长
        self.early_stopping_times=early_stopping_times  # 重复该次数后最短路径未下降则停止迭代
        self.num_solution_same_temperature=num_solution_same_temperature    # 每次等温过程中获取的解的数量

        self.distance_current = 10000  # 当前解的路径（单个值）
        self.distance_best_different_temperature = 10000  # 所有温度下最优解的最短路径（单个值）
        self.distance_best_same_temperature = [10000,]  # 不同温度下各自最优解的最短路径（列表：所有解）
        self.solution_current = [ i for i in range(self.num_city) ]  # 当前解（单个值）
        self.solution_best_different_temperature = [ i for i in range(self.num_city) ]   # 所有温度下获得的最优解（单个值）
        self.solution_best_same_temperature = [ list(range(self.num_city)) ]  # 降温过程中同一温度内的最优解（列表：所有解）


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
                    self.city_grapf[i][j]=int(dis)
                    self.city_grapf[j][i]=int(dis)


    # 使用模拟退火算法计算最短路径
    def simulated_annealing_algorithm(self,temperature,rate,num_solution_same_temperature):
        # 随机生成一个初始解（打乱当前解排序即可）
        self.creat_initial_solution()

        count_outer = 0
        count_sum = 0
        while temperature>0.01:
            count_inner=0
            for i in range(num_solution_same_temperature):
                # 探索新的解
                solution_temp = self.reach_new_solution(self.solution_current)
                distance_temp = self.distance_calculate(solution_temp,self.city_grapf)
                # 比较新解与记录全局温度的最优解
                if distance_temp < self.distance_best_different_temperature :
                    self.solution_best_different_temperature=solution_temp.copy()
                    self.distance_best_different_temperature=distance_temp

                # 比较新解与当前解
                if self.choose_new_solution(self.distance_current,distance_temp,temperature) :
                    self.solution_current=solution_temp.copy()
                    self.distance_current=distance_temp
                    count_inner=0
                else:
                    # 统计内部循环连续多少次没有更新解
                    count_inner=count_inner+1

                if count_inner>=self.early_stopping_times:
                    break

            # 将该温度下的最优解存进列表中
            self.solution_best_same_temperature.append(self.solution_current.copy())
            self.distance_best_same_temperature.append(self.distance_current)

            # 统计外部循环连续多少次没有更新解
            if self.solution_best_same_temperature[-1]==self.solution_best_same_temperature[-2] :
                count_outer=count_outer+1
            else:
                count_outer=0

            # 早停条件判断
            if count_outer>=self.early_stopping_times :
                print("外部循环触发早停,结束迭代，温度下降",count_sum,"次")
                break

            # 温度下降（迭代）
            count_sum = count_sum + 1
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
        self.distance_best_different_temperature = self.distance_current
        self.distance_best_same_temperature[0] = self.distance_current
        self.solution_best_different_temperature = self.solution_current.copy()
        self.solution_best_same_temperature[0] = self.solution_current.copy()

    # 通过城市列表计算路径
    def distance_calculate(self,solution,city_graph):
        distance=0
        for i in range(len(solution)-1):
            distance+=city_graph[solution[i]][solution[i+1]]
        distance+=city_graph[solution[-1]][solution[0]]
        return distance

    # 获得新解的方法
    def reach_new_solution(self,now_solution):
        new_solution=now_solution.copy()

        # 随机选择对当前路线的修改操作
        choose=random.randint(1,3)
        if choose==1:
            # 部分城市顺序倒置
            length=random.randint(2,6)
            city_a=random.randint(0,self.num_city-length)
            new_solution[city_a:city_a+length]=new_solution[city_a:city_a+length][::-1]
        elif choose==2:
            # 随机选择两个城市交换位置
            city_a = random.randint(0, self.num_city - 1)
            city_b = city_a
            while city_a == city_b:
                city_b = random.randint(0, self.num_city - 1)

            temp=new_solution[city_a]
            new_solution[city_a]=new_solution[city_b]
            new_solution[city_b]=temp
        elif choose==3:
            # 随机选择一个城市插入到随机的位置
            city_a = random.randint(0, self.num_city - 1)
            city_b = city_a
            while city_a == city_b :
                city_b = random.randint(0, self.num_city - 1)

            temp=new_solution.pop(city_a)
            new_solution.insert(city_b,temp)

        return new_solution

    # 状态选择函数
    def choose_new_solution(self,solution_old,solution_new,temperature):

        chance_of_drop = 0
        if solution_new<solution_old :
            return True
        elif solution_new==solution_old:
            chance_of_drop=1
        else:
            chance_of_drop=math.exp( -(solution_new-solution_old)/temperature )

        if chance_of_drop>random.random() :
            return True

        return False

    # 获取最优解
    def solution_best(self):
        best_distance = min(self.distance_best_same_temperature)
        location= self.distance_best_same_temperature.index(best_distance)
        best_solution = self.solution_best_same_temperature[location]

        if best_distance>self.distance_best_different_temperature :
            best_distance=self.distance_best_different_temperature
            best_solution=self.solution_best_different_temperature.copy()

        return best_solution,best_distance
