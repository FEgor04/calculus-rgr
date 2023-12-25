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
    vertical_color = 'red'

    c_array = np.array([10] + list(range(50, 200, 50)))
    c_array = np.concatenate([-c_array, c_array])

    for c in c_array:
        u_virtual = np.linspace(-10000, 10000, 100_000)
        v_virtual = np.array([c] * len(u_virtual))

        ax_virtual.plot(u_virtual, v_virtual, color=horizontal_color)
        virtual = np.array([ complex(u_virtual[i], v_virtual[i]) for i in range(len(u_virtual)) ])
        physical = w(virtual)

        x_physical = [z.real for z in physical]
        y_physical = [z.imag for z in physical]

        ax_physical.plot(x_physical, y_physical, color=horizontal_color)

    for c in c_array:
        v_virtual = np.linspace(-10000, 10000, 100_000)
        u_virtual = np.array([c] * len(u_virtual))

        ax_virtual.plot(u_virtual, v_virtual, color=vertical_color)
        virtual = np.array([ complex(u_virtual[i], v_virtual[i]) for i in range(len(u_virtual)) ])
        physical = w(virtual)

        x_physical = [z.real for z in physical]
        y_physical = [z.imag for z in physical]

        ax_physical.plot(x_physical, y_physical, color=vertical_color)

    ax_virtual.set_xlim([-200, 200])
    ax_virtual.set_ylim([-200, 200])
    
    if args.save:
        pu.save_fig(fig, args.save)
    else:
        plt.show()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('-s', '--save')

    args = parser.parse_args()
    main(args)
 
