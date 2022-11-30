from abc import ABC, abstractmethod


class FieldABC(ABC):

    @abstractmethod
    def value(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass


class Field(FieldABC):
    def __init__(self, value: str):
        self._value = None
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    def __repr__(self):
        return f"{self.__class__.__name__}(value={self.value!r})"
