# Press the green button in the gutter to run the script.
from factory import get_pet

if __name__ == '__main__':
    p = get_pet("dog")
    assert p.speak() == "Woof!"

    c = get_pet("cat")
    assert c.speak() == "Meow!"
