#import libraries
import pandas as pd


#file
import helperFunctions as hf

#import flask
import flask 

#open the dataset 
dataset=pd.read_csv("../mockdata/data.csv")
print(dataset)

percentageList=hf.purchaseToRate(dataset)
print(str(hf.sumPercentages(percentageList))+"%")


df=pd.DataFrame({"dates":[1,2,3],"rates":percentageList})

hf.makeDiagram(df)



