from queue import PriorityQueue
from typing import Optional

from abstract.engine import SolverEngine
from engines.astar.astar_node import AStarNode
from models.state import State


class AStarSolver(SolverEngine):

    @property
    def name(self):
        return 'A* Algorithm'

    def __init__(self, start, goal):
        super(AStarSolver, self).__init__(start, goal)
        self.priority_queue = PriorityQueue()  # The get command dequeues the *highest* priority element from the queue (Lowest cost in this case). Tried to implement a similar structure but that was about 15 times slower, then this lib

    def implementation(self) -> Optional[list[State]]:
        child_id = 0
        self.priority_queue.put( (0, child_id, (AStarNode(self.start, None, 0))) )
        while self.priority_queue.qsize():
            closest_child: AStarNode = self.priority_queue.get()[2]  # Note: [0] is the cost, [1] is the ID, [2] ist the Node
            self.visited_queue.append(closest_child)
            for child in (child for child in closest_child.children() if child not in self.visited_queue):
                child_id += 1  # If there are two child with the same cost, we will dequeue the first one discovered
                if child.value == self.goal:
                    return child.path
                self.priority_queue.put((child.cost, child_id, child))
        return None
