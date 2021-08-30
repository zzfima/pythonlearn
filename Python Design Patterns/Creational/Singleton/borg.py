class Borg:
    """Borg class making class attributes global"""

    # Attribute dictionary
    _shared_state = {}

    def __init__(self):
        """Make it an attribute dictionary"""
        self.__dict__ = self._shared_state
