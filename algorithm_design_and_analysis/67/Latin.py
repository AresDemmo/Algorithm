

answer = [1, 2, 3, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
ok = [15, 0, 0, 0, 1, 2, 4, 8]

def Latin(cnt):
    global answer
    if cnt == 16:
        print answer
        return
    for j in range(4):
        row = cnt / 4
        col = cnt % 4
        k = (1 << j)
        if (ok[row] & k == 0 and ok[4 + col] & k == 0):
            ok[row] = ok[row] | k
            ok[4 + col] = ok[4 + col] | k
            answer[cnt] = j + 1
            Latin(cnt + 1)    
            ok[row] = ok[row] ^ k
            ok[4 + col] = ok[4 + col] ^ k

if __name__ == '__main__':
    Latin(4)