"""Module for handling the runner's logic in the maze game."""

import maze as maze_module

from typing import Optional

def create_runner(x: int = 0, y: int = 0, orientation: str = "N") -> dict:
    """Create a new runner with default or specified properties.

    :param x: The starting x-coordinate.
    :param y: The starting y-coordinate.
    :param orientation: The starting orientation.
    :return: A dictionary representing the newly created runner.
    """
    return {
        "x": x,
        "y": y,
        "orientation": orientation
    }


def get_x(runner: dict) -> int:
    """Return the x-coordinate of the runner.

    :param runner: The runner to get the information from.
    :return: The x-coordinate of the runner.
    """
    return runner["x"]


def get_y(runner: dict) -> int:
    """Return the y-coordinate of the runner.

    :param runner: The runner to get the information from.
    :return: The y-coordinate of the runner.
    """
    return runner["y"]


def get_orientation(runner: dict) -> str:
    """Return the orientation of the runner.

    :param runner: The runner to get the information from.
    :return: The orientation of the runner.
    """
    return runner["orientation"]


def get_left_turn(orientation: str) -> str:
    """Calculate the new orientation after turning left.

    :param orientation: The current orientation.
    :return: The new orientation.
    """
    if orientation == "N": return "W"
    if orientation == "W": return "S"
    if orientation == "S": return "E"
    if orientation == "E": return "N"


def get_right_turn(orientation: str) -> str:
    """Calculate the new orientation after turning right.

    :param orientation: The current orientation.
    :return: The new orientation.
    """
    if orientation == "N": return "E"
    if orientation == "E": return "S"
    if orientation == "S": return "W"
    if orientation == "W": return "N"


def turn(runner: dict, direction: str) -> dict:
    """Turn the runner left or right and return the updated runner.

    :param runner: The runner to turn.
    :param direction: The direction to turn ("Left" or "Right").
    :return: The updated runner.
    """
    if direction == "Left":
        new_orientation = get_left_turn(runner["orientation"])
    else:
        new_orientation = get_right_turn(runner["orientation"])
    return {
        "x": runner["x"],
        "y": runner["y"],
        "orientation": new_orientation
    }


def forward(runner: dict) -> dict:
    """Move the runner forward one cell based on their orientation.

    :param runner: The runner to move.
    :return: The updated runner.
    """
    current_orientation = runner["orientation"]
    current_x = runner["x"]
    current_y = runner["y"]
    new_x = current_x
    new_y = current_y
    if current_orientation == "N":
        new_y = current_y + 1
    elif current_orientation == "S":
        new_y = current_y - 1
    elif current_orientation == "W":
        new_x = current_x - 1
    elif current_orientation == "E":
        new_x = current_x + 1
    return {
            "x": new_x,
            "y": new_y,
            "orientation": current_orientation
        }


def sense_walls(runner: dict, maze: dict) -> tuple[bool, bool, bool]:
    """Sense the walls to the left, front, and right of the runner.

    :param runner: The dictionary representing the runner.
    :param maze: The dictionary representing the maze.
    :return: A tuple of three booleans representing walls to the Left, Front, and Right.
    """
    walls = maze_module.get_walls(maze, runner["x"], runner["y"])
    current_orientation = runner["orientation"]
    if current_orientation == "N":
        left = walls[3]
        front = walls[0]
        right = walls[1]
    elif current_orientation == "E":
            left = walls[0]
            front = walls[1]
            right = walls[2]
    elif current_orientation == "S":
            left = walls[1]
            front = walls[2]
            right = walls[3]
    elif current_orientation == "W":
            left = walls[2]
            front = walls[3]
            right = walls[0]

    return (left, front, right)


def go_straight(runner: dict, maze: dict) -> dict:
     """Go straight, raising an error if a wall is in front."""
     wall_in_front = sense_walls(runner, maze)
     if wall_in_front[1]:
          raise ValueError("There is a wall in front!")

     return forward(runner)


def move(runner: dict, maze: dict) -> tuple[dict, str]:
    """Move the runner based on the left-hug algorithm.

    :param runner: The dictionary representing the runner.
    :param maze: The dictionary representing the maze.
    :return: A tuple containing the updated runner and the action string.
    """
    walls = sense_walls(runner, maze)
    left_wall = walls[0]
    front_wall = walls[1]
    right_wall = walls[2]

    if left_wall == False:
        runner = turn(runner, "Left")
        runner = forward(runner)
        return (runner, "LF")

    elif front_wall == False:
       runner = forward(runner)
       return (runner, "F")

    elif right_wall == False:
        runner = turn(runner, "Right")
        runner = forward(runner)
        return (runner, "RF")

    else:
       runner = turn(runner, "Left")
       runner = turn(runner, "Left")
       runner = forward(runner)
       return (runner, "B")


def explore(runner: dict, maze: dict, goal: Optional[tuple[int, int]] = None) -> list[tuple[int, int, Optional[str]]]:
    """Explore the maze until the runner reaches the goal.

    :param runner: The dictionary representing the runner.
    :param maze: The dictionary representing the maze.
    :param goal: The target coordinates as a tuple, or None for the top-right corner.
    :return: A list of tuples containing the x and y coordinates and the action string for each step.
    """
    if goal is None:
        goal = (maze["width"] - 1, maze["height"] - 1)
    history: list[tuple[int, int, Optional[str]]] = []
    while (runner["x"], runner["y"]) != goal:
        updated_runner, moves = move(runner, maze)
        history.append((runner["x"], runner["y"], moves))
        runner = updated_runner

    history.append((runner["x"], runner["y"], None))
    return history
