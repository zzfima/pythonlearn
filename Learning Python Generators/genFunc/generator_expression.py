if __name__ == '__main__':
    collection = ['a', 'b', 'c', 'd']

    # list comprehension
    col1 = [i.upper() for i in collection]
    print(col1)

    # generator expression
    col2 = (i.upper() for i in collection)
    print(col2)
    for i in col2:
        print(i)
