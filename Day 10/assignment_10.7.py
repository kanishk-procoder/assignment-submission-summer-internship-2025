import matplotlib.pyplot as plt
import numpy as np

subjects = ['Math', 'Physics', 'Chemistry', 'English']
sem1_marks = [75, 80, 65, 90]
sem2_marks = [85, 75, 80, 85]

plt.plot(subjects, sem1_marks, label='Semester 1', color='blue')
plt.plot(subjects, sem2_marks, label='Semester 2', color='green')

plt.title("SEMESTER RESULT COMPARISION")
plt.xlabel('Subjects')
plt.ylabel('Marks')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()