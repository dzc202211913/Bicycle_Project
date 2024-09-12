import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

v = 3.7
g = 9.81
M = np.array([[3.98, 0.285],
              [0.285, 0.146]])
K0 = np.array([[-6.62, -0.5],
               [-0.5, -0.125]])
K2 = np.array([[0, 7.33],
               [0, 0.6]])
C1 = np.array([[0 , 4.66],
               [-0.51, 0.404]])

Mat1 = np.block([[np.eye(2), np.zeros((2,2))],
              [v*C1, M]]) 
Mat2 = np.block([[np.zeros((2,2)), np.eye(2)],
              [-(g*K0+v*v*K2), np.zeros((2,2))]]) 
A = np.linalg.inv(Mat1)@Mat2

# 定义初始条件
x0 = np.array([0.174, 0, 0, 0]) #10°的弧度制

# 定义系统的微分方程
def system(t, x):
    return A @ x

# 模拟系统响应
t_span = (0, 2)  # 模拟 10 秒
t_eval = np.linspace(0, 2, 1000)  # 1000 个点进行采样
sol = solve_ivp(system, t_span, x0, t_eval=t_eval)

# 提取时间和状态值
time_points = sol.t
state_values = sol.y  # 所有状态变量的响应值

# 绘制四个状态变量随时间的变化
plt.figure(figsize=(10, 6))

for i in range(2):
    plt.plot(time_points, state_values[i, :], label=f'State {i+1}')

plt.title('System Initial Response')
plt.xlabel('Time (s)')
plt.ylabel('State Variables')
plt.legend()
plt.grid(True)
plt.show()