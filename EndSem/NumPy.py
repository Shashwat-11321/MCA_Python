import numpy as np
# A = np.array([[1, 2], [3, 4]])
# print("Original Matrix:\n", A)
# print("Transpose:\n", A.T)
arr = np.array([1, 2, 3, 4, 5, 6])
print(f"Array Before reshape {arr}")

arr.reshape(2, 3)

print(f"Array after reshape {arr}")
