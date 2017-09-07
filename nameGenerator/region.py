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



class Region :
	REGIONW = 10
	REGIONH = 10
	meanCityDensity = 10

	
	#Génère dans un premier temps des cases de type plaine ou montagne, sans règle. 
	#Fonction qui devra générer des bioms de cases, sur lequel placer les villes. 
	def generateCase(self):
		world= []
		for i in xrange(self.regionh):
			createL = []
			for j in xrange(self.regionw):
				createL.append(case.Case(int(rand.random()*2*0.75), [i,j]))

			world.append(createL)

		return world


	def cityCloseConstraint(self,a, b):
		#On retire tous les couples doublons 
		if(b[0]==a[0]):
			return False

		#On calcul la distance entre a et b, et on retire les couples qui ont une distance de 1
		bool1 = (np.linalg.norm(np.array(a[0])-np.array(b[0]))==1)
		return not bool1

		
		
	def hasCity(self) :
		for i in self.cases :
			for j in i :
				if j.type =="ville":
					return True

		return False

	def determinePossiblePosition(self):
		result = []

		#print("#nouvel appel : ")
		#Si la carte a pas de villes, on a pas de contraintes, on peut y aller random !
		if not self.hasCity():
			return [int(rand.random()*len(self.cases)), int(rand.random()*len(self.cases[0]))]

		problem = cstr.Problem()
		problem.reset()
		
		#print([[i.position, i.isWall]  for i in sum(self.cases,[])])
		problem.addVariable("cases", [[i.position, i.isWall, i.type]  for i in sum(self.cases,[])])
		problem.addVariable("casesVilles", [[i.position, i.isWall, i.type]  for i in sum(self.cases,[])])

		problem.addVariable
		#On crée une contrainte qui représente notre map : 
		#problem.addConstraint(lambda a,b,c: [a, b, c] == [self.cases.index(i), i.index(j), j.isWall], ("casex", "casey", "type")

		problem.addConstraint(lambda a : a[1] == False, ["cases"])
		problem.addConstraint(lambda b : b[2]=="ville", ["casesVilles"])
		problem.addConstraint(self.cityCloseConstraint, ["cases", "casesVilles"])
		


		#problem.addConstraint(lambda a:  , None)
		sol = problem.getSolutions()

		if(len(sol)==0):
			#print(sol)
			return []
		

		countCity = []
		countcase = [[], []]

		##Contrainte globale count  : 
		for i in sol : 
			if i["casesVilles"] not in countCity:
				countCity.append(i["casesVilles"])
				
			if i["cases"] not in countcase[0] : 
				countcase[0].append(i["cases"])
				countcase[1].append(1)
			else :
				ind = countcase[0].index(i["cases"])
				countcase[1][ind]= countcase[1][ind]+1

			

		#print(len(countCity))
		#print(countcase[1])
		
		possibleCases = [i for i, j in enumerate(countcase[1]) if j == len(countCity)]

		#print(possibleCases)
		if(len(possibleCases)==0):
			return []
		
		
		#print(sol)

		ind = possibleCases[int(rand.random()*len(possibleCases))]
		result = countcase[0][ind][0]
		#print(result)
		
		return result

	def setPositionVille(self,pos, city):
		#On le set sur la case : 
	
		self.cases[pos[0]][pos[1]].type=  self.cases[pos[0]][pos[1]].typeCase[2]
		self.cases[pos[0]][pos[1]].isWall= True

		city.pos=pos
		#print("## Ville a la nouvelle position:")
		#print(pos)

		return city

	##Fonction qui permet de générer les villes, et de les placer correctement sur la carte, tout en remplaçant la valeur des cases. 
	#Pour l'instant, elle génère les villes, mais ne les place pas. 
	def generateCity(self, density):
		
		cityList= []
		
		
		totalCity = int(((self.regionh)*(self.regionw))*density/100)


		for i in xrange(totalCity):
			cityT = ci.City(taille= int(rand.random()*5))
			pos = self.determinePossiblePosition()
			if(len(pos)==0):
				continue
			else :
				city = self.setPositionVille(pos, cityT)
				cityList.append(city)


		return cityList

	def __init__(self):
		self.bordure = []
		
		if(rand.random()<=0.5):
			self.cityDensity = Region.meanCityDensity -1 -int(rand.random()*5)
			regrand = 1+int(rand.random()*2)
			self.regionw = Region.REGIONW-regrand
			self.regionh = Region.REGIONH-regrand
		else :
			self.cityDensity = Region.meanCityDensity +1+int(rand.random()*5)
			regrand = 1+int(rand.random()*2)
			self.regionw = Region.REGIONW+regrand
			self.regionh = Region.REGIONH+regrand

		self.cases = self.generateCase()

		self.cities = self.generateCity(self.cityDensity)
		

	def __str__ (self):
		s=""
		s= s+ "map:"
		for i in self.cases : 
			s = s + "\n"
			for j in i :
				s = s + str(j) + "\t"
		
		s= s+"\n \n"
		s= s+"Densite : "+ str(self.cityDensity)
		s = s + "\n"+ "nbVille :"+ str(len(self.cities))
		s = s+"\ncities : \n"

		#for k in self.cities :
		#	s = s+ str(k)+"\n #####\n"

		return s

