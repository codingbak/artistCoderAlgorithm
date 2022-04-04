import sys
limit_number = 100000
sys.setrecursionlimit(limit_number)

input = sys.stdin.readline

n, m = map(int,input().split())

arraySet = [i for i in range(n+1)]

def searchRoot(idx):
    if arraySet[idx] == idx :
        return idx
    else:
        return searchRoot(arraySet[idx])

for _ in range(m):
    command, a, b = map(int, input().split())
    aRoot = searchRoot(a)
    bRoot = searchRoot(b)

    if command == 1:
        if aRoot == bRoot:
            print("YES")
        else:
            print("NO")
    else:
        if aRoot > bRoot:
            arraySet[bRoot] = aRoot
        elif bRoot > aRoot:
            arraySet[aRoot] = bRoot


