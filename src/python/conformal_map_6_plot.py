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

    # ax_virtual.set_title(r"\text{Виртуальное пространство}")
    # ax_physical.set_title(r"\text{Физическое пространство}")

    ax_virtual.set_xlabel(r"$U$")
    ax_virtual.set_ylabel(r"$V$")

    ax_physical.set_xlabel(r"$X$")
    ax_physical.set_ylabel(r"$Y$")

    r = 2
    ax_virtual.set_xlim([-r * 1.2, r * 1.2])
    ax_virtual.set_ylim([-r * 1.2, r * 1.2])

    x_virtual_1 = np.array(np.linspace(-r, r, 10_000))
    x_virtual = x_virtual_1
    x_virtual_2 = np.array(x_virtual_1[::-1])
    x_virtual = np.concatenate([x_virtual_1, x_virtual_2])
    y_virtual = np.concatenate([np.sqrt(r**2 - x_virtual_1**2), -np.sqrt(r**2 - x_virtual_2**2)])
    y_virtual = np.sqrt(r**2 - x_virtual**2)

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
 
