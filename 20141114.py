import random

class myGame:
	def __init__(self,title):
		self.title = title
	def start(self):
		pass


class updownGame(myGame):
	def __init__(self,title,lower=1,upper=9):
		myGame.__init__(self,title)
		self.lower = lower
		self.upper = upper
	
	def start(self):
		print 'Limit:',self.lower,self.upper
		rn =  random.randint(1,9)


		
		while True:
			an = input("input")
			if rn == an:
				print "right"
				break
			elif rn <an:
				print 'Down'
			else:
				print 'up'

	def setLimit(self,lower,upper):
		self.lower = lower
		self.upper = upper
class baseballGame(myGame):
	def __init__(self,title):
		myGame.__init__(self,title)

class baseballGame3(baseballGame):
	def __init__(self,title):
		baseballGame.__init__(self,title)

	def start(self):
		rlist = range(1,10)
		random.shuffle(rlist)
		rnlist = rlist[:3]

		# rn1 = random.randint(1,9)
		# rn2 = rn1
		# rn3 = rn1


		# while True:
		# 	if rn1 == rn2:
		# 		rn2 =  random.randint(1,9)
		# 	else:
		# 		break

		# while True:
		# 	if rn1 == rn3 or rn2 == rn3:
		# 		rn3 = 




		while True:
			an = raw_input('Input:')
			anlist = [an[0],an[1],an[2]]

			strike = 0
			ball = 0

			for i in range(len(anlist)):
				for j in range(len(anlist)):
					if str(rnlist[i]) == anlist[j] and i == j:
						strike = strike+1
					if str(rnlist[i]) == anlist[j] and i!= j:
						ball = ball + 1
			if strike == 3:
				print '****************right******************'
				break
			print 'Output:',strike,'S',ball,'B'


class baseballGame4(myGame):
	def __init__(self):
		pass


if __name__ == '__main__':
	myinst = baseballGame3('gg')
	myinst.start()