import time
import network
import socket
import machine
import ustruct

class Sender:
    def __init__(self):
        self.ssid = 'OnePlus 6T'
        self.password = '12345678'

        self.UDP_IP = "192.168.158.168"
        self.UDP_PORT = 3001
        self.UDP_BUFF = 256

        self.wlan = network.WLAN(network.STA_IF)
        self.wlan.active(True)
        self.wlan.connect(self.ssid, self.password)

        # Wait for connect or fail
        self.max_wait = 10
        while self.max_wait > 0:
            if self.wlan.status() < 0 or self.wlan.status() >= 3:
                break
            self.max_wait -= 1
            print('waiting for connection...')
            time.sleep(1)

        # Handle connection error
        if self.wlan.status() != 3:
            raise RuntimeError('network connection failed')
        else:
            self.status = self.wlan.ifconfig()
            print( 'Connected to ' + self.ssid + '. ' + 'Device IP: ' + self.status[0] )    

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind((self.status[0], 3002))
    

    def Send(self, inp):
    
        msgSend = str(inp)
        self.sock.sendto(msgSend.encode(), (self.UDP_IP, self.UDP_PORT))
        
        

