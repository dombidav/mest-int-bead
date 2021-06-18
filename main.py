from application.interaction import clear_output, confirm
from application.presentation import *

if __name__ == '__main__':
    while True:
        show_welcome()
        start = ask_for_start_state()
        target = target_state(start)
        solver = ask_for_solver()
        clear_output()
        solver_instance = solver(start, target)
        print_solution(solver_instance.solve(), solver_instance)
        if not confirm('Solver is done. Rerun?'):
            exit(1)
