from abc import ABC, abstractmethod


class BaseProduct(ABC):

    @abstractmethod
    def __add__(self, other):
        pass


class ProductOrder(ABC):

    @abstractmethod
    def __str__(self):
        pass
