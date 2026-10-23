import numpy as np

marks = np.array([
    [70, 80, 90],
    [60, 75, 85],
    [88, 92, 79],
    [55, 65, 70]
])

print("Shape:", marks.shape)
print("Data type:", marks.dtype)
print("Size:", marks.size)

print("First two students, last subject:")
print(marks[:2, -1])

print("Student averages:", marks.mean(axis=1).round(2))
print("Subject averages:", marks.mean(axis=0).round(2))

print("Marks after adding grace marks:")
print(marks + 5)

weights = np.array([0.3, 0.3, 0.4])
weighted_scores = np.dot(marks, weights)
print("Weighted scores:", weighted_scores)

arr = np.arange(12).reshape(3, 4)
print("Reshaped array:")
print(arr)

bonus_arr = np.arange(24).reshape(2, 3, 4)
print("Bonus array shape:", bonus_arr.shape)

for i, slice_arr in enumerate(bonus_arr):
    print(f"Slice {i} shape:", slice_arr.shape)