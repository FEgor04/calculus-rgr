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
    eps = 1e-9
    max_x = 10

    def compute_potential_line_y(x, c):
        return np.log(np.exp(x) - c)
    def compute_vector_line_y(x, c):
        return -np.log(c - np.exp(-x))

    c_range = [np.exp(i) for i in range(1, 10)]
    for C in c_range:
        x = np.linspace(- np.log(C) + eps, max_x, 10000)
        y_vector = compute_vector_line_y(x, C)
        ax.plot(x, y_vector, c='b', lw=pu.plot_lw())
        x_potential = np.linspace(np.log(C), max_x, 10000)
        y_potential = compute_potential_line_y(x_potential, C)
        ax.plot(x_potential, y_potential, c='r', lw=pu.plot_lw())

    ax.set_xlabel('$x$')
    ax.set_ylabel('$y$')

    # plt.ylim([-15, 15])
    # plt.xlim([-6, 6])

    ax.set_axisbelow(True)

    plt.grid()
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
 
