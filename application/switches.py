from abstract.engine import SolverEngine
from engines.astar import AStarSolver
from models.state import State, default_start, short_start, unsolvable_start


def engine(number: str) -> [SolverEngine, int, None]:
    if not number.isnumeric():
        return None
    switch = {
        0: 0,
        # 1: ManualSolver
        4: AStarSolver
    }
    return switch.get(int(number))


def possible_targets(number: str) -> [State, int, None]:
    if not number.isnumeric():
        return None
    switch = {
        0: 0,
        1: 1,
        2: 2
    }
    return switch.get(int(number))


def possible_starts(number: str) -> [State, int, None]:
    if not number.isnumeric():
        return None
    switch = {
        0: 0,
        1: 1,
        3: default_start(),
        4: short_start(),
        5: unsolvable_start()
    }
    return switch.get(int(number))
