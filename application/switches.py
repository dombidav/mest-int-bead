from abstract.engine import SolverEngine
from engines.astar.astar import AStarSolver
from engines.dfs.dfs import DepthFirstSolver
from engines.manual.manual import ManualSolver
from models.state import State, default_start, short_start, unsolvable_start, multi_solution_start


def engine(number: str) -> [SolverEngine, int, None]:
    if not number.isnumeric():
        return None
    switch = {
        0: 0,
        1: ManualSolver,
        2: DepthFirstSolver,
        4: AStarSolver
    }
    return switch.get(int(number))


def possible_starts(number: str) -> [State, int, None]:
    if not number.isnumeric():
        return None
    switch = {
        0: 0,
        1: 1,
        2: default_start(),
        3: short_start(),
        4: unsolvable_start(),
        5: multi_solution_start()
    }
    return switch.get(int(number))
