from models.person import Person
from models.state import State


def is_valid(state: State, moving_persons: list[Person]) -> bool:
    if max(person.minutes for person in moving_persons) > state.remaining_minutes:
        return False

    if len(moving_persons) not in [1, 2]:
        return False
    left_side = state.left_side.__contains__(moving_persons[0])

    if left_side != state.lamp_on_left:
        return False

    if len(moving_persons) == 2:
        if left_side:
            if not state.left_side.__contains__(moving_persons[1]):
                return False
        elif not state.right_side.__contains__(moving_persons[1]):
            return False
    return True


def clone_state(state: State) -> State:
    return State(state.left_side[:], state.right_side[:], state.remaining_minutes, state.lamp_on_left)


def move_persons(state: State, moving_persons: list[Person]) -> (State, int):
    new_state = clone_state(state)
    max_time: int = 0
    for person in moving_persons:
        if person.minutes > max_time:
            max_time = person.minutes
        if new_state.lamp_on_left:
            new_state.right_side.append(person)
            new_state.left_side.remove(person)
        else:
            new_state.left_side.append(person)
            new_state.right_side.remove(person)
    new_state.remaining_minutes -= max_time
    new_state.lamp_on_left = not new_state.lamp_on_left
    return new_state


def generate_children(state: State) -> list[State]:
    result = []
    side = state.left_side if state.lamp_on_left else state.right_side
    for i in range(len(side)):
        if is_valid(state, [side[i]]):
            result.append(move_persons(state, [side[i]]))
        for j in range(i + 1, len(side)):
            if is_valid(state, [side[i], side[j]]):
                result.append(move_persons(state, [side[i], side[j]]))
    return result
