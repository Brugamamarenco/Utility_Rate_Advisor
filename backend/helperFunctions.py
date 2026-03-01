#Calculate Impact 
def calculateImpact(productCost,creditMax): 
    ultilityRatio=productCost / creditMax
    convertToPercentage=ultilityRatio * 100 

    return convertToPercentage

#Sum 
def sumPercentages(percentageList): 
    return sum(percentageList)

#Convert Purchase To Perce tage Impact 
def purchaseToRate(dataset): 
    percentageList=[] 

    costInformation=dataset["cost"]
    maxCreditInformation=dataset["creditMax"][0]

    for cost in costInformation: 
        percentageImpact=round(calculateImpact(cost,maxCreditInformation),2)
        percentageList.append(percentageImpact)

        #debugging statement 
        print(str(percentageImpact)+"%")
    
    return percentageList 

#Data Modeling
import matplotlib.pyplot as plt
import seaborn as sns

def makeDiagram(df): 
    sns.lineplot(data=df,x="dates", y="rates")
    plt.show()

