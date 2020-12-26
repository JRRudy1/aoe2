
from aoe2tools import BuildOrderCollection
from aoe2tools.builds import *

if __name__ == '__main__':
    v = 0

    FC_builds = BuildOrderCollection(pop27_fc_boom,pop28_fc_knights,pop28_fc_unique)
    rush_builds = BuildOrderCollection(pop21_scouts,pop22_MaA_archers, pop23_archers)
    other_builds = BuildOrderCollection(pop22_scouts2unique,pop28_turk_fi)

    FC_builds.plot("C:\\Users\\Joshua\\PycharmProjects\\aoe2\\fc.png", v=v)
    rush_builds.plot("C:\\Users\\Joshua\\PycharmProjects\\aoe2\\rush.png", v=v)
    other_builds.plot("C:\\Users\\Joshua\\PycharmProjects\\aoe2\\other.png", v=v)

    print('Done.')
