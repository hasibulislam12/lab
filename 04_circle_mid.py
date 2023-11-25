import numpy as np
import matplotlib.pyplot as plt


h = 0
k = 0
r = 5

# Step 1: set X0, Y0 
x = [0]
y = [r]

# Step 2: Finding discision parameter p = 1 - R
p = 1 - r

# Step 3: finding 1/8 circle potions
while x[-1] < y[-1]:
    x.append(x[-1] + 1)
    if p < 0:
        y.append(y[-1])
        p = p + 2 * x[-1] + 1
    else:
        y.append(y[-1] - 1)
        p = p + 2 * x[-1] - 2 * y[-1] + 1

x = np.array(x)
y = np.array(y)


circle = []
circle.append(np.array([x, y]).T)
circle.append(np.array([y, x]).T)
circle.append(np.array([y, -x]).T)
circle.append(np.array([x, -y]).T)
circle.append(np.array([-x, -y]).T)
circle.append(np.array([-y, -x]).T)
circle.append(np.array([-y, x]).T)
circle.append(np.array([-x, y]).T)
circle = np.array(circle)


circle = circle + np.array([h, k])


plt.figure(figsize=(5,5))
for i in range(8):
    plt.plot(circle[i][:,0], circle[i][:,1])
plt.plot(h,k,'ro')
plt.show()







