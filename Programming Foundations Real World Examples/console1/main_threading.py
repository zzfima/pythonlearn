from threading import Thread
from time import sleep, time


def func_working(n):
    sleep(n)


if __name__ == '__main__':
    start_time = time()

    thread1 = Thread(target=func_working, args=(1,))
    thread2 = Thread(target=func_working, args=(1,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    end_time = time()

    print(end_time - start_time)
