import numpy as np
from matplotlib.ticker import MultipleLocator

from aoe2tools import Empire
from aoe2tools.utility import divider

class BuildOrder:
    resource_names  = ['food', 'wood', 'gold',    'stone', 'builder']
    resource_colors = ['red', 'green', 'gold', 'darkgrey',   'brown']

    # Creates build order object with given name
    def __init__(self, name=None, fontsize=None):
        self.name = name
        self.bo_ax = None
        self.plt_ax = None
        self.txt_ax = None
        self.k = 0
        self.fontsize = fontsize
        self.empire = None

    def __call__(self, f, **kwargs):
        self.execute_function = f
        self.name = f.__name__ if self.name is None else self.name
        if "fontsize" in kwargs: self.fontsize = kwargs["fontsize"]
        return self

    def execute(self,empire=None, v=1):
        print(divider)
        print(f'Executing build order "{self.name}" *')
        empire = empire if empire is not None else (self.empire if self.empire is not None else Empire())
        self.execute_function(empire)
        return empire

    def add_axes(self,ax=None,split=0.5,xmargin=0.10,ymargin=0.05):
        bo_ax = self.bo_ax if ax is None else ax
        fig = bo_ax.get_figure()
        fig_trans = fig.transFigure
        fig.transFigure = bo_ax.transAxes
        mx = xmargin; my = ymargin; s = split; W = 1; H = 1
        plt_coords = [mx,my,(W-3*mx)*s,H-2*my]
        txt_coords = [(W-3*mx)*s+1.5*mx,my,(W-3*mx)*(1-s)+mx,H-2*my]

        self.plt_ax = fig.add_axes(plt_coords,label=f"{self.name}_plt")
        self.txt_ax = fig.add_axes(txt_coords,label=f"{self.name}_txt")

        self.txt_ax.set(xticks=[], yticks=[])

        fig.transFigure = fig_trans
        return self.plt_ax, self.txt_ax

    def plot(self, ax=None, empire=None):
        ax = self.plt_ax if ax is None else ax
        empire = empire if empire is not None else (self.empire if self.empire is not None else Empire())
        ax.set_title(f'{self.name}', y=0.997, fontdict={'fontsize': 12, 'fontweight': 'bold'})

        self.draw_advance_lines(ax, empire)
        self.add_history_lines(ax, empire)
        self.add_totalvils_history_lines(ax, empire)
        self.draw_ages(ax, empire)
        self.add_point_labels(ax, empire)
        self.add_totalvils_point_labels(ax, empire)

        ax.set(ylim=[0, 5*np.ceil(ax.get_ylim()[-1]/5.)])
        ax.set(xlim=[0, 5*np.ceil(ax.get_xlim()[-1]/5. -0.1)])
        for axx in [ax.xaxis,ax.yaxis]:
            axx.set_major_locator(MultipleLocator(5))
            axx.set_minor_locator(MultipleLocator(1))

        for spine in ax.spines.values(): spine.set(visible=True, linewidth=1)
        ax.grid(b=True, which='major', color='grey', linestyle='-',lw=0.5)
        ax.grid(b=True, which='minor', color='lightgrey', linestyle='-',lw=0.3)

    def add_history_lines(self, ax=None, empire=None):
        ax = self.plt_ax if ax is None else ax
        empire = empire if empire is not None else (self.empire if self.empire is not None else Empire())
        vil_table = empire.get_history_table()[:,:]
        ts = vil_table[:,0].flatten()
        lns = []
        for ri,(r,c) in enumerate(zip(BuildOrder.resource_names, BuildOrder.resource_colors)):
            ar = vil_table[:,ri+1].flatten()
            if any(ar):
                lns += [ax.plot(ts, ar, color=c, label=r, lw=1.5,
                        clip_on=False, zorder=10)]
            else:
                lns += [None]
        return lns

    def add_totalvils_history_lines(self, ax=None, empire=None):
        ax = self.plt_ax if ax is None else ax
        empire = empire if empire is not None else (self.empire if self.empire is not None else Empire())

        hist = empire.get_history_table()
        ts = hist[:,0].flatten()
        ntotals = hist[:,-1].flatten()

        for i in range(1,len(ntotals)-1):
            previous_row = hist[i-1,:]
            current_row = hist[i,:]
            next_row = hist[i+1,:]
            dif = np.subtract(next_row[1:-2],current_row[1:-2])
            changed = [x != 0 for x in dif]

            params = dict(ls='--',markersize=2,lw=1)
            c = 'pink'
            m = 'o'
            if sum(changed) == 1:
                j = changed.index(1)
                c = BuildOrder.resource_colors[j]
            else:
                if current_row[-1] != previous_row[-1]:
                    ax.plot(ts[i],current_row[-1],marker=m, c=c, zorder=120, **params)
                m = ''
            ax.plot(ts[i:i+2], ntotals[i:i+2], marker=m, c=c, zorder=100+i, **params)

    def add_point_labels(self, ax=None, empire=None):
        ax = self.plt_ax if ax is None else ax
        empire = empire if empire is not None else (self.empire if self.empire is not None else Empire())
        hist = np.array(empire.get_history_table())
        resources = BuildOrder.resource_names
        colors = BuildOrder.resource_colors
        tar = hist[:, 0].flatten()
        for ri,(r,c) in enumerate(zip(resources,colors)):
            ar = hist[:,ri+1].flatten()
            for ti in range(1,len(tar)):
                N = ar[ti]
                if ar[ti] != ar[ti-1]:
                    x = tar[ti]
                    y = N if ar[ti] > ar[ti-1] else N
                    ax.text(x, y, f'{N}', ha='center', va='center', fontsize=4.5, fontweight='bold', zorder=10000+ti,
                            bbox=dict(facecolor='white', boxstyle='round,pad=0.1', edgecolor=c, linewidth=0.8))

    def add_totalvils_point_labels(self, ax=None, empire=None):
        ax = self.plt_ax if ax is None else ax
        empire = empire if empire is not None else (self.empire if self.empire is not None else Empire())
        hist = np.array(empire.get_history_table())

        tar = hist[:, 0].transpose()
        ar = hist[:,-1].transpose()
        osx = 1
        osy = 1
        for j in range(1,len(tar)):
            N = ar[j]
            if ar[j] != ar[j-1]:
                x = tar[j] - osx
                y = (N + osy) if ar[j] > ar[j-1] else (N - osy)
                if j == len(tar) - 1:
                    x = tar[j] - 1.5
                    y = N
                ax.text(x, y, f'{N}',ha='center',va='center',fontsize=7,fontweight='bold',zorder=1000)

    def draw_advance_lines(self, ax=None, empire=None):
        ax = self.plt_ax if ax is None else ax
        empire = empire if empire is not None else (self.empire if self.empire is not None else Empire())
        lns = [ax.axvline(t, ls=':', c='orange', lw=1) for t in empire.advances]
        return lns

    def draw_ages(self, ax=None, empire=None):
        ax = self.plt_ax if ax is None else ax
        empire = self.empire if empire is None else empire

        y = (5 * np.ceil(ax.get_ylim()[-1] / 5.) - 2.75)
        props = dict(ha='center', weight='bold', fontsize=7.5, fontfamily='serif', va='center',
                     bbox=dict(facecolor='w',boxstyle='round'))

        feudal_txt = castle_txt = None
        if len(empire.advances) >= 2:
            t = np.average(empire.advances[:2])
            feudal_txt = ax.text(t,y, r"I$\longrightarrow$II", **props)

        if len(empire.advances) >= 4:
            t = np.average(empire.advances[2:])
            castle_txt = ax.text(t,y,r"II$\longrightarrow$III", **props)

        return feudal_txt, castle_txt

    def add_text(self, ax=None, empire=None):
        ax = self.plt_ax if ax is None else ax
        empire = empire if empire is not None else (self.empire if self.empire is not None else Empire())

        lines = empire.lines
        ax.text(0.02, 0.98, "\n".join(lines), transform=ax.transAxes, va='top', ha='left',
                font='consolas', fontsize=self.fontsize)