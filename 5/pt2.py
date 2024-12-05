import math

#f = open("test_1.txt", "r")
f = open("input.txt", "r")

rules = {}
pages = []
newline_flag = False

for line in f.readlines():
    if len(line.strip()) == 0:
        newline_flag = True
        continue

    if not newline_flag:
        first_page, second_page = line.split('|')
        if first_page.strip() in rules:
            rules[first_page.strip()].append(second_page.strip())
        else:
            rules[first_page.strip()] = [second_page.strip()]
    else:
        pages.append(line.strip())

middle_total = 0
for seq_pages in pages: # check if page sequence is valid
    pages_order = seq_pages.split(',')
    pages_seen = {}
    valid = True

    for page in pages_order:
        if page in rules:
            must_be_after = rules[page]
            for subsequent_page in must_be_after:
                if subsequent_page in pages_seen:
                    valid = False
                    break
        pages_seen[page] = True
        if valid == False:
            break

    if not valid:
        # reorder pages!!!
        new_page_order = []
        i = 0
        for i in range(len(pages_order)):
            page_to_add = pages_order[i]
    
            if new_page_order == [] or (not page_to_add in rules):
                new_page_order.append(page_to_add)
            else:
                placed = False
                new_rules = rules[page_to_add]
                for j in range(len(new_page_order)):
                    existing_page = new_page_order[j]
                    if existing_page in new_rules:
                        new_page_order.insert(j, page_to_add)
                        placed = True
                        break
                if not placed:
                    new_page_order.append(page_to_add)
        
        middle_index = len(new_page_order) // 2
        middle_total += int(new_page_order[middle_index])

print(middle_total)