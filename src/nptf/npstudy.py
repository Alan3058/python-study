import numpy as np
from numpy import linalg

a = np.random.randint(1, 10, (3, 5))
print('ndaaray特性', a)
print('数组维度a.shape=', a.shape)
print('元素类型a.dtype=', a.dtype)
print('元素数量a.size=', a.size)
print('数组轴a.ndim=', a.ndim)

a = np.array([1, 2, 3, 4, 5, 6])
print('数组转矩阵：', a)
print('矩阵形状shape：', a.shape)
a.shape = (2, 3)
print('矩阵变形：', a)

a = np.random.randint(2, 10, (2, 3))
print('整形矩阵随机生成：', a)

a = (np.random.rand(2, 3))
print('浮点矩阵随机生成：', a)

a = np.array(range(1, 7))
a.shape = (2, 3)
b = np.array(range(1, 7))
b.shape = (2, 3)
print('矩阵元素相乘：', a, b, a * b, sep='\n')

b.shape = (3, 2)
print('矩阵乘法：', a, b, np.dot(a, b), sep='\n')

print('矩阵转置：', a, a.transpose(), sep='\n')

a = np.array(range(1, 5))
a.shape = (2, 2)
print('矩阵逆矩阵：', a, linalg.inv(a), sep='\n')

a = np.arange(1, 10).reshape((3, 3)) + 5
print('矩阵与数运算：', a)

a = np.arange(1, 7)
print('resharp不对元数组修改，有返回值', a.reshape((2, 3)))
a.resize(3, 2)
print('resize对元数组修改，无返回值', a)
