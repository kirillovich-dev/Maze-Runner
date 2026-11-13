"""Module for creating and managing the maze structure."""

def create_maze(width: int = 5, height: int = 5) -> dict:
    """Create a new maze with the given dimensions.

    :param width: The width of the maze.
    :param height: The height of the maze.
    :return: A dictionary representing the newly created maze.
    """
    return {
        "width": width,
        "height": height,
        "horizontal_walls": [],
        "vertical_walls": []
    }


def add_horizontal_wall(maze: dict, x_coordinate: int, horizontal_line: int) -> dict:
    """Add a horizontal wall to the maze at the specified coordinates.

    :param maze: The maze to add the wall to.
    :param x_coordinate: The x-coordinate of the wall.
    :param horizontal_line: The horizontal line number of the wall.
    :return: A new maze dictionary with the horizontal wall added.
    """
    current_walls = list(maze["horizontal_walls"])
    current_walls.append((x_coordinate, horizontal_line))
    return{
        "width": maze["width"],
        "height": maze["height"],
        "horizontal_walls": current_walls,
        "vertical_walls": maze["vertical_walls"]
    }


def add_vertical_wall(maze: dict, y_coordinate: int, vertical_line: int) -> dict:
    """Add a vertical wall to the maze at the specified coordinates.

    :param maze: The maze to add the wall to.
    :param y_coordinate: The y-coordinate of the wall.
    :param vertical_line: The vertical line number of the wall.
    :return: A new maze dictionary with the vertical wall added.
    """
    current_walls = list(maze["vertical_walls"])
    current_walls.append((y_coordinate, vertical_line))
    return{
        "width": maze["width"],
        "height": maze["height"],
        "horizontal_walls": maze["horizontal_walls"],
        "vertical_walls": current_walls
    }


def get_dimensions(maze: dict) -> tuple[int, int]:
    """Get the width and height of the maze.

    :param maze: The maze to get dimensions for.
    :return: A tuple containing the width and height.
    """
    return (maze["width"], maze["height"])


def get_walls(maze: dict, x: int, y: int) -> tuple[bool, bool, bool, bool]:
    """Get the walls surrounding a specific coordinate in the maze.

    :param maze: The maze to check.
    :param x: The x-coordinate to check.
    :param y: The y-coordinate to check.
    :return: A tuple of booleans representing walls to the North, East, South, and West.
    """
    north = False
    east = False
    south = False
    west = False
    if x == 0:
        west = True
    if y == 0:
        south = True
    if x == maze["width"] - 1:
        east = True
    if y == maze["height"] - 1:
        north = True
    if (x, y + 1) in maze["horizontal_walls"]:
        north = True
    if (x, y) in maze["horizontal_walls"]:
        south = True
    if (y, x + 1) in maze["vertical_walls"]:
        east = True
    if (y, x) in maze["vertical_walls"]:
        west = True

    return (north, east, south, west)
