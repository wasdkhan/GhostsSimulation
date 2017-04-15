from pos import Pos
from grid import Map

Map = Map()

class Ghost:
	def __init__(self, _p):
		self.pos = _p

	def dec(self, tpos):
		nextPos = self.pos.nPos()
		val = Map.valPos(nextPos)
		if val < 3:
			lPos, __, rPos = self.pos.adjPos()
			lDist = 1000000
			rDist = 1000000
			if Map.valPos(lPos) > 2: 
				lDist = lPos.dist(tpos)
			if Map.valPos(rPos) > 2:
				rDist = rPos.dist(tpos)
			if lDist < rDist:
				self.pos = lPos
			elif rDist > lDist:
				self.pos = rPos
			else:
				self.pos.orient = (self.pos.orient - 2) % 4
				self.pos = self.pos.nPos()
		elif val == 8:
			lPos, fPos, rPos = nextPos.adjPos()
			lDist = 1000000
			fDist = 1000000
			rDist = 1000000
			if Map.valPos(lPos) > 2:
				lDist = lPos.dist(tpos)
			if Map.valPos(rPos) > 2:
				rDist = rPos.dist(tpos)
			if Map.valPos(fPos) > 2:
				fDist = fPos.dist(tpos)
			#minDist = min(lDist, rDist, fDist)
			self.pos = nextPos
			if lDist < fDist and lDist < rDist:
				self.pos.orient = (self.pos.orient - 1) % 4
			elif rDist < fDist and rDist < lDist:
				self.pos.orient = (self.pos.orient + 1) % 4
		else:
			self.pos = nextPos