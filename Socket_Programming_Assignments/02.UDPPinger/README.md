# UDP Pinger Lab
**과제내용**
간단한 인터넷 ping 서버에 대해 공부하고 UDP를 사용하여 이에 대응하는 클라이언트를 프로그래밍 한다. 서버 코드는 다음과 같이 완성된 상태로 주어진다. 이에 대응하는 클라이언트를 작성하라.

## Server Code
```python
# UDPPingerServer.py
# We will need the following module to generate randomized lost packets
import random
from socket import *

# Create a UDP socket
# Notice the use of SOCK_DGRAM for UDP packets
serverSocket = socket(AF_INET, SOCK_DGRAM)
# Assign IP address and port number to socket
serverSocket.bind(('', 12000))

while True:
    # Generate random number in the range of 0 to 10
    rand = random.randint(0, 10)
    # Receive the client packet along with the address it is coming from
    message, address = serverSocket.recvfrom(1024)
    # Capitalize the message from the client
    message = message.upper()# If rand is less is than 4, we consider the packet lost and do not respond
    if rand < 4:
        continue
    # Otherwise, the server responds
    serverSocket.sendto(message, address)
```

서버 코드는 간단하다. UDP 소켓을 열고 무한 루프를 돌면서 클라이언트로 부터 받은 문자열을 대문자화하여 돌려준다. 단, 0~10 사이의 랜덤한 숫자를 하나 생성하는데 이 숫자가 4보다 작으면 loss가 발생한 것으로 가정하고 이때는 대문자화한 문자열을 반환하지 않는다.

## Client Code
클라이언트 프로그램은 다음과 같은 동작을 해야한다.
* 서버로 UDP ping message를 10개 보낸다.
* 서버로부터 응답이 오기를 1초동안 기다린다.
* 1초가 넘도록 응답이 없으면 loss가 발생했다고 판단하고 "Request timed out" 을 출력한다.
* 응답이 있으면 RTT를 계산하여 출력한다.

### Message Format
ping으로 보내는 message의 포맷은 다음과 같다.

**Ping *sequence_number* *time***

* ***sequence_number***는 1 부터 10까지 각 message의 연속적인 숫자이다.
* ***time***는 클라이언트가 message를 보낸 시간이다.


### 나의 결과
```bash
Request timed out
PING 2 2023-05-03 22:41:53.868917 RTT: 155ms
PING 3 2023-05-03 22:41:53.873435 RTT: 167ms
Request timed out
PING 5 2023-05-03 22:41:54.874705 RTT: 140ms
PING 6 2023-05-03 22:41:54.874901 RTT: 95ms
Request timed out
PING 8 2023-05-03 22:41:55.876219 RTT: 496ms
Request timed out
PING 10 2023-05-03 22:41:56.878262 RTT: 485ms
```