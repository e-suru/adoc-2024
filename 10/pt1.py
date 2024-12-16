def read_map(filepath):
    f = open(filepath, "r")
    map = {}
    i = 0
    for line in f.readlines():
        map[i] = [int(x) for x in line.strip()] # ROWS COLS NOTATION ALWAYS
        i += 1
    print(map)
    return map

def bfs_for_trailheads(map:dict):
    sources = []
    score = 0
    for rows in range(len(map.keys())):
        for cols in range(len(map[rows])):
            if map[rows][cols] == 0:
                sources.append([rows, cols])
    for s in sources:
        score += run_bfs(map, s)
    print(score)

def run_bfs(map, s):
    score = 0
    visited = {}
    for r in range(len(map.keys())):
        for c in range(len(map[r])):
            visited[r,c] = False
    
    queue = [s]
    while queue:
        s = queue.pop(0)
        if map[s[0]][s[1]] == 9:
            score += 1
        # add valid adjacent vertices
        if s[0] > 0: # if not top row
            if map[s[0]-1][s[1]] == (map[s[0]][s[1]] + 1) and visited[s[0]-1,s[1]] == False:
                queue.append([s[0]-1,s[1]])
                visited[s[0]-1,s[1]] = True
        if s[0] < len(map.keys()) - 1: # if not bottom row
            if map[s[0]+1][s[1]] == (map[s[0]][s[1]] + 1) and visited[s[0]+1,s[1]] == False:
                queue.append([s[0]+1,s[1]])
                visited[s[0]+1,s[1]] = True
        if s[1] > 0: # if not left column
            if map[s[0]][s[1]-1] == (map[s[0]][s[1]] + 1) and visited[s[0],s[1]-1] == False:
                queue.append([s[0],s[1]-1])
                visited[s[0],s[1]-1] = True
        if s[1] < len(map[s[0]]) - 1: # if not right hand column
            if map[s[0]][s[1]+1] == (map[s[0]][s[1]] + 1) and visited[s[0],s[1]+1] == False:
                queue.append([s[0],s[1]+1])
                visited[s[0],s[1]+1] = True

    print(score)
    return score

map = read_map("input.txt")
#map = read_map("test1.txt")
bfs_for_trailheads(map)