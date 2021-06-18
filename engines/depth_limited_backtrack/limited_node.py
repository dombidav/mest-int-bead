from abstract.node import Node
from models.operations import *


class LimitedNode(Node):
    def __init__(self, value, parent):
        super(LimitedNode, self).__init__(value, parent)

    def create_children(self):
        if not self.children:
            possibles = generate_children(self.value)
            for possible_state in possibles:
                child = LimitedNode(possible_state, self)
                self.children.append(child)
