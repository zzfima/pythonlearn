import threading
import time

garlic_count = 0
lock = threading.Lock()


def shopper():
    global garlic_count
    start_time = time.time()
    for i in range(10):
        time.sleep(0.5)
        lock.acquire()
        print(threading.current_thread().getName())
        garlic_count += 1
        lock.release()
    finish_time = time.time()
    print(f'Thread {threading.current_thread().getName()} works {finish_time - start_time}')


if __name__ == '__main__':
    barron = threading.Thread(target=shopper, name='th1')
    olivia = threading.Thread(target=shopper, name='th2')
    barron.start()
    olivia.start()
    barron.join()
    olivia.join()
    print('We should buy', garlic_count, 'garlic.')
