from models.person import Person


class State(object):
    def __init__(self, left_side, right_side=None, remaining_minutes=0,
                 lamp_on_left=True):
        super(State, self).__init__()

        self.left_side = left_side
        self.right_side = right_side or []
        self.remaining_minutes = remaining_minutes
        self.lamp_on_left = lamp_on_left

    def __eq__(self, other):
        return isinstance(other, State) and (self.left_side == other.left_side)

    def __str__(self):
        left_side = '[' + ', '.join(map(str, self.left_side)) + (', *' if self.lamp_on_left else '') + ']'
        right_side = '[' + ', '.join(map(str, self.right_side)) + ('' if self.lamp_on_left else ', *') + ']'
        return left_side + ' -- ' + right_side


def short_start():
    """
    This is an easy problem for debugging purposes
    :return with only three person and plenty of time
    """
    return State([Person(1), Person(2), Person(5)], remaining_minutes=11)


def unsolvable_start():
    """
    Unsolvable problem for debugging purposes
    :return: State with 5 person and not enough time
    """
    return State([Person(1), Person(2), Person(5), Person(8), Person(10)], remaining_minutes=11)


def target_state(starting_state):
    return State([], starting_state.left_side[:], 0, False)


def default_start():
    return State([Person(1), Person(2), Person(5), Person(10)], remaining_minutes=17)


def multi_solution_start():
    return State([Person(1), Person(2), Person(3), Person(4)], remaining_minutes=30)
