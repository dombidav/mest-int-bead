from application.interaction import clear_output, confirm
from application.presentation import *

if __name__ == '__main__':
    while True:
        show_welcome()
        solver = ask_for_solver()
        clear_output()
        start = ask_for_start_state()
        target = ask_for_target_state(start)
        print_solution(solver(start, target))
        if not confirm('Solver is done. Rerun?'):
            exit(1)