# -*- coding: utf-8 -*-

import sys
from random import random
import random
import math
import pandas as pd

#La generation du personnage doit se faire après la generation d'au moins la ville. 
#Le personnage est le centre d'une quête. 
#Un joueur allant dans un ville aura accès à une ou plusieurs quêtes (pouvant l'emmener dans d'autres villes).
#Si on compare a minecraft, lorsque l'on casse un bloc de feuille, on drop un objet. 
#Aller dans une ville (casser un bloc), permet de découvrir des quêtes associées a cette ville. 



def encodeSyll(syll, encoding):
		result=[]
		for i in syll :
			result.append(i.encode(encoding=encoding,errors='replace'))

		return result

def calculChance (chance):
		result=[]
		for i in range(0, len(chance)) :
			if i == 0:
				result.append(chance[i])
			else :

				result.append(chance[i]+result[i-1])
		return result

def getIndexFromRand(rand, randLuck):

	rand = int(math.floor(1+rand*100))
	#print("rand : ")
	#print(rand)
	for i in randLuck :
		if rand <= i:
			#print("index renvoye :")
			#print(randLuck.index(i))
			return randLuck.index(i)
		else :
			continue


class Character :
	genre = ["m", "f"]
	profession = ["marchand", "paysan", "forgeron", "taneur", "cordonnier", "artisan", "noble", "marin", "guide", "soldat", "chasseur"]
	proportionsProfession= [10,40,4,3,4,4,1,10,2,20,2]
	randomProfession = calculChance(proportionsProfession)


	encoding = "latin-1"
	syllabes = pd.read_table("Data/syllabes.csv",encoding= encoding, header = 0,delimiter="@", dtype=None)

	syllFroid =encodeSyll(syllabes.ix[pd.isnull(syllabes["Froid"])!=True, "Froid"].tolist(), encoding)
	syllChaud =encodeSyll(syllabes.ix[pd.isnull(syllabes["Chaud"])!=True, "Chaud"].tolist(), encoding)
	syllSec =  encodeSyll(syllabes.ix[pd.isnull(syllabes["Sec"])!=True, "Sec"].tolist(), encoding)
	syllHumide = encodeSyll(syllabes.ix[pd.isnull(syllabes["Humide"])!=True, "Humide"].tolist(), encoding)
	syllNeutre = encodeSyll(syllabes.ix[pd.isnull(syllabes["Neutre"])!=True, "Neutre"].tolist(), encoding)


	def generateName(self,syll):
		probLenFName = [2,2,2,2,2,2,3,3,3,4]
		probLenSName = [2,2,2,2,3,3,3,3,3,3,4,4,4,4,4]
		lenFName = random.choice(probLenFName)
		lenSName = random.choice(probLenSName)
		FName = ""
		SName = ""
		for i in range(0, lenFName):
			FName = FName + random.choice(syll)
		for i in range(0,lenSName):
			SName = SName + random.choice(syll)

		return FName.title() +" "+SName.title()



	def __init__(self, genre = None, ville= "", profession = None):
		self.name=self.generateName(Character.syllNeutre)
		if genre == None :
			self.genre=  Character.genre[int(math.floor(random.random()*len(Character.genre)))]
		else :
			self.genre = Character.genre[genre]
	
		self.relations=[]
		self.ville = ville
		#print(Character.randomProfession)
		#print(getIndexFromRand(random.random(),Character.randomProfession))
		if profession == None  :
			self.profession = Character.profession[int(getIndexFromRand(random.random(),Character.randomProfession))]
		else :
			self.profession = Character.profession[profession]


	def defineCity(self, ville):
		self.ville = ville

	def __str__ (self):
		s = ""
		s = "Name : "
		s = s + self.name
		s = s +"\n"+"Genre : "
		s = s + str(self.genre)
		s = s +"\n"+ "Profession : "
		s = s + str(self.profession)

		return s

	"""
	print("\n Neutre \n")
	for i in range (0, 10):
		print(generateName(syllNeutre)).decode()
	"""





