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

    sampling_rate = 2_500
    
    x_center = -1
    y_center = 0
    dx = 1
    dy = 1
    

    eps = 0.05
    x = np.concatenate([
            np.linspace(x_center - dx, x_center - eps, sampling_rate),
            np.linspace(x_center + eps, x_center + dx, sampling_rate),
            ])
    y = np.concatenate([
            np.linspace(y_center - dy, y_center - eps, sampling_rate),
            np.linspace(y_center+dy, y_center+dy, sampling_rate)
        ])
    xv, yv = np.meshgrid(x, y)

    def f(u, v):
        return 2 / ( (u+1)**2 + v**2 )

    z = f(xv, yv)
    levels = np.arange(0, 400, 20)
    cs = ax.contourf(xv, yv, z, levels=levels)
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
 
