import numpy as np

array = np.array([[1,2,3],
                  [4,5,6],
                  [7,8,9]])

print(array > 2)
print(array < 5)

filtered_elements = array[(array > 2) & (array < 5)]
print(filtered_elements)

