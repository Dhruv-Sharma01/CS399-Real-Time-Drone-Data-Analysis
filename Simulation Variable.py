import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Circle

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_aspect('equal')

# Parameters
num_points = 10
points = np.random.uniform(-8, 8, (num_points, 2))
speeds = np.random.uniform(0.05, 0.2, num_points)
angles = np.random.uniform(0, 2 * np.pi, num_points)
radii = np.random.uniform(0.5, 1.5, num_points)
max_radius_variation = 0.3  # Max variation in radius size

# Initial colors (all red)
colors = [(1, 0, 0, 1)] * num_points  # RGBA for red

# Scatter plot and circles
point_scatter = ax.scatter(points[:, 0], points[:, 1], color=colors)
circles = [Circle((x, y), radius=r, color=(1, 0.5, 0.5), fill=False, lw=1.5) for (x, y), r in zip(points, radii)]
for circle in circles:
    ax.add_patch(circle)

# Update function for animation
def update(frame):
    global points, angles, colors, radii
    # Move points randomly based on their speeds and angles
    points[:, 0] += speeds * np.cos(angles)
    points[:, 1] += speeds * np.sin(angles)

    # Update point and circle positions
    point_scatter.set_offsets(points)
    for i, circle in enumerate(circles):
        # Vary the radius within a range
        radii[i] = np.clip(radii[i] + np.random.uniform(-max_radius_variation, max_radius_variation), 0.5, 2.0)
        circle.set_radius(radii[i])
        circle.set_center(points[i])

    # Reset all colors to red
    colors = [(1, 0, 0, 1)] * num_points  # RGBA for red
    for circle in circles:
        circle.set_edgecolor((1, 0.5, 0.5))  # Light red

    # Check for intersections
    for i in range(num_points):
        for j in range(i + 1, num_points):
            dist = np.linalg.norm(points[i] - points[j])
            if dist < radii[i] + radii[j]:  # Check if circles intersect
                colors[i] = (0, 0, 1, 1)  # Blue
                colors[j] = (0, 0, 1, 1)  # Blue
                circles[i].set_edgecolor('blue')
                circles[j].set_edgecolor('blue')

    # Update colors in scatter plot
    point_scatter.set_facecolors(colors)

    # Boundary conditions to keep points within view
    for i in range(num_points):
        if points[i, 0] < -10 or points[i, 0] > 10:
            angles[i] = np.pi - angles[i]
        if points[i, 1] < -10 or points[i, 1] > 10:
            angles[i] = -angles[i]

# Create animation
ani = FuncAnimation(fig, update, frames=200, interval=50)
plt.show()
