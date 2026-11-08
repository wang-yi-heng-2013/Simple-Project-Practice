import numpy as np
import matplotlib
matplotlib.use('TkAgg')   # 指定交互式后端，确保弹窗；若报错可删掉这行用默认
import matplotlib.pyplot as plt

# 让输出的图表能显示中文
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


# 图表绘制方法调用接口
def paint_extrance(loss):
    # 定义函数
    def function(x,y):
        return 5*np.cos(x*y)+x*y+pow(y,3)

    # 获取损失值坐标
    x,y,z=[],[],[]
    for temp in loss[::1]:
        x.append(temp[0])
        y.append(temp[1])
        z.append(function(temp[0],temp[1]))

    # 绘制损失值下降趋势图
    loss_changes(z)
    # 绘制3D图
    paint_3D_chart(function,x,y,z)


# 绘制损失函数下降趋势图
def loss_changes(loss):
    x=range(len(loss))
    y=loss

    plt.plot(x,y)
    plt.xlabel("温度下降次数")
    plt.ylabel("函数值")
    plt.title("模拟退火算法求最小函数值下降趋势")
    plt.savefig("question_2_loss.png")
    plt.show()

# 绘制函数的三维图
def paint_3D_chart(function,loss_x,loss_y,loss_z):
    # 生成基于x轴和y轴的网格
    x = np.linspace(-5, 5, 100)
    y = np.linspace(-5, 5, 100)
    X, Y = np.meshgrid(x, y)

    # 获取z的函数值
    Z = function(X,Y)

    # 创建三维坐标轴
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')

    # 绘制函数曲面
    surf = ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.75, edgecolor='none')
    # 绘制迭代坐标
    ax.scatter(loss_x,loss_y,loss_z,c='red',s=30,marker='o',label='loss')

    # 标签与颜色条
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('函数3D坐标图')
    fig.colorbar(surf, shrink=0.5, aspect=10, pad=0.2)

    # 弹出窗口展示（阻塞，直到关闭窗口）
    plt.show()
