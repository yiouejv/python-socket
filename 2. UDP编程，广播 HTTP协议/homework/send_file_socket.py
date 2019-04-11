from socket import *
import time
sockfd = socket(AF_INET, SOCK_STREAM)
sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
sockfd.bind(('0.0.0.0', 10000))
sockfd.listen(5)
print('wait connect ...')
connfd, addr = sockfd.accept()
data = connfd.recv(1024).decode()
size = 1024 * 1024 * 5  # 每次读取的字节大小
bf = b''  # 实际读取的大小
i = 0  # 记录读取的次数
while True:
    with open('smoke.jpg', 'rb') as rf:
        rf.seek(size * i, 0)
        bf = rf.read(size)
        connfd.send(bf)  # 传输发送
        i += 1
        if len(bf) < size:  # 最后一次读取判断
            break
        time.sleep(0.2)

print('发送成功!')
connfd.close()
sockfd.close()
