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

def encodeSyll(syll, encoding):

	result=[]
	for i in syll :
		result.append(i.encode(encoding=encoding,errors='replace'))

	return result

def generateName(syll):
	
	probLenFName = [2,2,2,2,2,2,3,3,3,4,5]
	probLenSName = [2,2,2,2,3,3,3,3,3,3,4,4,4,4,4,5]
	lenFName = rand.choice(probLenFName)
	lenSName = rand.choice(probLenSName)
	FName = ""
	SName = ""
	for i in range(0, lenFName):
		FName = FName + rand.choice(syll)
	for i in range(0,lenSName):
		SName = SName + rand.choice(syll)

	return FName +" "+SName



encoding = "latin-1"
syllabes = pd.read_table("Data/syllabes.csv",encoding= encoding, header = 0,delimiter="@", dtype=None)

print(syllabes.ix[pd.isnull(syllabes["Froid"])!=True, 4])

syllFroid =encodeSyll(syllabes.ix[pd.isnull(syllabes["Froid"])!=True, "Froid"].tolist(), encoding)
syllChaud =encodeSyll(syllabes.ix[pd.isnull(syllabes["Chaud"])!=True, "Chaud"].tolist(), encoding)
syllSec =  encodeSyll(syllabes.ix[pd.isnull(syllabes["Sec"])!=True, "Sec"].tolist(), encoding)
syllHumide = encodeSyll(syllabes.ix[pd.isnull(syllabes["Humide"])!=True, "Humide"].tolist(), encoding)

print(syllFroid)

print("\n Sec \n")
for i in range (0, 10):
	print(generateName(syllSec))

print("\n Humide \n")
for i in range (0, 10):
	print(generateName(syllHumide))
	
print("\n Chaud \n")
for i in range (0, 10):
	print(generateName(syllChaud))

print("\n Froid \n")
for i in range (0, 10):
	print(generateName(syllFroid))
	
	