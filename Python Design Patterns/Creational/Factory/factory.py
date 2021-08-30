from cat import Cat
from dog import Dog


def get_pet(pet="dog"):
    """Simple factory to create pets"""
    pets = dict()
    pets["dog"] = Dog("Hope")
    pets["cat"] = Cat("Peace")

    return pets[pet]
