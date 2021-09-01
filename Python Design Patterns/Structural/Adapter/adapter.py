class Adapter:
    """This changes the generic method name to individualized method names"""

    def __init__(self, obj, **adapted_method):
        """Change the name of the method"""
        self._object = obj

        # Add a new dictionary item that establishes the mapping between the generic method name:
        # speak() and the concrete method
        # For example, speak() will be translated to speak_korean() if the mapping says so
        self.__dict__.update(adapted_method)

    def __getattr__(self, attr):
        """Simply return the rest of attributes!"""
        return getattr(self._object, attr)
