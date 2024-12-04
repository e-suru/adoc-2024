#f = open("test_input_pt1.txt", "r")
f = open("input.txt", "r")
total_mul = 0

for line in f.readlines():
    i = 0
    while i < len(line)-4:
        #print(line[i:i+4])
        if line[i:i+4] != 'mul(':
            i += 1
        else:
            invalid = False
            string_num_1 = ""
            string_num_2 = ""

            for j in range(0, 3):
                if line[i+4+j].isdigit():
                    string_num_1 += line[i+4+j]
                elif line[i+4+j] == ',':
                    i += 3+j
                    break
                else:
                    invalid = True
                    break
            if line[i+1] != ',':
                invalid = True

            if invalid:
                continue
            else:
                i += 2
                for j in range(0,3):
                    #print(line[i+j])
                    if line[i+j].isdigit():
                        string_num_2 += line[i+j]
                    elif line[i+j] == ')':
                        i += j - 1
                        break
                    else:
                        invalid = True
                        break
            if line[i+1] != ')':
                invalid = True

            if invalid:
                continue
            else:
                if string_num_1.isdigit() and string_num_2.isdigit():
                    num1 = int(string_num_1)
                    num2 = int(string_num_2)
                    total_mul += num1 * num2
            i += 1

print(total_mul)

