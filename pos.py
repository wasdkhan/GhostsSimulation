import math

BLOCKSIZE = 3.5
HBLOCKSIZE = 1.75
BEPSILON = 0.01

UP = 0
DOWN = 2
RIGHT = 1
LEFT = 3

class Pos:
	def __init__(self, coord, o):
		self.orient = o
		if len(coord) == 2:
			self.x = coord[0]
			self.y = coord[1]
			self.updateInd()
		elif len(coord) == 4:
			self.x1 = coord[0]
			self.x2 = coord[1]
			self.y1 = coord[2]
			self.y2 = coord[3]
			self.updatePos()

	def updateInd(self):
		m = self.x / BLOCKSIZE;
		self.x1 = int(m)
		r = self.x - self.x1 * BLOCKSIZE;
		if abs(r - HBLOCKSIZE) < BEPSILON * 5.0:
			self.x2 = self.x1
		elif r >= HBLOCKSIZE:
			self.x2 = self.x1 + 1
		else:
			self.x2 = self.x1
			self.x1 -= 1
		m = self.y / BLOCKSIZE;
		self.y1 = int(m);
		r = self.y - self.y1 * BLOCKSIZE;
		if abs(r - HBLOCKSIZE) < BEPSILON * 5.0:
			self.y2 = self.y1
		elif r >= HBLOCKSIZE:
			self.y2 = self.y1 + 1
		else:
			self.y2 = self.y1;
			self.y1 -= 1
		self.y1 += 1
		self.y2 += 1
		self.x1 += 1
		self.x2 += 1

	def updatePos(self):
		self.x = ((self.x1 - 1.0) * 0.5 + (self.x2 - 1.0) * 0.5) * BLOCKSIZE + HBLOCKSIZE
		self.y = ((self.y1 - 1.0) * 0.5 + (self.y2 - 1.0) * 0.5) * BLOCKSIZE + HBLOCKSIZE

	def nPos(self): #get next position based on current position
		if self.orient == UP:
			y1n = self.y1 - 1
			y2n = self.y2 - 1
			return Pos((self.x1, self.x2, y1n, y2n), UP)
		elif self.orient == DOWN:
			y1n = self.y1 + 1
			y2n = self.y2 + 1
			return Pos((self.x1, self.x2, y1n, y2n), DOWN)
		elif self.orient == LEFT:
			x1n = self.x1 - 1
			x2n = self.x2 - 1
			return Pos((x1n, x2n, self.y1, self.y2), LEFT)
		elif self.orient == RIGHT:
			x1n = self.x1 + 1
			x2n = self.x2 + 1
			return Pos((x1n, x2n, self.y1, self.y2), RIGHT)
		else: return None

	def adjPos(self):
		rOrient = (self.orient + 1) % 4
		lOrient = (self.orient - 1) % 4
		lPos = Pos((self.x1, self.x2, self.y1, self.y2), rOrient).nPos()
		rPos = Pos((self.x1, self.x2, self.y1, self.y2), lOrient).nPos()
		return lPos, rPos

	def dist(self, pos2):
		apos1 = ((self.x1 + self.x2)/2, (self.y1 + self.y2)/2)
		apos2 = ((pos2.x1 + pos2.x2)/2, (pos2.y1 + pos2.y2)/2)
		return math.sqrt(math.pow((apos1[0] - apos2[0]),2) + math.pow((apos1[1] - apos2[1]),2))

	def printC(self):
		print self.x1, self.x2 
		print self.y1, self.y2
		print self.orient

	def printD(self):
		print self.x, self.y
		print self.orient