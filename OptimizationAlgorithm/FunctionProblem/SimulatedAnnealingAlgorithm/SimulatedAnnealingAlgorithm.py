import math
import random

class simulatedannealingalgorithm:
    def __init__(self,function,border_min_x,border_max_x,border_min_y,border_max_y,
                 temperature=600,rate=0.97,num_solution_same_temperature=400,early_stopping_times=20):
        # 获取函数和定义域
        self.function=function
        self.border_min_x=border_min_x
        self.border_max_x=border_max_x
        self.border_min_y=border_min_y
        self.border_max_y=border_max_y

        # 获取算法所需参数
        self.temperature=temperature    # 温度
        self.rate=rate  # 降温效率
        self.num_solution_same_temperature=num_solution_same_temperature    # 马尔科夫链长度
        self.early_stopping_times=early_stopping_times  # 早停条件

        # 设定需要保存的解
        self.solution_current=[100,100,100] # 当前解
        self.solution_best_same_temperature=[[100,100,100]]  # 保存各个温度下获得的最优解
        self.solution_best_different_temperature=[100,100,100]   # 全局最优解


    # 算法开始入口
    def start(self):
        self.creat_initial_solution()
        self.simulated_annealing_algorithm()


    # 模拟退火算法迭代过程
    def simulated_annealing_algorithm(self):
        count_sum=0
        count_outer=0
        while self.temperature>0.01 :
            count_inner=0
            for _ in range(self.num_solution_same_temperature):
                # 探索新解
                solution_new=self.search_new_solution(self.solution_current)

                # 比较新解与全局最优解
                if solution_new[2]<self.solution_best_different_temperature[2] :
                    self.solution_best_different_temperature=solution_new.copy()

                # 比较新解与当前解
                if self.choose_new_solution(solution_new[2],self.solution_current[2],self.temperature) :
                    self.solution_current=solution_new.copy()
                    count_inner=0
                else:
                    count_inner=count_inner+1

                # 判断是否触发早停
                if count_inner>=self.early_stopping_times :
                    break


            # 内部循环结束，保存当前温度下的当前解
            self.solution_best_same_temperature.append(self.solution_current.copy())

            # 判断是否触发早停
            if self.solution_best_same_temperature[-1]==self.solution_best_same_temperature[-2] :
                count_outer=count_outer+1
            else:
                count_outer=0

            # 早停条件判断
            if count_outer >= self.early_stopping_times:
                print("外部循环触发早停,结束迭代，温度下降", count_sum, "次")
                break

            count_sum=count_sum+1
            self.temperature=self.temperature*self.rate


    # 随机获取一个初始解
    def creat_initial_solution(self):
        self.solution_current[0] = random.random() * 10 - 5
        self.solution_current[1] = random.random() * 10 - 5
        self.solution_current[2] = self.function(self.solution_current[0],self.solution_current[1])

        # 将所有解都设置为该初始值
        self.solution_best_different_temperature=self.solution_current.copy()
        self.solution_best_same_temperature[0]=self.solution_current.copy()


    # 状态生成函数（探索新解）
    def search_new_solution(self,solution_old):
        # 在当前解周围添加扰动，从而迭代出新解坐标
        solution_new=[100,100,100]
        while not (solution_new[0]>=-5 and solution_new[0]<=5 and solution_new[1]>=-5 and solution_new[1]<=5) :
            solution_new[0] = solution_old[0] + random.gauss(0, 0.1)
            solution_new[1] = solution_old[1] + random.gauss(0, 0.1)

        # 获取新解的函数值
        solution_new[2]=self.function(solution_new[0],solution_new[1])

        return solution_new


    # 状态选择函数
    def choose_new_solution(self,solution_new,solution_old,temperature):
        chance_of_drop=0
        if solution_new<solution_old :
            return True
        elif math.isclose(solution_new,solution_old) :
            chance_of_drop=1
        else:
            chance_of_drop = math.exp(-(solution_new - solution_old) / temperature)

        if chance_of_drop>random.random() :
            return True

        return False


    # 获取最优解
    def solution_best(self):
        best_solution=self.solution_best_same_temperature[-1].copy()
        if self.solution_best_different_temperature[2]<best_solution[2] :
            best_solution=self.solution_best_different_temperature.copy()

        return best_solution
