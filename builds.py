
from aoe2tools.buildorder import BuildOrder

##################################################
############ Fast Castle Build Orders ############
##################################################

@BuildOrder('27+2 Pop FC-Boom', fontsize=8.8)
def pop27_fc_boom(empire):
    empire.standard_start()
    empire.produce_vils_until(14, 'food')
    empire.produce_vils_until(9, 'wood')
    empire.produce_vils_until(3, 'gold')
    empire.click_feudal()
    empire.rebalance_eco(food=13, wood=10, gold=3)
    empire.reach_feudal()
    empire.produce_vils(2, 'wood')
    empire.click_castle()
    empire.rebalance_eco(food=11, wood=14, gold=3)
    empire.reach_castle()
    empire.produce_vils_until(14, 'food')

@BuildOrder('28+2 Pop FC-Knights', fontsize=8.8)
def pop28_fc_knights(empire):
    empire.standard_start()
    empire.produce_vils_until(14, 'food')
    empire.produce_vils_until(10, 'wood')
    empire.produce_vils_until(3, 'gold')
    empire.click_feudal()
    empire.rebalance_eco(food=13, wood=11, gold=3)
    empire.reach_feudal()
    empire.produce_vils(2, 'gold')
    empire.click_castle()
    empire.reach_castle()

@BuildOrder('28+2 Pop FC-UniqueUnit', fontsize=8.8)
def pop28_fc_unique(empire):
    empire.standard_start()
    empire.produce_vils_until(14, 'food')
    empire.produce_vils_until(9, 'wood')
    empire.produce_vils_until(2, 'gold')
    empire.produce_vils_until(2, 'stone')
    empire.click_feudal()
    empire.rebalance_eco(food=12, wood=9, gold=2, stone=4)
    empire.reach_feudal()
    empire.produce_vils(2, 'stone')
    empire.click_castle()
    empire.reach_castle()


##################################################
############### Rush Build Orders ################
##################################################

@BuildOrder('23 Pop Archers', fontsize=9)
def pop23_archers(empire):
    empire.standard_start()
    empire.produce_vils_until(13, 'food')
    empire.produce_vils_until(9, 'wood')
    empire.click_feudal()
    empire.rebalance_eco(food=8, wood=11, gold=3)
    empire.reach_feudal()
    empire.produce_vils_until(8, 'gold')
    empire.produce_vils_until(16, 'food')
    empire.produce_vils_until(14, 'wood')
    empire.click_castle()

@BuildOrder('21 Pop Scouts', fontsize=8.5)
def pop21_scouts(empire):
    empire.standard_start(food=6,wood=3)
    empire.produce_vils_until(14, 'food')
    empire.produce_vils_until(6, 'wood')
    empire.click_feudal()
    empire.rebalance_eco(food=10, wood=10)
    empire.reach_feudal()
    empire.produce_vils_until(18, 'wood')
    empire.produce_vils(5, 'gold')
    empire.produce_vils_until(10, 'gold')
    empire.click_castle()

@BuildOrder('22 Pop M@A into Archers', fontsize=8.5)
def pop22_MaA_archers(empire):
    empire.standard_start(food=6,wood=4)
    empire.produce_vils_until(14, 'food')
    empire.build('Barracks')
    empire.produce_vils(1, 'wood')
    empire.produce_vils(2, 'gold')
    empire.research_loom()
    empire.click_feudal()
    empire.rebalance_eco(food=9, wood=10, gold=2)
    empire.reach_feudal()
    empire.build("Archery Range #1")
    empire.produce_vils_until(7, 'gold')
    empire.produce_vils_until(16, 'food')
    empire.click_castle()
    empire.build("Archery Range #2")

##################################################
############### Other Build Orders ###############
##################################################

@BuildOrder('28+2+2 Pop Turk FImp', fontsize=8.8)
def pop28_turk_fi(empire):
    empire.standard_start()
    empire.produce_vils_until(12, 'food')
    empire.produce_vils_until( 8, 'wood')
    empire.produce_vils_until(15, 'food')
    empire.produce_vils_until( 5,'gold')
    empire.click_feudal()
    empire.rebalance_eco(food=11, wood=12, gold=5)
    empire.reach_feudal()
    empire.produce_vils(2, 'gold')
    empire.click_castle()
    empire.reach_castle()
    empire.produce_vils(2, 'gold')
    empire.click_imperial()
    empire.rebalance_eco(food=7, wood=12, gold=13)
    empire.reach_imperial()

@BuildOrder('22 Pop Scouts into Unique Unit', fontsize=8.5)
def pop22_scouts2unique(empire):
    empire.standard_start(food=6,wood=3)
    empire.produce_vils_until(14, 'food')
    empire.produce_vils_until(7, 'wood')
    empire.research_loom()
    empire.click_feudal()
    empire.rebalance_eco(food=11, wood=10)
    empire.build('Barracks')
    empire.reach_feudal()
    empire.build('Stable')
    empire.produce_vils_until(16, 'food')
    empire.produce_vils(3, 'stone')
    empire.produce_vils(4, 'gold')
    empire.produce_vils_until(10, 'gold')
    empire.reassign_vils(2, 'food', 'stone')
    empire.reassign_vils(1, 'food', 'gold')
    empire.click_castle()
