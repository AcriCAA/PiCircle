import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

def animate_circle(center, radius_first, radius_second, interval=20, speed_multiplier=2):
    """
    Animates two points rotating clockwise around a circle indefinitely.
    The second point rotates around the first point.
    """
    cx, cy = center

    # Create a figure and axis with black background
    fig, ax = plt.subplots(figsize=(6, 6))
    fig.patch.set_facecolor('black')  # Set figure background color
    ax.set_facecolor('black')  # Set axis background color

    ax.set_xlim(cx - (radius_first + radius_second) - 1, cx + (radius_first + radius_second) + 1)
    ax.set_ylim(cy - (radius_first + radius_second) - 1, cy + (radius_first + radius_second) + 1)
    ax.set_aspect('equal')  # Ensure the aspect ratio is equal

    # Remove axis lines and ticks
    ax.set_xticks([])
    ax.set_yticks([])
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # Initialize points and scatter plots with neon colors
    # point_first, = ax.plot([], [], 'o', color='#00FFFF', markersize=6, label='Point 1')  # Neon teal
    #E50000
    point_first, = ax.plot([], [], 'o', color='#E50000', markersize=6, label='Point 1')  # Neon teal
    point_second, = ax.plot([], [], 'o', color='#39FF14', markersize=6, label='Point 2')  # Neon green

    # scatter_first = ax.scatter([], [], c='#00FFFF', s=10)  # Neon teal trail
    scatter_first = ax.scatter([], [], c='#E50000', s=10)  # Neon teal trail
    scatter_second = ax.scatter([], [], c='#39FF14', s=10)  # Neon green trail

    dots_x_first, dots_y_first = [], []
    dots_x_second, dots_y_second = [], []

    def init():
        point_first.set_data([], [])
        point_second.set_data([], [])
        scatter_first.set_offsets(np.empty((0, 2)))
        scatter_second.set_offsets(np.empty((0, 2)))
        return point_first, point_second, scatter_first, scatter_second

    def update(frame):
        angle_first = -2 * np.pi * frame / 360  
        angle_second = speed_multiplier * angle_first

        x1 = cx + radius_first * np.cos(angle_first)
        y1 = cy + radius_first * np.sin(angle_first)

        x2 = x1 + radius_second * np.cos(angle_second)
        y2 = y1 + radius_second * np.sin(angle_second)

        point_first.set_data([x1], [y1])
        point_second.set_data([x2], [y2])

        dots_x_first.append(x1)
        dots_y_first.append(y1)
        dots_x_second.append(x2)
        dots_y_second.append(y2)

        scatter_first.set_offsets(np.c_[dots_x_first, dots_y_first])
        scatter_second.set_offsets(np.c_[dots_x_second, dots_y_second])

        return point_first, point_second, scatter_first, scatter_second

    ani = FuncAnimation(fig, update, frames=None, init_func=init, interval=interval, blit=True)

    plt.show()

# Run animation
animate_circle(center=(0, 0), radius_first=9, radius_second=10, interval=10, speed_multiplier=np.pi)
