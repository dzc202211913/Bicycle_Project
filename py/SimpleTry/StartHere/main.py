import numpy as np
import tracks
import detect

# 选择轨迹
x , y = tracks.track1()

# 两点间时间间隔
t = 0.1

# 定义初始状态
v = 0
x_0 = np.array([5, 0, 0, 0])
x0 = 0
y0 = 0
vH = np.array([1, 0])

# 自行车的位置轨迹表示
a = [0]
b = [0]

for i in range(1001):
    # 下面这个过程是在只知道轨迹的情况下去估算目标的速度以及运动方向
    if i-1 < 0:
        xN = 0
        yN = 0
        vN = 0
        vHN = np.array([1, 0])
    else:
        xP = x[i-1]
        xN = x[i]
        yP = y[i-1]
        yN = y[i]
        vN,vHN = detect.detect(xP,yP,xN,yN,t)

    # 设计一个跟随系统
    a1 = a[i]