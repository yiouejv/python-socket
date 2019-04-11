from multiprocessing import Process
import os

def read_file(filename):
    '''读取文件， 返回读取到的字节流'''
    with open(filename, 'rb') as rf:
        byte_arr = rf.read()
    return byte_arr


def to_file(byte_arr, filename):
    '''字节流写入到文件
       参数： byte_arr  写入文件的字节数组
             filename  写入的文件名
    '''
    length = len(byte_arr)
    size = 1024*1024*5  # 每次读取5兆
    with open(filename, 'wb') as wf:
        while True:
            if length < size:
                wf.write(byte_arr[:length])
                break
            wf.write(byte_arr[:size])
            byte_arr = byte_arr[size:]
            length -= size
    print('ok')


def main():
    filename = 'smoke.jpg'
    size = os.path.getsize(filename)
    byte_arr = read_file(filename)
    byte_up = byte_arr[: size// 2]   # 取前一半  7//2=3  6//2=3
    byte_below = byte_arr[size//2 :]  # 取后一半
    p1 = Process(target=to_file, args=(byte_up, '上半部分.jpg'))
    p2 = Process(target=to_file, args=(byte_below, '下半部分.jpg'))
    p1.start()
    p2.start()
    p1.join()
    p2.join()


if __name__ == '__main__':
    main()

