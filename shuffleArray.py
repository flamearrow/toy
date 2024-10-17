import random
from typing import List


def shuffle(nums) -> List[int]:
    # Fisher-Yates - do this in place, looping from end to start, swap end with a random before
    for i in range(len(nums) - 1, 0, -1):
        j = random.randint(0, i)
        nums[i], nums[j] = nums[j], nums[i]
    return nums
