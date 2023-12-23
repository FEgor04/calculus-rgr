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

    x_virtual = np.linspace(-2000, 2000, 100_000)
    y1_virtual = np.array([5 for x in x_virtual])
    y2_virtual = np.array([-5 for x in x_virtual])
    y_virtual = np.concatenate([y1_virtual, y2_virtual])
    
    ax_virtual.plot(x_virtual, y1_virtual, label=r"$V = 5$")
    ax_virtual.plot(x_virtual, y2_virtual, label=r"V = -5")

    virtual_numbers_1 = np.array([complex(x_virtual[i], y1_virtual[i]) for i in range(len(x_virtual))])
    virtual_numbers_2 = np.array([complex(x_virtual[i], y2_virtual[i]) for i in range(len(x_virtual))])
    # virtual_numbers = np.concatenate([virtual_numbers_1, virtual_numbers_2])
    physical_numbers_1 = [w(z) for z in virtual_numbers_1]
    physical_numbers_2 = [w(z) for z in virtual_numbers_2]

    x_physical_1 = [z.real for z in physical_numbers_1]
    y_physical_1 = [z.imag for z in physical_numbers_1]
    x_physical_2 = [z.real for z in physical_numbers_2]
    y_physical_2 = [z.imag for z in physical_numbers_2]

    ax_physical.plot(x_physical_1, y_physical_1, label="V = 5")
    ax_physical.plot(x_physical_2, y_physical_2, label="V = -5")

    ax_virtual.legend()
    ax_virtual.grid()

    ax_physical.legend()
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
 
