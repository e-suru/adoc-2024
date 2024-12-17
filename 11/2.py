import sys
import copy

stones = [int(x.strip()) for x in open(sys.argv[1]).read().split(' ')]
blinks = int(sys.argv[2])

stones_dict = {i:stones.count(i) for i in set(stones)}

for i in range(blinks): 
    temp_tally = {}
    for num in stones_dict.keys():
        if num == 0:
            if 1 not in temp_tally:
                temp_tally[1] = stones_dict[num]
            else:
                temp_tally[1] += stones_dict[num]
        else:
            digits = len(str(num))
            if digits % 2 == 0:
                first_half = int(str(num)[:digits//2])
                second_half = int(str(num)[digits//2:])

                if first_half not in temp_tally:
                    temp_tally[first_half] = stones_dict[num]
                else:
                    temp_tally[first_half] += stones_dict[num]
                
                if second_half not in temp_tally:
                    temp_tally[second_half] = stones_dict[num]
                else:
                    temp_tally[second_half] += stones_dict[num]
            else:
                new_num = num*2024
                if new_num not in temp_tally:
                    temp_tally[num*2024] = stones_dict[num]
                else:
                    temp_tally[num*2024] += stones_dict[num]
    stones_dict = temp_tally

print(sum(stones_dict.values()))

