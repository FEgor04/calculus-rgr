import numpy as np
import matplotlib.pyplot as plt
import argparse
import plot_utils as pu  

def main(args):
    pu.figure_setup()

    fig_size = pu.get_fig_size(10, 5)
    fig = plt.figure()
    ax = fig.add_subplot(111)

    # For z^2 = 1, z is constant at ±1
    y = np.linspace(-1, 1, 400)
    z1 = np.ones_like(y)
    z2 = -np.ones_like(y)
    ax.plot(y, z1, label=r'$z^2 = 1$', color='blue')
    ax.plot(y, z2, color='blue')

    # For y + |z| = 0, z = ±y
    y = np.linspace(-1, 0, 400)
    z3 = y
    z4 = -y 
    ax.plot(y, z3, label=r'$y + \sqrt{z^2} = 0$', color='red')
    ax.plot(y, z4, color='red')

    # For y + z^2 = 2, z = sqrt(2-y)
    y = np.linspace(1, 2, 400)
    z5 = np.sqrt(2-y)
    z6 = -np.sqrt(2-y)
    ax.plot(y, z5, label=r'$y + z^2 = 2$', color='green')
    ax.plot(y, z6, color='green')
    
    ax.set_xlabel('$y$')
    ax.set_ylabel('$z$')

    ax.set_axisbelow(True)
    ax.grid()
    #ax.legend()
    # plt.tight_layout()

    plt.text(-1,  1, f'A', fontsize=12, ha='right', va='bottom')
    plt.text( 0,  0, f'B', fontsize=12, ha='left',  va='bottom')
    plt.text(-1, -1, f'C', fontsize=12, ha='right', va='bottom')
    plt.text( 1, -1, f'D', fontsize=12, ha='right', va='bottom')
    plt.text( 2,  0, f'E', fontsize=12, ha='left' , va='bottom')
    plt.text( 1,  1, f'F', fontsize=12, ha='right', va='bottom')

    plt.legend(bbox_to_anchor=(1.05, 1),
                         loc='upper left', borderaxespad=0.)
    if args.save:
        pu.save_fig(fig, args.save)
    else:
        plt.show()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--save')
    args = parser.parse_args()
    main(args)
