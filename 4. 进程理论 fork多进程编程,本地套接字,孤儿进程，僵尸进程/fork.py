#encoding: utf-8
import os
from time import sleep

pid = os.fork()
if pid < 0:
    print('创建进程失败')
elif pid == 0:
    print('这是新的进程')
else:
    sleep(1)
    print('这是原有的进程')

print('##演示完毕')





