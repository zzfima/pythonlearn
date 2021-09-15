class Vehicle:
    def __init__(self, color, manufacturer):
        self.color = color
        self.manufacturer = manufacturer
        self.gas = 4

    def drive(self):
        if self.gas > 0:
            self.gas -= 1
            print(f'The {self.color} {self.manufacturer} goes VROOM!')
        else:
            print(f'The {self.color} {self.manufacturer} is out of gas')
