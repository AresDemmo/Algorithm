def halfsearch(a, x):
    l = 0
    r = len(a) - 1
    while l < r:
        mid = (l + r) / 2
        if (a[mid] <= x):
            l = mid + 1
        else:
            r = mid
    return l

def Find(a, L, U):
    return (halfsearch(a, L), halfsearch(a, U - 1) - 1)

if __name__ == '__main__':
    a = [1, 2, 3, 4, 5, 6, 7]
    print Find(a, 2, 5)
