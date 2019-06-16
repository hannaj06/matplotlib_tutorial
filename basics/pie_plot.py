import matplotlib.pyplot as plt


labels = ['eggs', 'chicken', 'chips', 'veggies']
diet = [80, 60, 50, 15]

plt.pie(diet, labels=labels, autopct='%1.1f%%')
plt.axis('equal')
plt.show()