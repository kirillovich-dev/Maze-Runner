def create_runner(x: int = 0, y: int = 0, orientation: str = "N"):
        return {
        "x": x,
        "y": y,
        "orientation": orientation
    }

def get_x(runner):
    return runner["x"]

def get_y(runner):
    return runner["y"]

def get_orientation(runner):
    return runner["orientation"]

def get_left_turn(orientation):
    if orientation == "N": return "W"
    if orientation == "W": return "S"
    if orientation == "S": return "E"
    if orientation == "E": return "N"

def get_right_turn(orientation):
    if orientation == "N": return "E"
    if orientation == "E": return "S"
    if orientation == "S": return "W"
    if orientation == "W": return "N"

def turn(runner, direction):
    if direction == "Left":
        new_orientation = get_left_turn(runner["orientation"])
    else:
        new_orientation = get_right_turn(runner["orientation"])
    return {
        "x": runner["x"],
        "y": runner["y"],
        "orientation": new_orientation
    }

def forward(runner):
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
