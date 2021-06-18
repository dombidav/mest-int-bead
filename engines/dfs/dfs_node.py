from abstract.node import Node
from models.operations import *


class DfsNode(Node):
    def __init__(self, value, parent):
        super(DfsNode, self).__init__(value, parent)

    def create_children(self):
        for possible_state in (generate_children(self.value)):
            yield DfsNode(possible_state, self)
