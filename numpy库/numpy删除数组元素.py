import numpy as np

a = np.array((1, 2, 3, 4))
b = np.delete(a, 1)
print(b)
b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(np.delete(b, 1, axis=0))
print(np.delete(b, [1, 2], axis=0))  # 删除b行列式的第一和第二行
print(np.delete(b, [0, 2], axis=1))
