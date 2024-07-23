import numpy as np
import matplotlib.pyplot as plt

def track1():
    #时间向量，总共移动100秒，其中1秒汇报10次坐标，共1000个点
    T = np.linspace(0, 100, 1000)

    #速度的规定，前10秒加速，最后3秒减速，最高速度3m/s
    a1 = 0.3
    a2 = -1

    # 转圈半径
    R = 0

    # 坐标集合以及速度方向和速度值
    x = [0]
    y = [0]
    vH = np.array([1,0])

    # 录入坐标数据
    for t in T:
        # 临时坐标数据初始化
        x1 = 0
        y1 = 0
        # 实际坐标读取
        x2 = x[round(10*t)-1]
        y2 = y[round(10*t)-1]
        # 速度设置
        if t <= 10:
            v = a1 * t
        elif t >= 97:
            v = v + a2 * (100 - t)
        else:
            v = 3
        # 速度方向更新：暂时考虑直线
        
        # 临时坐标生成
        x1 = x2 + v * t * vH[0]
        y1 = y2 + v * t * vH[1]
        
        x.append(x1)
        y.append(y1)
    
    return x, y

# # 绘制状态图像
# plt.figure(figsize=(10, 6))
# plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
# plt.rcParams['axes.unicode_minus'] = False    # 解决负号显示问题
# # 创建折线图
# plt.plot(x, y, marker='o', markersize=1, linestyle='-', color='b', label='轨迹')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.legend()
# plt.title('状态随时间的演变')
# plt.xlim(0, 100)  # 设置x轴范围
# plt.ylim(-30, 30)  # 设置y轴范围
# plt.grid(True)

# plt.show()