from functools import cache


f = open("input.txt")


@cache
def rec(cfg, nums):


    if cfg == "":
        return 1 if nums == () else 0

    if nums == ():
        return 0 if "#" in cfg else 1

    res = 0
    # Allow to skip

    if cfg[0] in ".?":
        res += rec(cfg[1:], nums)

    # Get chunk
    # print(cfg, nums)
    if cfg[0] in "#?":
        if len(cfg) >= nums[0]:
            # print(cfg, nums)
            if (cfg[:nums[0]].replace("?", "#").count("#") == nums[0]) and (nums[0] == len(cfg) or cfg[nums[0]] != "#"):
                res += rec(cfg[nums[0] + 1:], nums[1:])

    # print(res)
    return res


t = 0
for line in f:
    # print(line)
    cfg = (line.split()[0] + "?") * 5
    nums = (line.split()[1] + ",") * 5
    nums = tuple(map(int, tuple(nums.split(",")[:-1])))
    # print(cfg, nums)
    out = rec(cfg[:-1], nums)
    # print(line, out)
    t += out


print(t)
