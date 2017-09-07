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
	nbRegionMoyen = 3

	#La somme en ligne ou en colonne de toute les regions+bordures ne peut dépasser 
	def regionPlacementConstring(self,a, b): 



	###Crée des zone de bordure entre les regions et les place pour créer le pays.
	def positionRegion(self):

		problem = cstr.Problem()
		problem.reset()

		#On veut que le pays place aleatoirement les regions, de tel sorte a ce que celle-ci soit 
		#1) connecte par une bordure interieur
		#2) en contact avec une bordure exterieur, utilisable pour se connecter a un autre pays

		problem.addVariable("regions", [[i.regionw, i.regionh]  for i in sum(self.cases,[])])
		problem.addVariable("")

		problem.addVariable
		#On crée une contrainte qui représente notre map : 
		#problem.addConstraint(lambda a,b,c: [a, b, c] == [self.cases.index(i), i.index(j), j.isWall], ("casex", "casey", "type")

		problem.addConstraint(lambda a : a[1] == False, ["cases"])
		problem.addConstraint(lambda b : b[2]=="ville", ["casesVilles"])
		problem.addConstraint(self.cityCloseConstraint, ["cases", "casesVilles"])
		


		#problem.addConstraint(lambda a:  , None)
		sol = problem.getSolutions()

		
	### Fonction qui crée l'eau  de façon cohérente, selon certaines règles. 
	def createWaterZone(self):
		pass

	### Fonction qui crée des chaines de montagnes de façon cohérente, selon certaines règles. 
	def createMountainChain(self):
		pass

	### L'idée est de créer un ensemble de région "cohérentes", liées les unes aux autres, avec des particularités géographiques. 
	### Cet ensemble sera nommé pays, et sera controlle les differents factions. 
	def __init__(self):

		self.centreGravite= []
		self.faction = []
		self.nbRegion = 0
		self.regions = []
		if(rand.random()<=0.5):
			self.nbRegion= Country.nbRegionMoyen - rand.randint(0,2)
		else :
			self.nbRegion= Country.nbRegionMoyen + rand.randint(0,2)
			
		for i in xrange(self.nbRegion):
			self.regions.append(r.Region())

		maxWidth = 0
		maxHeight= 0


		for i in self.regions : 
			#On rajoute 2 pour les bordures
			maxWidth = maxWidth + i.regionw+2
			maxHeight= maxHeight+ i.regionh+2

		#On recupere ainsi un carre dans lequel on doit placer nos regions. 
		#print(maxWidth)
		#print(maxHeight)


	def __str__ (self):
		s= ""
		s= "Taille : \n "
		s= len(self.regions) 

		return s

