#!/usr/bin/env python3

import socket
import Adafruit_DHT
import time

HOST = '192.168.1.190'  # The server's hostname or IP address
PORT = 1024        # The port used by the server
sensor = Adafruit_DHT.DHT22
pin = 4 
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    for i in range(1,12000):
        # Try to grab a sensor reading.  
        #Use the read_retry method which will retry up
        # to 15 times to get a sensor reading 
        #(waiting 2 seconds between each retry).
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
        msg = '{index} humidity {h} temperature \
                {t}'.format(index=i, h=humidity, t=temperature)
        a = msg.encode()
        s.send(bytes(a))
        data = s.recv(1024)
        time.sleep(2)

print('Received', repr(data))
