from socket import *

# 인자1 : 어드레스 필드
# AF_INET  : IPv4 ==> 보통 이것 사용
# AF_INET6 : IPv6

# 인자2 : 소켓 타입 (SOCK_STREAM:"연결지향형"과 SOCK_DGRAM:"비연결지향형"을 주로사용)

# << 연결지향형 >>
# 1. 중간에 데이터가 소멸되지 않고 목적지로 전송
# 2. 전송 순서대로 데이터가 수신
# 3. 전송되는 데이터의 경계가 존재하지 않음
# 4. 소켓대 소켓의 연결은 반드시 1:1이어야 함

# << 비연결지향형 >>
# 1. 전송된 순서에 상관없이 가장 빠른 전송을 지향한다.
# 2. 전송된 데이터는 손실의 우려가 있고 파손의 우려가 있다
# 3. 전송되는 데이터의 경계가 존재한다.
# 4. 한번에 전송할수 있는 데이터의 크기가 제한됨

# cf. 데이터를 세번에 나누어 보냈을때 세번에 나누어서 받아야되는 전송특성을 ==> 전송되는 데이터의 경계가 존재한다고 함!


serverSock = socket(AF_INET, SOCK_STREAM)
serverSock.bind(('', 8080))
serverSock.listen(1)


connectionSock, addr = serverSock.accept()

print(str(addr),'에서 접속이 확인되었습니다.')

data = connectionSock.recv(1024)
print('받은 데이터 : ', data.decode('utf-8'))

connectionSock.send('I am a server.'.encode('utf-8'))
print('메시지를 보냈습니다.')