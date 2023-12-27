import matplotlib.pyplot as plt
import numpy as np
import argparse

def main(args):
    # Setting up the 3D plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Range of values for x, y, z
    x = np.linspace(-1, 1, 400)
    y = np.linspace(-1, 2, 400)
    z = np.linspace(-1, 1, 400)
    X, Z = np.meshgrid(x, z)
    Y, Z = np.meshgrid(y, z)

    # First equation: y + sqrt(x^2 + z^2) = 0 {y >= -1}
    Y1 = -np.sqrt(X**2 + Z**2)
    Y1[Y1 < -1] = np.nan  # Apply the condition y >= -1

    # Second equation: x^2 + z^2 = 1 {-1 <= y <= 1}
    theta = np.linspace(0, 2 * np.pi, 100)
    z = np.linspace(-1, 1, 100)
    theta, z = np.meshgrid(theta, z)
    x = np.cos(theta)
    y = np.sin(theta)

    # Third equation: x^2 + y + z^2 = 2 {y >= 1}
    Y3 = 2 - X**2 - Z**2
    Y3[Y3 < 1] = np.nan  # Apply the condition y >= 1

    # Plotting
    ax.plot_wireframe(X, Y1, Z, color='r')
    ax.plot_surface(x, z, y, color='b', alpha=0.4)
    ax.plot_surface(X, Y3, Z, color='g', alpha=0.8)
    #ax.plot_surface(X, Y3, Z, rstride=1, cstride=1, cmap='viridis', edgecolor='none')

    # Setting labels
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')
    ax.view_init(elev=10, azim=25)

    if args.save:
        plt.savefig(args.save)
    else:
        plt.show()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--save', help='Save the plot to a file')
    args = parser.parse_args()
    main(args)
