import numpy as np
import control  as ctrl
import matplotlib.pyplot as plt

g = 9.81
M = np.array([[3.98, 0.285],
              [0.285, 0.146]])
K0 = np.array([[-6.62, -0.5],
               [-0.5, -0.125]])
K2 = np.array([[0, 7.33],
               [0, 0.6]])
C1 = np.array([[0 , 4.66],
               [-0.51, 0.404]])

v = 0

Mat1 = np.block([[np.eye(2), np.zeros((2,2))],
              [v*C1, M]]) 
Mat2 = np.block([[np.zeros((2,2)), np.eye(2)],
              [-(g*K0+v*v*K2), np.zeros((2,2))]]) 
A = np.linalg.inv(Mat1)@Mat2

B = np.linalg.inv(Mat1)

C = np.array([[1,0,0,0],[0,1,0,0]])

sys = ctrl.StateSpace(A, B, C, np.zeros((2,4)))

# 定义时间向量
t = np.linspace(0, 5, 100)

# 定义控制输入（全为0）
u = np.zeros((4, len(t)))

# 设置初始条件
x0 = np.array([5, 5, 0, 0])  # Example initial condition

# 计算系统响应
T, Y = ctrl.forced_response(sys, T=t, U=u, X0=x0)

# 绘制状态随时间变化的图
plt.figure(figsize=(10, 8))

for i in range(2):
    plt.plot(T, Y[i], label=f'State x{i+1}')

plt.xlabel('Time (s)')
plt.ylabel('States')
plt.title('State Response over Time (Four-Dimensional State Space with Four-Dimensional Control)')
plt.legend()
plt.grid(True)
plt.show()