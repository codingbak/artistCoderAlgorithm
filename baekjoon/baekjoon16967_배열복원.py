
H,W,X,Y = map(int,input().split())

matrix = [list(map(int,input().split())) for _ in range(X+H)]

for y in range(H):
    for x in range(W):
        matrix[y+X][x+Y] -= matrix[y][x]

for y in range(H):
    for x in range(W):
        print(matrix[y][x],end=" ")
    print()