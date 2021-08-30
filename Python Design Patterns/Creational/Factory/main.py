from factory import get_pet

if __name__ == '__main__':
    d = get_pet("dog")
    assert d.speak() == "Woof!"

    c = get_pet("cat")
    assert c.speak() == "Meow!"
