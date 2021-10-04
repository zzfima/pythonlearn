import threading
import time


class Olivia:
    def __del__(self):
        print('Olivia died.')

    def kitchen_cleaner(self):
        while True:
            print('Olivia cleaned the kitchen.')
            time.sleep(1)


if __name__ == '__main__':
    o = Olivia()
    olivia = threading.Thread(target=o.kitchen_cleaner)
    olivia.daemon = True
    olivia.start()

    print('Barron is cooking...')
    time.sleep(0.6)
    print('Barron is cooking...')
    time.sleep(0.6)
    print('Barron is cooking...')
    time.sleep(0.6)
    print('Barron is done!')
