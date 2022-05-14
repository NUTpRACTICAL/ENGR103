import math
import pandas as pd

def calmaxPower_actialPower(wS, r, ef):
    turbineRadius = r
    windSpeed=wS
    turbineEfficiency =ef
    airDensity = 1.2
    highestWindSpeed=23.98*0.44704
    lowestWindSpeed = 8.25*0.44704
    squaredRadius = turbineRadius**2
    surfaceArea = squaredRadius*(math.pi)
    maxPower = surfaceArea* (0.5)*(airDensity)*(highestWindSpeed**3)
    actualPower= maxPower*turbineEfficiency
    numberOfTurbine= (2.57*10**10)/(actualPower*31556926)
    return ("max power= ", maxPower,"number of turbine: ",numberOfTurbine,"Actual Power: ", actualPower)

print(calmaxPower_actialPower(0.5,2,0.98))
print(calmaxPower_actialPower(15,2,0.98))
print(calmaxPower_actialPower(0.5,3,0.6))
print(calmaxPower_actialPower(0.5,2,0.98))

def calOrificeDiameter(h,qO):
    volumeOfPond = 2 * 200 * 200  # meter
    q_in = qO
    d = 0.01  # guess
    c = 0.98
    g = 9.81
    h =h
    while True:
        a = (math.pi * (d ** 2)) / 4
        q_out = a * c * (math.sqrt(2 * g * h))
        if q_out >= q_in:
            break
        d = d + 0.001
    return d

print(calOrificeDiameter(2,2),"meter")
print(calOrificeDiameter(1,2),"meter")
print(calOrificeDiameter(2,0.5),"meter")
print(calOrificeDiameter(1,0.5),"meter")

#part C
def worldPowerChange(year1, year2, powerSource):
    file_path="C:\\Users\\Chou_\\Downloads\\energy_use_terrawatthours.csv"
    file=pd.read_csv(file_path)
    world1 = file.loc[:, 'year']
    power_type = file.loc[:, 'variable']
    power1 = file.loc[:, 'generation_twh']

    for x in range(len(power_type)):
        if power_type[x] == powerSource and int(world1[x]) == int(year1):
            year1Power=power1[x]

    for x in range(len(power_type)):
        if power_type[x] == powerSource and int(world1[x]) == int(year2):
            year2Power=power1[x]

    rateBtY1Y2="Between years ", year1, " and ", year2," the ", powerSource, " power generation changed by ",((year2Power-year1Power)/year1Power)*100,"%"

    return (rateBtY1Y2)

print(worldPowerChange(2000,2021,"Hydro"))
print(worldPowerChange(2010,2021,"Coal"))
print(worldPowerChange(2010,2021,"Gas"))
print(worldPowerChange(2010,2021,"Wind"))








