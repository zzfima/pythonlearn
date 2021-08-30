from cat_factory import CatFactory
from dog_factory import DogFactory
from pet_store import PetStore

if __name__ == '__main__':
    ps1 = PetStore(DogFactory)
    assert ps1.show() == "Woof! Beaf Meat"

    ps2 = PetStore(CatFactory)
    assert ps2.show() == "Meow! Fish Salmon"
