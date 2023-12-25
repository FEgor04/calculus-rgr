import argparse
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np
import plot_utils as pu
import matplotlib
import conformal_utils as cu
from conformal_utils import w


def main(args):
    fig, (ax_virtual, ax_physical) = cu.setup()

    x_virtual = np.linspace(-100, 100, 100_000)
    y_virtual = [x for x in x_virtual]

    ax_virtual.plot(x_virtual, y_virtual)

    virtual_numbers = [complex(x_virtual[i], y_virtual[i]) for i in range(len(x_virtual))]
    physical_numbers = [w(z) for z in virtual_numbers]

    x_physical = [z.real for z in physical_numbers]
    y_physical = [z.imag for z in physical_numbers]

    ax_physical.plot(x_physical, y_physical)

    ax_virtual.grid()
    ax_physical.grid()

    if args.save:
        pu.save_fig(fig, args.save)
    else:
        plt.show()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('-s', '--save')

    args = parser.parse_args()
    main(args)
 
