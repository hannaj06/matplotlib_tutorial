import matplotlib.pyplot as plt
import random
import numpy as np 

year = range(10)


server_costs = np.linspace(0, 10, 10)
software_costs = np.linspace(10, 25, 10)
rent_costs = [12, 12, 12, 24, 24, 24, 24, 36, 36, 36]

#legend hack
plt.plot([], [], color='r', label='server costs')
plt.plot([], [], color='c', label='software costs')
plt.plot([], [], color='b', label='rent costs')

plt.xlabel('year')
plt.ylabel('cost')
plt.stackplot(year, server_costs, software_costs, rent_costs, colors=['r', 'c', 'b'])
plt.legend()
plt.show()