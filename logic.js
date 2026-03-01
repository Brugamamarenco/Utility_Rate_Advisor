//define variables
const rate=document.getElementById("ur");

//storage 
let rates=[] 

//calculate the percentage impact 
function calculatePercentage(costOfPurchase,maxCardLimit){
    uRate=(costOfPurchase/maxCardLimit)
    return uRate;
}

//append to rates 
function appendToRates(costList){
    for (let i=0; i<costList.length; i++){
        rates.push(calculatePercentage(costList[i])); 
}}
