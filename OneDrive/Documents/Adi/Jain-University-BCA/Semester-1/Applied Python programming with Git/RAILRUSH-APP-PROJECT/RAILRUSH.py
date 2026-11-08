import random
print("         WELCOME TO RAILRUSH         ")
print("     --------------------------      ")
username=input("Enter the Name of the Passenger: ")
age=int(input("Enter the Age of the Passenger: "))
fromdest=input("Enter the From Station (Station A,Station B,Station C,Station D,Station E): ").strip().upper()
todest=input("Enter the To Station (Station A, Station B,Station C,Station D,Station E): ").strip().upper()
classoftravel=input("Enter the Class to Travel (Gen, CC, 3A, 2A, 1A): ").strip().upper()
userdetails=[username,age,fromdest,todest,classoftravel]

def calculatedistance(source,destination):
    distancesofstation={"STATION A": 0,"STATION B": 100, "STATION C": 250, "STATION D": 400,"STATION E": 750}
    startkm=-1
    endkm=-1
    for station in distancesofstation:
        if source==station:
            startkm=distancesofstation[station]
        elif destination==station:
            endkm=distancesofstation[station]
    if startkm==-1 or endkm==-1:
        print("Invalid From/To Station")
        return 0
    else:
        distanceoftravel=abs(startkm-endkm)
        return distanceoftravel

distance=calculatedistance(fromdest, todest)
print("The Distance of Travel: ",distance)

def travelfare(distance, classoftravel, age):
    classesoftravel={"GEN":1,"CC":1.5,"3A":2,"2A":3,"1A":5}
    rate=-1
    for classes in classesoftravel:
        if classoftravel==classes:
            rate=classesoftravel[classes]
    if rate==-1:
        print("Invalid Class of Travel")
        return 0
    else:
        basefare=distance*rate
        if age<=13:
            finalfare=basefare*0.5
        elif age>=60:
            finalfare=basefare*0.25
        else:
            finalfare=basefare
        return finalfare

fare=travelfare(distance,classoftravel,age)
print("The Calculated Total Fare:" ,fare)

def generatepnr():
    pnr=random.randint(1000000000,9999999999)
    return pnr

pnrnumber=generatepnr()
print("Your PNR Number is: ",pnrnumber)

ticketsummary=f"Name of the Passenger {username}\n Age of the Passenger {age}\n Travelling from {fromdest} to {todest}\n Travel Class {classoftravel}\n Fare for travel {fare}\n PNR Number {pnrnumber}"
f=open("tickets.txt",'w')
f.write(ticketsummary)
f.close()