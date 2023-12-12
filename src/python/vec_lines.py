import argparse
import matplotlib.pyplot as plt
import numpy as np
import plot_utils as pu


def main(args):
    pu.figure_setup()

    fig_size = pu.get_fig_size(10, 5)
    fig = plt.figure()
    ax = fig.add_subplot(111)

    for C in [0.1, 0.5, 1.0, 2.0, 4.0, 8.0, 16.0, 32.0, 64.0]:
        x = np.linspace(- np.log(C), 10, 100000)
        y = np.log(C - np.exp(- x))
        ax.plot(x, y, c='b', lw=pu.plot_lw())

    ax.set_xlabel('$x$')
    ax.set_ylabel('$y$')

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
