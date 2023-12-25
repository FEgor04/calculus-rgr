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
    ax_virtual.set_aspect('auto')
    ax_physical.set_aspect('auto')

    horizontal_color = 'blue'

    for c in [-150, -100, -50, -25, -10, 10, 25, 50, 100, 150]:
        u_virtual = np.linspace(-10000, 10000, 100_000)
        v_virtual = np.array([c] * len(u_virtual))

        ax_virtual.plot(u_virtual, v_virtual, color=horizontal_color)
        virtual = np.array([ complex(u_virtual[i], v_virtual[i]) for i in range(len(u_virtual)) ])
        physical = w(virtual)

        x_physical = [z.real for z in physical]
        y_physical = [z.imag for z in physical]

        ax_physical.plot(x_physical, y_physical, color=horizontal_color)
    
    if args.save:
        pu.save_fig(fig, args.save)
    else:
        plt.show()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('-s', '--save')

    args = parser.parse_args()
    main(args)
 
