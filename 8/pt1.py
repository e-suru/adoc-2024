import itertools

empty_char = "."
antinode_char = "@"

def load_map(filepath: str):
    f = open(filepath, "r")
    map_dict = {} # STRICT - ROWS COLUMNS NOTATION
    node_chars = {}
    rows_index = 0
    for row in f.readlines():
        map_dict[rows_index] = {}
        row_to_process = row.strip()
        for col_index in range(len(row_to_process)):
            value = row_to_process[col_index]
            map_dict[rows_index][col_index] = value

            if not value == empty_char:
                if not value in node_chars:
                    node_chars[value] = [[rows_index, col_index]]
                else:
                    node_chars[value].append([rows_index, col_index])
        rows_index += 1
    return map_dict, node_chars

def find_antinodes(map_dict, node_chars):
    max_rows = len(map_dict)
    max_cols = len(map_dict[0])
    num_antinodes = 0
    for node_char_type in node_chars:
        node_coords = node_chars[node_char_type]
        node_duos = list(map(list, itertools.permutations(node_coords, 2)))
        
        for duo in node_duos:
            rows_diff = duo[1][0] - duo[0][0]
            cols_diff = duo[1][1] - duo[0][1]
            #antinode_1 = [duo[0][0] + rows_diff, duo[0][1] + cols_diff]
            antinode_2 = [duo[0][0] - rows_diff, duo[0][1] - cols_diff]

            #if check_antinode(antinode_1, map_dict, max_rows, max_cols):
            #    num_antinodes += 1
            #    map_dict[antinode_1[0]][antinode_1[1]] = antinode_char
            if check_antinode(antinode_2, map_dict, max_rows, max_cols):
                num_antinodes += 1
                map_dict[antinode_2[0]][antinode_2[1]] = antinode_char
    print(num_antinodes)
    display_map(map_dict)
    return map_dict

def check_antinode(antinode, map_dict, max_rows, max_cols):
    if antinode[0] >= 0 and antinode[0] < max_rows and antinode[1] >= 0 and antinode[1] < max_cols:
        ##if map_dict[antinode[0]][antinode[1]] == empty_char:
            if not map_dict[antinode[0]][antinode[1]] == antinode_char:
                return True
    return False

def display_map(map_dict):
    for row in map_dict:
        for col in map_dict[row]:
            print(map_dict[row][col],end="")
        print()

#map_dict, node_chars = load_map("test_1.txt")
map_dict, node_chars = load_map("input.txt")
find_antinodes(map_dict, node_chars)