from abc import ABC, abstractmethod

import items as items


class Abstract(ABC):
    @abstractmethod
    def __init__(self, items, space):
        self.items = items
        self.space = space

    @abstractmethod
    def add(self, title, count):
        pass

    @abstractmethod
    def remove(self, title, count):
        pass

    @property
    @abstractmethod
    def get_free_space(self):
        pass

    @property
    @abstractmethod
    def items(self):
        pass

    @property
    @abstractmethod
    def get_unique_items_count(self, title):
        pass

    @items.setter
    def items(self, value):
        self._items = value
