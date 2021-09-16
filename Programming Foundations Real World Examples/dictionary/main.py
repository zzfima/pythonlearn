import hashlib


def caller_id(lookup_number):
    for k, v in rolodex.items():
        if lookup_number == v:
            return k


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

    print(hash("Bad Behaviour"))
    rolodex = {'Aaron': 5556069,
               'Bill': 5559824,
               'Dad': 5552603,
               'David': 5558331,
               'Dillon': 5553538,
               'Jim': 5555547,
               'Mom': 5552603,
               'Olivia': 5556397,
               'Verne': 5555309}
    print(rolodex['Bill'])
    rolodex['Amanda'] = 4354545
    print(rolodex['Amanda'])
    print(caller_id(5552603))
