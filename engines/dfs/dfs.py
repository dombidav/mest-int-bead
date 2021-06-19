from abstract.engine import SolverEngine
from engines.dfs.dfs_node import DfsNode


class DepthFirstSolver(SolverEngine):

    def __init__(self, start, goal):
        super().__init__(start, goal)

    @property
    def name(self):
        return 'Depth First Search Algorithm'

    def implementation(self):
        start_node = DfsNode(self.start, None)
        stack = [start_node]
        while stack:
            currentNode = stack.pop()

            if currentNode.value == self.goal:
                return currentNode.path

            self.visited.append(currentNode)
            for child in (child for child in currentNode.children() if child not in self.visited):
                stack.append(child)
        return None
