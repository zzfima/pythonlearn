class PetStore:
    def __init__(self, pet_factory=None):
        self._pet_factory = pet_factory

    def show(self):
        return self._pet_factory.get_pet().speak() + " " + self._pet_factory.get_food().taste()
