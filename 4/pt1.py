import re

def check_horizontal(f):
    xmas_regex = r"XMAS"
    samx_regex = r"SAMX"
    total_h = 0
    for line in f:
        xmas_matches = len(re.findall(xmas_regex, line))
        samx_matches = len(re.findall(samx_regex, line))
        total_h += xmas_matches + samx_matches
    return total_h

def check_vertical(f):
    lines = {}
    i = 0
    total_v = 0
    for line in f:
        lines[i] = line.strip()
        i += 1
    for j in range(i-3):
        current_line = lines[j]
        
        x_indexes = [m.start() for m in re.finditer('X', current_line)]
        for x in x_indexes:
            if (lines[j+1][x]=='M') and (lines[j+2][x]=='A') and (lines[j+3][x]=='S'):
                total_v += 1

        s_indexes = [m.start() for m in re.finditer('S', current_line)]
        for s in s_indexes:
            if (lines[j+1][s]=='A') and (lines[j+2][s]=='M') and (lines[j+3][s]=='X'):
                total_v += 1
    return total_v

def check_diagonal(f):
    lines = {}
    i = 0
    total_d = 0
    for line in f:
        lines[i] = line.strip()
        i += 1
    
    for j in range(i-3):
        current_line = lines[j]
        x_indexes = [m.start() for m in re.finditer('X', current_line)]
        for x in x_indexes:
            if x>=3:
                if (lines[j+1][x-1]=='M') and (lines[j+2][x-2]=='A') and (lines[j+3][x-3]=='S'): #left down diagonal
                    total_d += 1
            if x<=len(current_line)-4:
                if (lines[j+1][x+1]=='M') and (lines[j+2][x+2]=='A') and (lines[j+3][x+3]=='S'): #right down diagonal
                    total_d += 1

        s_indexes = [m.start() for m in re.finditer('S', current_line)]
        for s in s_indexes:
            if s>=3:
                if (lines[j+1][s-1]=='A') and (lines[j+2][s-2]=='M') and (lines[j+3][s-3]=='X'): #left down diagonal
                    total_d += 1
            if s<=len(current_line)-4:
                if (lines[j+1][s+1]=='A') and (lines[j+2][s+2]=='M') and (lines[j+3][s+3]=='X'): #right down diagonal
                    total_d += 1
    return total_d

total_xmas = 0
#f = open("test1.txt", "r")
f = open("input.txt", "r")
f_lines = []
for line in f.readlines():
    f_lines.append(line)
total_xmas += check_horizontal(f_lines)
total_xmas += check_vertical(f_lines)
total_xmas += check_diagonal(f_lines)

print(total_xmas)

    