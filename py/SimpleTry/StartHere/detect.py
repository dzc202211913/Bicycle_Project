import numpy as np

def detect(xP,yP,xN,yN,t):
    vN = np.sqrt((yN-yP)**2 + (xN-xP)**2)/(t)
    # 给定点A和B的坐标
    A = np.array([xP, yP])
    B = np.array([xN, yN])
     # 计算向量AB
    vector_AB = B - A
    # 计算向量的长度（范数）
    length = np.linalg.norm(vector_AB)
    # 单位化向量
    vHN = vector_AB / length

    return vN, vHN