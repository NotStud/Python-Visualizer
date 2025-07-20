import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Example: Load your data as a 2D numpy array
# Replace this with your actual data loading method (e.g., from a file)
data = np.array([
    [98.24864462, 98.07632476, 97.86936916, 97.95477711, 100, 78.23988354, 58.4502055, 38.97586246, 19.50547596, 0.009426542, -19.48740421, -38.96007113, -58.43804237, -78.23266369, -100, -97.94300422, -97.8488377, -98.04931893, -98.2176363, -98.30349883],
    [98.55997006, 98.54826163, 98.62836443, 99.00435392, 100, 79.2647139, 59.15551239, 39.35534062, 19.66651091, 0.009130724, -19.64906037, -39.34027032, -59.14425543, -79.25854225, -100, -98.99361333, -98.60871434, -98.52194986, -98.5295477, -98.54774185],
    # ... (all your other rows)
])

# For demonstration, I'm only using 2 rows here.
# You would replace this with your full dataset.

# Create grid coordinates for plotting
ny, nx = data.shape
x = np.linspace(0, nx-1, nx)
y = np.linspace(0, ny-1, ny)
X, Y = np.meshgrid(x, y)

# 3D Surface Plot
fig = plt.figure(figsize=(12, 6))

ax = fig.add_subplot(121, projection='3d')
surf = ax.plot_wireframe(X, Y, data, rstride=1, cstride=1)
ax.set_xlabel('X position')
ax.set_ylabel('Y position')
ax.set_zlabel('Potential V')
ax.set_title('3D Wireframe of Potential V(x,y)')

# 2D Plot of V(x) at middle y (fixed y)
mid_y = ny // 2
ax2 = fig.add_subplot(122)
ax2.plot(x, data[mid_y, :], marker='o')
ax2.set_xlabel('X position')
ax2.set_ylabel('Potential V')
ax2.set_title(f'Potential V(x) at Y = {mid_y}')
ax2.grid(True)

plt.tight_layout()
plt.show()
