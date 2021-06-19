import re

from abstract.engine import SolverEngine
from application.interaction import clear_output
from models.operations import move_persons, is_valid
from models.person import find_person
from models.state import target_state


def ask_move(current_state):
    clear_output()
    print("""
    Move person(s) from one side to another, by sending their numbers. You can send multiple people by simply writing both numbers separated by a comma. No need to specify sides.
    Z - undo your last move
    Q - Exit
    ex: 
    Send only one person: `3`
    Send two people: `3, 2`
    """)
    while True:
        print('')
        print(f'Current state: {current_state} | remaining minutes: {current_state.remaining_minutes}')
        ans = input('Move:').strip(' ').replace(' ', '')
        while not re.search("^[0-9zq]+,?[0-9]*$", ans):
            ans = input('Unknown command. Move:').strip(' ').replace(' ', '')
        split = ans.split(',')
        if split[0].lower() == 'z':
            return None
        elif split[0].lower() == 'q':
            exit(0)
        if len(split) == 1:
            moving_persons = [find_person(split[0], current_state)]
        else:
            moving_persons = [find_person(split[0], current_state), find_person(split[1], current_state)]
        if not is_valid(current_state, moving_persons):
            print('Invalid move.')
            continue
        return move_persons(current_state, moving_persons)


class ManualSolver(SolverEngine):

    @property
    def name(self):
        return 'Manually solved'

    def __init__(self, start, goal):
        super(ManualSolver, self).__init__(start, goal)
        self.stack = [start]

    def implementation(self):
        while target_state(self.start) != self.stack[-1]:
            current_state = self.stack[-1]
            new_state = ask_move(current_state)
            if new_state is None:
                self.stack.pop()
            else:
                self.stack.append(new_state)
        return self.stack
