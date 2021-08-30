from car import Car


class Builder:
    """Abstract builder"""

    def __init__(self):
        self.car = None

    def create_new_car(self):
        self.car = Car()
