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
import country as country
import constraint as cstr




class World:
	#Nombre de pays composant le monde : 
	WORLDW = 1
	WORLDH = 1



	### L'idée est de superposer les pays, les uns avec les autres, selon les sorties, et de creer les points de passage entre les différents pays. 
	#Chaque pays sera séparé a un autre, soit par une chaine de montagne, soit par de l'eau (lac, rivière, mer). 
	#Aller d'un pays à un autre est infaisable de façon spontannée, il faut passer par certains points de passages, obligés. 

	def __init__(self):
		self.countries = country.Country()
		

	def __str__ (self):
		s=""
		s= s+str(self.countries)

		return s

