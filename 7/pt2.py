import itertools

def load_computations_file(filepath):
    f = open(filepath, "r")
    comps = []
    for line in f.readlines():
        total, nums = line.split(":")
        list_nums_in_row = [int(x) for x in nums.strip().split(" ")]
        comps.append({int(total): list_nums_in_row})
    return comps

def test_computation(total: int, nums: list[int]):
    # 0 - addition
    # 1 - multiplication
    b_permutations = ["".join(seq) for seq in itertools.product("01", repeat=len(nums)-1)]
    found_valid_perm = False
    if nums == [6, 86, 15]: 
        print("HMMMMMMMMMMMMMMMMMMMMM")
    for perm in b_permutations:
        print(perm)
        running_total = nums[0]
        for i in range(0, len(perm)):
            if int(perm[i]) == 0:
                running_total = running_total + nums[i+1]
            else:
                running_total = running_total * nums[i+1]
        print(running_total)
        if running_total == total:
            found_valid_perm = True
            break
    return found_valid_perm

def test_after_concat(total: int, nums: list[int]):
    concat_permutations = ["".join(seq) for seq in itertools.product("01", repeat=len(nums))]
    # 0 - no concatenation
    # 1 - concatenate 2 values
    b_found_valid_perm = False
    for c in concat_permutations:
        new_nums = [nums[0]]
        for i in range(1, len(c)):
            if int(c[i]) == 0:
                new_nums.append(nums[i])
            else:
                new_nums[-1] = int(str(new_nums[-1]) + str(nums[i]))
        if test_computation(total, new_nums):
            b_found_valid_perm = True
            break
    return b_found_valid_perm

def test_all_comps(comps: list):
    sum_valid_comps = 0
    for comp in comps:
        total_for_comp = next(iter(comp)) # dict with only 1 key
        print(comp)
        if test_after_concat(total_for_comp, comp[total_for_comp]):
            print("valid!")
            print("total added ", total_for_comp)
            sum_valid_comps += total_for_comp
    print(sum_valid_comps)

comps_list = load_computations_file("test_1.txt")
# comps_list = load_computations_file("input.txt")
test_all_comps(comps_list)