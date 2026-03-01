#Calculate The Impact Of Each Purchase On The Credit Limit
def calculateImpact(productCost,creditMax): 
    ultilityRatio=(productCost/creditMax)
    convertToPercentage=ultilityRatio * 100 

    return round(convertToPercentage,2)

#Sum The Percentages To Get Total Impact Of All Purchases On The Credit Limit
def sumPercentages(percentageList): 
    return sum(percentageList)

#Convert Purchase To Perce tage Impact 
def purchaseToRate(dataset): 
    percentageList=[] 
    percentageAccumlation=[]

    costInformation=dataset["cost"]
    maxCreditInformation=dataset["creditMax"][0]

    for cost in costInformation: 
        print("Cost: " + str(cost))
        percentageImpact=round(calculateImpact(cost,maxCreditInformation),2)
        

        percentageList.append(percentageImpact)

        #debugging statement 


    return percentageList

#Print Results 
def printResults(dataset):
    for index,row in dataset.iterrows(): 
        print(row["product"]+": $"+str(row["cost"])+"=>"+str(calculateImpact(row["cost"],row["creditMax"]))+"%")

#Return The Dateset 
def returnDatesAndCost(dataset): 
    dates=dataset["date"]
    costs=dataset["cost"]

    return dates,costs

