#import socket module
from socket import *
import sys # In order to terminate the program
import os # In order to manipulate file

#Prepare a sever socket
serverSocket = socket(AF_INET, SOCK_STREAM)
serverPort = 6789
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

while True:
    #Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    message = connectionSocket.recv(1024).decode()
    filename = message.split()[1]

    try:
        f = open(filename[1:])
        outputdata = f.readlines();

        #Send one HTTP header line into socket
        connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())
        
        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.close()
        f.close()
    except IOError:
        #Send response message for file not found
        connectionSocket.send("HTTP/1.1 404 Bad Request\r\n\r\n".encode())

        #Close client socket
        connectionSocket.close()

    serverSocket.close()
    sys.exit()  #Terminate the program after sending the corresponding data