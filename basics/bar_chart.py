import matplotlib.pyplot as plt

x1 = [2, 4, 6, 8, 10]
x2 = [1, 3, 5, 7, 9]
y1 = [4, 7, 3, 5, 1]
y2 = [5, 3, 2, 6, 2]

plt.bar(x1, y1, label='first series', color='b')
plt.bar(x2, y2, label='second series', color='r')
plt.xlabel('bar number')
plt.ylabel('magnitude')
plt.title('Bar Chart Example')
plt.legend()
plt.show()