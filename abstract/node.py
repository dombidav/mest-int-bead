from __future__ import annotations

from abc import ABCMeta, abstractmethod

from models.state import State


class Node(metaclass=ABCMeta):
    def __init__(self, value: State, parent: Node = None, start: State = None, goal: State = None):
        self.children: list[Node] = []
        self.parent = parent
        self.value = value
        self.cost: int = 0
        if parent:
            self.path = parent.path[:]
            self.path.append(value)
            self.start = parent.start
            self.goal = parent.goal
        else:
            self.path = [value]
            self.start = start
            self.goal = goal

    @abstractmethod
    def create_children(self):
        pass
