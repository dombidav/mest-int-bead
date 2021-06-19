from queue import PriorityQueue

from abstract.engine import SolverEngine
from engines.greedy.greedy_node import GreedyNode


class GreedySolver(SolverEngine):
    @property
    def name(self):
        return 'Greedy BFS algorithm (Greedy search)'

    def __init__(self, start, goal):
        super(GreedySolver, self).__init__(start, goal)
        self.open_nodes = PriorityQueue()

    def implementation(self):
        start_node = GreedyNode(self.start, None)
        child_id = 0
        self.open_nodes.put((0, child_id, start_node))
        while not self.path and self.open_nodes.qsize():
            closest_child = self.open_nodes.get()[2]
            self.visited.append(closest_child)
            for child in (child for child in closest_child.children() if child not in self.visited):
                if child.value == self.goal:
                    return child.path

                child_id += 1
                self.open_nodes.put((child.cost, child_id, child))
        return None
