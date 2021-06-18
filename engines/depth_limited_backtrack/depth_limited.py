from typing import Optional

from abstract.engine import SolverEngine
from abstract.node import Node
from application.interaction import numeric_input
from engines.depth_limited_backtrack.limited_node import LimitedNode
from models.state import State


class DepthLimitedSolver(SolverEngine):
    """
    Depth-first search with depth limit and circle detection.
    """
    @property
    def name(self) -> str:
        return "Depth Limited Backtrack"

    def implementation(self) -> Optional[list[State]]:
        start_node = LimitedNode(self.start, None)
        self.path = [start_node.value]
        depth_limit = numeric_input('Depth limit:')
        recurse = self.recurse(start_node, depth_limit)
        return recurse or None

    def recurse(self, current_node: Node, depth_limit: int):
        if self.goal == current_node.value:
            return current_node.path

        if depth_limit <= 0:
            return None

        self.visited_queue.append(current_node)
        for result in (self.recurse(child, depth_limit - 1) for child in current_node.create_children() if child not in self.visited_queue):
            if result:
                return result
        return None
