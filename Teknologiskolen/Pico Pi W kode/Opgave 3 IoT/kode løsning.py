import PicoRobotics
import BNO055
import utime
import machine
from const import *
from device import uAPDS9960 as APDS9960

#Robotics setup
board = PicoRobotics.KitronikPicoRobotics()

#Network setup
sender = BNO055.Sender()

#Farvesensor setup
bus = machine.SoftI2C(sda=machine.Pin(4), scl=machine.Pin(5), timeout=100_000)
apds = APDS9960(bus)
apds.enableLightSensor()

#Variabler
#Variabel til bevægelse af servo 2
val = 1


def ScanColor():
    #Variabler til farvesensoren
    oval = -1
    ovalR = -1
    ovalG = -1
    ovalB = -1
    
    #Kode til at læse farverne
    valA = apds.readAmbientLight()
    if valA != oval:
        #print("AmbientLight={}".format(valA))
        oval = valA
        
    valR = apds.readRedLight()
    if valR != ovalR:
        print("RedLight={}".format(valR))
        ovalR = valR
            
    valG = apds.readGreenLight()
    if valG != ovalG:
        print("GreenLight={}".format(valG))
        ovalG = valG
            
    valB = apds.readBlueLight()
    if valB != ovalB:
        print("BlueLight={}".format(valB))
        ovalB = valB
        
    #Kode til at bruge det vi læser
    if 500 <= valR <= 800 and 450 <= valG <= 800 and 500 <= valB <= 800: # Hvis gul
        board.servoWrite(1, 60)
        print("Gul!")
        #Nu ved vi den er gul, så lad os sende det videre til serveren
        sender.Send("Gul")
        
        
    if 300 <= valR <= 600 and 100 <= valG <= 300 and 175 <= valB <= 350: # Hvis Rod
        board.servoWrite(1, 150)
        print("Rod!")
        sender.Send("Rod")
        
    if 2000 <= valR <= 5000 and 400 <= valG <= 650 and 400 <= valB <= 600: # Hvis Gron
        board.servoWrite(1, 130)
        print("Gron!")
        sender.Send("Gron")
        
    if 90 <= valR <= 290 and 200 <= valG <= 400 and 250 <= valB <= 500: # Hvis Bla
        board.servoWrite(1, 90)
        print("Bla!")
        sender.Send("Bla")
        
    if  1100 <= valR <= 1300 and 1100 <= valG <= 1300 and 1500 <= valB <= 1850: # Hvis Hvid
        board.servoWrite(1, 40)
        print("Hvid!")
        sender.Send("Hvid")
    
#Her er vores loop
while True:
    
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
        ScanColor()
        utime.sleep(1)
        val = 3
        
    if(val == 3):
        board.servoWrite(2, 5)
        print("Aflevering")
        utime.sleep(1)
        val = 1
        
    
    

    
    
    


    
        
