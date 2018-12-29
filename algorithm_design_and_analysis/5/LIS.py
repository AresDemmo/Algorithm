import numpy

def lower_bound(nums, target):
    first, size = 0, len(nums)
    while size > 0:
        half = size >> 1
        mid = first + half
        if nums[mid] < target:
            first = mid + 1
            size = size - half - 1
        else:
            size = half
    return first


def LIS(A):
    inf = max(A) + 1
    answer = [inf for i in range(len(A))]
    id = [0 for i in range(len(A))]
    fa = [-1 for i in range(len(A))]
    for i in range(len(A)):
        k = lower_bound(answer, A[i])
        answer[k] = A[i]
        id[k] = i
        if k > 0: fa[i] = id[k - 1]
    key = id[lower_bound(answer, inf) - 1]
    answer = []
    while key != -1:
        answer += [A[key]]
        key = fa[key]
    answer.reverse()
    return answer


if __name__ == '__main__':
    A = [2, 8, 4, -4, 5, 9, 11]