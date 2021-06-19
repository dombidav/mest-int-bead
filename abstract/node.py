from abc import ABCMeta, abstractmethod


class Node(metaclass=ABCMeta):
    def __init__(self, value, parent=None):
        self.parent = parent
        self.value = value
        self.cost = 0
        if parent:
            self.path = parent.path[:]
            self.path.append(value)
        else:
            self.path = [value]

    @abstractmethod
    def children(self):
        pass
