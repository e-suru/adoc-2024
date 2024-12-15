f = open("test1.txt", "r")
all_original = f.read().split('')
all_reformat = ""
for i in range(all_original):
    new_string = ""
    if i % 2 == 1: # odd = empty
        for x in range(all_original[i]):
            new_string += '-1'
    else:
        for x in range(all_original[i]):
            new_string += all_original[i]
    all_reformat += new_string

for k in range(20):
    to_move_index_s = len(all_reformat) - 1
    to_move_index_e = len(all_reformat) - 1
    
    while to_move_index_s > -1:
        file_found = True
        while all_reformat[to_move_index_s] == -1:
            to_move_index_s -= 1
            if to_move_index_s < 0:
                file_found = False
                break
        
        if file_found:
            to_move_index_e = to_move_index_s
            for x in range(to_move_index_s, len(all_reformat)-1):
                if all_reformat[to_move_index_e] == all_reformat[to_move_index_s]:
                    to_move_index_e += 1
                else:
                    break

            empty_index_s = 0
            empty_index_e = 0

            for x in range(0, to_move_index_s):
                if (empty_index_e - empty_index_s) == (to_move_index_e - to_move_index_s):
                    continue

    
