import runner as runner_module
import maze as maze_module
import csv
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


def write_exploration_csv(exploration: list) -> None:
    """Write the exploration log to a CSV file."""
    with open("exploration.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Position", "x-coordinate", "y-coordinate", "Actions"])

        position = 1
        for x, y, action in exploration:
            if action is not None:
                action_str = action
            else:
                action_str = ""
            writer.writerow([position, x, y, action_str])
            position += 1


def write_statistics(filename: str, exploration: list, path: list) -> None:
    """Write the statistics of the run to a text file.
    :param filename: The name of the input maze file.
    :param exploration: The list of exploration tuples.
    :param path: The list of shortest path coordinates.
    """
    score = len(exploration) / 4 + len(path)

    with open("statistics.txt", "w") as file:
        file.write(f"{filename}\n")
        file.write(f"{score}\n")
        file.write(f"{len(exploration)}\n")
        file.write(f"{path}\n")
        file.write(f"{len(path)}\n")

test_exploration = [(0,0,"F"), (0,1,"F"), (0,2,"B"), (0,1,"LF"), (1,1,"LF"), (1,2,"RF"), (2,2,None)]
test_path = shortest_path(test_exploration)

write_statistics("test.mz", test_exploration, test_path)
write_exploration_csv(test_exploration)
