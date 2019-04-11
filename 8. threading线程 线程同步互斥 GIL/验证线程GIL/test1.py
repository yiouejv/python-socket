from Tedu.python第二阶段.网络编程 import *
import time

# 计算密集型
def count(x, y):
    c = 0
    while c < 6000000:
        c += 1
        x += 1
        y += 1


# IO密集型函数
def write():
    with open('test.txt', 'w') as f:
        for i in range(1000000):
            f.write('hello world\n')


def read():
    with open('test.txt', 'r') as f:
        lines = f.readlines()


t = time.time()
# for i in range(10):
#     count(1, 1)

for i in range(10):
    write()
    read()

print('Line cpu', time.time()-t)