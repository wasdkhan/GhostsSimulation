from pos import Pos
from grid import Map

Map = Map()

class Ghost:
	def __init__(self, _p):
		self.p = _p

	def dec(self, tpos):
		nextPos = self.p.nPos()
		val = Map.valPos(nextPos)
		while val < 3:
			self.p.orient = (self.p.orient + 1) % 4
			print "dir", self.p.orient
			nextPos = self.p.nPos()
			val = Map.valPos(nextPos)
		lPos, rPos = nextPos.adjPos()
		lDist = 1000000
		rDist = 1000000
		if Map.valPos(lPos) > 2:
			lDist = lPos.dist(tpos)
		if Map.valPos(rPos) > 2:
			rDist = rPos.dist(tpos)
		if lDist < rDist: 
			self.p = nextPos 
			self.p.orient = (self.p.orient - 1) % 4
		elif lDist >= rDist:
			self.p = nextPos
			self.p.orient = (self.p.orient + 1) % 4
