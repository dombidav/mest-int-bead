from typing import Optional

from abstract.engine import SolverEngine
from engines.dfs.dfs_node import DfsNode
from models.state import State


class DepthFirstSolver(SolverEngine):

    def __init__(self, start: State, goal: State):
        super().__init__(start, goal)

    @property
    def name(self) -> str:
        return 'Depth First Search Algorithm'

    def implementation(self) -> Optional[list[State]]:
        start_node = DfsNode(self.start, None)
        stack: list[DfsNode] = [start_node]
        while stack:
            currentNode = stack.pop()

            if currentNode.value == self.goal:
                return currentNode.path

            self.visited_queue.append(currentNode)
            for child in (child for child in currentNode.create_children() if child not in self.visited_queue):
                stack.append(child)
        return None
