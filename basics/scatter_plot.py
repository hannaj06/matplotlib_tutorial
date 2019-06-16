import matplotlib.pyplot as plt
import random


test_scores = [random.randint(45,100) for i in range(100)]
study_minutes =[i * 5 * random.random() for i in test_scores]

plt.scatter(study_minutes, test_scores, marker='x')
plt.xlabel('time studying for exam')
plt.ylabel('test score')
plt.title('Example Scatter Plot - Test Score vs Studying Time')
plt.show()

