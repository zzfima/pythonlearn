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

    with open(r"C:\Users\zzfim\Downloads\python-3.9.7-amd64.exe", "rb") as file:
        md5 = hashlib.md5()
        for chunk in iter(lambda: file.read(1024), b""):
            md5.update(chunk)
        print(md5.hexdigest())
