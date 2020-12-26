import numpy as np
from aoe2tools.utility import vdict, string_space, vprint

class Empire:

    def __init__(self, v=1):
        self.n_mil = 1
        self.villagers = vdict(food=0, wood=0, gold=0, stone=0, builder=0, idle=0)
        self.age = ""
        self.tc_time = 0
        self.history = [(self.tc_time, self.villagers.copy())]
        self.advances = []
        self.lines = []
        self.v = v

    @property
    def n_vils(self):
        return sum([v for v in self.villagers.values()])

    @n_vils.setter
    def n_vils(self, value):
        assert value >= self.n_vils, f'n_vils setr: {value} must be >= n_vils'
        self.villagers['idle'] += (value - self.n_vils)

    @property
    def pop(self):
        return self.n_vils + self.n_mil

    def execute_build_order(self,build_order_obj, v=None):
        self.v = v if v is not None else v
        build_order_obj.execute(self)

    def add2history(self,time=None,vils=None):
        time = self.tc_time if time is None else time
        vils = self.villagers.copy() if vils is None else vils
        self.history += [(time, vils)]

    def start_game(self,starting_vils=3, v=1):
        self.vilprint(f'  Dark Age Start', v=self.v)
        self.age = 'dark'
        self.tc_time += starting_vils
        self.villagers['idle'] += starting_vils
        self.add2history()

    def reassign_vils(self,n,src,dst, timestep=True, record=True, v=1):
        vils = self.villagers
        assert n <= vils[src], f"Attempting to reassign more villagers than exist from {src} to {dst}"
        self.villagers[src] -= n
        self.villagers[dst] += n
        if timestep:
            self.tc_time += 1
        if record:
            self.add2history()
        self.vilprint(f'    Reassign {n} villagers from {src} to {dst}', v=self.v)

    def reassign_starting_vils(self, dst, v=1):
        vils = self.villagers
        src = 'idle'
        n = vils[src]
        self.villagers[src] -= n
        self.villagers[dst] += n
        self.vilprint(f'    Send starting {n} vils to {dst}', v=self.v)
        self.lines.append(f'Send starting {n} vils to {dst}')
        self.add2history()

    def rebalance_eco(self,food=0, wood=0, gold=0, stone=0, builder=0, idle=0):
        re_vils = vdict(food=food, wood=wood, gold=gold, stone=stone, builder=builder, idle=idle)
        re_n_vils = sum([val for val in re_vils.values()])
        assert re_n_vils == self.n_vils, f'invalid number of vils ({re_n_vils} vs {self.n_vils}'
        self.villagers = re_vils
        self.add2history()
        self.lines.append(f'  ~ {food}f, {wood}w, {gold}g, {stone}s, {builder}b')

    def produce_vils(self, n, dst, v=1):
        self.villagers[dst] += n
        self.tc_time += n
        self.add2history()
        self.vilprint(f'    Send {n} new villagers to {dst}', v=self.v)
        self.lines.append(f'  +{n:>2} (^{self.villagers[dst]:>2}) to {dst}')

    def produce_vils_until(self, n, dst, v=1):
        dn = n - self.villagers[dst]
        assert dn >= 0, "producing negative villagers"
        self.villagers[dst] += dn
        self.tc_time += dn
        self.add2history()
        self.vilprint(f'    Send {dn} new villagers to {dst}', v=self.v)
        self.lines.append(f'  +{dn:>2} (^{n:>2}) to {dst}')

    def click_feudal(self, v=1):
        self.age = 'adv2feudal'
        self.advances += [self.tc_time]
        self.tc_time += 2
        self.vilprint(f'  Click up to the Feudal Age', v=self.v)
        self.lines.append(f'Click up to the Feudal Age')

    def reach_feudal(self, v=1):
        self.age = 'feudal'
        self.tc_time += 3
        self.advances += [self.tc_time]
        self.add2history()
        self.vilprint(f'  Feudal Age Reached', v=self.v)
        self.lines.append(f'Reach the Feudal Age')

    def click_castle(self, v=1):
        self.age = 'adv2castle'
        self.advances += [self.tc_time]
        self.tc_time += 2
        self.vilprint(f'  Click up to the Castle Age', v=self.v)
        self.lines.append(f'Click up to the Castle Age')

    def reach_castle(self, v=1):
        self.age = 'castle'
        self.tc_time += 4
        self.advances += [self.tc_time]
        self.add2history()
        self.vilprint(f'  Castle Age Reached', v=self.v)
        self.lines.append(f'Reach the Castle Age')


    def click_imperial(self, v=1):
        self.age = 'adv2imperial'
        self.advances += [self.tc_time]
        self.tc_time += 2
        self.vilprint(f'  Click up to the Imperial Age', v=self.v)
        self.lines.append(f'Click up to the Imperial Age')

    def reach_imperial(self, v=1):
        self.age = 'imperial'
        self.tc_time += 5
        self.advances += [self.tc_time]
        self.add2history()
        self.vilprint(f'  Imperial Age Reached', v=self.v)
        self.lines.append(f'Imperial the Castle Age')

    def research_loom(self, v=1):
        self.tc_time += 1
        self.add2history()
        self.vilprint(f'  Research Loom', v=self.v)
        self.lines.append(f'Research Loom')

    def standard_start(self, food=6, wood=4, starting_vils=3):
        self.start_game(starting_vils)
        self.reassign_starting_vils('food')
        self.produce_vils_until(food, 'food')
        self.produce_vils(wood, 'wood')

    def build(self, *buildings, v=1):
        for building in buildings:
            self.vilprint(f'    Build {building}', v=self.v)
            self.lines.append(f'  Build [{building}]')

    def vilprint(self,string, v=None):
        v = v if v is not None else self.v
        vprint(string_space(string, '->', f'{self.tc_time:2} {self.villagers} {self.n_vils:2}'), v=v)

    def get_history_table(self):
        tbl = np.zeros([len(self.history),6+1+1],dtype=int)
        for i,(t,d) in enumerate(self.history):
            cols = [v for v in d.values()]
            tbl[i,:] = [t] + cols + [sum(cols)]
        return tbl
