import numpy as np
import control  as ctrl
from scipy.linalg import solve_continuous_are
import matplotlib.pyplot as plt

g = 9.81
M = np.array([[80.81722 , 2.31941332208709],
     [2.31941332208709,0.29784188199686]])
K0 = np.array([[-80.95,-2.59951685249872],
      [-2.59951685249872,-0.80329488458618]])
K2 = np.array([[0,76.59734589573222],
      [0,2.65431523794604]])
C1 = np.array([[0 , 33.86641391492494],
      [-0.85035641456978,1.68540397397560]])

v = 0

Mat1 = np.block([[np.eye(2), np.zeros((2,2))],
              [v*C1, M]]) 
Mat2 = np.block([[np.zeros((2,2)), np.eye(2)],
              [-(g*K0+v*v*K2), np.zeros((2,2))]]) 
A = np.linalg.inv(Mat1)@Mat2

Mat3 = np.array([[0,0],
                 [0,0],
                 [1,0],
                 [0,1]]) # 这里是因为只有两个状态是可控的
B = np.linalg.inv(Mat1)@Mat3

C = np.array([[1,0,0,0],[0,1,0,0]])

sys = ctrl.StateSpace(A, B, C, np.zeros((2,2)))

# 设计反馈矩阵

Q = np.array([[10,0,0,0],[0,10,0,0],[0,0,100,0],[0,0,0,1000]])
R = np.array([[1,0],[0,10000]])

# 求解Riccati方程
P = solve_continuous_are(A, B, Q, R)

# 计算反馈增益矩阵K
K = np.linalg.inv(R).dot(B.T.dot(P))
print(K)

syscl = ctrl.StateSpace(A-B@K, np.zeros((4,2)), C, np.zeros((2,2)))

# 定义初始状态
x0 = np.array([10, 15, 0, 0])

# 定义时间向量
t = np.linspace(0, 5, 100)

# 计算系统的初始响应
t, y, x = ctrl.initial_response(syscl, T=t, X0=x0, return_x=True)

# 绘制每个状态变量的响应
plt.figure()
plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
plt.rcParams['axes.unicode_minus'] = False    # 解决负号显示问题
for i in range(x.shape[0]):
    plt.plot(t, x[i, :], label=f'x{i+1}')
plt.xlabel('时间 (s)')
plt.ylabel('状态变量')
plt.title('状态变量的初始响应')
plt.legend()
plt.grid(True)
plt.xlim(0, 5)  # 设置x轴范围
plt.ylim(-90, 90)  # 设置y轴范围
plt.show()