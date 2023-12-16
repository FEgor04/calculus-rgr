import argparse
import matplotlib.pyplot as plt
import numpy as np
import plot_utils as pu


def main(args):
    pu.figure_setup()

    fig_size = pu.get_fig_size(10, 5)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    eps = 1e-9
    max_x = 6

    total_x = []
    total_y = []

    def compute_y(x, C):
        return - np.log(C - np.exp(-x))


    c_range = [np.exp(i) for i in range(1, 20)]
    for C in c_range:
        x = np.linspace(- np.log(C) + eps, max_x, 1000)
        y = compute_y(x, C)
        ax.plot(x, y, c='b', lw=pu.plot_lw())

        X = np.linspace(- np.log(C) + eps, max_x, 20)
        total_x += list(X)
        total_y += list(compute_y(X, C))
        

    total_x = np.array(total_x)
    total_y = np.array(total_y)

    U = np.exp(total_x)
    V = - np.exp(total_y)
    # N = np.sqrt(np.square(U) + np.square(V))
    N = 1

    q = ax.quiver(total_x, total_y, U/N, V/N, angles='xy', scale_units='xy')
    # ax.quiverkey(q, X=0.3, Y=1.1, U=10, label=r"$\vec H$", labelpos='E')

    ax.set_xlabel('$x$')
    ax.set_ylabel('$y$')

    # plt.ylim([-15, 15])
    # plt.xlim([-6, 6])

    ax.set_axisbelow(True)

    plt.grid()
    plt.tight_layout()

    plt.legend()

    if args.save:
        pu.save_fig(fig, args.save)
    else:
        plt.show()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('-s', '--save')

    args = parser.parse_args()
    main(args)
