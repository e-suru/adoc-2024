f = open("input.txt", "r")

col1 = []
col2 = []
total_diff = 0

for row in f.readlines():
    val1, val2 = row.split("   ")
    col1.append(int(val1.strip()))
    col2.append(int(val2.strip()))

col1.sort()
col2.sort()

for i in range(len(col1)):
    total_diff += abs(col1[i] - col2[i])

print(total_diff)
    