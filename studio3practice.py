showers= input("How many showers do you take per week: ")
print(showers)
time_shower= input("How long are your showers: ") #min
print(time_shower)
gallons_water= (int(showers)*int(time_shower)*2) #gallons
print("You use approximately", gallons_water, "gallons of water showering per week")