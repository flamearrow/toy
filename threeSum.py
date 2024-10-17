from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    # sortedNums = sorted(nums)
    nums = sorted(nums)

    # return two nums from sortedNum[start] to sortedNum[end] that adds to target, or None
    def twoSum(start, target):
        seen = set()
        ret = set()
        for i in range(start, len(nums)):
            comp = target - nums[i]
            if comp in seen:
                ret.add((nums[i], comp))
            seen.add(nums[i])
        return ret

    ret = []
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        cur = nums[i]
        target = 0 - cur
        result = twoSum(i + 1, target)
        for one, two in result:
            ret.append([cur, one, two])
    return ret


if __name__ == '__main__':
    for r in threeSum([0, 0, 0, 0]):
        print(r, end="\n")