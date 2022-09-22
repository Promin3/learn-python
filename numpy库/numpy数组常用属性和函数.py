import numpy as npy

b = npy.array([i for i in range(12)])
a = b.reshape((3, 4))  # 转换为2维数组
print(a)
print(len(a))
print(a.size)
print(a.ndim)  # 数组维度
print(a.shape)
print(a.dtype)
L = a.tolist()
print(L)
b = a.flatten()
print(b)