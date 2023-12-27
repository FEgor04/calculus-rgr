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

    c_array = [0, 0.5, 1, 2, 10, 20, 50]
    horizontal_colors = plt.get_cmap("viridis")
    vertical_colors =   plt.get_cmap("viridis")

    sampling_rate = 500_000

    def plot_complex(ax, numbers, color):
        x = [z.real for z in numbers]
        y = [z.imag for z in numbers]

        ax.plot(x, y, color=color)

    def draw_horizontal_line(c, color):
        u_virtual = np.linspace(-10000, 10000, sampling_rate)
        v_virtual = np.array([c] * len(u_virtual))
        virtual = np.array([ complex(u_virtual[i], v_virtual[i]) for i in range(len(u_virtual)) ])

        plot_complex(ax_virtual, virtual, color)
        plot_complex(ax_physical, w(virtual), color)

    def draw_vertical_line(c, color):
        v_virtual = np.linspace(-10000, 10000, sampling_rate)
        u_virtual = np.array([c] * len(v_virtual))
        virtual = np.array([ complex(u_virtual[i], v_virtual[i]) for i in range(len(u_virtual)) ])

        plot_complex(ax_virtual, virtual, color)
        plot_complex(ax_physical, w(virtual), color)



    for i in range(len(c_array)):
        c = c_array[i]
        c_vertical = vertical_colors(i / len(c_array))
        c_horizontal = horizontal_colors(i / len(c_array))
        draw_horizontal_line(c, color=c_horizontal)
        draw_vertical_line(c, color=c_vertical)
        if c > 0:
            draw_horizontal_line(-c, color=c_horizontal)
            draw_vertical_line(-c, color=c_vertical)
        
    ax_virtual.set_xlim([-15, 15])
    ax_virtual.set_ylim([-15, 15])

    ax_physical.set_xlim([-5, 5])
    ax_physical.set_ylim([-5, 5])
    
    if args.save:
        pu.save_fig(fig, args.save)
    else:
        plt.show()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('-s', '--save')

    args = parser.parse_args()
    main(args)
 
