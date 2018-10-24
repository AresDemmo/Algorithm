

def select(A):
    sorted(A)
    answer = []
    ini = -10
    for i in A:
        if abs(i - ini) > 4:
            ini = i + 4
            answer += [ini]
    return answer

if __name__ == '__main__':
    A = [1, 4, 5, 6, 3, 7, 9 ,10]
    print select(A)