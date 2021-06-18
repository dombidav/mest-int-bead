from abc import ABCMeta, abstractmethod
import time
from queue import PriorityQueue
from typing import Optional

from models.state import State


class SolverEngine(metaclass=ABCMeta):
    def __init__(self, start: State, goal: State):
        self.path: list[State] = []
        self.visited_queue: list[State] = []
        self.priority_queue = PriorityQueue()
        self.start: State = start
        self.goal: State = goal
        self.execution_time: float = 0

    def solve(self) -> Optional[list[State]]:
        start_time = time.time()
        result = self.implementation()
        self.execution_time = time.time() - start_time
        return result

    @abstractmethod
    def implementation(self) -> Optional[list[State]]:
        pass

    @property
    @abstractmethod
    def name(self) -> str:
        pass
