import numpy as np

data = np.array([6, 7, 1, 9, 2])
print(data)

n = 5
list_zeros = [0] * n
print("list zeros:", list_zeros)

zeros_array_id = np.zeros(n)
print("zeros array id:", zeros_array_id)

l_data = [4, 5, 6, 7, 8, 9]

data = [6, 5]
print("data", data * 3)

n_data = np.array([6, 5])
print("n_data", n_data * 3)

n_data = np.array([1, 4, 2, 7, 4, 3, 1, 1, 2])
n_data.sort()
print("n_data", n_data[::-1])
deleted_index = np.where(n_data == 4)
print("deleted_index", deleted_index)
deleted_index = np.where(n_data == 4)[0][0]
n_data = np.delete(n_data, deleted_index)
print("n_data", n_data)

# zip
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])

zipped_arr = np.dstack((arr1, arr2))[0]
print("zipped_arr", zipped_arr)
for i in range(len(arr1)):
    print(zipped_arr[i])

for index, value in np.ndenumerate(arr1):
    print(index, value)

data = [5, 6, 7, 1, 9]

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
even_numbers = arr[arr % 2 == 0]
print(arr %2 == 0)
print(even_numbers)
sum_even_numbers = np.sum(even_numbers)
print("sum_even_numbers", sum_even_numbers)
