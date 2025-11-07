import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr*2)

list = np.array([1, 2, 3, 4, 5])
print(np.mean(list))
print(sum(list))

arr = np.array([1, 2, 3, 4, 5])
print(arr[1])
print(arr[2:5])
print(arr[0] + arr[4])

arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)

arr = np.array([
    [(1, 2), (3, 4)],
    [(5, 6), (7, 8)],
    [(9, 10), (11, 12)]])
print(arr)

b = np.array([[1, 2, 3, 4, 5]])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([
    [[1, 2, 3], [4, 5, 6]],
    [[1, 2, 3], [4, 5, 6]]
])

print(b.ndim)
print(c.ndim)
print(d.ndim)

arr = np.array([1,2,3,4,5])
print(arr.dtype)

arr = np.array([1,2,3,4,5], dtype="S")
print(arr)
print(arr.dtype)