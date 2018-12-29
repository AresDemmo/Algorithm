#MergeSort

import sys

def Merge(a, b, l, mid, r):
    iter1 = l
    iter2 = mid + 1
    iterb = l
    while iter1 <= mid and iter2 <= r:
        if cmp(a[iter1], a[iter2]) < 0:
            b[iterb] = a[iter1]
            iter1 += 1
        else:
            b[iterb] = a[iter2]
            iter2 += 1
        iterb += 1
    if iter1 <= mid:
        while iter1 <= mid:
            b[iterb] = a[iter1]
            iterb += 1
            iter1 += 1
    else:
        while iter2 <= r:
            b[iterb] = a[iter2]
            iterb += 1
            iter2 += 1
    for i in range(l, r + 1):
        a[i] = b[i]
            

def MergeSort(a, b, l, r):
    if l < r:
        mid = (l + r) / 2
        MergeSort(a, b, l, mid)
        MergeSort(a, b, mid + 1, r)
        Merge(a, b, l, mid, r)


def main():
    n = input('please input the length of sequence')
    a = [0 for i in range(n)]
    b = [0 for i in range(n)]
    for i in range(n):
        a[i] = input();
    MergeSort(a, b, 0, n-1)
    print a
    

if __name__ == '__main__':
    main()
