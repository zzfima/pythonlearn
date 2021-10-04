import this

if __name__ == '__main__':
    # ordered
    t1 = ('a', 1, 88.4, 2)
    print(t1)
    for i in t1:
        print(i)

    l1 = ['a', 1, 88.4, 2]
    print(l1)
    for i in l1:
        print(i)

    # unordered
    d1 = {'a': 1, 'b': 2}
    for i in d1:
        print(i)

    s1 = {'a', 1, 88.4, 2}
    print(s1)
    for i in s1:
        print(i)

    s2 = {'a', 2}
    print(f's1 - s2 = {s1 - s2}')
