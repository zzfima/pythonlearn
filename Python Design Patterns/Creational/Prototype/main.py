from car import Car
from prototype import Prototype

if __name__ == '__main__':
    p = Prototype()
    p.register_object("v1", Car())
    p.register_object("v2", Car())
    co = p.clone("v2")
    print(co)
