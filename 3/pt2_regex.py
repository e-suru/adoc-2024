import re

#f = open("test_input_pt1.txt", "r")
f = open("input.txt", "r")
mul_regex = r"mul\([\d]{1,3},[\d]{1,3}\)|do\(\)|don\'t\(\)"
total = 0
do_flag = True

for line in f.readlines():
    all_matches = re.findall(mul_regex, line)
    for match in all_matches:
        if match[0] == 'm':
            if do_flag:
                num1, num2 = match[4:len(match)-1].split(',')
                total += int(num1) * int(num2)
            else:
                continue
        elif match[:3] == 'don':
            do_flag = False
        else:
            do_flag = True

print(total)