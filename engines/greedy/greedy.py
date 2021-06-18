from typing import Optional

from abstract.engine import SolverEngine
from models.state import State


class GreedySolver(SolverEngine):
    @property
    def name(self):
        return 'Greedy Best First algorithm (Greedy search)'

    def __init__(self, start, goal):
        super(GreedySolver, self).__init__(start, goal)

    def implementation(self) -> Optional[list[State]]:
        pass
