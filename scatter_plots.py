import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7]
y = [5,7,4,6,9,3,2]

plt.scatter(x,y, label='scatter plot', s=100, color='g', marker='*')
plt.title('Amazing scatter plot')
plt.xlabel('xLabel')
plt.ylabel('yLabel')
plt.legend()
plt.show()

