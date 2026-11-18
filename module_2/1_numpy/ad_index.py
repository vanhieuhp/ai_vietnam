import time

import numpy as np

a = np.array([1, 2, 3, 4, 5])

print(a[[1, 3, 4]])

print(a[a > 3])

# reshaping: change the shape of an array without changing its data
arr = np.array([[1, 2], [3, 4], [5, 6]])
print(arr.reshape(2, 3))

arr = np.array([[1, 2], [3, 4]])
print(arr.flatten())

a = np.array([[1, 2], [3, 4], [5, 6]])
b = np.array([1, 2])
result = a + b
print(result)

a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])
result = a * b
print(result)


def multiplizeList(size=100000000):
    list1 = list(range(size))
    list2 = list1.copy()

    initialIime = time.time()

    resultantList = [(a * b) for a, b, in zip(list1, list2)]

    print("Time taken by Lists to perform multiplication: ", (time.time() - initialIime, " second"))


def multiplizeNumpy(size=1000):
    list1 = np.array(range(size))
    list2 = list1.copy()

    initialIime = time.time()

    resultantList = list1 * list2

    print("Time taken by Numpy to perform multiplication: ", (time.time() - initialIime, " second"))


# multiplizeList()
# multiplizeNumpy()

numbers = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(numbers.reshape((2,4), order="C"))

print(numbers.reshape((2,4), order="F"))