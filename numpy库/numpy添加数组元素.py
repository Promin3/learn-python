import numpy as np

a = np.array((1, 2, 3))
b = np.append(a, 10)
print(b)
print(np.append(a, [10, 20]))
print(np.append(a, (4, 6)))
c = np.zeros((2, 3), dtype=int)
print(np.append(a, c))
print(np.concatenate((a, [10, 20], a)))
print(np.concatenate((c, np.array([10, 20, 30, 40, 50, 60]).reshape(2, 3))))
print(np.concatenate((c, np.array([[1, 2, 3], [4, 5, 6]]))))
print(np.concatenate((c, np.array([[1, 2, 3]]))))

