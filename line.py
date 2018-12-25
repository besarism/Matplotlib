import matplotlib.pyplot as plt

x = [1,2,3]
y = [5,7,4]
x2 = [1,2,3]
y2 = [10,12,8]

plt.plot(x,y, label='First Line')
plt.plot(x2,y2, label='Second Line')
plt.title('Interesting Graph')
plt.xlabel('xLabel')
plt.ylabel('yLabel')
plt.legend()
plt.show()
