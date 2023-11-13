import math
#pt1.1
chosenFuel=10000
ve=10000 #m/s
mF=100000
m0= chosenFuel + mF #kg, chosen fuel weight + dry weight
v = (math.log(m0/mF))*ve #velocity equation
#print("The velocity to travel from Earth to Mars is", v, "m/s")
    
#pt 1.2 d/v
distance=75000000000 #km to m
timeEtoM = distance/v
#print("It takes", timeEtoM, "seconds to travel from Earth to Mars") #s
days= timeEtoM/(60*60*24) #dimensional analysis -- seconds to minutes to days to hr

#print("It takes", days, "days to travel from Earth to Mars")
fuelCost= chosenFuel*1000 #$

#print("Fuel costs", fuelCost, "dollars")
damagesCost=days*120000 #$
damageTOTAL=fuelCost+damagesCost
#print("There are", damagesCost, "dollars in damages")
print()

#pt 1.3 input
x = float(input("Enter an amount of fuel between [0-100,000 kg]  "))

while x>100000 or x<=0:
    print("Invalid Amount. Enter an amount of fuel between [0-100,000 kg]   ")
    x = float(input("Enter an amount of fuel between [0-100,000 kg]  "))
    if x<100001 and x>=0:
        continue

chosenFuel=x
v = (math.log((chosenFuel+mF)/mF))*ve #velocity equation
timeEtoM = distance/v
days= timeEtoM/(60*60*24)
fuelCost= chosenFuel*1000
damagesCost=days*120000 #$
damageTOTAL=fuelCost+damagesCost
#print("The user input is", chosenFuel, "kg of fuel", "\n", "Time traveled took", timeEtoM, "seconds/in", days,"days", "\n", "Damage done in", damagesCost, "days and cost", damageTOTAL, "dollars")

#PART 2.1
csvOutputLabels="Fuel,Velocity,Duration,Fuel Cost,Losses,Value Loss"
csvOutputVariables=chosenFuel,v,days,fuelCost,damagesCost,damageTOTAL
print()
print(csvOutputLabels)
print(csvOutputVariables)

vRounded = round(v,2)
daysRounded = round(days,2)
fuelCostRounded = round(fuelCost,2)
damagesCostRounded = round(damagesCost,2)
damageTOTALRounded = round(damageTOTAL,2)

chosenFuelLabel=(format(x,",")+" kg")
velocityLabel=(str(format(vRounded,","))+" m/s")
durationLabel=(str(format(daysRounded, ","))+" days")
fuelCostLabel=(str(format(fuelCostRounded, ","))+ " USD")
lossesLabel=(str(format(damagesCostRounded, ","))+ " USD")
valueLostLabel=(str(format(damageTOTALRounded,","))+ " USD")

#2.2
print("-"*50)
cvsChosenFuel=("Desired output when user enters fuel in kg=", x)

csvFORMATLABELS=((format("Fuel", "<20"))+ ((format("Velocity", "<20")))+ (format("Duration", "<22"))+
                 (format("Fuel Cost", "<25"))+ (format("Losses", "<28"))+ (format("Value Lost", "<20")))
   
csvFORMATVARIABLES=(format(chosenFuelLabel,"<20")+format(velocityLabel,"<20")+format(durationLabel,"<22")+
    format(fuelCostLabel,"<25")+format(lossesLabel,"<28")+format(valueLostLabel,"<20"))


#2.3
option="""
How would you like to format the output?
1. CSV
2. Human-readable
Select 1 or 2    """

attempts=1
maxAttempts=5

print(option)
userChoice=int(input("1 or 2:  "))
while userChoice != 1 and userChoice!=2:
    print("Invalid Choice, Try again. Attempt", attempts,"\n", "Choose 1 or 2: ")
    attempts+=1
    print(option)
    userChoice=int(input("1 or 2:  "))
    if (userChoice==1 or userChoice==2):
        attempts=0
    elif attempts==maxAttempts:
        print("\n","Too Many Attempts. Exiting Program")
        exit()
if userChoice==1:
    print()
    print(csvOutputLabels)
    print(csvOutputVariables)
elif userChoice==2:
    print()
    print(csvFORMATLABELS)
    print(csvFORMATVARIABLES)
if  attempts==maxAttempts:
    print("\n","Too Many Attempts. Exiting Program")
    exit()