import threading

chopstick_a = threading.Lock()
chopstick_b = threading.Lock()
chopstick_c = threading.Lock()

sushi_amount = 500


def ef(first_chopstick, second_chopstick):
    global sushi_amount
    while sushi_amount > 0:
        first_chopstick.acquire()
        second_chopstick.acquire()

        if sushi_amount > 0:
            sushi_amount -= 1
            print(threading.currentThread().getName() + ', sushi remained: ' + str(sushi_amount))

        second_chopstick.release()
        first_chopstick.release()


if __name__ == '__main__':
    threading.Thread(target=ef, name='barron', args=(chopstick_a, chopstick_b)).start()
    threading.Thread(target=ef, name='olivia', args=(chopstick_b, chopstick_c)).start()
    threading.Thread(target=ef, name='steeve', args=(chopstick_c, chopstick_a)).start()
