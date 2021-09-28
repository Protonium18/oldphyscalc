import math
import traceback

def chatInit():    
    chatInput()
        
def chatInput():
    print('')
    inputMain = input().lower().split()
    str1=inputMain[0]
    str2=False
    str3=False
    str4=False
    
    if len(inputMain) > 1:
        str2=inputMain[1]

    if len(inputMain) > 2:
        str3=inputMain[2]
        try:
            str3=float(str3)
        except:
            str3=str3

    if len(inputMain) > 3:
        str4=inputMain[3]
        try:
            str4=float(str4)
        except:
            str4=str4

            
            
    if str1 == 'reset':
        print('Reset!')
        chatInit()
        
    elif str1 == 'kinetic':
        try:
            controllerKinCalc(str2, str3, str4)

        except(UnboundLocalError):
            traceback.print_exc()
            print('Incorrect command.')
            chatInput()
            
    elif str1 == 'momentum':
        try:
            controllerMomentumCalc(str2, str3, str4)

        except(UnboundLocalError):
            print('Incorrect command.')
            chatInput()

    elif str1 == 'convert':
        try:
            controllerConvertCalc(str2, str3, str4)

        except(UnboundLocalError):
            traceback.print_exc()
            print('Incorrect command1.')
            chatInput()

    elif str1 == 'electro':
        try:
            controllerElectroCalc(str2, str3, str4)

        except(UnboundLocalError):
            traceback.print_exc()
            print('Incorrect command1.')
            chatInput()

    elif str1 == 'help':
        try:
            chatPrint(str2)
            
        except(UnboundLocalError):
            print('Incorrect command.')
            chatInput()
    else:
        print('Incorrect command.')
        chatInput()
        
#controllers        
def controllerKinCalc(functionCall, variable1, variable2):
    if functionCall == 'mass':
        massKinCalc(variable1, variable2)

    elif functionCall == 'speed':
        speedKinCalc(variable1, variable2)

    elif functionCall == 'energy':
        energyKinCalc(variable1, variable2)

    else:
        print('Invalid command.')
        chatInput()

def controllerMomentumCalc(functionCall, variable1, variable2):
    if functionCall == 'mass':
        massMomentumCalc(variable1, variable2)

    elif functionCall == 'speed':
        speedMomentumCalc(variable1, variable2)

    elif functionCall == 'momentum':
        momentumMomentumCalc(variable1, variable2)

    else:
        print('Invalid command.')
        chatInput()

def controllerConvertCalc(functionCall, variable1, variable2):
    if functionCall == 'weight':
        weightConvertCalc(variable1, variable2)

    if functionCall == 'length':
        lengthConvertCalc(variable1, variable2)

    else:
        print('Invalid command.')
        chatInput()

def controllerElectroCalc(functionCall, variable1, variable2):
    if functionCall == 'arcvoltage':
        electroVoltDistCalc(variable1, variable2)

    if functionCall == "arcdist":
        electroDistVoltCalc(variable1, variable2)

    if functionCall == "magstrength":
        magnetStrengthCalc(variable1, variable2)

    if functionCall == "magforce":
        magnetForceCalc(variable1, variable2)

    else:
        print('Invalid command.')
        chatInput()
        
#kinetic
def massKinCalc(speed, kinEnergy):
    mass = round((kinEnergy/0.5)/speed**2, 3)
    print('Mass: %skg' %(mass))
    chatInput()

def speedKinCalc(mass, kinEnergy):
    speed = round(math.sqrt((kinEnergy/0.5)/mass),2)
    print('Speed: %sm/s' %(speed))
    chatInput()

def energyKinCalc(mass, speed):
    kinEnergy = round(0.5*mass*speed**2)
    prefix = 'J'
        
    print('Kinetic Energy: %s%s' %(kinEnergy, prefix))
    chatInput()


#momentum
def massMomentumCalc(speed, momentum):
    mass = round(momentum/speed, 2)
    print('Mass of object is: '+str(mass)+'kg')
    chatInput()

def speedMomentumCalc(mass, momentum):
    speed = round(momentum/mass, 2)
    print('Speed of object is: '+str(speed)+'m/s')
    chatInput()

