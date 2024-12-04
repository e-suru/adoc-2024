import re

#f = open("test_input_pt1.txt", "r")
f = open("input.txt", "r")
mul_regex = 'mul\([\d]{1,3},[\d]{1,3}\)'
total = 0

for line in f.readlines():
    all_muls = re.findall(mul_regex, line)
    for mul in all_muls:
        num1, num2 = mul[4:len(mul)-1].split(',')
        total += int(num1) * int(num2)

print(total)