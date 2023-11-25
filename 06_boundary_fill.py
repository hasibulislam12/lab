"""Boundary fill algorithm"""
import matplotlib.pyplot as plt
import numpy as np

def boundary_fill(x, y, fill_color, boundary_color):
    global img
    if x < 0 or x >= img.shape[0] or y < 0 or y >= img.shape[1]:
        return
    current_color = img[x][y]
    if current_color != boundary_color and current_color != fill_color:
        img[x][y] = fill_color
        boundary_fill(x + 1, y, fill_color, boundary_color)
        boundary_fill(x - 1, y, fill_color, boundary_color)
        boundary_fill(x, y + 1, fill_color, boundary_color)
        boundary_fill(x, y - 1, fill_color, boundary_color)

def main():
    global img
    img = np.zeros((10, 10))
    img[2:4, 2:4] = 1
    img[2:4, 6:8] = 1
    img[6:8, 2:4] = 1
    img[6:8, 6:8] = 1
    plt.imshow(img, cmap='gray')
    plt.show()
    boundary_fill(5, 5, 2, 1)
    plt.imshow(img, cmap='gray')
    plt.show()

if __name__ == '__main__':
    main()
