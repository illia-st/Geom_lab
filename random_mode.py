from minimum_bounding_rectangle import minimum_bounding_rectangle as MBR
import random
import numpy as np
import matplotlib.pyplot as plt

def run():
    random_number = random.randint(101, 10**4)
    print("Number of points to generate: " + str(random_number)) 
    points = np.random.rand(random_number, 2)
    plt.scatter(points[:,0], points[:,1])
    bbox = MBR(points=points)
    plt.fill(bbox[:,0], bbox[:,1], alpha=0.2)
    plt.axis('equal')
    plt.show()
    return bbox