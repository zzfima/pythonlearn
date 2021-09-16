import hashlib

if __name__ == '__main__':
    # Hash functions
    print(hash('Hello world'))
    print(hash('Hello world'))
    print(type(hash('Hello world')))

    sha256_1 = hashlib.sha256()
    sha256_1.update(b'Hello world')
    print(sha256_1.hexdigest())

    sha256_2 = hashlib.sha256()
    sha256_2.update(b'Hello world')
    print(sha256_2.hexdigest())

    with open(r".\venv\Scripts\python.exe", "rb") as file:
        md5 = hashlib.md5()
        for chunk in iter(lambda: file.read(1024), b""):
            md5.update(chunk)
        print(
            f'{md5.hexdigest()} is same as d59663b8d5f110f55ec5507c8dfdcc82? ')
