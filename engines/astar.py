from queue import PriorityQueue
from typing import Optional

from abstract.engine import SolverEngine
from models.astar_node import AStarNode
from models.state import State


class AStarSolver(SolverEngine):

    @property
    def name(self):
        return 'A* Algorithm'

    def __init__(self, start, goal):
        super(AStarSolver, self).__init__(start, goal)
        self.priority_queue = PriorityQueue()

    def implementation(self) -> Optional[list[State]]:
        start_state = AStarNode(self.start, None, self.start, self.goal)
        child_id = 0
        self.priority_queue.put((0, child_id, start_state))
        while not self.path and self.priority_queue.qsize():
            closest_child: AStarNode = self.priority_queue.get()[2]
            closest_child.create_children()
            self.visited_queue.append(closest_child.value)
            for child in closest_child.children:
                if child.value not in self.visited_queue:
                    child_id += 1  # Not sure about this, probably so there are no duplicates?
                    if not child.cost:
                        self.path = child.path
                        break
                    self.priority_queue.put((child.cost, child_id, child))
        if not self.path:
            return None
        return self.path
