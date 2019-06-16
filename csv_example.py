import matplotlib.pyplot as plt
import csv
import numpy as np

x = []
y = []


## csv module
with open('example.csv', 'r') as csvfile:
	plots = csv.reader(csvfile, delimiter=',')
	for row in plots:
		x.append(int(row[0]))
		y.append(int(row[1]))

plt.plot(x, y, label='Load from file')
plt.show()


## numpy module
x, y = np.loadtxt('example.csv', delimiter=',', unpack=True)
plt.plot(x, y, label='Load from file')
plt.show()
