### Author : Maximilien Matsakis, 2017 ###

# -*- coding: utf-8 -*-
import sys
sys.path.append('./contextGenerator')
import codecs

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
import world as w



file = codecs.open("Result/result.txt", "w", "utf-8")


def deleteContent(pfile):
    pfile.seek(0)
    pfile.truncate()

def main():

	world = w.World()
	#print(world)
	deleteContent(file)
	file.write(u'\ufeff')
	file.write(str(world))
	file.close()



if __name__ == '__main__':
 	main()