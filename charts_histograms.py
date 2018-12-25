import matplotlib.pyplot as plt
import random as ran

ages = ran.sample(range(131), 30)
#ages = [115, 94, 2, 54, 17...]
bins = [n for n in range(0, 131, 10)]
#bins = [0, 10, 20...130]

plt.hist(ages, bins, rwidth=0.75, histtype='bar')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Title Graph')
plt.legend()
plt.show()
