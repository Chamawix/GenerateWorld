# -*- coding: utf-8 -*-


from random import random
import math


class Case :
	typeCase = ["plaine", "montagne", "ville", "eau"]

	def getWallAttribute(self,i):
		if(i>1):
			return True
		else :
			return False

	def __init__(self, typec=None, pos=None):
		self.type = Case.typeCase[typec]
		self.position = pos
		self.isWall =self.getWallAttribute(typec)


	def __str__(self):
		s = ""
		s= s+str(self.position[0])+ "/"+str(self.position[1])
		s= s + "/"+ str(self.type)
		return s



