from minimum_bounding_rectangle import minimum_bounding_rectangle as MBR
import random
import numpy as np
import matplotlib.pyplot as plt

def run():
    n = int(input("Enter number of points: ")) 
    if n > 100:
        print("You can't use manual mode with more than 100 points")
        return
    points = np.zeros((n, 2))
    
    for i in range(n):
        x, y = input("Enter x and y coordinates for point {}: ".format(i+1)).split()
        points[i][0] = float(x)
        points[i][1] = float(y)
    print("Points entered:", points)
    plt.scatter(points[:,0], points[:,1])
    bbox = MBR(points=points)
    plt.fill(bbox[:,0], bbox[:,1], alpha=0.2)
    plt.axis('equal')
    plt.show()
    return bbox