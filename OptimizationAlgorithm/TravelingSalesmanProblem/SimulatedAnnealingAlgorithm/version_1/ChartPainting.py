import matplotlib.pyplot as plt

def loss_changes(loss):
    x=range(len(loss))
    y=loss

    plt.plot(x,y)
    plt.xlabel("温度下降次数")
    plt.ylabel("最短路径")
    plt.title("模拟退火算法最短路径下降趋势")
    plt.savefig("version_2_result.png")
    plt.show()


def path_vision_plot(x,y,solution):
    x_order=[]
    y_order=[]
    for i in range(len(solution)):
        node=solution[i]
        x_order.append(x[node])
        y_order.append(y[node])

    plt.plot(x,y,marker="o",linestyle="-")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("城市最短路径可视化连接")
    plt.savefig("version_2_path.png")
    plt.show()