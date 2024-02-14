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
        
    if 700 <= valR <= 1000 and 700 <= valG <= 1000 and 750 <= valB <= 1050: # Hvis gul
        board.servoWrite(1, 60)
        print("Gul!")
        sender.Send("Gul")
        
    if 820 <= valR <= 920 and 320 <= valG <= 450 and 520 <= valB <= 640: # Hvis Rod
        board.servoWrite(1, 150)
        print("Rod!")
        sender.Send("Rod")
        
    if 225 <= valR <= 310 and 400 <= valG <= 500 and 410 <= valB <= 510: # Hvis Gron
        board.servoWrite(1, 130)
        print("Gron!")
        sender.Send("Gron")
        
    if 160 <= valR <= 300 and 320 <= valG <= 500 and 620 <= valB <= 800: # Hvis Bla
        board.servoWrite(1, 90)
        print("Bla!")
        sender.Send("Bla")
        
    if  1100 <= valR <= 1300 and 1100 <= valG <= 1300 and 1500 <= valB <= 1850: # Hvis Hvid
        board.servoWrite(1, 40)
        print("Hvid!")
        sender.Send("Hvid")
    
    
while True:
    utime.sleep(0.1)
    
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
        
    
    

    
    
    


    
        
