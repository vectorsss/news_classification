from socket import *


def send_info(senddata):
    address='127.0.0.1'   #服务器的ip地址
    port=12345           #服务器的端口号
    buffsize=8192        #接收数据的缓存大小
    s = socket(AF_INET, SOCK_STREAM)
    s.connect((address,port))
    s.send(senddata.encode())
    recvdata=s.recv(buffsize).decode('utf-8')
    s.close()
    return recvdata
