# From: https://medium.com/better-programming/singleton-in-python-5eaa66618e3d

class Singleton:

    def __init__(self, cls):
        """
        Instantiates Singleton object and sets internal class state.
        :param cls: Class to be used in the Singleton 
        """
        self._cls = cls

    def Instance(self):
        """
        Returns the Singleton's object.
        """
        try:
            return self._instance
        except AttributeError:
            self._instance = self._cls()
            return self._instance

    def __call__(self):
        """
        Provides an error if the class is called directly.
        """
        raise TypeError('Singletons must be accessed through `Instance()`.')

    def __instancecheck__(self, inst):
        """
        Checks if an instance as an instance of the current internal class. 
        """
        return isinstance(inst, self._cls)