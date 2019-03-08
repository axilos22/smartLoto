import pandas as pd

class Parser:
    
    def __init__(self,filename,relativePath="../ressources/",separator=';'): 
        self.file = relativePath+filename
        self.dataFrame = pd.read_csv(self.file,separator,None,0)
        
    def showData(self):
        print(self.dataFrame)
        
    def dataFrame(self):
        return self.dataFrame
    
    def computeBasicStats(self):
        self.computeAverage()
        
    def computeAverage(self):
        means = [0,0,0,0,0,0]
        headers = ["boule_1","boule_2","boule_3","boule_4","boule_5","numero_chance"]
        for i in range(len(means)):
            means[i] = self.dataFrame[headers[i]].mean()
            print("mean({0}) = {1}".format(headers[i],means[i]))
#filename = "trainingSet.csv"
#file = folder+filename

#data = pd.read_csv(file,';',None,0)

#print(data.head())