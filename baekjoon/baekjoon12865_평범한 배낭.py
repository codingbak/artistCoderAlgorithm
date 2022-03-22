## 첫 생각 : 물품무게로 정렬후 투 포인터를 이용하여 최대 값을 확인 후 출력한다.

N, K = map(int,input().split())

stuffArray = [list(map(int,input().split())) for _ in range(N)]

stuffArray = sorted(stuffArray, key=lambda x:x[0])

leftX = 0
rightX = 0

answer = 0

while(rightX!=N):

    dummy = 0
    checkBackPack = 0

    for i in range(leftX,rightX+1):
        checkBackPack += stuffArray[i][0]
        dummy += stuffArray[i][1]

    if checkBackPack > K:
        leftX += 1

    elif checkBackPack < K:
        rightX += 1
        if dummy > answer:
            answer = dummy

    else :
        rightX += 1
        if dummy > answer:
            answer = dummy
print(answer)

