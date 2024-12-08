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
    for perm in b_permutations:
        running_total = nums[0]
        for i in range(0, len(perm)):
            if int(perm[i]) == 0:
                running_total = running_total + nums[i+1]
            else:
                running_total = running_total * nums[i+1]
        if running_total == total:
            found_valid_perm = True
            break
    return found_valid_perm

def test_all_comps(comps: list):
    sum_valid_comps = 0
    for comp in comps:
        total_for_comp = next(iter(comp)) # dict with only 1 key
        if test_computation(total_for_comp, comp[total_for_comp]):
            sum_valid_comps += total_for_comp
    print(sum_valid_comps)

# comps_list = load_computations_file("test_1.txt")
comps_list = load_computations_file("input.txt")
test_all_comps(comps_list)