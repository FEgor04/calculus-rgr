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
    r = np.sqrt(2) * 2
    sampling_rate = 100_000
    u_virtual_1 = np.linspace(-r, r, sampling_rate)
    v_virtual_1 = np.sqrt(r**2 - u_virtual_1 ** 2)
    u_virtual_2 = np.array(u_virtual_1[::-1])
    v_virtual_2 = -np.sqrt(r**2 - u_virtual_2 ** 2)
    u_virtual = np.concatenate([u_virtual_1, u_virtual_2])
    v_virtual = np.concatenate([v_virtual_1, v_virtual_2])
    virtual_numbers = np.array([complex(u_virtual[i], v_virtual[i]) for i in range(len(u_virtual))])

    def plot_complex(ax, numbers, color):
        x = [z.real for z in numbers]
        y = [z.imag for z in numbers]

        ax.plot(x, y, color=color)

    plot_complex(ax_virtual, virtual_numbers, 'orange')
    plot_complex(ax_physical, w(virtual_numbers), 'orange')
    
    if args.save:
        pu.save_fig(fig, args.save)
    else:
        plt.show()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('-s', '--save')

    args = parser.parse_args()
    main(args)
 
