from abstract.engine import SolverEngine
from application.interaction import numeric_input
from engines.depth_limited_backtrack.limited_node import LimitedNode


class DepthLimitedSolver(SolverEngine):
    """
    Depth-first search with depth limit and circle detection.
    """
    @property
    def name(self):
        return "Depth Limited Backtrack"

    def implementation(self):
        start_node = LimitedNode(self.start, None)
        self.path = [start_node.value]
        depth_limit = numeric_input('Depth limit:')
        recurse = self.recurse(start_node, depth_limit)
        return recurse or None

    def recurse(self, current_node, depth_limit):
        if self.goal == current_node.value:
            return current_node.path

        if depth_limit <= 0:
            return None

        self.visited.append(current_node)
        for result in (self.recurse(child, depth_limit - 1) for child in current_node.children() if child not in self.visited):
            if result:
                return result
        return None
