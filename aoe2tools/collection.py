
import matplotlib.pyplot as plt

from aoe2tools.empire import Empire
from aoe2tools.utility import divider

class BuildOrderCollection:

    def __init__(self,*build_orders):
        if len(build_orders) == 1 and type(build_orders[0]) is list:
            self.build_orders = build_orders[0]
        else:
            self.build_orders = build_orders

    def plot(self, plot_path=".\\builds.png", v=1):
        print(divider)
        print('Creating build order plot for:')
        build_orders = self.build_orders
        for bo in build_orders:
            print(f'  {bo.name}')
        N = len(build_orders)

        fig = plt.figure()
        fig.set_size_inches((7,3*N))

        s = 0.95
        ds = (1 - s) / 2
        main_ax = fig.add_axes([ds, ds, s, s])
        fig.transFigure = main_ax.transAxes
        main_ax.set(xticks=[], yticks=[])
        for spine in main_ax.spines.values(): spine.set(visible=False)

        for i,build_order in enumerate(build_orders):

            empire = Empire()
            empire.execute_build_order(build_order, v=v)

            bo_ax = fig.add_axes([0, ((N-1-i)/N), 1, 1/N], label=f"{build_order.name}")

            bo_ax.set(xticks=[],yticks=[])
            for spine in bo_ax.spines.values(): spine.set(visible=True, linewidth=2)
            plt_ax,txt_ax = build_order.add_axes(bo_ax, split=0.7, xmargin=0.06, ymargin=0.13)

            build_order.plot(plt_ax, empire)
            build_order.add_text(txt_ax, empire)

        plt.savefig(plot_path,dpi=400)
        print(divider)
        print(f'Plot saved to {plot_path}')
        print(divider, '\n')
