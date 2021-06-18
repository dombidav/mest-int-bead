from __future__ import annotations

from abstract.node import Node
from models.operations import *


def g(node: AStarNode):
    """Cost to get here. I want to find the shortest possible solution"""
    return node.path_length


def h(node: AStarNode):
    """Heuristic on this node. In practice remaining time should be considered too, but this is good enough for underestimation, also pretty efficient."""
    return len(node.value.left_side)


class AStarNode(Node):
    def __init__(self, value, parent, path_length=0):
        super(AStarNode, self).__init__(value, parent)
        self.path_length = path_length
        self.cost = self.get_cost()

    def get_cost(self):
        return h(self) + g(self)

    def create_children(self):
        if not self.children:
            possibles = generate_children(self.value)
            for possible_state in possibles:
                child = AStarNode(possible_state, self, path_length=self.path_length+1)
                self.children.append(child)
