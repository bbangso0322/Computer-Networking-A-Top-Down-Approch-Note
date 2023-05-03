# UDPPingerClient.py

from socket import *
from datetime import datetime

# set server ip, port
serverName = 'localhost'
serverPort = 12000

# create socket and set timeout
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1)

for i in range(1,11):
    clientSocket.sendto(f"Ping {i} {datetime.now()}".encode(), (serverName, serverPort))
    try:
        recvMessage, serverAddress = clientSocket.recvfrom(1024)
        recvMessage = recvMessage.decode()
        rtt = (datetime.now() - datetime.strptime(recvMessage.split(' ')[3], "%H:%M:%S.%f")).microseconds
        print(f'{recvMessage} RTT: {rtt}ms')

    except timeout:
        print("Request timed out")

clientSocket.close()