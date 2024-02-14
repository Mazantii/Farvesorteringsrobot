import PicoRobotics
import utime
import machine

#Robotics setup
board = PicoRobotics.KitronikPicoRobotics()

#Variabler
#Variabel til bevægelse af servo 2
val = 1

#Herinde er dit loop
while True:
    #Herinde skal du skrive din kode til at bevæge din motor
    #board.servoWrite(???, ???)