import PicoRobotics
import utime
import machine
from const import *
from device import uAPDS9960 as APDS9960

#Robotics setup
board = PicoRobotics.KitronikPicoRobotics()

#Farvesensor setup
bus = machine.SoftI2C(sda=machine.Pin(4), scl=machine.Pin(5), timeout=100_000)
apds = APDS9960(bus)
apds.enableLightSensor()
#Koden ovenover er setup kode, den burde du ikke skulle pille ved.


#Variabler
#Variabel til bevægelse af servo 2
val = 1

farve = 1


#Dette er en funktion, den gør noget når vi kalder på den.
#def ScanColor():
    #Variabler til farvesensoren
 #   oval = -1
  #  ovalR = -1
   # ovalG = -1
    #ovalB = -1
    
    #Kode til at læse farverne
    #Kodebidder hints:
    #apds.readRedLight()
    #print("RedLight={}".format(valR))







    #Skriv kode herunder som får din rampe til at bevæge sig når den scanner en bestemt farve
    
    
    
    
#Her er vores loop
while True:
    #Her læser vi en farve!
    farve = apds.readBlueLight()
    print(farve)
    
    
    
    #Bevægelse af sensor 2
    if(val == 1):
        board.servoWrite(2, 100)
        print("Samler op")
        utime.sleep(1)
        val = 2
    
    if(val == 2):
        board.servoWrite(2, 42)
        print("Drejer til scanning")
        utime.sleep(0.5)
        utime.sleep(1)
        val = 3
        
    if(val == 3):
        board.servoWrite(2, 5)
        print("Aflevering")
        utime.sleep(1)
        val = 1
        
    
    

    
    
    


    
        
