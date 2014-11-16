import pandas as pd 
from pandas import DataFrame
import numpy as np 
import os 



def readCSV():
	DFs = {}

	for root, dirs, files in os.walk("data/"):
		for csv in files:
			df = pd.read_csv("data/" + str(csv), low_memory = False)
			DFs[str(csv)] = df

	for df in DFs:
		fileName = "data/pickled/" + str(df)[:-4]
		DFs[df].to_pickle(fileName)

def readPickles():
	DFs = {}

	for root, dirs, files in os.walk("data/pickled/"):
		for serial in files:
			df = pd.read_pickle("data/pickled/" + str(serial))
			DFs[str(serial)] = df

	return DFs


readCSV()

# readPickles()

