
Script to create "build order plots". Main file: "./aoe2plot.py". Source code: "./aoe2tools/"

Build orders are located in "builds.py". Follow the template of these builds to add new ones. 

The build order plots to be created are specificied in "aoe2plot.py". 
Any number of build orders can be stacked together as a plot, but 3 is the optimal number for printing to paper.


For the plots that are generated:

The x-axis represents a kind of of arbitrary pseudo-time unit, defined by the number of villagers you would have if you never stopped villager production to research loom or advance to Feudal. Using this unit is convenient because it doesn't rely on the player maintaining perfectly constant villager production.

The dotted line represents your total number of villagers as the game progresses; thus it goes up with a slope of 1 while you maintain constant villager production, but stays flat while you are advancing to the next age. The color of a segment of the dotted line represents which resource new villagers should be sent to during that period. The number labels indicate the villager population at which a transition occurs.

The colored lines represent the number of villagers on each resource as the game progresses. The numbered junctions indicate the number of villagers after which you should stop sending villagers to the resource. Changes that happen during age transitions correspond to economy rebalancing, which is typical performed soon after clicking up. These rebalances are also reflected in the text on the right of the graphs by lines starting with "~".

Note that I do not differentiate between food sources. In my opinion, the standard pattern of sheep, boar, berries, boar #2, etc. and the ways you can deviate from it is something that you really just need to practice and learn by heart. The bigger picture of what resources you are focusing on throughout the game for a given strategy, and more importantly why, is really what I am looking to capture with these graphs.