total_safe_reports = 0
f = open("input.txt", "r")
for row in f.readlines():
    safe = True
    pos_neg_flag_set = False
    pos_neg_flag = 0
    index_to_delete = -1

    levels = row.split(' ')
    for i in range(1, len(levels)):
        diff = int(levels[i]) - int(levels[i-1])
        if diff == 0 or abs(diff) > 3:
            safe = False
            break
        else:
            if not pos_neg_flag_set:
                pos_neg_flag = diff
                pos_neg_flag_set = True
                continue
            else:
                if (diff < 0 and pos_neg_flag < 0) or (diff > 0 and pos_neg_flag > 0):
                    continue
                else:
                    safe = False
                    break

    if not safe:
        for j in range(0, len(levels)+1):
            safe = True
            pos_neg_flag_set = False
            pos_neg_flag = 0
            index_to_delete = -1

            new_levels = levels[:j] + levels[j+1:]
            print(new_levels)
            for i in range(1, len(new_levels)):
                diff = int(new_levels[i]) - int(new_levels[i-1])

                if diff == 0 or abs(diff) > 3:
                    safe = False
                    break
                else:
                    if not pos_neg_flag_set:
                        pos_neg_flag = diff
                        pos_neg_flag_set = True
                        continue
                    else:
                        if (diff < 0 and pos_neg_flag < 0) or (diff > 0 and pos_neg_flag > 0):
                            continue
                        else:
                            safe = False
                            break
            if safe:
                break

    if safe:
        total_safe_reports += 1

print(total_safe_reports)
        

