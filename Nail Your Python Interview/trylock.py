import threading
import time

lock = threading.Lock()


def f1():
    print('f1 starts')
    print(lock.acquire(blocking=False))
    f2()
    lock.release()
    print('f1 finished')


def f2():
    l = lock.acquire(blocking=False)
    print(l)
    if l:
        print('f2 starts')
        time.sleep(1)
        print('f2 finished')
        lock.release()
    else:
        print('not locked, out')


if __name__ == '__main__':
    th1 = threading.Thread(target=f1, name='th1')
    th1.start()
    th1.join()
