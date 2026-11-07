import matplotlib.pyplot as plt

# 绘制损失函数下降趋势图
def loss_changes(loss):
    x=range(len(loss))
    y=loss

    plt.plot(x,y)
    plt.xlabel("温度下降次数")
    plt.ylabel("最短路径")
    plt.title("模拟退火算法最短路径下降趋势")
    #plt.savefig("version_4_result.png")
    plt.show()

# 绘制最短路线
def path_vision_plot(x,y,solution):
    x_order=[]
    y_order=[]
    for i in range(len(solution)):
        node=solution[i]
        x_order.append(x[node])
        y_order.append(y[node])

    # 首尾相连
    x_order.append(x_order[0])
    y_order.append(y_order[0])

    plt.plot(x_order,y_order,marker="o",linestyle="-")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("城市最短路径可视化连接")
    #plt.savefig("version_4_path.png")
    plt.show()