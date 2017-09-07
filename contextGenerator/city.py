# -*- coding: utf-8 -*-

import character as ch
import random as rand
from random import random
import pandas as pd
import math


class City : 
	#Ordre de grandeur en taille de villes :
	# 1 à 5 habitants, taille sur carte 1x1
	# 5 à 25 habitants, taille sur carte 1x1
	# 25 à 125 habitants, taille sur carte 1x1
	# 125 à 625 habtiants, taille sur carte 1x1
	# 625 à 3125 habitants, taille sur carte 2x2<
	# 3125 à 15625 habitants, taille sur carte 2x2
	# 15625 à 78125 habitants, taille sur carte 3x3

	tailleVille = ["lieudit", "hammeau", "village", "petiteVille", "ville", "grandeVille", "centreRegion"]
	climat = ["neutre", "chaud", "froid", "sec", "humide"]
	typeVille = ["cotiere, montagne, plaine"]

	encoding = "latin-1"
	syllabes = pd.read_table("Data/syllabes.csv",encoding= encoding, header = 0,delimiter="@", dtype=None)

	syllNeutre = ch.encodeSyll(syllabes.ix[pd.isnull(syllabes["Neutre"])!=True, "Neutre"].tolist(), encoding)

	def generateCityName(self,syll):
		probLenFName = [2,2,2,2,2,2,3,3,3,4,4]
		lenFName = rand.choice(probLenFName)
		FName = ""
		for i in range(0, lenFName):
			FName = FName + rand.choice(syll)

		
		return FName.title()


	def generateHabitants(self):
		#Chaque taille de ville est une multiplication par 5 de la ville plus petite d'un cran, avec un facteur random et un minimum de 1 habitant:
		#print("taille ville :")
		#print(City.tailleVille.index(self.taille))
		nbHabitant=  int(math.floor(pow(5,City.tailleVille.index(self.taille)) + random()*pow(5, City.tailleVille.index(self.taille)+1)))
		
		for i in xrange(nbHabitant):
			hab = ch.Character()
			hab.defineCity(self.name)
			self.habitants.append(hab)

		#print(len(self.habitants))
	
	def __init__(self, nom = None, taille= 2, typeVille= 0, nbVoisin=4, climat = 0 ):
		if nom == None :
			self.name= self.generateCityName(City.syllNeutre)
		else :
			self.name = nom 
		
		#Position en haut à gauche de la ville. 
		self.position= [0,0]
		
		self.taille = City.tailleVille[taille]
		self.typeVille = City.typeVille[typeVille]
		self.nombreVilleVoisine = nbVoisin
		self.villesVoisines = []
		self.distancesVV = []
		self.region = ""
		self.climat = City.climat[climat]
		self.habitants= []
		self.generateHabitants()
		
	


	def calculateDistanceVV(self, ville):
		dist = numpy.linalg.norm(numpy.array(self.position)-numpy.array(ville.position))

		return dist

	def addVoisin(self, ville):
		self.villesVoisines.append(ville)
		self.distancesVV.append(self.calculateDistanceVV(ville))


	def __str__ (self):
		s = ""
		s = s +"Nom : "
		s = s+self.name+"\n"

		s=  s + "Taille : "
		s = s + str(len(self.habitants)) +" habitants\n"
		#s = s + "Habitants : "
		#for i in self.habitants:
		#	s = s + "\n"
		#	s= s+ str(i)

		return s




