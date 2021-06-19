from queue import PriorityQueue

from abstract.engine import SolverEngine
from engines.astar.astar_node import AStarNode


class AStarSolver(SolverEngine):

    @property
    def name(self):
        return 'A* Algorithm'

    def __init__(self, start, goal):
        super(AStarSolver, self).__init__(start, goal)
        self.open_nodes = PriorityQueue()  # The get command dequeues the *highest* priority element from the queue (Lowest cost in this case). Tried to implement a similar structure but that was about 15 times slower, then this lib

    def implementation(self):
        child_id = 0  # If there are two child with the same cost, we will dequeue the first one discovered
        self.open_nodes.put((0, child_id, AStarNode(self.start, None, 0)))
        while self.open_nodes.qsize():
            current_node = self.open_nodes.get()[2]  # [0] is the cost, [1] is the ID, [2] is the Node
            self.visited.append(current_node)
            for unvisited_child in (child for child in current_node.children() if child not in self.visited):
                if unvisited_child.value == self.goal:
                    return unvisited_child.path
                child_id += 1
                self.open_nodes.put((unvisited_child.cost, child_id, unvisited_child))
        return None
