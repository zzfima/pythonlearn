if __name__ == '__main__':
    stuff = ['a', 'b', 'c', 'd', 'e']
    for s in stuff:
        stuff.remove(s)
    print(stuff)

    stuff = ['a', 'b', 'c', 'd', 'e']
    for s in list(stuff):
        stuff.remove(s)
    print(stuff)
