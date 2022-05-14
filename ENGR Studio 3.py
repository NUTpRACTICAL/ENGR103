import numpy as np

#showering
time_showering = input("how long is your shower in minutes: ")
time_perweek_showerinhg= input ("how many times do you shower per week: ")
gallon_showering= (2*(int(time_showering))*(int(time_perweek_showerinhg)))

#Bathroom
time_bathroom= input("how many times do you use the bathroom per day(washing hands, flushing toilet, brushing teeth: ")
gallon_bathroom= (7*3*(int(time_bathroom)))

#Washing cloth
load_cloth= input ("how many loads of cloth per week")
gallon_cloth= 25*(int(load_cloth))

#washing dishes
meal_per_day= input ("how many meals do you have everyday: ")
dish_washing_perDay= input ("how many dishes do you wash everyday: ")
gallon_dish=((int (meal_per_day))+(int(dish_washing_perDay)))*7*7

#drinking water
cups_perDay= input("how many cups of water do you drink: ")
gallon_drinking_water=(int(cups_perDay))*8

#total water used calculation with array
water_used= np.array([gallon_drinking_water, gallon_dish, gallon_cloth, gallon_bathroom, gallon_showering])
total_water_used=np.sum(water_used)
bathtubOfWaterUsed= round(total_water_used/45)
print("You use about ",total_water_used, " of gallon per week, which is equal to ", bathtubOfWaterUsed, "45 gallon bathtub.")
print("Moreover, you are also using water that are not visible, such as electricity, food production, watering lawns, and more.")
print("water to know about it? please visit https://www.epa.gov/watersense/how-we-use-water")
