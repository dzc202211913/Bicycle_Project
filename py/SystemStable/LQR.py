import numpy as np

# 老是算不对，不知道是不是错了

def gain(A,B,Q,R,S): 
    P = S
    Mat1 = B.T @ P @ B + R
    F1 = np.linalg.inv(Mat1) @ B.T @ P @ A
    P1 = (A - B @ F1).T @ P @ (A - B @ F1) + F1.T @ R @ F1 + Q
    for i in range(10):
        Mat2 = (B.T) @ P1 @ B + R
        F2 = np.linalg.inv(Mat2) @ B.T @ P1 @ A
        Mat3 = F2 - F1
        s = 0
        for element in np.nditer(Mat3):
            s = s + element
        if s <= 0.001:
            break
        P2 = (A - B @ F2).T @ P1 @ (A - B @ F2) + F2.T @ R @ F2 + Q
        F1 = F2
        P1 = P2
    # 使用 round 函数保留小数点后3位
    F2 = np.round(F2, 3)
    return F2