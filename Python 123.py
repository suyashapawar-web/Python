import numpy as np
data1 = [('name', 'S15'), ('class', int), ('height', float)]
studentsd = [('James', 5, 48.5), ('Nail', 6, 52.5), ('Paul', 5, 42.10), ('Pit', 5, 40.11)]
# create a structured array
students = np.array(studentsd, dtype=data1)
print("Original array:")
print(students)
print("Sort by height:")
print(np.sort(students, order='height'))