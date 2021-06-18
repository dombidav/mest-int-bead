from abstract.node import Node
from models.operations import *


class DfsNode(Node):
    def __init__(self, value, parent):
        super(DfsNode, self).__init__(value, parent)

    def create_children(self):
        if not self.children:
            possibles = generate_children(self.value)
            for possible_state in possibles:
                child = DfsNode(possible_state, self)
                self.children.append(child)
