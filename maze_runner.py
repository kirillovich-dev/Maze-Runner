import runner as runner_module
import maze as maze_module
from typing import Optional

def shortest_path(exploration: list[tuple[int, int, Optional[str]]]) -> list[tuple[int, int]]:
    """Find the shortest path by removing loops from the exploration."""
    path: list[tuple[int, int]] = []
    for x, y, _ in exploration:
        if (x,y) not in path:
            path.append((x, y))
        else:
            while path[-1] != (x, y):
                path.pop()
    return path
