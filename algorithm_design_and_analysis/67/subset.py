

def subset(S, M, cnt, sub, cont):
    if cnt == len(S) or cont + S[cnt] > M:
        return
    if (cont + S[cnt] == M):
        print sub + [S[cnt]]
        return
    subset(S, M, cnt + 1, sub + [S[cnt]], cont + S[cnt])
    subset(S, M, cnt + 1, sub, cont)


if __name__ == '__main__':
    S = [1, 1, 2, 4, 5, 6, 8, 9, 10]
    M = 13
    subset(S, M, 0, [], 0)