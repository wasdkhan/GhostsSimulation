from pos import Pos
from grid import Map
from ghost import Ghost
import time, threading

import numpy as np
import matplotlib.pyplot as plt

UP = 0
DOWN = 2
RIGHT = 1
LEFT = 3

PACMAN = 12
BLINKY = -2

Grid = Map()
Omap = np.array(Grid.map)
np.copyto(Grid.map, Omap)
tpos = Pos((1, 2, 1, 2), 1)
print "Pacman located at: "
tpos.printD()
Grid.colorPos(tpos, PACMAN)

g = Ghost(Pos((13, 14, 14, 15), UP)) #den
#g = Ghost(Pos((26, 27, 29, 30), LEFT)) #corner
Grid.colorPos(g.pos, BLINKY)

plt.pcolor(Grid.map)
plt.colorbar()
plt.axis('equal')
i = 0
fname = "pics/frame" + str(i) + ".png"
plt.savefig(fname)

def loop(ghost, tpos, grid, omap, i):
	print "Blinky located at: "
	ghost.pos.printD()
	startOrient = ghost.pos.orient
	ghost.dec(tpos)
	Grid.resetColor(omap)
	Grid.colorPos(ghost.pos, BLINKY)
	Grid.colorPos(tpos, PACMAN)
	plt.pcolor(Grid.map)
	plt.axis('equal')
	i += 1
	fname = "pics/frame" + str(i) + ".png"
	plt.savefig(fname)
	nextTime = 0.333334
	if ghost.pos.orient != startOrient:
		nextTime += 0.1
	t = threading.Timer(nextTime, loop, (ghost, tpos, grid, omap, i))
	t.start()
	if ghost.pos.equals(tpos):
		print "Blinky caught Pacman! Game Ended"
		t.cancel()

loop(g, tpos, Grid, Omap, i)
