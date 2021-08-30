class Car:
    """Product"""

    def __init__(self):
        self._model = None
        self._tires = None
        self._engine = None

    def __str__(self):
        return '{} | {} | {}'.format(self._model, self._tires, self._engine)
