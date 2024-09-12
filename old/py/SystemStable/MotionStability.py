import numpy as np
import control as ctrl
import matplotlib.pyplot as plt
import ADC

g = 9.81
M = np.array([[3.98, 0.285],
              [0.285, 0.146]])
K0 = np.array([[-6.62, -0.5],
               [-0.5, -0.125]])
K2 = np.array([[0, 7.33],
               [0, 0.6]])
C1 = np.array([[0 , 4.66],
               [-0.51, 0.404]])

v = 1

Mat1 = np.block([[np.eye(2), np.zeros((2,2))],
              [v*C1, M]]) 
Mat2 = np.block([[np.zeros((2,2)), np.eye(2)],
              [-(g*K0+v*v*K2), np.zeros((2,2))]]) 
A = np.linalg.inv(Mat1)@Mat2

B = np.linalg.inv(Mat1)

C = np.array([[1,0,0,0],[0,1,0,0]])

D = np.zeros((2,4))

#矩阵Mat3用于选择输入的后两个
Mat3 = np.array([[0,0,0,0],[0,0,0,0],[0,0,1,0],[0,0,0,1]])
B = B @ Mat3

F, G = ADC.sys(A, B)

Q = np.array([[10,0,0,0],[0,100,0,0],[0,0,1,0],[0,0,0,1]])  # 状态权重矩阵
# 这里选择了给车把转角δ更大的权重，是为了减小稳定性调控对于航向的影响
R = np.array([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])  # 输入权重矩阵

# 创建离散时间状态空间系统
sys_d = ctrl.ss(F, G, C, D, True)

# 计算LQR反馈增益矩阵
K, S, E = ctrl.dlqr(F, G, Q, R)

# 计算三秒内的响应情况
t = np.linspace(0, 3, 300)
x0 = np.array([0.174, 0, 0, 0]).T

# 用循环来算状态响应，要累死你爹吗
x1out = []
x2out = []
x3out = []
x4out = []
u3in = []
u4in = []
# 只想知道以上这四个值，画出折线图就行
u0 = np.array([0, 0, 0, 0])
for i in range(300):
    u = -K @ x0
    # 饱和函数
    if u[2] >= 2.5:
        u[2] = 2.5
    if u[2] <= -2.5:
        u[2] = -2.5
    if u[3] >= 2.5:
        u[3] = 2.5
    if u[3] <= -2.5:
        u[3] = -2.5
    x1 = F @ x0 + G @ u
    x1out.append(x1[0])
    x2out.append(x1[1])
    x3out.append(x1[2])
    x4out.append(x1[3])
    u3in.append(u[2])
    u4in.append(u[3])
    x0 = x1

# 绘制状态图像
plt.figure(figsize=(6, 6))
plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
plt.rcParams['axes.unicode_minus'] = False    # 解决负号显示问题
plt.subplot(2, 1, 1)
# 创建折线图
plt.plot(t, x1out, marker='o', markersize=1, linestyle='-', color='b', label='x1')
plt.plot(t, x2out, marker='s', markersize=1, linestyle='--', color='r', label='x2')
plt.plot(t, x3out, marker='o', markersize=1, linestyle='-', color='y', label='x3')
plt.plot(t, x4out, marker='s', markersize=1, linestyle='--', color='g', label='x4')
plt.xlabel('时间')
plt.ylabel('状态')
plt.legend()
plt.title('状态随时间的演变')
plt.xlim(0, 3)  # 设置x轴范围
plt.ylim(-1.5, 1.5)  # 设置y轴范围
plt.grid(True)

# 绘制输入图像
plt.subplot(2, 1, 2)
# 创建第一个折线图
plt.plot(t, u3in, marker='o', markersize=1, linestyle='-', color='b', label='Tφ')
# 创建第二个折线图
plt.plot(t, u4in, marker='s', markersize=1, linestyle='--', color='r', label='Tδ')
plt.xlabel('时间')
plt.ylabel('输入')
plt.legend()
plt.title('输入随时间的演变')
plt.grid(True)
plt.xlim(0, 3)  # 设置x轴范围
plt.ylim(-2.8, 2.8)  # 设置y轴范围
plt.tight_layout()
plt.show()