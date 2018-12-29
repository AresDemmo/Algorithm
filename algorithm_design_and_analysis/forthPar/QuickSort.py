# -*- coding: UTF-8 -*-
#QuickSort

def Partition(a, l, r):
    key = a[l]
    while l < r:
        while l < r and a[r] >= key:
            r -= 1
        while l < r and a[r] < key:
            a[l] = a[r]
            l += 1
            a[r] = a[l]
    a[l] = key
    return l

def QuickSort(a, l, r):
    if l < r:
        mid = Partition(a, l, r)
        QuickSort(a, l, mid)
        QuickSort(a, mid + 1, r)

def QSort(a):
    "使用python的语言特性，虽然代码简短，但是这种方法比较慢"
    if len(a) <= 1 : return a
    return QSort([i for i in a[1:] if i <= a[0]]) + [a[0]] + QSort([j for j in a[1:] if j > a[0]])

def main():
    n = input('please input the length of sequence')
    a = [0 for i in range(n)]
    for i in range(n):
        a[i] = input()
    print QSort(a)
    QuickSort(a, 0, n-1)
    print a
    

if __name__ == '__main__':
    main()
