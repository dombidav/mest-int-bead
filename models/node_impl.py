from abstract.node import Node
from models.operations import *


class AStarNode(Node):
    def __init__(self, value, parent, start=0, goal=0):
        super(AStarNode, self).__init__(value, parent, start, goal)
        self.cost = self.get_cost()

    def get_cost(self):
        if self.value == self.goal:
            return 0
        return len(self.value.left_side)

    def create_children(self):
        if not self.children:
            possibles = generate_children(self.value)
            for possible_state in possibles:
                child = AStarNode(possible_state, self)
                self.children.append(child)
