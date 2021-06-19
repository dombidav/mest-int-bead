from abstract.node import Node
from models.operations import *


class GreedyNode(Node):
    def __init__(self, value, parent):
        super(GreedyNode, self).__init__(value, parent)
        self.cost = self.get_cost()

    def get_cost(self):  # h() function
        return len(self.value.left_side)

    def children(self):
        for possible_state in (generate_children(self.value)):
            yield GreedyNode(possible_state, self)
