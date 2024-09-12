import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

g = 9.81
M = sp.Matrix([[80.81722 , 2.31941332208709],
     [2.31941332208709,0.29784188199686]])
K0 = sp.Matrix([[-80.95,-2.59951685249872],
      [-2.59951685249872,-0.80329488458618]])
K2 = sp.Matrix([[0,76.59734589573222],
      [0,2.65431523794604]])
C1 = sp.Matrix([[0 , 33.86641391492494],
      [-0.85035641456978,1.68540397397560]])

v_list = [] #自变量
re_list =[[],[],[],[]] #特征值实部
im_list = [[],[],[],[]] #特征值虚部

for v in np.arange(0, 10.0, 0.2):
      v_list.append(v) #把v加进自变量列表
      x = sp.Symbol('x')
      Mat = x*x*M + v*C1*x + g*K0 + v*v*K2
      equation = Mat.det()
      solution = sp.solve(equation, x) #solution是方程的解，也就是特征值
      lenth = len(solution)
      for i in range(0,lenth):
            comp_str = str(solution[i])
            comp_str = comp_str.replace(' ', '').replace('I', 'j').replace('*', '')
            solution[i] = complex(comp_str) #把原来的str格式转化为复数
            if isinstance(solution[i], complex):
                  re_list[i].append(solution[i].real) #把第i个值的实部加入relist的第i列
                  im_list[i].append(solution[i].imag)
            elif isinstance(solution[i], float):
                  re_list[i].append(solution[i])
                  im_list[i].append(0)
            else:
                  print("error")

plt.plot(v_list, re_list[0], label='re1', color='yellow', marker='o', markersize=3)
plt.plot(v_list, re_list[1], label='re2', color='green', marker='o', markersize=3)
plt.plot(v_list, re_list[2], label='re3', color='red', marker='o', markersize=3)
plt.plot(v_list, re_list[3], label='re4', color='blue', marker='o', markersize=3)

# 虚部的部分好像不用关心
# plt.plot(v_list, im_list[0], label='im1', color='yellow', marker='x', markersize=3)
# plt.plot(v_list, im_list[1], label='im2', color='green', marker='x', markersize=3)
# plt.plot(v_list, im_list[2], label='im3', color='red', marker='x', markersize=3)
# plt.plot(v_list, im_list[3], label='im4', color='blue', marker='x', markersize=3)

plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
plt.rcParams['axes.unicode_minus'] = False    # 解决负号显示问题

plt.xlim(0, 10)
plt.ylim(-10, 10)

plt.axhline(0, color='black', linewidth=0.5) #添加x轴

plt.title('特征值实部变化图')
plt.xlabel('速度')
plt.ylabel('特征值实部的值')

plt.show()