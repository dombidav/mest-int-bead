from abstract.node import Node
from models.operations import *


class LimitedNode(Node):
    def __init__(self, value, parent):
        super(LimitedNode, self).__init__(value, parent)

    def children(self):
        for possible_state in (generate_children(self.value)):
            yield LimitedNode(possible_state, self)
