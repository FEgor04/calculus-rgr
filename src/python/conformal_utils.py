import plot_utils as pu
import matplotlib.pyplot as plt
import numpy as np

def setup():
    fig = plt.figure()
    fig, (ax_virtual, ax_physical) = plt.subplots(
            nrows = 1,
            ncols = 2,
            figsize=(12,6),
            )


    ax_virtual.set_title("Виртуальное пространство")
    ax_virtual.set_xlabel(r"$u$")
    ax_virtual.set_ylabel(r"$v$")
    ax_virtual.spines['top'].set_visible(False);
    ax_virtual.spines['right'].set_visible(False);
    ax_virtual.set_aspect('equal', 'box')
    ax_virtual.scatter(-1, 0, color='red', s=40, marker='x', label=r'выколотая точка $z = -1$')
    ax_virtual.grid()

    ax_physical.set_title("Физическое пространство")
    ax_physical.set_xlabel(r"$x$")
    ax_physical.set_ylabel(r"$y$")
    ax_physical.spines['top'].set_visible(False);
    ax_physical.spines['right'].set_visible(False);
    ax_physical.set_aspect('equal', 'box')
    ax_physical.grid()
    ax_physical.scatter(1, 0, color='red', s=40, marker='x', label=r'выколотая точка $w = 1$')

    plt.legend()

    return fig, (ax_virtual, ax_physical)


def w(z: complex):
    return (z-1)/(z+1)
