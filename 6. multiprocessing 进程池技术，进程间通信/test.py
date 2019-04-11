from multiprocessing import Pipe, Queue, Process
import time

# fd1, fd2 = Pipe()
q = Queue()

def fun1():
    # fd1.send('hahha,我是进程1')
    q.put(1)
    q.put(2)
    q.put(3)


def fun2():
    # print(fd2.recv())
    print(q.get())


p1 = Process(target=fun1)
p2 = Process(target=fun2)
p1.start()
p2.start()
p1.join()
p2.join()



