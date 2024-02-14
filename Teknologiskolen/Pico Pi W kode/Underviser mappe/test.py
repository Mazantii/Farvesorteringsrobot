import PicoRobotics
import BNO055
from time import sleep
import machine
from const import *
from device import uAPDS9960 as APDS9960

sender = BNO055.Sender()
bus = machine.SoftI2C(sda=machine.Pin(4), scl=machine.Pin(5), timeout=100_000)

apds = APDS9960(bus)
board = PicoRobotics.KitronikPicoRobotics()
directions = ["f","r"]

print("Light Sensor Test")
print("=================")
apds.enableLightSensor()
board.motorOn(1, "f", 100)

oval = -1
ovalR = -1
ovalG = -1
ovalB = -1
while True:
    sleep(0.1)
    sender.Send("Gul")
    board.motorOn(1, "r", 13)
    
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
        
    if 900 <= valR <= 1100 and 750 <= valG <= 925 and 575 <= valB <= 775: # Hvis gul
        board.servoWrite(1, 70)
        sender.Send("Gul")
        sleep(0.25)
        
    if 600 <= valR <= 850 and 120 <= valG <= 300 and 200 <= valB <= 400: # Hvis Rod
        board.servoWrite(1, 150)
        sender.Send("Rod")
        sleep(0.25)
        
    if 225 <= valR <= 310 and 265 <= valG <= 325 and 300 <= valB <= 375: # Hvis Gron
        board.servoWrite(1, 130)
        sender.Send("Gron")
        sleep(0.25)
        
    if 100 <= valR <= 250 and 200 <= valG <= 350 and 450 <= valB <= 600: # Hvis Bla
        board.servoWrite(1, 100)
        sender.Send("Bla")
        sleep(0.25)
        
    if  950 <= valR <= 1150 and 850 <= valG <= 1100 and 1000 <= valB <= 1300: # Hvis Hvid
        board.servoWrite(1, 30)
        sender.Send("Hvid")
        sleep(0.25)
        
