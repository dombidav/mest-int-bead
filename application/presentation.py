from application.interaction import choice
from application.manual_start import init_manual_start
from application.switches import *
from models.state import State, target_state


def ask_for_solver():
    print("""
    Please select solver engine:
        0 - Exit
        1 - Solve Manually
        2 - Solve with Depth first algorithm
        3 - Solve with Greedy best first
        4 - Solve with A* algorithm
    """)

    return choice(engine, unknown_message='Unknown solver:')


def print_solution(solution_list: list[State], solver: SolverEngine = None):
    if solution_list:
        print(f'Done with {solver.name} in {solver.execution_time * 1_000_000} μs')
        print('(Note: asterisk or * signals the position of the lamp)')
        print('------')
        print('Steps:')
        for i in range(len(solution_list) - 1):
            current_state: State = solution_list[i]
            next_state: State = solution_list[i + 1]
            diff: list[Person] = []
            if current_state.lamp_on_left:
                diff = [person for person in current_state.left_side if person not in next_state.left_side]
            else:
                diff = [person for person in current_state.right_side if person not in next_state.right_side]
            print(
                f'{i}: {current_state} -> move {" and ".join(map(str, diff))} to {"right" if current_state.lamp_on_left else "left"}')
        print('==================')
        print(solution_list[-1])
        print(f'{solution_list[-1].remaining_minutes} minutes remaining')
    else:
        print('No solution for problem')
