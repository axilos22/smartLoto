class Drawing:
	drawingId = 0
	
	def __init__(self,date,balls,luckNb):
		self.drawingId = Drawing.drawingId
		self.date = date
		self.ball1 = balls[0]
		self.ball2 = balls[1]
		self.ball3 = balls[2]
		self.ball4 = balls[3]
		self.ball5 = balls[4]
		self.luckNb = luckNb
		Drawing.drawingId+=1
	
	def parseStr(str):
		print("parser")
		
	def __repr__(self):
		return "Drawing #{0}-{7}\n[1]={1}\n[2]={2}\n[3]={3}\n[4]={4}\n[5]={5}\nL={6}\n".format(self.drawingId,
				self.ball1,
				self.ball2,
				self.ball3,
				self.ball4,
				self.ball5,
				self.luckNb,
				self.date)
	def __str__(self):
		return "Drawing #{0}-{7}\t[1]={1}\t[2]={2}\t[3]={3}\t[4]={4}\t[5]={5}\tL={6}\n".format(self.drawingId,
				self.ball1,
				self.ball2,
				self.ball3,
				self.ball4,
				self.ball5,
				self.luckNb,
				self.date)