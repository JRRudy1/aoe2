
from aoe2tools import BuildOrderCollection
from builds import *

if __name__ == '__main__':
    v = 1

    FC_builds = BuildOrderCollection(pop27_fc_boom,pop28_fc_knights,pop28_fc_unique)
    rush_builds = BuildOrderCollection(pop21_scouts,pop22_MaA_archers, pop23_archers)
    other_builds = BuildOrderCollection(pop22_scouts2unique,pop28_turk_fi)

    #FC_builds.plot(".\\fc_builds.png", v=v)
    rush_builds.plot(".\\rush_builds.png", v=v)
    #other_builds.plot(".\\other_builds.png", v=v)

    print('Done.')
