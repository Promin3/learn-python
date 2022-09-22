import numpy as np

a = np.array((1, 2, 3, 5, 3, 4))
pos = np.argwhere(a == 3)
print(pos)
a = np.array([[1, 2, 3], [4, 5, 2]])
print(2 in a)
pos = np.argwhere(a == 2)
print(pos)
b = a[a > 2]
print(b)
a[a > 2] = -1
print(a)
