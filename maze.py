def create_maze(width=5, height=5):
    return {
        "width": width,
        "height": height,
        "horizontal_walls": [],
        "vertical_walls": []
    }

def add_horizontal_wall(maze, x_coordinate, horizontal_line):
    current_walls = list(maze["horizontal_walls"])
    current_walls.append((x_coordinate, horizontal_line))
    return{
        "width": maze["width"],
        "height": maze["height"],
        "horizontal_walls": current_walls,
        "vertical_walls": maze["vertical_walls"]
    }

def add_vertical_wall(maze, y_coordinate, vertical_line):
    current_walls = list(maze["vertical_walls"])
    current_walls.append((y_coordinate, vertical_line))
    return{
        "width": maze["width"],
        "height": maze["height"],
        "horizontal_walls": maze["horizontal_walls"],
        "vertical_walls": current_walls
    }

def get_dimensions(maze):
    return (maze["width"], maze["height"])

def get_walls(maze, x, y):
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
