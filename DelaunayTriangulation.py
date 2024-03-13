import numpy as np
num_points=20
points = np.random.rand(num_points,2)
from scipy.spatial import Delaunay
tri = Delaunay(points)
import matplotlib.pyplot as plt
plt.triplot(points[:,0], points[:,1], tri.simplices)
plt.plot(points[:,0], points[:,1], 'o')
plt.show()