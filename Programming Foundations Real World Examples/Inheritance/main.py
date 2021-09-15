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
