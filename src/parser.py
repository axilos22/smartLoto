import csv
import pandas as pd

folder = "../ressources/"
filename = "trainingSet.csv"
file = folder+filename

data = pd.read_csv(file,';',None,0)

print(data.head())