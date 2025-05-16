import matplotlib.pyplot as plt
import numpy as np

def draw_star(n_points=5, inner_radius=0.5, outer_radius=1):
    """
    Draw a star with n_points using polar coordinates.
    inner_radius: radius of inner vertices
    outer_radius: radius of outer vertices
    """

    print(f"Drawing a {n_points}-pointed star...")

    angles = np.linspace(0, 2 * np.pi, num=2 * n_points, endpoint=False)
    radii = np.empty(2 * n_points)

    # Alternate between outer and inner radius
    radii[::2] = outer_radius
    radii[1::2] = inner_radius

    # Convert polar to Cartesian coordinates
    x = radii * np.cos(angles)
    y = radii * np.sin(angles)

    # Close the star shape by repeating the first point
    x = np.append(x, x[0])
    y = np.append(y, y[0])

    # Plotting
    plt.figure(figsize=(6, 6))
    plt.plot(x, y, marker='o', color='blue', linestyle='-', linewidth=2)
    plt.fill(x, y, color='skyblue', alpha=0.5)
    plt.title(f"{n_points}-Pointed Star Graph")
    plt.axis('equal')
    plt.grid(True)
    plt.show()

# Run star shapes 

draw_star(n_points=5)  # 5-point star
