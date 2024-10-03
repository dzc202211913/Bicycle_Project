import numpy as np
from scipy.linalg import expm, inv

def sys(A,B):
    # 采样周期
    T = 0.01

    # 计算离散系统矩阵
    A_d = expm(A * T)
    B_d = inv(A) @ (A_d - np.eye(A.shape[0])) @ B

    # 使用 round 函数保留小数点后3位
    A_d = np.round(A_d, 3)
    B_d = np.round(B_d, 3)

    return A_d,B_d