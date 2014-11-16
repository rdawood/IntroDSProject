import pandas as pd 
from pandas import DataFrame
import numpy as np 
import os 



def readCSV():
	DFs = {}

	for root, dirs, files in os.walk("data/"):
		for csv in files:
			print csv
			df = pd.read_csv("data/" + str(csv))
			DFs[str(csv)] = df


	for df in DFs:
		DFs[df].to_pickle("data/pickled/" + str(df)[-4])

def readPickles():
	DFs = {}

	for root, dirs, files in os.walk("data/pickled/"):
		for serial in files:
			df = pd.read_pickle("data/pickled/" + str(serial))
			DFs[str(serial)] = df

	return DFs()


#readCSV()

#readPickles()