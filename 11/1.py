import sys
import math

stones = [int(x.strip()) for x in open(sys.argv[1]).read().split(' ')]
blinks = int(sys.argv[2])

for i in range(blinks): 
    new_stones = []
    for s in stones:
        if s == 0:
            new_stones.append(1)
        else:
            digits = len(str(s))
            if digits % 2 == 0:
                new_stones.append(int(str(s)[:digits//2]))
                new_stones.append(int(str(s)[digits//2:]))
            else:
                new_stones.append(s*2024)
    stones = new_stones

print(len(stones))

