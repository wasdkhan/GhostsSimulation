from pos import Pos
from grid import Map
from ghost import Ghost

UP = 0
DOWN = 2
RIGHT = 1
LEFT = 3

Map = Map()
tpos = Pos((1, 2, 1, 2), 1)
tpos.printC()
print Map.valPos(tpos)

# pos2 = pos1.nPos()
# pos1.printC()
# pos2.printC()

# pos3, pos4 = pos2.adjPos()
# pos4.printC()
# pos3.printC()

g = Ghost(Pos((14, 15, 11, 12), RIGHT))
for i in xrange(5):
	g.p.printC()
	print Map.valPos(g.p)
	g.dec(tpos)
