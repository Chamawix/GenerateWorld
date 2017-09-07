# -*- coding: utf-8 -*-


# -*- coding: utf-8 -*-

import sklearn as sk 
import scipy as sc 
import numpy as np 
import pandas as pd
import stemming.paicehusk as st 
from Tkinter import Tk
from tkFileDialog import askopenfilename
import nltk as nltk
import asciitable as asci
import re
import math
import random as rand
import character as ch
import city as ci
import region as r
import case as case
import constraint as cstr


class Country :
	#Nombre de régions composant le pays: 
	COUNTRYW = 1
	COUNTRYH = 1
	nbRegionMoyen = 8



	#La somme en ligne ou en colonne de toute les regions+bordures ne peut dépasser 
	def regionPlacementConstraint(self, aa, b, taillec): 
		#On retire tous les couples doublons
		#print(aa)
		#print(taillec)
		tailleb= taillec[len(aa)]
		boul = True

		if(b[0][0]+tailleb>self.maxW or b[0][1]+tailleb>self.maxH):
			#print("les limites sont depassees")
			return False

		casesInterdites = []
		for a in aa :
			ind = aa.index(a)
			taillea=taillec[ind]
			for i in xrange(taillea):
				for j in xrange(taillea):
					casesInterdites.append([a[0][0]+i, a[0][1]+j])
		
		if len(aa)==0:
			if(b[0]==self.center):
				return True
			else :
				return False

		#if True :
		for a in aa:
			#a = aa[len(aa)-1]
			ind = aa.index(a)
			taillea=taillec[ind]
			if(a[0][0]+taillea>self.maxH or a[0][1]+taillea>self.maxH):
			#print("les limites sont depassees")
				return False

			if(b[0]==a[0]):
				#print("je suis dans egal !")
				return False
			
			#print("a:")
			#print(a)
			#print("b:")
			#print(b)
			

			#On Vérifie que les cases dispos sont en bordure exacte avec le carre 

			if((b[0][1]<=a[0][1]+taillea and b[0][1]>a[0][1]-tailleb+1 ) and  (b[0][0]-a[0][0]==taillea or a[0][0]-b[0][0]==tailleb)):
				#On verifie que cette case positive ne viole aucune contrainte sur les autres régions existante
				for i in xrange(tailleb):
					for j in xrange(tailleb):
						if [b[0][0]+i, b[0][1]+j] in casesInterdites:
							return False
						else :
							boul=True
						# 
			elif((b[0][0]<=a[0][0]+taillea  and b[0][0]>a[0][0]-tailleb+1 ) and (a[0][1]-b[0][1]==tailleb or b[0][1]-a[0][1]==taillea)):
				for i in xrange(tailleb):
					for j in xrange(tailleb):
						if [b[0][0]+i, b[0][1]+j] in casesInterdites:
							return False
						else :
							boul=True
				
			else:
				boul = False

		return boul



	###Crée des zone de bordure entre les regions et les place pour créer le pays.
	def positionRegion(self):
		problem = cstr.Problem()
		problem.reset()


		problem.addVariable("monde", self.refpos)
		problem.addVariable("regions", self.posRegion)
		problem.addVariable("tailleCarre",self.tailleRegions)


		problem.addConstraint(self.regionPlacementConstraint, ["regions", "monde", "tailleCarre"])


		sol = problem.getSolutions()

		#pas de solutions : 
		if(len(sol)==0):
			print("pas de solutions")
			#print(positions)
			return -1

		else :
			#print(sol)
			print("Il y a n solutions avec n = :")
			print(len(sol))

		ind = sol[int(rand.random()*len(sol))]
		ind = self.refpos.index(ind["monde"])

		return ind



		
	### Fonction qui crée l'eau  de façon cohérente, selon certaines règles. 
	def createWaterZone(self):
		pass

	### Fonction qui crée des chaines de montagnes de façon cohérente, selon certaines règles. 
	def createMountainChain(self):
		pass

	### L'idée est de créer un ensemble de région "cohérentes", liées les unes aux autres, avec des particularités géographiques. 
	def __init__(self):
		self.nbRegion = 0
		self.regions = []
		#Contient le texte des positions :
		self.positions= []
		#Contient les positions :
		self.refpos=[]
		self.tailleRegions = []
		self.tailleRegions.append([])

		
		if(rand.random()<=0.5):
			self.nbRegion= Country.nbRegionMoyen - rand.randint(0,2)
		else :
			self.nbRegion= Country.nbRegionMoyen + rand.randint(0,2)
			
		for i in xrange(self.nbRegion):
			self.regions.append(r.Region())

		maxWidth = 0
		maxHeight= 0

		


		#On recupere ainsi un carre dans lequel on doit placer nos regions. 
		#print(maxWidth)
		#print(maxHeight)
		for i in self.regions : 
			maxWidth = maxWidth + i.regionw
			maxHeight= maxHeight+ i.regionh
			self.tailleRegions[0].append(i.regionw)

		

		#Si on fixe maxWidth et maxHeight

		print(len(self.tailleRegions[0]))

		self.maxW = maxWidth
		self.maxH = maxHeight
		self.center = [int(maxWidth/2), int(maxHeight/2)]


		boole=True
		while boole :
			self.positions=[]
			self.posRegion = []
			self.posRegion.append([])
			for i in xrange(maxWidth):
				for j in xrange(maxHeight):
					self.refpos.append([[i, j]])
					self.positions.append("n")

			for i in self.regions :
				boole=False
				#print(self.posRegion)
				app = self.positionRegion()
				if(app==-1):
					boole = True
					break
				self.posRegion[0].append(self.refpos[app])
				
				#print(self.posRegion)

				indReg = self.regions.index(i)

				for j in i.cases:
					for k in j :
						pos = self.posRegion[0][indReg]
						#(pos)
						#print("positions")
						#print(self.posRegion)
						#print("position")
						#print(pos)
						#print(k.position)
						index = self.refpos.index([[k.position[0]+pos[0][0],k.position[1]+pos[0][1]]] )
						self.positions[index]= k.type

						#print(self.positions[index])
				#print(self)


	def __str__ (self):
		s= ""
		s= "Taille : \n "
		print(len(self.positions))
		#print(math.sqrt(len(self.positions)))
		p = 0
		for i in self.positions:
			
			#print(self.positions.index(i)%math.sqrt(len(self.positions)))
			if(p%math.sqrt(len(self.positions)))==0:
				s= s+"\n"

			p=p+1
			if i[0]!="n":
				s = s+" "+i[0]
			else :
				s = s+" "+"_"

		#print(s)
		return s



def main2():
	c=Country()

	print(c)

if __name__ == '__main__':
 	main2()
