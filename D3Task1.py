
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


# 2. Slicing
print("\nFirst two students:")
print(marks[:2])

print("\nLast subject of first two students:")
print(marks[:2, -1])


# 3. Calculate averages
student_avg = np.mean(marks, axis=1)
subject_avg = np.mean(marks, axis=0)

print("\nStudent averages:", np.round(student_avg, 2))
print("Subject averages:", subject_avg)


# 4. Broadcasting - Add 5 grace marks
grace_marks = marks + 5

print("\nMarks after adding 5 grace marks:")
print(grace_marks)


# 5. Weighted scores using np.dot()
weights = np.array([0.3, 0.3, 0.4])

weighted_scores = np.dot(marks, weights)

print("\nWeighted scores:", weighted_scores)


# 6. Reshape np.arange(12) into 3x4
numbers = np.arange(12)
reshaped = numbers.reshape(3, 4)

print("\nReshaped array (3x4):")
print(reshaped)
