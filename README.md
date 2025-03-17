# Animated Circle Motion with Matplotlib

This Python script creates an animated visualization of two points rotating in circular motion. The first point moves in a large circular path, while the second point rotates around the first at a speed multiplier of pi. The animation uses a black background with neon colors for the points and trails. There are a few different versions but the one that works best is ```draw_circle_pi_dark.py```. Run ```draw_circle.py`` to see how it is drawn using a rational number speed variable and then run ```draw_circle_pi_dark.py``` to see how it draws with irrational pi as the speed variable. 

## Inspiration
This project was inspired by an article from WIRED by Rhett Allain: [Can't Wrap Your Head Around Pi? Here's a Cool Visual to Help](https://www.wired.com/story/cant-wrap-your-head-around-pi-heres-a-cool-visual-to-help/). The visualization demonstrates circular motion in an engaging and intuitive way.

## Features
- Customizable radii to change the shape of the animation.
- Smooth and continuous animation using `matplotlib.animation.FuncAnimation`.
- Aesthetic neon colors on a black background.
- Axis lines and ticks are removed for a cleaner visualization.

## Requirements
Make sure you have Python installed on your Mac. You will also need the following Python packages:

```bash
pip install matplotlib numpy
```

## How to Run on macOS
1. Open the Terminal.
2. Navigate to the folder containing the script:
   ```bash
   cd /path/to/your/script
   ```
3. Run the script using Python:
   ```bash
   python draw_circle_pi_dark.py
   ```

## Customization
### Changing the Shape of the Animation
You can modify the variables `radius_first` and `radius_second` in the function call to adjust the paths of the points.

#### Example 1: Larger Inner Circle, Smaller Outer Rotation
```python
animate_circle(center=(0, 0), radius_first=5, radius_second=2, interval=10, speed_multiplier=3)
```

#### Example 2: Equal Radii
```python
animate_circle(center=(0, 0), radius_first=7, radius_second=7, interval=15, speed_multiplier=2)
```

#### Example 3: Extreme Differences
```python
animate_circle(center=(0, 0), radius_first=10, radius_second=1, interval=5, speed_multiplier=5)
```

Experimenting with different values will change the way the points move and interact.

## Notes
- If the animation is lagging, try increasing the `interval` value to reduce the frame rate.
- The speed of the second point is controlled by `speed_multiplier`, which can be fine-tuned for different effects.

## License
This project is free to use and modify.

