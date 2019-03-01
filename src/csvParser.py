import pandas as pd

class Parser:
    
    def __init__(self,filename):
        defaultFolder = "../ressources/"
        self.file = defaultFolder+filename
        self.dataFrame = pd.read_csv(self.file,';',None,0)
        
    def showData(self):
        print(self.dataFrame)

#filename = "trainingSet.csv"
#file = folder+filename

#data = pd.read_csv(file,';',None,0)

#print(data.head())