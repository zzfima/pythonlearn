from cat_factory import CatFactory
from dog_factory import DogFactory
from pet_store import PetStore

if __name__ == '__main__':
    factory = DogFactory()
    ps1 = PetStore(factory)
    assert ps1.show() == "Woof! Beaf Meat"

    factory = CatFactory()
    ps2 = PetStore(factory)
    assert ps2.show() == "Meow! Fish Salmon"
