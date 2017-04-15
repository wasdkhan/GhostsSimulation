from pos import Pos
from grid import Map
from ghost import Ghost
import time, threading

UP = 0
DOWN = 2
RIGHT = 1
LEFT = 3

Grid = Map()
omap = Grid.map
tpos = Pos((1, 2, 1, 2), 1)
print "Pacman located at: "
tpos.printD()

g = Ghost(Pos((13, 14, 14, 15), UP))

def loop(ghost, tpos, grid, omap):
	print "Blinky located at: "
	ghost.pos.printD()
	startOrient = ghost.pos.orient
	ghost.dec(tpos)
	nextTime = 0
	if ghost.pos.orient != startOrient:
		nextTime = 0.1
	if ghost.pos.orient == UP or ghost.pos.orient == DOWN: 
		nextTime += 0.333334
	else: 
		nextTime += 0.166667
	t = threading.Timer(nextTime, loop, (ghost, tpos, grid, omap))
	t.start()
	if ghost.pos.equals(tpos):
		print "Blinky caught pacman! Game Ended"
		t.cancel()

loop(g, tpos, Grid, omap)
