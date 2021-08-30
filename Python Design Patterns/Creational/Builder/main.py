from director import Director
from skylark_builder import SkylarkBuilder

if __name__ == '__main__':
    builder = SkylarkBuilder()
    director = Director(builder)
    director.construct_car()
    print(director.get_car())

