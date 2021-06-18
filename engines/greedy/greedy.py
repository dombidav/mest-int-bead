from typing import Optional

from abstract.engine import SolverEngine
from engines.greedy.greedy_node import GreedyNode
from models.state import State


class GreedySolver(SolverEngine):
    @property
    def name(self):
        return 'Greedy BFS algorithm (Greedy search)'

    def __init__(self, start, goal):
        super(GreedySolver, self).__init__(start, goal)

    def implementation(self) -> Optional[list[State]]:
        start_node = GreedyNode(self.start, None)
        child_id = 0
        self.priority_queue.put((0, child_id, start_node))
        while not self.path and self.priority_queue.qsize():
            closest_child: GreedyNode = self.priority_queue.get()[2]
            self.visited_queue.append(closest_child)
            for child in (child for child in closest_child.create_children() if child not in self.visited_queue):
                child_id += 1
                if child.value == self.goal:
                    self.path = child.path
                    break
                self.priority_queue.put((child.cost, child_id, child))
        if not self.path:
            return None
        return self.path
