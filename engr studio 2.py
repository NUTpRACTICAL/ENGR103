mpg = 30 #set mile per gallon value
gUsed = mpg*14032 #compute the average gallon of gas used per year
costOGas1 = gUsed*4.72 # calculate the total cost of oil used in a year in oregon
costOGas2=gUsed*5.92# calculate the total cost of oil used in a year in Cali
print(gUsed)#print out the average gallon of gas used per year
print(costOGas1)#print out the  total cost of oil used in a year in Oregon
print(costOGas2)#print out the  total cost of oil used in a year in Cali

mpge = 108 #set mile per gallon for electric car value
gUsed = mpge*14032 #compute the average gallon of gas used per year for electric car
pUsed = gUsed*33.7 #convert gallon of gas used per year into power in kWh
costOPower1 = pUsed*0.1116 #calculate the Cost of power over year at home
costOPower2=pUsed*0.3#calculate the Cost of power over year at EV charging station
print(gUsed)#print out the average gallon of gas used per year for electric car
print(costOPower1)#print out the Cost of power over year at home
print(costOPower2)#print out the Cost of power over year at EV charging station