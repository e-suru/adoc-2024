total_safe_reports = 0
f = open("input.txt", "r")
for row in f.readlines():
    safe = True
    pos_neg_flag_set = False
    pos_neg_flag = 0

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
    if safe:
        total_safe_reports += 1

print(total_safe_reports)
        

