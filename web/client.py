from socket import *
def sen_info(info):
    address='127.0.0.1'   #服务器的ip地址
    port=12345           #服务器的端口号
    buffsize=4096        #接收数据的缓存大小
    s = socket(AF_INET, SOCK_STREAM)
    s.connect((address,port))
    s.send(info.encode())
    recvdata=s.recv(buffsize).decode('utf-8')
    s.close()
    return recvdata
