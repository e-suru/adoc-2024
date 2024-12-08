import copy

guard_char = "^"
obstruction_char = "#"
hard_path_limit = 10000

def load_maze(filepath: str):
    f = open(filepath, "r")
    maze_obj = {}
    obstruction_dict = {}
    initial_loc = [0,0]
    row = 0
    for line in f.readlines():
        maze_obj[row] = {}
        obstruction_dict[row] = {}

        for col in range(len(line.strip())):
            if line[col] == guard_char:
                initial_loc = [row, col]
                maze_obj[row][col] = True
                obstruction_dict[row][col] = False
            elif line[col] == obstruction_char:
                obstruction_dict[row][col] = True
                maze_obj[row][col] = False
            else:
                obstruction_dict[row][col] = False
                maze_obj[row][col] = False
            col += 1
        row += 1
    
    return maze_obj, obstruction_dict, initial_loc

def does_path_loop(maze_obj: dict, obstruction_dict: dict, current_loc: list):
    maze_width = len(maze_obj[0].keys())
    maze_height = len(maze_obj.keys())
    direction = 0 # DIRECTION 0 = UP
                    # DIRECTION 1 = RIGHT
                    # DIRECTION 2 = DOWN
                    # DIRECTION 3 = LEFT
    current_path = 0

    while (current_loc[0] < maze_height) and (current_loc[0] > 0) and (current_loc[1] < maze_width) and (current_loc[1] > 0):
        new_loc = current_loc.copy()
        # while not at the edge of the maze, inspect new location
        if direction == 0:
            new_loc[0] -= 1
        elif direction == 1:
            new_loc[1] += 1
        elif direction == 2:
            new_loc[0] += 1
        else:
            new_loc[1] -= 1

        if not (new_loc[0] < maze_height) or not (new_loc[0] >= 0) or not (new_loc[1] < maze_width) or not (new_loc[1] >= 0):
            break

        if obstruction_dict[new_loc[0]][new_loc[1]] == True:
            direction = (direction + 1) % 4
        else:
            current_loc = new_loc.copy() ## Q - don't need to copy here??
            current_path += 1
            if current_path > hard_path_limit:
                return True

            maze_obj[current_loc[0]][current_loc[1]] = True

    #display_maze(maze_obj, obs_dict, current_loc)
    return False

def are_paths_the_same(last_path, current_path):
    if len(last_path) > 3 and (len(last_path) == len(current_path)):
        for i in range(len(last_path)):
            if not last_path[i] == current_path[i]: # NOT CORRECT - CAN BE SAME PATH BUT OFFSET. NEED TO USE DICT
                return False
        return True
    else:
        return False

def display_maze(maze_obj, obs_dict, current_loc):
    for rows_index in range(len(maze_obj)):
        for cols_index in range(len(maze_obj[rows_index])):
            if current_loc[0] == rows_index and current_loc[1] == cols_index:
                print(guard_char, end='')
            elif obs_dict[rows_index][cols_index] == True:
                print(obstruction_char, end='')
            elif maze_obj[rows_index][cols_index] == True:
                print("X", end='')
            else:
                print(".", end='')
        print()

def test_paths(maze_obj: dict, obs_dict: dict, initial_loc: list):
    invalid_maps = 0
    for i in range(len(maze_obj)):
        for j in range(len(maze_obj[i])):
            if obs_dict[i][j] == True or maze_obj[i][j] == guard_char:
                j += 1
            else: 
                new_obs = copy.deepcopy(obs_dict)
                new_obs[i][j] = True
                if (does_path_loop(maze_obj, new_obs, initial_loc)):
                    invalid_maps += 1
    print(invalid_maps)

#f = open("test_1.txt", "r")
#f = open("input.txt", "r")
#maze_obj, obs_dict, initial_loc = load_maze("test_1.txt")
maze_obj, obs_dict, initial_loc = load_maze("input.txt")
test_paths(maze_obj, obs_dict, initial_loc)