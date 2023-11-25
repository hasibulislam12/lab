import matplotlib.pyplot as plt
import numpy as np

points = np.array([[0,0], [4,6]])

del_x = points[-1][0] - points[0][0]
del_y = points[-1][1] - points[0][1]

m = del_y / del_x

if abs(m) >=1:
	del_y = m/abs(m)
	del_x = del_y/m
else:
	del_x = m/abs(m)
	del_y = m * del_x

resulted_points = [points[0]]

while True:
	x = resulted_points[-1][0] + del_x
	y = resulted_points[-1][1] + del_y
	if abs(x) > abs(points[-1][0]) or abs(y) > abs(points[-1][1]):
		break
	resulted_points.append([x, y])

resulted_points = np.array(resulted_points)
resulted_points = np.round(resulted_points)
resulted_points = resulted_points.astype(np.int32)
plt.plot(resulted_points[:,0], resulted_points[:,1])
plt.show()