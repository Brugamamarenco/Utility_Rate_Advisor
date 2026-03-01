#import libraries
import pandas as pd

#flask to connect to frontend
from flask import Flask 
app=Flask(__name__)



#file
import helperFunctions as hf


#Define route to get the data from the .csv file
@app.route("/data")
#Open The Dataset
def runDataSet(): 
    data=pd.read_csv("../mockdata/data.csv")
  
    return data


#Get A Log Of The Purchases (translated into rates) and return it in a list to the frontend
@app.route("/logOfRates")
def rateHistory(dataset): 
    ratePercentageList=hf.purchaseToRate(dataset)

    return ratePercentageList




#Testing Results 
percentageList=hf.purchaseToRate(runDataSet()) 



print(hf.printResults(runDataSet()))
print("Total: "+str(hf.sumPercentages(percentageList))+"%")
    