def momentumMomentumCalc(mass, speed):
    momentum = round(mass*speed, 2)
    print('Momentum of object is: '+str(momentum)+'kg*m/s')
    chatInput()

def momentumContactCalc(force, momentum):
    contactTime = round(momentum/force, 2)
    print("Contact time is: " +str(contactTime)+" seconds")
    chatInput()

def momentumContactMomentumCalc(force, contactTime):
    momentum = round(force*contactTime, 2)
    print("Momentum is: " +str(momentum)+"kg*m/s")
    chatInput()

def momentumContactForceCalc(momentum, contactTime):
    force = round(momentum/contactTime, 2)
    print("Force is: "+str(force)+"N")
    chatInput()

#conversion
def weightConvertCalc(toConvert, weight):
    if toConvert == 'imperial':
        kg = round(weight/2.205,2)
        print(str(weight)+" lbs converts to: "+str(kg)+"kg")
        chatInput()
        
    if toConvert == 'metric':
        lbs = round(weight*2.205,2)
        print(str(weight)+"kg converts to: "+str(lbs)+" lbs")
        chatInput()

    if toConvert == '':
        print("Invalid input.")
        chatInput()

def lengthConvertCalc(toConvert, length):
    if toConvert == "imperial":
        ft = round(length*3.281, 2)
        print(str(length)+"m converts to: " +str(ft)+"ft")
        chatInput()

    if toConvert == "metric":
        m = round(length/3.281, 2)
        print(str(length)+"ft converts to: "+ str(m)+"m")
        chatInput()

    if toConvert == '':
        print("Invalid input.")
        chatInput()

#electromagnetism
def electroVoltDistCalc(pressure, distance):
    voltage = (pressure*(distance*1000)*0.7)*1000
    print("To arc %sm in %s atmosphere of pressure, voltage would have to be: %sV" %(distance, pressure, voltage))
    chatInput()

def electroDistVoltCalc(pressure, voltage):
    distance = round(((voltage/1000)/(pressure*0.7))/1000, 4)
    print("With %sV in %s atmosphere of pressure, electricity could arc: %sm" %(voltage, pressure, distance))
    chatInput()

def magnetStrengthCalc(current, distance):
    tesla = round(((1.257*10**-6)*current)/(2*3.1415*distance), 3)
    print("With %sA of current, a magnetic field with %sT would be felt at a distance of %sm." %(current, tesla, distance))
    chatInput()

def magnetForceCalc(tesla, surfarea):
    force = (tesla**2)*surfarea
    print("%sN of force would be felt in a magnetic field of %sT with %scm of surface area." %(force, tesla, surfarea))
    chatInput()


def chatPrint(selectType):
    if selectType == 'all':
        chatPrintKinetic(1)
        chatPrintMomentum(1)
        chatPrintConvert(1)
        
    elif selectType == 'kinetic':
        chatPrintKinetic(0)

    elif selectType == 'momentum':
        chatPrintMomentum(0)

    elif selectType == 'convert':
        chatPrintConvert(0)

    else:
        print('Incorrect command.')
        chatInput()

def chatPrintKinetic(allTrue):
    print('Kinetic energy:')
    print('Syntax: kinetic <type> <number> <number>')
    print('mass - Mass of an object with speed then kinetic energy.')
    print('speed - Speed of an object with mass then kinetic energy.')
    print('energy - Energy of a moving objcect with mass then speed.')
    if allTrue == 0:
        chatInput()

    else:
        print('')

def chatPrintMomentum(allTrue):
    print('Momentum:')
    print('Syntax: momentum <type> <number> <number>')
    print('mass - Mass of an object with speed then momentum.')
    print('speed - Speed of an object with mass then momentum')
    print('momentum - Momentum of a moving objcect with mass then speed.')
    if allTrue == 0:
        chatInput()

    else:
        print('')

def chatPrintConvert(allTrue):
    print('Conversion:')
    print('Syntax: convert <type> <type> <number>')
    print('weight - Converts weight, either imperial or metric.')
    print('length - Converts length to imperial or metric.')
    chatInput()


chatInit()
