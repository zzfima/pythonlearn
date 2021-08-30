from singleton import Singleton

if __name__ == '__main__':
    s1 = Singleton(f1="Lambda1")
    print(s1)
    s2 = Singleton(f2="Lambda2")
    print(s1)
    s3 = Singleton(f3="Lambda3")
    print(s1)
