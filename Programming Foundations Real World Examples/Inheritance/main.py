import queue
from pprint import pprint

if __name__ == '__main__':
    my_tuple = ('a', 34, 'ff')
    print(my_tuple)

    my_list = ['a', 34, 'ff']
    print(my_list)

    print('\n Dif my_list  - my_tuple')
    pprint(list(set(dir(my_list)) - set(dir(my_tuple))))
    print('\n Dif my_tuple - my_list')
    pprint(list(set(dir(my_tuple)) - set(dir(my_list))))

    q = queue.Queue(3)
    q.put('a')
    q.put('ab')
    q.put('ac')
    print(q.get())
    print(q.get())

    try:
        print(q.get(block=False))
        print(q.get(block=False))
    except queue.Empty:
        print("An exception occurred because of empty queue try get object")
    print(f'Queue is empty: {q.empty()}')

    try:
        q.put('a', block=False)
        q.put('ab', block=False)
        q.put('ac', block=False)
        q.put('ad', block=False)
        q.put('ae', block=False)
    except queue.Full:
        print("An exception occurred because of full queue try add object")
