import hashlib

if __name__ == '__main__':
    # Hash functions
    print(hash('Hello world'))
    print(hash('Hello world'))
    print(type(hash('Hello world')))

    md5_1 = hashlib.md5()
    md5_1.update(b'Hello world')
    print(md5_1.hexdigest())

    md5_2 = hashlib.md5()
    md5_2.update(b'Hello world')
    print(md5_2.hexdigest())
