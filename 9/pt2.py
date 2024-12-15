
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
            "contents": contents,
            "data_starts": 0
        }
        i += 1
    return filesystem

def move_blocks(filesystem: dict):
    for k in range(25):
        print("iteration " + str(k))
        move_blocks_right(filesystem)
    
    print_filesystem(filesystem)
    get_checksum(filesystem)
    return filesystem

def move_blocks_right(filesystem: dict):
    block_to_move_index = len(filesystem) - 1
    while block_to_move_index >= 0:
        we_move = True
        while len(filesystem[block_to_move_index]["contents"]) == 0:
            block_to_move_index -= 1
            if block_to_move_index < 0:
                we_move = False
                break
        
        if we_move:
            # inspect contents - multiple files in one block  
            unique_vals = set(filesystem[block_to_move_index]["contents"])
            
            for val in unique_vals:
                contents_to_move = [val for x in range(filesystem[block_to_move_index]["contents"].count(val))]

                empty_block_index = -1
                current_index = 0
                while current_index < block_to_move_index:
                    # if current index not full
                    empty_space_at_current = filesystem[current_index]["max_size"] - len(filesystem[current_index]["contents"])
                    if empty_space_at_current > 0:
                        if empty_space_at_current >= len(contents_to_move):
                            empty_block_index = current_index
                            break
                    current_index += 1
                
                if not empty_block_index == -1:
                    if not filesystem[empty_block_index]["data_starts"] == 0:
                        if filesystem[empty_block_index]["data_starts"] >= len(contents_to_move):
                            c = contents_to_move + filesystem[empty_block_index]["contents"]
                            filesystem[empty_block_index]["contents"] = c
                            filesystem[empty_block_index]["data_starts"] = 0
                        else:
                            filesystem[empty_block_index]["contents"] += contents_to_move
                    else:
                        filesystem[empty_block_index]["contents"] += contents_to_move

                    if (not filesystem[block_to_move_index]["contents"][0] == val) and (len(unique_vals) > 1):
                        for x in range(len(filesystem[block_to_move_index]["contents"])):
                            if not filesystem[block_to_move_index]["contents"][x] == val:
                                filesystem[block_to_move_index]["data_starts"] = x
                    
                    new_contents = []
                    for item in filesystem[block_to_move_index]["contents"]:
                        if not item == val:
                            new_contents.append(item)

                    filesystem[block_to_move_index]["contents"] = new_contents

        block_to_move_index -= 1


def print_filesystem(filesystem):
    for x in range(len(filesystem)):
        #print(str(x))
        print(filesystem[x])

def get_checksum(filesystem):
    i = 0
    checksum = 0
    for x in range(len(filesystem)):
        #for y in range(filesystem[x]["max_size"]):
        i += filesystem[x]["data_starts"]
        for item in filesystem[x]["contents"]:
            checksum += i * int(item)
            i += 1
        i += filesystem[x]["max_size"] - len(filesystem[x]["contents"]) + filesystem[x]["data_starts"]

    print(checksum)
            
#filesystem = load_filesystem("test1.txt")
filesystem = load_filesystem("input.txt")
filesystem = move_blocks(filesystem)