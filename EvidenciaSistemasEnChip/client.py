import socket

HEADER = 64
PORT = 3333
respuesta = ""
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!Disconnect"
SERVER = "10.25.104.34"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_lenght = len(message)
    send_lenght = str(msg_lenght).encode(FORMAT)
    send_lenght += b' ' * (HEADER - len(send_lenght))
    client.send(send_lenght)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

while respuesta != DISCONNECT_MESSAGE:
    #send("Hello World")
    respuesta = input()
    send(respuesta)