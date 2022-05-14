import pandas as pd
import numpy as np

def findSig(hour):
    filePath="C:\\Users\\Chou_\\Downloads\\wave_height.csv"
    file=pd.read_csv(filePath)

    hour1=np.array(file.loc[:, "Wave Height Hour 1"])
    hour2=np.array(file.loc[:, "Wave Height Hour 2"])
    hour3=np.array(file.loc[:, "Wave Height Hour 3"])

    sortedH1 = -np.sort(-hour1)
    sortedH2 = -np.sort(-hour2)
    sortedH3 = -np.sort(-hour3)
    oneThird = int(len(sortedH1) / 3)
    new_hour1=np.empty(oneThird)
    new_hour2=np.empty(oneThird)
    new_hour3=np.empty(oneThird)

    if hour=="Hour 1":
        for i in range(oneThird):
            new_hour1[i]=sortedH1[i]
        print(np.average(new_hour1))
    elif hour=="Hour 2":
        for i in range(oneThird):
            new_hour2[i]=sortedH2[i]
        print(np.average(new_hour2))
    elif hour=="Hour 3":
        for i in range(oneThird):
            new_hour3[i]=sortedH3[i]
        print(np.average(new_hour3))
    else:
        print("Please Enter The Right Hour")

        

