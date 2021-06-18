from __future__ import annotations

from abc import ABCMeta, abstractmethod
from typing import Optional

from models.state import State


class Node(metaclass=ABCMeta):
    def __init__(self, value: State, parent: Node = None):
        self.children: list[Node] = []
        self.parent = parent
        self.value = value
        self.cost: int = 0
        if parent:
            self.path = parent.path[:]
            self.path.append(value)
        else:
            self.path = [value]

    @abstractmethod
    def create_children(self):
        pass
