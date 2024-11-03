#!/usr/bin/env
# First mandatory coding assignment in the USN course for Python introduction
# Author Anders Bakken / bakken.anders@gmail.com
# Calculating cost differences between electric and petrol car

#Define variables and initialize default values

#kmPrYearl = 0 #Initiating to 10.000km pr default
insuranceElectric = 5000 #Pr Yearh
insurancePetrol = 7500 #Pr Year
trafficInsuranceFee = 8.38 #Pr day - Equal fee no matter engine type
fuleUsageElectric = 0.2 #kWh /km assuming home carginig
electricCost = 2.0 # kr/kWh
fuleCostPetro = 1.0 #kr /km
tollElectric = 0.1 #pr km
tollPetrol = 0.3 #pr km

#Calculate the total cost of electric car
def calculateElectricCost(kmPrYear):
    fulecostElectricPrYear = kmPrYear * fuleUsageElectric * electricCost
    tollCostElectricPrYear = tollElectric * kmPrYear
    totalYearlyCostElectric = fulecostElectricPrYear + tollCostElectricPrYear + insuranceElectric + (trafficInsuranceFee * 365)
    return totalYearlyCostElectric

#Calculate the total cost of petrol car
def calculatePetrolCost(kmPrYear):
    fulecostPetrolPrYear = kmPrYear * fuleCostPetro
    tollCostPetrol = tollPetrol * kmPrYear
    totalCYearlyCostPetrol = fulecostPetrolPrYear + tollCostPetrol + insurancePetrol + (trafficInsuranceFee * 365)
    return totalCYearlyCostPetrol

#Calculate the difference between the two
def calculateCostDifference(kmPrYear):
    costDifference = calculatePetrolCost(kmPrYear) - calculateElectricCost(kmPrYear)
    return costDifference

#Print formatting and initalization of the methods
def printOut():
    kmPrYearly = 0
    try:
        kmPrYearly = int(input("Input yearly milage. Default value is 10000km ") or 10000)
    except ValueError:
        kmPrYearly = 10000
    print("Yearly Costs")
    print("Electric Cost: ", calculateElectricCost(kmPrYearly));
    print("Petrol Cost: ", calculatePetrolCost(kmPrYearly));
    print("Cost Difference", calculateCostDifference(kmPrYearly)); 

printOut() #run the magic