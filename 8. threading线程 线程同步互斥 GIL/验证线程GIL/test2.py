from threading import Thread
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

count_ = []
t = time.time()
for x in range(10):
    th = Thread(target=count, args=(1,1))
    count_.append(th)
    th.start()

for i in count_:
    i.join()
print('thread cpu:', time.time()-t)
