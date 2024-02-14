import PicoRobotics
import utime
import machine

#Robotics setup
board = PicoRobotics.KitronikPicoRobotics()

#Variabler
#Variabel til bevægelse af servo 2
val = 1

while True:
    
    #Bevægelse af sensor 2
    
    #Samle op kode
    if(val == 1):
        board.servoWrite(2, 100)
        print("Samler op")
        utime.sleep(1)
        val = 2
    
    #Dreje til scanningspunkt kode
    if(val == 2):
        board.servoWrite(2, 42)
        print("Drejer til scanning")
        utime.sleep(1)
        val = 3
        
    #Aflevere den til rampen kode
    if(val == 3):
        board.servoWrite(2, 5)
        print("Aflevering")
        utime.sleep(1)
        val = 1
        
    
    

    
    
    


    
        
