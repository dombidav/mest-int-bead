from abstract.engine import SolverEngine
from engines.astar import AStarSolver
from models.state import *
from models.operations import *
from models.state import State


def print_solution(solution_list: list[State], solver: SolverEngine = None):
    if solution_list:
        print(f'Done with {a.name} in {a.execution_time * 1_000_000} μs')
        print('(Note: asterisk or * signals the position of the lamp)')
        print('------')
        print('Steps:')
        for i in range(len(solution_list) - 1):
            current_state: State = solution_list[i]
            next_state: State = solution_list[i+1]
            diff: list[Person] = []
            if current_state.lamp_on_left:
                diff = [person for person in current_state.left_side if person not in next_state.left_side]
            else:
                diff = [person for person in current_state.right_side if person not in next_state.right_side]
            print(f'{i}: {current_state} -> move { " and ".join(map(str, diff)) } to { "right" if current_state.lamp_on_left else "left" }')
        print('==================')
        print(solution_list[-1])
        print(f'{solution_list[-1].remaining_minutes} minutes remaining')
    else:
        print('No solution for problem')


if __name__ == '__main__':
    print('Starting...')
    start = start_state()
    a = AStarSolver(start, target_state(start))
    solution = a.solve()
    print_solution(solution, a)
