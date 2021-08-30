from cat import Cat
from whiskas import Whiskas


class CatFactory:
    """Concrete Factory"""

    def get_pet(self):
        return Cat("Hope")

    def get_food(self):
        return Whiskas()
