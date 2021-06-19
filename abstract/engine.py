import time
from abc import ABCMeta, abstractmethod
from queue import PriorityQueue
from typing import Optional

from abstract.node import Node
from models.state import State


class SolverEngine(metaclass=ABCMeta):
    def __init__(self, start: State, goal: State):
        self.path: list[State] = []
        self.visited: list[Node] = []
        self.start: State = start
        self.goal: State = goal
        self.execution_time: float = 0

    def solve(self) -> Optional[list[State]]:
        start_time = time.time()
        self.path = self.implementation()
        self.execution_time = time.time() - start_time
        return self.path

    @abstractmethod
    def implementation(self) -> Optional[list[State]]:
        pass

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    def discovered(self, child: Node) -> Optional[Node]:
        for node in self.visited:
            if node.value == child.value:
                return child
        return None
