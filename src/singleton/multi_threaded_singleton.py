from __future__ import annotations
import threading


class SingletonMeta(type):
    """
    A thread-safe implementation of Singleton.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            with cls._lock:
                if cls not in cls._instances:
                    instance = super().__call__(*args, **kwargs)
                    cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    """
    A base class for Singleton classes.
    """

    _lock = threading.Lock()

    def __init__(self):
        if hasattr(self, "_initialized"):
            raise Exception("This class is a singleton!")
        self._initialized = True
        # Initialize your singleton instance here
