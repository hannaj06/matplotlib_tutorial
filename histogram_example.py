import matplotlib.pyplot as plt
import random


random_nums = [random.randint(45,100) for i in range(100)]
bins = [40, 50, 60, 70, 80, 90, 100]

plt.hist(random_nums, bins, histtype='bar', rwidth=0.8)
plt.title('Histogram Example')
plt.show()



plt.hist(random_nums, bins, histtype='bar', cumulative=True, rwidth=0.8)
plt.title('Histogram Example')
plt.show()