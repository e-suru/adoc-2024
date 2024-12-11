
def load_filesystem(filepath):
    """
    Inputs filepath to input.txt
    Outputs an object representing the whole filesystem as initially read from the file

    {
        block_id: {
            empty: bool
            file_id: int (-1 = empty)
            max_size: int
            contents: List[string]
        },
    }
    """
    f = open(filepath, "r")
    filesystem = {}
    file_string = f.read().strip()
    i = 0
    for block in file_string:
        is_empty = (i % 2 == 1)
        file_id = -1
        contents = []
        if not is_empty:
            file_id = i // 2
            contents = [int(file_id) for x in range(int(block))]
        filesystem[i] = {
            "empty": is_empty,
            "file_id": file_id,
            "max_size": int(block),
            "contents": contents
        }
        i += 1
    return filesystem

def move_blocks(filesystem: dict):
    files_moved = True
    while files_moved:
        files_moved = False
        empty_blocks = get_empty_blocks(filesystem)
        block_to_move_index = len(filesystem) - 1

        while block_to_move_index >= 0:
            block_to_move = filesystem[block_to_move_index]
            max_empty_block_size = max(filesystem.keys())
            if (block_to_move["empty"] or len(block_to_move["contents"])>max_empty_block_size):
                block_to_move_index -= 1
                if (not block_to_move_index >= 0):
                    break
                continue
            if (len(empty_blocks) == 0):
                break
            
            move_the_files = True
            size_block = len(block_to_move["contents"])
            excess = 0
            while not size_block in empty_blocks:
                size_block += 1
                excess += 1
                if size_block > max_empty_block_size:
                    move_the_files = False
                    break
            
            if move_the_files:
                new_location = empty_blocks[size_block].pop(0)
                if empty_blocks[size_block] == []:
                    empty_blocks.pop(size_block)
                
                new_contents = [block_to_move["file_id"] for i in range(len(block_to_move["contents"]))] + [int("-1") for j in range(excess)]
                filesystem[new_location]["contents"] = new_contents
                filesystem[new_location]["empty"] = False

                filesystem[block_to_move_index]["contents"] = []
                filesystem[block_to_move_index]["empty"] = True
                files_moved = True
            block_to_move_index -= 1
        print_filesystem(filesystem)
    get_checksum(filesystem)
        

        
    print_filesystem(filesystem)
    return filesystem

def get_empty_blocks(filesystem):
    empty_blocks = {}
    for i in range(len(filesystem)):
        if filesystem[i]["empty"] and (not len(filesystem[i]["contents"]) == filesystem[i]["max_size"]):
            block_max_size = filesystem[i]["max_size"]
            if block_max_size in empty_blocks:
                empty_blocks[block_max_size].append(i)
            else:
                empty_blocks[block_max_size] = [i]
    return empty_blocks

def print_filesystem(filesystem):
    for x in range(len(filesystem)):
        print(str(x))
        print(filesystem[x])

def get_checksum(filesystem):
    i = 0
    checksum = 0
    for x in range(len(filesystem)):
        for item in filesystem[x]["contents"]:
            if not int(item) == -1:
                checksum += i * int(item)
            i += 1
    print(checksum)
            
filesystem = load_filesystem("test1.txt")
#filesystem = load_filesystem("input.txt")
filesystem = move_blocks(filesystem)
get_checksum(filesystem)