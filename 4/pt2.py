import re

def check_mas(f):
    lines = {}
    i = 0
    total_mas = 0
    for line in f:
        lines[i] = line.strip()
        i += 1

    for j in range(i-2):
        current_line = lines[j]
        m_indexes = [m.start() for m in re.finditer(r'(?=(M[A-Z]M))', current_line)]
        for m in m_indexes:
            if (lines[j+1][m+1]=="A") and (lines[j+2][m]=="S") and (lines[j+2][m+2]=="S"):
                total_mas += 1

        s_indexes = [m.start() for m in re.finditer(r'(?=(S[A-Z]S))', current_line)]
        for s in s_indexes:
            if (lines[j+1][s+1]=="A") and (lines[j+2][s]=="M") and (lines[j+2][s+2]=="M"):
                total_mas += 1

        m_s_indexes = [m.start() for m in re.finditer(r'(?=(M[A-Z]S))', current_line)]
        for m in m_s_indexes:
            if (lines[j+1][m+1]=="A") and (lines[j+2][m]=="M") and (lines[j+2][m+2]=="S"):
                total_mas += 1
        

        s_m_indexes = [m.start() for m in re.finditer(r'(?=(S[A-Z]M))', current_line)]
        for m in s_m_indexes:
            if (lines[j+1][m+1]=="A") and (lines[j+2][m]=="S") and (lines[j+2][m+2]=="M"):
                total_mas += 1

    return total_mas

#f = open("test1.txt", "r")
f = open("input.txt", "r")
f_lines = []
for line in f.readlines():
    f_lines.append(line)

print(check_mas(f_lines))