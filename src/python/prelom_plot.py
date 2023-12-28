import argparse
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np
import plot_utils as pu
import matplotlib


def main(args):
    pu.figure_setup()

    fig_size = pu.get_fig_size(10, 5)
    fig = plt.figure()

    ax = fig.add_subplot(111)

    sampling_rate = 1000
    
    x_center = -1
    y_center = 0
    dx = 4
    dy = 4
    

    eps = 0.0
    x = np.linspace(x_center - dx, x_center + dx, sampling_rate)
    y = np.linspace(y_center - dy, y_center + dy, sampling_rate)
    xv, yv = np.meshgrid(x, y, sparse=True)

    def f(x, y):
        return 2 / ( (x+1)**2 + y**2 )

    z = f(xv, yv)
    levels = [0, 0.5, 1, 2, 5, 10, 50, 100, 150, 200, 1000, 2000, 4000, 8000]
    cs = ax.contourf(x, y, z, levels=levels, norm="symlog")
    cbar = fig.colorbar(cs)
    cbar.ax.set_ylabel(r"$n(x,y)$")

    ax.set_xlabel(r"$x$")
    ax.set_ylabel(r"$y$")

    ax.set_axisbelow(True)

    ax.grid()
    plt.tight_layout()

    if args.save:
        pu.save_fig(fig, args.save)
    else:
        plt.show()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('-s', '--save')

    args = parser.parse_args()
    main(args)
 
