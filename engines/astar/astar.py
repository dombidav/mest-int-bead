from queue import PriorityQueue
from typing import Optional

from abstract.engine import SolverEngine
from engines.astar.astar_node import AStarNode
from models.state import State, target_state


class AStarSolver(SolverEngine):

    @property
    def name(self):
        return 'A* Algorithm'

    def __init__(self, start, goal):
        super(AStarSolver, self).__init__(start, goal)
        self.priority_queue = PriorityQueue()  # The get command dequeues the *highest* priority element from the queue (Lowest cost in this case). Tried to implement a similar structure but that was about 15 times slower, then this lib

    def implementation(self) -> Optional[list[State]]:
        start_node = AStarNode(self.start, None, 0)
        child_id = 0
        self.priority_queue.put((0, child_id, start_node))
        while not self.path and self.priority_queue.qsize():
            closest_child: AStarNode = self.priority_queue.get()[2]
            closest_child.create_children()
            self.visited_queue.append(closest_child.value)
            for child in closest_child.children:
                if child.value not in self.visited_queue:
                    child_id += 1  # Not sure about this, probably so there are no duplicates?
                    if child.value == self.goal:
                        self.path = child.path
                        break
                    self.priority_queue.put((child.cost, child_id, child))
        if not self.path:
            return None
        return self.path
