from __future__ import annotations

from abstract.node import Node
from models.operations import *


class GreedyNode(Node):
    def __init__(self, value, parent):
        super(GreedyNode, self).__init__(value, parent)
        self.cost = self.get_cost()

    def get_cost(self):  # h()
        return len(self.value.left_side)

    def create_children(self):
        if not self.children:
            possibles = generate_children(self.value)
            for possible_state in possibles:
                child = GreedyNode(possible_state, self)
                self.children.append(child)
