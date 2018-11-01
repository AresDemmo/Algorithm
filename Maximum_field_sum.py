
import numpy
import random


def DPAlgo(nums):
    answer = nums[0]
    sums = 0
    mins = nums[0]
    for i in nums:
        sums += i
        mins = min(mins, sums)
        answer = max(answer, sums - mins)
    return answer

def MergeAlgo(nums, l, r):
    """
        1: the max sum of sequence's left
        2: the max sum of sequence's mid
        3: the max sum of sequence's right
        4: the sum of sequence
    """
    if l == r:
        return [nums[l], nums[l], nums[l], nums[l]]
    mid = (l + r) / 2;
    [l1, l2, l3, l4] = MergeAlgo(nums, l, mid)
    [r1, r2, r3, r4] = MergeAlgo(nums, mid + 1, r)
    m1 = max(l1, l4 + r1)
    m2 = max(l2, r2, l3 + r1)
    m3 = max(r3, r4 + l3)
    m4 = l4 + r4
    return [m1, m2, m3, m4]

if __name__ == '__main__':
    nums = [1,-2,3,5,-1,2]
    print MergeAlgo(nums, 0, len(nums) -1)
    print DPAlgo(nums)