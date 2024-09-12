import numpy as np
from scipy.integrate import solve_ivp
import csv

v = 3.5
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
B = np.zeros((4,4))
C = np.zeros((4,4))
D = np.zeros((4,4))

# 定义初始条件
x0 = np.array([0.174, 0, 0, 0]) #10°的弧度制

# 定义系统的微分方程
def system(t, x):
    return A @ x

# 模拟系统响应
t_span = (0, 2)  # 模拟 2 秒
t_eval = np.arange(0, 2, 0.001)  # 0.001s 的时间间隔进行采样
sol = solve_ivp(system, t_span, x0, t_eval=t_eval)

# 提取采样点
time_points = sol.t
response_points = sol.y[0, :]  # 假设对第一个状态变量的响应进行采样

# 计算状态导数
derivatives = A @ state_values

# 初始化列表存储结果
results = []

# 遍历每个时间点，计算C向量
for i in range(len(time_points)):
    # 当前状态值
    x_t = state_values[:, i]  # 4维列向量

    # 当前导数值
    dx_t = derivatives[:, i]  # 4维列向量

    # 计算C向量：C = dx_t - A @ x_t
    C = dx_t - A @ x_t

    # 存储第一个、第二个状态变量以及C向量的四个值
    results.append([x_t[0], x_t[1], C[0], C[1], C[2], C[3]])

# 将结果保存到 CSV 文件
output_file = 'system_response_with_C.csv'
with open(output_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['State 1', 'State 2', 'C1', 'C2', 'C3', 'C4'])  # 写入标题行
    writer.writerows(results)

print(f"采样结果已保存到 {output_file}")