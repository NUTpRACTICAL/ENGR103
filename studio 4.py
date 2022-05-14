import pandas as pd
import numpy as np

file_path='C:\\Users\\Chou_\\Downloads\\energy_use_terrawatthours.csv'
file=pd.read_csv(file_path)

world1=file.loc[:, 'year']
power_type1=file.loc[:, 'variable']
power1=file.loc[:, 'generation_twh']

cntr1=0
empty_power=np.empty(11)

#for x in range(len(power_type1)):
 #   if int(world1[x])==2000:
 #       print("Energy from", power_type1[x], " accounts for ", power1[x], " twh of world power in year 2000")

#for x in range(len(power_type1)):
 #   if power_type1[x]=="Clean" or power_type1[x]=="Fossil":
 #       print("Energy from", power_type1[x], " accounts for ", power1[x], " twh of world power in year ", world1[x])

for x in range (len(power_type1)):
    if power_type1[x]=="Clean" and power1[x] > power1[x+1]:
        print("In year ", world1[x]," world Clean energy production was greater than world Coal energy production")
    
    
