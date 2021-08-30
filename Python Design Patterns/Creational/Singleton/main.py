from singleton import Singleton

if __name__ == '__main__':
    s1 = Singleton(f1="Lambda1")
    s2 = Singleton(f2="Lambda2")
    s3 = Singleton(f3="Lambda3")

    print(Singleton())
