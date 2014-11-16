import pandas as pd 
from pandas import DataFrame
import numpy as np 
import os 


DFs = {}

# set 0 to 1 to write csv's to pickles
if 1 == 0:
	for root, dirs, files in os.walk("data/"):
		for csv in files:
			print csv
			df = pd.read_csv("data/" + str(csv))
			DFs[str(csv)] = df


	for df in DFs:
		DFs[df].to_pickle("data/pickled/" + str(df)[-4])

# set 0 to 1 to read pickles as dataframes
if 1 == 0:
	for root, dirs, files in os.walk("data/pickled/"):
		for serial in files:
			df = pd.read_pickle("data/pickled/" + str(serial))
			DFs[str(serial)] = df

print DFs.keys()
