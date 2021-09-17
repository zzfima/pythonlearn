if __name__ == '__main__':
    collection = ['abc', 'bcd', 'cde', 'def']

    # list comprehension
    col1 = [i.upper() for i in collection]
    print(col1)

    # generator expression
    col2 = (i.upper() for i in collection)
    print(col2)
    for i in col2:
        print(i)

    col3 = (i for i in range(11) if i % 2 == 0)
    print(col3)
    for i in col3:
        print(i)

    int_coll = [1, 2, '6', 65, '76']
    col4 = (int(i) for i in int_coll)
    print(list(col4))

    col5 = (i[::-1] for i in (i.upper() for i in collection))
    print(list(col5))

    col5 = (i[::-1] for i in (i.upper() for i in collection))
    print(col5.__next__())
    print(col5.__next__())
    print(col5.__next__())
    print(col5.__next__())

    for i in (i for i in range(11) if i % 3 == 0):
        print(i)
