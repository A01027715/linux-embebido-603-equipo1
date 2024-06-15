import serial
import time
from utils import find_available_serial_ports
import socket

arduino = serial.Serial('COM7', 9600)


HEADER = 64
PORT = 3334
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!Disconnect"
SERVER = "172.23.208.1"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

while True:
    booleano = arduino.readline().decode(FORMAT).strip()
    if(booleano == "V"):
        send(booleano)
        print(booleano)
        #time.sleep(5)
        booleano = ""
        send(booleano)
    elif(booleano == "R"):
        send(booleano)
        print(booleano)
        #time.sleep(5)
        booleano = ""
        send(booleano)



arduino.close()
