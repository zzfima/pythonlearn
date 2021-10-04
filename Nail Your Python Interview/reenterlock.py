import threading
import time

lock = threading.RLock()


def f1():
    print('f1 starts')
    lock.acquire()
    f2()
    lock.release()
    print('f1 finished')


def f2():
    lock.acquire()
    print('f2 starts')
    time.sleep(1)
    print('f2 finished')
    lock.release()


if __name__ == '__main__':
    th1 = threading.Thread(target=f1, name='th1')
    th1.start()
    th1.join()
