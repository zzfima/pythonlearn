from bonzo import Bonzo
from dog import Dog


class DogFactory:
    """Concrete Factory"""

    def get_pet(self):
        return Dog("Hope")

    def get_food(self):
        return Bonzo()
