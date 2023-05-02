# 01. Webserver

**과제내용**

다음과 같은 skeleton 코드가 주어진다. 
1. 웹 브라우저를 통해 `http://<my-ip-address>:6789/HelloWorld.html`를 입력하여 HTTP 요청을 보내면 이에 대하여 `HelloWorld.html` 파일을 리턴하는 응답 서버를 만들어라
2. 파일이 없으면 **404 Not Found** 메시지를 리턴하라.

```python
#import socket module
from socket import *
import sys # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket
#Fill in start
#Fill in end
while True:
    #Establish the connection
    print('Ready to serve...')
    connectionSocket, addr =
    #Fill in start
    #Fill in end
    try:
        message =
        #Fill in start
        #Fill in end
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = #Fill in start
        #Fill in end
        #Send one HTTP header line into socket
        #Fill in start
        #Fill in end
        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
    except IOError:
        #Send response message for file not found
        #Fill in start#Fill in end
        #Close client socket
        #Fill in start
        #Fill in end
serverSocket.close()
sys.exit()  #Terminate the program after sending the corresponding data
```

