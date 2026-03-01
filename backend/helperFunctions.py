#Calculate Impact 
def calculateImpact(productCost,creditMax): 
    ultilityRatio=(productCost/creditMax)
    convertToPercentage=ultilityRatio * 100 

    return convertToPercentage

#Sum 
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
        print("Hello World: "+str(round(sum(percentageList))))
        percentageAccumlation.append(round(sum(percentageList),2))
    
    return percentageList