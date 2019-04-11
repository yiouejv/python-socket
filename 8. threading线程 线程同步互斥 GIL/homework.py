from signal import signal, SIGINT, SIGQUIT, SIGTSTP, SIGUSR1, SIGUSR2, \
                  SIG_IGN, pause, SIGKILL, SIGCHLD
import os
from multiprocessing import Lock, Process


pid = os.fork()


def father(sig, frame):  # 司机
    # print('father打印子进程pid', pid)
    if sig == SIGUSR1:
        print('老司机开车了')
    elif sig == SIGUSR2:
        print('车速有点快,系好安全带')
    elif sig == SIGTSTP:
        os.kill(pid, SIGUSR1)
    else:
        raise ValueError('sig未知错误')


def child(sig, frame):  # 售票员
    # print('child 打印 父进程pid', os.getppid())
    if sig == SIGINT:
        os.kill(os.getppid(), SIGUSR1)
    elif sig == SIGQUIT:
        os.kill(os.getppid(), SIGUSR2)
    elif sig == SIGUSR1:
        print('售票员: 到站了,下车')
        print('售票员下车')
        print('司机下车')
        os._exit(0)
    else:
        raise ValueError('sig未知错误')


if pid < 0:
    print('创建进程失败')
elif pid == 0:  # 子进程(售票员)
    print('售票员已准备')
    while True:
        signal(SIGQUIT, child)  # CTRL + \
        signal(SIGINT, child)  # Ctrl + C
        signal(SIGUSR1, child)
        # 子进程忽略父进程信号
        signal(SIGTSTP, SIG_IGN)  # CTRL + Z
        signal(SIGUSR2, SIG_IGN)
        # print('子进程打印父进程pid', os.getppid())
        pause()

else:  # 父进程(司机)
    print('汽车行驶...')
    while True:
        signal(SIGTSTP, father)  # CTRL + Z
        signal(SIGUSR1, father)
        signal(SIGUSR2, father)
        # 父进程忽略子进程信号
        signal(SIGQUIT, SIG_IGN)  # CTRL + \
        signal(SIGINT, SIG_IGN)
        # print('父进程打印子进程pid', pid)
        pause()
