import numpy as np
import matplotlib.pyplot as plt

def translation_translate(polygon, translate_x, translate_y):
	homogeneous_polygon = np.column_stack((polygon, np.ones(len(polygon))))
	translate_matrix = np.array([
			[1, 0, translate_x],
			[0, 1, translate_y],
			[0, 0, 1]
		])

	translated_polygon_homogeneous = np.dot(translate_matrix, homogeneous_polygon.T).T
	return translated_polygon_homogeneous[:, :2]

def translation_scaling(polygon, scale_x, scale_y):
	# Scaling matrix
	scaling_matrix = np.array([
	    [scale_x, 0],
	    [0, scale_y]
	])
	return np.dot(polygon, scaling_matrix.T)

def translation_reflection(polygon, x_axis=True, y_axis=True):
	x_axis = -1 if x_axis else 1
	y_axis = -1 if y_axis else 1
	# Scaling matrix
	scaling_matrix = np.array([
	    [x_axis, 0],
	    [0, y_axis]
	])
	return np.dot(polygon, scaling_matrix.T)

def translation_shearing(polygon, shear_x, shear_y):
	shear_matrix = np.array([
	    [1, shear_x],
	    [shear_y, 1]
	])

	return np.dot(polygon, shear_matrix.T) 

def translation_roation(polygon, angle_degrees):
	# Convert angle to radians
	angle_radians = np.radians(angle_degrees)

	# Rotation matrix
	rotation_matrix = np.array([
	    [np.cos(angle_radians), -np.sin(angle_radians)],
	    [np.sin(angle_radians), np.cos(angle_radians)]
	])
	return np.dot(polygon, rotation_matrix.T)




plt.figure(figsize=(9,6))

# Define the polygon (example: square)
polygon = np.array([(0, 0), (1, 0), (1, 1), (0, 1)])

plt.subplot(2,3,1)
plt.plot(polygon[:,0], polygon[:,1], c='black')
plt.plot(polygon[[0,-1]][0], polygon[[0,-1]][1], c='black')
plt.title('Original')


"""_______________________Translate_____________________________"""
translate_x = 3
translate_y = 3
translate_polygon = translation_translate(polygon, translate_x, translate_y)

plt.subplot(2,3,2)
plt.plot(translate_polygon[:,0], translate_polygon[:,1], c='red')
plt.plot(translate_polygon[[0,-1],0], translate_polygon[[0,-1],1], c='red')
plt.title('translate_polygon')
plt.xlim(min(np.min(polygon[:, 0]), np.min(translate_polygon[:, 0])) - 1,
         max(np.max(polygon[:, 0]), np.max(translate_polygon[:, 0])) + 1)
plt.ylim(min(np.min(polygon[:, 1]), np.min(translate_polygon[:, 1])) - 1,
         max(np.max(polygon[:, 1]), np.max(translate_polygon[:, 1])) + 1)

# Add labels and legend
plt.legend()



"""_______________________Scaling_____________________________"""
scale_x = 2
scale_y = 3
scaled_polygon = translation_scaling(polygon, scale_x, scale_y)
# Plot the original and scaled polygons
plt.subplot(2,3,3)
plt.plot(scaled_polygon[:,0], scaled_polygon[:,1], c='red')
plt.plot(scaled_polygon[[0,-1],0], scaled_polygon[[0,-1],1], c='red')

# Set plot limits
plt.xlim(min(np.min(polygon[:, 0]), np.min(scaled_polygon[:, 0])) - 1,
         max(np.max(polygon[:, 0]), np.max(scaled_polygon[:, 0])) + 1)
plt.ylim(min(np.min(polygon[:, 1]), np.min(scaled_polygon[:, 1])) - 1,
         max(np.max(polygon[:, 1]), np.max(scaled_polygon[:, 1])) + 1)

# Add labels and legend
plt.title('Scaled_polygon')
plt.legend()


"""_______________________reflect_____________________________"""
x_axis = True
y_axis = True
reflection_polygon = translation_reflection(polygon, x_axis=True, y_axis=True)
# Plot the original and scaled polygons
plt.subplot(2,3,4)
plt.plot(reflection_polygon[:,0], reflection_polygon[:,1], c='red')
plt.plot(reflection_polygon[[0,-1],0], reflection_polygon[[0,-1],1], c='red')

# Set plot limits
plt.xlim(min(np.min(polygon[:, 0]), np.min(reflection_polygon[:, 0])) - 1,
         max(np.max(polygon[:, 0]), np.max(reflection_polygon[:, 0])) + 1)
plt.ylim(min(np.min(polygon[:, 1]), np.min(reflection_polygon[:, 1])) - 1,
         max(np.max(polygon[:, 1]), np.max(reflection_polygon[:, 1])) + 1)

# Add labels and legend
plt.title('reflection_polygon_polygon')
plt.legend()



"""_______________________Shearing_____________________________"""
shear_x = 0.5  # Horizontal shear
shear_y = 0.2  # Vertical shear
shearing_polygon = translation_shearing(polygon, shear_x, shear_y)
# Plot the original and scaled polygons
plt.subplot(2,3,5)
plt.plot(shearing_polygon[:,0], shearing_polygon[:,1], c='red')
plt.plot(shearing_polygon[[0,-1],0], shearing_polygon[[0,-1],1], c='red')

# Set plot limits
plt.xlim(min(np.min(polygon[:, 0]), np.min(shearing_polygon[:, 0])) - 1,
         max(np.max(polygon[:, 0]), np.max(shearing_polygon[:, 0])) + 1)
plt.ylim(min(np.min(polygon[:, 1]), np.min(shearing_polygon[:, 1])) - 1,
         max(np.max(polygon[:, 1]), np.max(shearing_polygon[:, 1])) + 1)

# Add labels and legend
plt.title('shearing_polygon_polygon')
plt.legend()


"""_______________________rotation_____________________________"""
angle_degrees = 45
rotation_polygon = translation_roation(polygon, angle_degrees)
# Plot the original and scaled polygons
plt.subplot(2,3,6)
plt.plot(rotation_polygon[:,0], rotation_polygon[:,1], c='red')
plt.plot(rotation_polygon[[0,-1],0], rotation_polygon[[0,-1],1], c='red')

# Set plot limits
plt.xlim(min(np.min(polygon[:, 0]), np.min(rotation_polygon[:, 0])) - 1,
         max(np.max(polygon[:, 0]), np.max(rotation_polygon[:, 0])) + 1)
plt.ylim(min(np.min(polygon[:, 1]), np.min(rotation_polygon[:, 1])) - 1,
         max(np.max(polygon[:, 1]), np.max(rotation_polygon[:, 1])) + 1)

# Add labels and legend
plt.title('rotation_polygon_polygon')
plt.legend()





plt.show()














