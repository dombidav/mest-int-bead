from application.presentation import print_solution
from engines.astar import AStarSolver
from models.state import *

if __name__ == '__main__':
    print('Starting...')
    start = start_state()
    a = AStarSolver(start, target_state(start))
    solution = a.solve()
    print_solution(solution, a)
