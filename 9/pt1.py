
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

def move_blocks(filesystem):
    filesystem_size = len(filesystem) - 1
    block_to_move_index = filesystem_size # start with last block and move towards front until no more free space
    empty_block_index = 0 # start from front and move towards back until all files placed
    while True:
        if (block_to_move_index == empty_block_index or empty_block_index > filesystem_size or block_to_move_index < 0):
            break
        block_to_move = filesystem[block_to_move_index]
        empty_block = filesystem[empty_block_index]

        if (block_to_move["empty"] == True) or (block_to_move["contents"] == []):
            block_to_move_index -= 1
            continue

        for x in range(len(block_to_move["contents"])):
            while (empty_block["empty"] == False) or (len(empty_block["contents"]) == empty_block["max_size"]):
                empty_block_index += 1
                if empty_block_index == block_to_move_index or empty_block_index > filesystem_size or block_to_move_index < 0:
                    break
                empty_block = filesystem[empty_block_index]
            empty_block["contents"].append(block_to_move["file_id"])
            block_to_move["contents"].pop()
        
    print_filesystem(filesystem)
    return filesystem

def print_filesystem(filesystem):
    for x in range(len(filesystem)):
        print(str(x))
        print(filesystem[x])

def get_checksum(filesystem):
    i = 0
    checksum = 0
    for x in range(len(filesystem)):
        for item in filesystem[x]["contents"]:
            checksum += i * int(item)
            i += 1
    print(checksum)
            
#filesystem = load_filesystem("test1.txt")
filesystem = load_filesystem("input.txt")
filesystem = move_blocks(filesystem)
get_checksum(filesystem)