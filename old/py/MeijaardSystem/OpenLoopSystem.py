import numpy as np
import control  as ctrl
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

B = np.linalg.inv(Mat1)

C = np.array([[1,0,0,0],[0,1,0,0]])

sys = ctrl.StateSpace(A, B, C, np.zeros((2,4)))

# 先不考虑反馈的事，先观察开环系统的情况


# # 计算系统矩阵 A 的特征值
# eigenvalues = np.linalg.eigvals(A)

# # 打印特征值
# print("系统矩阵 A 的特征值:")
# print(eigenvalues)

# # 检查特征值的实部是否都为负
# is_stable = np.all(np.real(eigenvalues) < 0)
# if is_stable:
#     print("系统是渐近稳定的。")
# else:
#     print("系统是不稳定的。")

# 定义初始状态
x0 = np.array([0, 0, 0, 0])

# 定义时间向量
t = np.linspace(0, 5, 100)

# 计算系统的初始响应
t, y, x = ctrl.initial_response(sys, T=t, X0=x0, return_x=True)

# 绘制每个状态变量的响应
plt.figure()
plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
plt.rcParams['axes.unicode_minus'] = False    # 解决负号显示问题
for i in range(x.shape[0]):
    plt.plot(t, x[i, :], label=f'x{i+1}')
plt.xlabel('时间 (s)')
plt.ylabel('状态变量')
plt.title('v=5时,状态变量的初始响应')
plt.legend()
plt.grid(True)
plt.xlim(0, 5)  # 设置x轴范围
plt.ylim(-90, 90)  # 设置y轴范围
plt.show()