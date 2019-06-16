import matplotlib.pyplot as plt


x = [1,2,3,4,5]
y = [4,7,4,7,3]

plt.plot(x,y)
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('titles even support \n line breaks')
plt.show()



#legend example
x = [1,2,3,4,5]
y = [4,7,4,7,3]
y2 = [6,7,8,9,2]

plt.plot(x,y, label='line 1')
plt.plot(x,y2, label='line 2')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('titles even support \n line breaks')
plt.legend()
plt.show()






