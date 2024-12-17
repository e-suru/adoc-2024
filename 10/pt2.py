def get_map(filename):
    f = open(filename, "r")
    map = {(int(x),int(y)): int(c) for y, l in enumerate(f.readlines()) 
           for x, c in enumerate(l.strip())}
    return map

def get_unique_trails(map):
    sources = [xy for xy in map if map[xy] == 0]
    score = sum(len((find_trails(map, xy, []))) for xy in sources)
    print(score)
    return

directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
def find_trails(map, xy, trail):
    # recurive function to find trails dfs
    if map[xy] == 9:
        return [trail]
    else:
        trails = []
        for d in directions:
            new_xy = (xy[0] + d[0], xy[1] + d[1])
            if map.get(new_xy) == map.get(xy) + 1:
                trails += find_trails(map, new_xy, trail+[new_xy])
        return trails


#map = get_map("test1.txt")
map = get_map("input.txt")
get_unique_trails(map)