import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Create the figure and 3D axes
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Define the data for the 3D plot
t = np.linspace(0, 2*np.pi, 100)
x = np.cos(t)
y = np.sin(t)
z = t

# Initialize the 3D plot with empty lines
line, = ax.plot([], [], [])

# Function to update the 3D plot
def update(frame):
    # Update the data for the line
    line.set_data(x[:frame], y[:frame])
    line.set_3d_properties(z[:frame])
    return line,

# Create the animation
animation = FuncAnimation(fig, update, frames=len(t), interval=100, blit=True)

# Set the axis labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Animated 3D Plot')

# Set the limits of the plot
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_zlim(0, 2*np.pi)

# Save the animation as an MP4 video file
animation.save('animation.mp4', writer='ffmpeg')

# Display the plot
plt.show()
