import time
from abc import ABCMeta, abstractmethod


class SolverEngine(metaclass=ABCMeta):
    def __init__(self, start, goal):
        self.path = []
        self.visited = []
        self.start = start
        self.goal = goal
        self.execution_time = 0

    def solve(self):
        start_time = time.time()
        self.path = self.implementation()
        self.execution_time = time.time() - start_time
        return self.path

    @abstractmethod
    def implementation(self):
        pass

    @property
    @abstractmethod
    def name(self):
        pass

    def discovered(self, child):
        for node in self.visited:
            if node.value == child.value:
                return child
        return None
