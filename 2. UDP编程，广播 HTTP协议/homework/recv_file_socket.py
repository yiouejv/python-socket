from socket import *
sockfd = socket(AF_INET, SOCK_STREAM)
sockfd.connect(('127.0.0.1', 10000))
sockfd.send('请求下载！'.encode())
count = 0  # 统计写入的次数
with open('smoke2.jpg', 'ab') as af:
    while True:
        try:
            data = sockfd.recv(1024)
            if data == b'':
                break
            print('写入', data)
            af.write(data)
            count += 1
            print('写入%s次'  % count)
        except:
            print('异常发生')
            break

print('ok')
sockfd.close()