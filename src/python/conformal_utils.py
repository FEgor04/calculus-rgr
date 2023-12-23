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
    ax_virtual.set_xlabel(r"$U$")
    ax_virtual.set_ylabel(r"$V$")

    ax_physical.set_title("Физическое пространство")
    ax_physical.set_xlabel(r"$X$")
    ax_physical.set_ylabel(r"$Y$")

    return fig, (ax_virtual, ax_physical)


def w(z: complex):
    return (z+1)/(z-1)
