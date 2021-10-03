class EmptyClass:
    pass


def god_init(ec: EmptyClass):
    ec.call_to_god = lambda msg: 'Please my lord, save ' + msg.upper()


if __name__ == '__main__':
    v = EmptyClass()
    god_init(v)

    print(v.call_to_god('Nasrallah'))
