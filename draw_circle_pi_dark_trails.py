import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

def animate_circle(center, radius_first, radius_second, interval=20, speed_multiplier=2, trail_length=50):
    """
    Animates two points rotating clockwise around a circle indefinitely.
    The second point rotates around the first point.
    Includes glow and fading trails.
    """
    cx, cy = center

    # Create figure with black background
    fig, ax = plt.subplots(figsize=(6, 6))
    fig.patch.set_facecolor('black')  
    ax.set_facecolor('black')  

    ax.set_xlim(cx - (radius_first + radius_second) - 1, cx + (radius_first + radius_second) + 1)
    ax.set_ylim(cy - (radius_first + radius_second) - 1, cy + (radius_first + radius_second) + 1)
    ax.set_aspect('equal')  

    # Remove axis lines and labels
    ax.set_xticks([])
    ax.set_yticks([])
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # Initialize points and scatter plots with neon colors
    point_first, = ax.plot([], [], 'o', color='#00FFFF', markersize=8, alpha=0.8)  # Neon teal with glow effect
    point_second, = ax.plot([], [], 'o', color='#39FF14', markersize=8, alpha=0.8)  # Neon green with glow effect

    scatter_first = ax.scatter([], [], c=[], s=20, alpha=0.5, cmap="cool")  
    scatter_second = ax.scatter([], [], c=[], s=20, alpha=0.5, cmap="cool")  

    # Lists to store the points and fading effect
    dots_x_first, dots_y_first, dots_alpha_first = [], [], []
    dots_x_second, dots_y_second, dots_alpha_second = [], [], []

    def init():
        point_first.set_data([], [])
        point_second.set_data([], [])
        scatter_first.set_offsets(np.empty((0, 2)))
        scatter_second.set_offsets(np.empty((0, 2)))
        return point_first, point_second, scatter_first, scatter_second

    def update(frame):
        nonlocal dots_x_first, dots_y_first, dots_alpha_first
        nonlocal dots_x_second, dots_y_second, dots_alpha_second

        angle_first = -2 * np.pi * frame / 360  
        angle_second = speed_multiplier * angle_first

        x1 = cx + radius_first * np.cos(angle_first)
        y1 = cy + radius_first * np.sin(angle_first)

        x2 = x1 + radius_second * np.cos(angle_second)
        y2 = y1 + radius_second * np.sin(angle_second)

        # Update main points
        point_first.set_data([x1], [y1])
        point_second.set_data([x2], [y2])

        # Append new positions with alpha fading
        dots_x_first.append(x1)
        dots_y_first.append(y1)
        dots_alpha_first.append(1.0)  

        dots_x_second.append(x2)
        dots_y_second.append(y2)
        dots_alpha_second.append(1.0)  

        # Keep only the most recent 'trail_length' points
        if len(dots_x_first) > trail_length:
            dots_x_first.pop(0)
            dots_y_first.pop(0)
            dots_alpha_first.pop(0)
        
        if len(dots_x_second) > trail_length:
            dots_x_second.pop(0)
            dots_y_second.pop(0)
            dots_alpha_second.pop(0)

        # Reduce alpha of older points for fading effect
        dots_alpha_first = [max(a - 0.02, 0) for a in dots_alpha_first]
        dots_alpha_second = [max(a - 0.02, 0) for a in dots_alpha_second]

        # Update scatter plots with fading trails
        scatter_first.set_offsets(np.c_[dots_x_first, dots_y_first])
        scatter_first.set_color([(0, 1, 1, a) for a in dots_alpha_first])  # Neon teal fading
        
        scatter_second.set_offsets(np.c_[dots_x_second, dots_y_second])
        scatter_second.set_color([(0.22, 1, 0.08, a) for a in dots_alpha_second])  # Neon green fading

        return point_first, point_second, scatter_first, scatter_second

    ani = FuncAnimation(fig, update, frames=None, init_func=init, interval=interval, blit=True)

    plt.show()

# Run animation
animate_circle(center=(0, 0), radius_first=3, radius_second=2, interval=20, speed_multiplier=3, trail_length=50)
