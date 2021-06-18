from typing import Optional

from abstract.engine import SolverEngine
from engines.dfs.dfs_node import DfsNode
from models.state import State, target_state


class DepthFirstSolver(SolverEngine):

    def __init__(self, start: State, goal: State):
        super().__init__(start, goal)

    @property
    def name(self) -> str:
        return 'Depth First Search Algorithm'

    def implementation(self) -> Optional[list[State]]:
        start_node = DfsNode(self.start, None)
        stack: list[DfsNode] = [start_node]
        visited = set()
        while stack:
            currentNode = stack.pop()
            if currentNode not in visited:
                if currentNode.value == self.goal:
                    return currentNode.path
                visited.add(currentNode)
                child: DfsNode
                currentNode.create_children()
                for child in currentNode.children:
                    stack.append(child)
        return None
