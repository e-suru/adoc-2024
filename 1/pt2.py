f = open("input.txt", "r")
col1 = []
col2 = []
for row in f.readlines():
    val1, val2 = row.split("   ")
    col1.append(int(val1.strip()))
    col2.append(int(val2.strip()))

# problem: multiply col1 value x by how many times x appears in col2
col2_values = {}
for x in col2:
    if x in col2_values:
        col2_values[x] += 1
    else:
        col2_values[x] = 1

similarity_score = 0
for i in col1:
    if i in col2_values:
        similarity_score += i * col2_values[i]

print(similarity_score)