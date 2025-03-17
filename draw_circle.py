import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

def animate_circle(center, radius_first, radius_second, interval=20, speed_multiplier=2):
    """
    Animates two points rotating clockwise around a circle indefinitely.
    The second point rotates around the first point.

    Parameters:
        center (tuple): Coordinates of the circle's center (x, y).
        radius_first (float): Radius of the first point's circular path.
        radius_second (float): Radius of the second point's circular path (relative to the first point).
        interval (int): Time in milliseconds between animation frames.
        speed_multiplier (float): Speed multiplier for the second point.
    """
    # Unpack center coordinates
    cx, cy = center
    
    # Create a figure and axis
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_xlim(cx - (radius_first + radius_second) - 1, cx + (radius_first + radius_second) + 1)
    ax.set_ylim(cy - (radius_first + radius_second) - 1, cy + (radius_first + radius_second) + 1)
    ax.set_aspect('equal')  # Ensure the aspect ratio is equal
    # ax.set_title("Infinite Animation: Red vs Green Dot Plots")
    
    # Initialize points and scatter plots
    point_first, = ax.plot([], [], 'ro', label='Point 1')  # Red dot
    point_second, = ax.plot([], [], 'go', label='Point 2')  # Green dot
    
    scatter_first = ax.scatter([], [], c='#00FFFF', s=10)  # Green dots for first point
    scatter_second = ax.scatter([], [], c='#39FF14', s=10)  # teal dots for second point
    
    # Lists to store discrete dot positions
    dots_x_first = []
    dots_y_first = []
    
    dots_x_second = []
    dots_y_second = []
    
    def init():
        print("Initializing animation...")
        point_first.set_data([], [])
        point_second.set_data([], [])
        scatter_first.set_offsets(np.empty((0, 2)))
        scatter_second.set_offsets(np.empty((0, 2)))
        return point_first, point_second, scatter_first, scatter_second

    def update(frame):
        
        angle_first = -2 * np.pi * frame / 360  # Rotate continuously
        angle_second = speed_multiplier * angle_first
        
        x1 = cx + radius_first * np.cos(angle_first)
        y1 = cy + radius_first * np.sin(angle_first)
        
        x2 = x1 + radius_second * np.cos(angle_second)
        y2 = y1 + radius_second * np.sin(angle_second)
        
        # Update positions of both points
        point_first.set_data([x1], [y1])
        point_second.set_data([x2], [y2])
        
        # Append current positions to dots lists
        dots_x_first.append(x1)
        dots_y_first.append(y1)
        
        dots_x_second.append(x2)
        dots_y_second.append(y2)
        
        # Update scatter plots with new dot positions
        scatter_first.set_offsets(np.c_[dots_x_first, dots_y_first])
        scatter_second.set_offsets(np.c_[dots_x_second, dots_y_second])
        
        return point_first, point_second, scatter_first, scatter_second

    ani = FuncAnimation(fig, update, frames=None,
                        init_func=init,
                        interval=interval,
                        blit=True)

    plt.show()

# Run infinite animation
animate_circle(center=(0, 0), radius_first=3, radius_second=2,
               interval=20, speed_multiplier=3)
