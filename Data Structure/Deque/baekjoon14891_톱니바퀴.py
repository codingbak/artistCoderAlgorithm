from collections import deque

gearSet = [deque(list(map(int,input()))) for _ in range(4)]

K = int(input())

for i in range(K):

    command = list(map(int, input().split()))

    rotateInfo = [0, 0, 0, 0]
    rotateInfo[command[0]-1] = command[1]

    start = command[0] - 1

    while start != 0:
        if gearSet[start][6] == gearSet[start-1][2]:
            break
        else:
            if rotateInfo[start] == -1:
                rotateInfo[start-1] = abs(rotateInfo[start])
            else:
                rotateInfo[start - 1] = -1
        start -= 1


    start = command[0] - 1

    while start != 3:
        if gearSet[start][2] == gearSet[start+1][6]:
            break
        else:
            if rotateInfo[start] == -1:
                rotateInfo[start + 1] = abs(rotateInfo[start])
            else:
                rotateInfo[start + 1] = -1
        start += 1

    for i in range(4):
        gearSet[i].rotate(rotateInfo[i])

result = 0
point = 1

for i in range(4):
    if gearSet[i][0] == 1:
        result += point
    point *= 2

print(result)




