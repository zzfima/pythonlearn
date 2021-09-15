from car import Car


class ECar(Car):
    def __init__(self):
        self.charge = 3

    def drive(self):
        if self.charge > 0:
            self.charge -= 1
            print(f'The {self.color} {self.manufacturer} goes shhh!')
        else:
            print(f'The {self.color} {self.manufacturer} is out of charge')
