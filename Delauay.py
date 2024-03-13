import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

def in_circle(a, b, c, point):
    """
    Check if point is inside the circumcircle of triangle abc.
    """
    d = 2 * (a[0] * (b[1] - c[1]) + b[0] * (c[1] - a[1]) + c[0] * (a[1] - b[1]))
    ux = ((a[0]**2 + a[1]**2) * (b[1] - c[1]) + (b[0]**2 + b[1]**2) * (c[1] - a[1]) + (c[0]**2 + c[1]**2) * (a[1] - b[1])) / d
    uy = ((a[0]**2 + a[1]**2) * (c[0] - b[0]) + (b[0]**2 + b[1]**2) * (a[0] - c[0]) + (c[0]**2 + c[1]**2) * (b[0] - a[0])) / d
    r = np.sqrt((a[0] - ux)**2 + (a[1] - uy)**2)
    distance = np.sqrt((point[0] - ux)**2 + (point[1] - uy)**2)
    return distance < r

def bowyer_watson(points):
    """
    Bowyer-Watson algorithm for Delaunay triangulation.
    """
    # Create a bounding super-triangle
    super_triangle = np.array([[-1, -1], [4, -1], [2, 4]])
    
    triangles = [super_triangle]
    
    for point in points:
        bad_triangles = []
        for triangle in triangles:
            if triangle.shape[0] == 3 and in_circle(triangle[0], triangle[1], triangle[2], point):
                bad_triangles.append(triangle)
        
        polygon = []
        for triangle in bad_triangles:
            for edge in triangle:
                if not any(np.array_equal(edge, e) for e in polygon):
                    polygon.append(edge)
        
        triangles = [t for t in triangles if t not in bad_triangles]
        
        for edge in polygon:
            triangles.append(np.array([edge, point]))
    
    # Remove triangles that include super-triangle vertices
    triangles = [t for t in triangles if not any(np.array_equal(vertex, super_triangle[0]) or
                                                  np.array_equal(vertex, super_triangle[1]) or
                                                  np.array_equal(vertex, super_triangle[2]) for vertex in t)]
    
    return triangles

def plot_triangulation(points, triangles):
    # Plotting points after triangulation
    plt.subplot(1, 2, 2 )
    plt.triplot(points[:, 0], points[:, 1], triangles)
    plt.plot(points[:, 0], points[:, 1], 'o', color='red')
    plt.title(' Delaunay Triangulation')

    plt.tight_layout()
    plt.show()

# Generate random points
np.random.seed(20)
points = np.random.rand(10, 2)

# Perform Delaunay triangulation using Bowyer-Watson algorithm
triangles = bowyer_watson(points)

# Plot the triangulation
plot_triangulation(points, triangles)
